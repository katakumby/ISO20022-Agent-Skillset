"""Offline ISO 20022 retrieval. Python 3.10+, standard library only."""
import sys
sys.dont_write_bytecode = True
import argparse, hashlib, json, re, sqlite3
from pathlib import Path
from urllib.parse import unquote
TEXT_EXT = {".md", ".mmd", ".txt", ".json", ".xml", ".xsd", ".csv", ".tsv"}
def digest(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):h.update(b)
    return h.hexdigest()
def load(path):return json.loads(Path(path).read_text(encoding="utf-8-sig"))
def safe_path(root,relative,must_exist=True):
    if not isinstance(relative,str) or not relative or "\\" in relative:raise ValueError("Expected a portable relative path")
    if relative.startswith("/") or re.match(r"^[a-zA-Z]:",relative) or ".." in relative.split("/"):raise ValueError("Path escapes package")
    base=Path(root).resolve();p=base.joinpath(*relative.split("/"));current=p
    while current!=base:
        if current.is_symlink():raise ValueError("Symbolic links are not accepted inside a snapshot")
        current=current.parent
    resolved=p.resolve()
    if resolved!=base and base not in resolved.parents:raise ValueError("Path escapes package")
    if must_exist and not resolved.is_file():raise ValueError("Packaged file unavailable: "+relative)
    return resolved
def metadata(text):
    text=text.replace("\r\n","\n")
    if not text.startswith("---\n"):return {},text,1
    end=text.find("\n---",4)
    if end<0:return {},text,1
    result={}
    for line in text[4:end].splitlines():
        if ":" not in line:continue
        key,val=line.split(":",1)
        try:result[key]=json.loads(val.strip())
        except ValueError:result[key]=val.strip().strip("\"'")
    boundary=end+4
    return result,text[boundary:],text[:boundary].count("\n")+1
def normalize(identifier):
    s=identifier.strip().lower()
    if s.startswith("urn:"):s=s.rsplit(":",1)[-1]
    if not re.fullmatch(r"[a-z]{4}\.\d{3}(?:\.\d{3}\.\d{2,})?",s):raise ValueError("Use an exact message ID, family, or message namespace")
    return s
def compact(meta):
    keys=("message_id","message_family","namespace","schema_status","documentation_status","source_ids","source_editions",
          "source_line","schema_path","source_locations","review_status","limitations","qname_or_schema_path","message_sets",
          "source_id","origin","diagram_origin","diagram_kind")
    out={};omitted=[]
    for k in keys:
        if k not in meta:continue
        v=meta[k];encoded=json.dumps(v,ensure_ascii=False)
        if len(encoded)>650:
            if isinstance(v,list):
                short=[]
                for item in v[:3]:
                    if len(json.dumps(short+[item],ensure_ascii=False))>650:break
                    short.append(item)
                out[k]=short
            else:out[k]=encoded[:220]+"..."
            omitted.append(k)
        else:out[k]=v
    if omitted:out.update(metadata_fields_truncated=omitted,metadata_continuation="Use metadata for complete values")
    return out
class Corpus:
    def __init__(self,skill_root,snapshot=None):
        self.skill_root=Path(skill_root).resolve()
        self.config=load(self.skill_root/"config.json") if (self.skill_root/"config.json").is_file() else {}
        if not isinstance(self.config,dict):raise ValueError("Configuration must be an object")
        for key in ("default_collection","default_edition"):
            if self.config.get(key) is not None and not isinstance(self.config[key],str):raise ValueError("Invalid configuration: "+key)
        if self.config.get("evidence_pack") is not None and not re.fullmatch(r"[a-zA-Z0-9_-]{1,100}",str(self.config["evidence_pack"])):raise ValueError("Invalid evidence pack identifier")
        active=load(self.skill_root/"knowledge/active.json")
        self.snapshot_id=snapshot or active["snapshot_id"]
        if not re.fullmatch(r"[a-zA-Z0-9_-]{1,100}",self.snapshot_id):raise ValueError("Invalid snapshot identifier")
        self.root=self.skill_root/"knowledge/snapshots"/self.snapshot_id
        self.manifest=load(self.root/"manifest.json")
        if self.manifest.get("format_version")!=1 or self.manifest.get("snapshot_id")!=self.snapshot_id:raise ValueError("Unsupported or mismatched manifest")
        index=safe_path(self.root,"index.sqlite")
        self.db=sqlite3.connect(index.as_uri()+"?mode=ro",uri=True);self.db.row_factory=sqlite3.Row
        self.db.execute("PRAGMA query_only=ON")
        info=dict(self.db.execute("SELECT key,value FROM info"))
        if info.get("snapshot_id")!=self.snapshot_id or info.get("format_version")!="1":raise ValueError("Index belongs to another snapshot")
    def close(self):self.db.close()
    def file(self,path):
        row=self.db.execute("SELECT 1 FROM files WHERE path=?",(path,)).fetchone()
        if row is None or Path(path).suffix.lower() not in TEXT_EXT:raise ValueError("Not a packaged text reference: "+path)
        return safe_path(self.root,path)
    def text(self,path):
        data=self.file(path).read_bytes()
        expected=self.db.execute("SELECT sha256 FROM files WHERE path=?",(path,)).fetchone()[0]
        if hashlib.sha256(data).hexdigest()!=expected:raise ValueError("Packaged text checksum mismatch: "+path)
        return data.decode("utf-8-sig").replace("\r\n","\n")
    def envelope(self,data):return {"snapshot_id":self.snapshot_id,**data}
    def info(self):
        return self.envelope({"label":self.manifest.get("label"),"format_version":1,
            "reference_files":self.manifest.get("text_file_count"),
            "indexed_documents":self.db.execute("SELECT count(*) FROM documents").fetchone()[0],
            "defaults":self.config,"evidence_policy":"Text only; original inspection requires explicit request and local evidence.",
            "research_policy":"Offline only; no external research.",
            "continuation":"Pass --snapshot "+self.snapshot_id+" on subsequent commands for this answer."})
    def record(self,row,snippet=None):
        d=dict(row);m=json.loads(d["metadata"])
        result={"path":d["path"],"title":d["title"],"kind":d["kind"],"domain":d["domain"],**compact(m)}
        if snippet:result["snippet"]=snippet
        return result
    def resolve(self,identifier,offset=0,limit=10):
        key=normalize(identifier);exact=len(key.split("."))==4;column="message_id" if exact else "family"
        rows=self.db.execute("SELECT * FROM documents WHERE kind='message-index' AND "+column+"=? ORDER BY message_id",(key,)).fetchall()
        records=[]
        for row in rows[offset:offset+limit]:
            r=self.record(row);folder=Path(row["path"]).parent
            r["related_references"]=[(folder/name).as_posix() for name in ("mdr-evidence.md","business.md","roles.md","structure.md")
                if self.db.execute("SELECT 1 FROM files WHERE path=?",((folder/name).as_posix(),)).fetchone()]
            records.append(r)
        return self.envelope({"query":key,"exact":exact,"total":len(rows),"ambiguous":len(rows)>1,"offset":offset,"next_offset":offset+len(records) if offset+len(records)<len(rows) else None,
                              "records":records,"absence_scope":"This embedded snapshot only"})
    def collection_aliases(self,value):
        path="catalog/message-sets.json"
        if not self.db.execute("SELECT 1 FROM files WHERE path=?",(path,)).fetchone():return [value]
        if not hasattr(self,"_collection_records"):self._collection_records=json.loads(self.text(path)).get("records",[])
        values={value}
        for record in self._collection_records:
            aliases=[record.get("set_slug"),record.get("message_set")]
            if any(isinstance(x,str) and x.casefold()==value.casefold() for x in aliases):
                values.update(x for x in aliases if isinstance(x,str) and x)
        return sorted(values)
    def search(self,query,args):
        words=re.findall(r"[^\W_]+",query,re.UNICODE)[:32]
        if not words:raise ValueError("Supply at least one search term")
        match=" AND ".join('"'+w.replace('"','""')+'"' for w in words)
        clauses=["search MATCH ?"];params=[match];applied={}
        use_defaults=not args.all_scopes and not args.message and not args.namespace and not args.source and not args.under
        for attr,tag in (("kind","kind"),("domain","domain"),("message","message"),("namespace","namespace"),
                         ("collection","collection"),("edition","edition"),("source","source"),("status","status")):
            val=getattr(args,attr,None)
            if val is None and use_defaults and attr in ("collection","edition"):val=self.config.get("default_"+attr)
            if val:
                if attr=="message":
                    val=normalize(val);tag="message" if len(val.split("."))==4 else "family"
                values=self.collection_aliases(val) if attr=="collection" else [val]
                clauses.append("EXISTS(SELECT 1 FROM tags t WHERE t.doc_id=d.id AND t.key=? AND t.value IN ("+",".join("?" for _ in values)+"))")
                params.extend([tag]+values);applied[attr]=val
        if args.under:
            prefix=args.under.replace("\\","/").rstrip("/")+"/"
            safe_path(self.root,prefix+"_scope_check",must_exist=False)
            clauses.append("substr(d.path,1,?)=?");params.extend([len(prefix),prefix]);applied["under"]=prefix
        where=" AND ".join(clauses)
        total=self.db.execute("SELECT count(*) FROM search JOIN documents d ON d.id=search.rowid WHERE "+where,params).fetchone()[0]
        rows=self.db.execute("SELECT d.* FROM search JOIN documents d ON d.id=search.rowid WHERE "+where+
            " ORDER BY bm25(search,5.0,1.0),d.path LIMIT ? OFFSET ?",params+[args.limit,args.offset]).fetchall()
        records=[]
        for row in rows:
            _,body,body_line=metadata(self.text(row["path"]))
            scored=[(sum(w.lower() in line.lower() for w in words),i,line) for i,line in enumerate(body.splitlines())]
            best=max(scored,default=(0,0,""),key=lambda x:(x[0],-x[1]))
            r=self.record(row,best[2][:450]);r["snippet_is_partial_evidence"]=True;r["snippet_line"]=body_line+best[1];records.append(r)
        while len(records)>1 and len(json.dumps(records,ensure_ascii=False))>args.budget-700:records.pop()
        nxt=args.offset+len(records)
        return self.envelope({"query":query,"filters":applied,"total":total,"offset":args.offset,"returned":len(records),
            "next_offset":nxt if nxt<total else None,"records":records,
            "absence_scope":"Matching indexed text in these filters; not proof of corpus-wide absence",
            "warning":"Read complete relevant sections; snippets can omit conditions."})
    def headings(self,path):
        headings=[];fence=None
        for i,line in enumerate(self.text(path).splitlines(),1):
            f=re.match(r"^\s*(["+chr(96)+r"~]{3,})",line)
            if f:
                char=f.group(1)[0];fence=None if fence==char else (char if fence is None else fence);continue
            if fence:continue
            m=re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$",line)
            if m:headings.append({"line":i,"level":len(m.group(1)),"heading":m.group(2)})
        return headings
    def outline(self,path,offset=0,limit=30):
        hs=self.headings(path)
        return self.envelope({"path":path,"total":len(hs),"offset":offset,"headings":hs[offset:offset+limit],
            "next_offset":offset+limit if offset+limit<len(hs) else None})
    def read(self,path,args,meta_only=False):
        text=self.text(path);m,body,body_line=metadata(text);start_line=body_line
        if meta_only:selected=json.dumps(m,ensure_ascii=False,indent=2);start_line=1
        elif getattr(args,"start_line",None) is not None or getattr(args,"end_line",None) is not None:
            if args.section:raise ValueError("Choose a section or a line range, not both")
            first=getattr(args,"start_line",None);last=getattr(args,"end_line",None)
            lines=text.splitlines()
            if first is None or last is None or first<1 or last<first or last>len(lines):raise ValueError("Supply a valid inclusive --start-line and --end-line")
            selected="\n".join(lines[first-1:last]);start_line=first
        elif args.section:
            hs=self.headings(path);matches=[h for h in hs if h["heading"].casefold()==args.section.casefold()]
            if len(matches)!=1:return self.envelope({"path":path,"error":"Section missing or ambiguous","candidates":matches,"use":"outline"})
            h=matches[0]
            end=next((x["line"]-1 for x in hs if x["line"]>h["line"] and x["level"]<=h["level"]),len(text.splitlines()))
            selected="\n".join(text.splitlines()[h["line"]-1:end]);start_line=h["line"]
        else:selected=body
        offset=args.offset
        if offset>len(selected):raise ValueError("Continuation offset outside selected text")
        cap=max(500,args.budget-2000);end=min(len(selected),offset+cap)
        if end<len(selected):
            split=selected.rfind("\n",offset,end)
            if split>offset+cap//2:end=split+1
        chunk=selected[offset:end];line=start_line+selected[:offset].count("\n")
        return self.envelope({"path":path,"section":args.section,"metadata":compact(m),
            "source_line_start":None if meta_only else line,"source_line_end":None if meta_only else line+chunk.count("\n"),"offset":offset,
            "text_representation":"frontmatter-json" if meta_only else "source-text",
            "selection_scope":"metadata" if meta_only else "line-range" if getattr(args,"start_line",None) is not None else "section" if args.section else "body",
            "context_warning":"A line range may omit enclosing conditions or table headers/notes." if getattr(args,"start_line",None) is not None else None,
            "next_offset":end if end<len(selected) else None,"selection_complete":end==len(selected),"contains_entire_selection":offset==0 and end==len(selected),
            "partial_line":(offset>0 and selected[offset-1]!="\n") or (end<len(selected) and selected[end-1]!="\n"),
            "text":chunk,"citation":str(self.file(path)),
            "warning":"Continue before asserting all conditions, table rows, or constraints." if end<len(selected) else None})
    def links(self,path,match,offset,limit):
        found=[]
        for m in re.finditer(r"!?\[([^\]\n]*)\]\((<[^>\n]+>|[^)\n]+)\)",self.text(path)):
            if match and match.casefold() not in (m.group(1)+" "+m.group(2)).casefold():continue
            href=m.group(2).strip("<>")
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:",href) or href.startswith("#"):target=href
            else:
                base=(self.root/Path(path).parent/unquote(href.split("#")[0])).resolve()
                target=base.relative_to(self.root).as_posix() if self.root in base.parents else "outside-package"
            found.append({"label":m.group(1),"target":target})
        return self.envelope({"path":path,"total":len(found),"offset":offset,"links":found[offset:offset+limit],
            "next_offset":offset+limit if offset+limit<len(found) else None})
    def source(self,source_id):
        if not re.fullmatch(r"src-\d{6}",source_id):raise ValueError("Invalid source ID")
        path="evidence/sources/"+source_id+".md";self.file(path)
        result={"source_id":source_id,"provenance_path":path};attachment=self.config.get("evidence_pack")
        if attachment:
            ep=self.skill_root/"evidence-packs"/attachment;man=load(ep/"evidence-manifest.json")
            if man.get("corpus_sources_sha256")==self.manifest.get("corpus_sources_sha256"):
                result["local_originals"]=[str(safe_path(ep,x["path"])) for x in man["files"] if source_id in x.get("source_ids",[])]
            else:result["evidence_limitation"]="Evidence pack belongs to another source register"
        result["inspection_policy"]="Locations only; open non-text files only on explicit request."
        return self.envelope(result)
def parser():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1],help="Installed research skill directory")
    p.add_argument("--snapshot",help="Pin the snapshot returned by first command")
    p.add_argument("--budget",type=int,default=None,help="Approximate character budget, not tokenizer units")
    sub=p.add_subparsers(dest="command",required=True);sub.add_parser("info")
    q=sub.add_parser("resolve");q.add_argument("identifier");q.add_argument("--offset",type=int,default=0);q.add_argument("--limit",type=int,default=10)
    q=sub.add_parser("search");q.add_argument("query")
    for key in ("kind","domain","message","namespace","collection","edition","source","status","under"):q.add_argument("--"+key)
    q.add_argument("--all-scopes",action="store_true");q.add_argument("--limit",type=int,default=5);q.add_argument("--offset",type=int,default=0)
    q=sub.add_parser("outline");q.add_argument("path");q.add_argument("--offset",type=int,default=0);q.add_argument("--limit",type=int,default=30)
    for cmd in ("read","metadata"):
        q=sub.add_parser(cmd);q.add_argument("path");q.add_argument("--section");q.add_argument("--offset",type=int,default=0)
        if cmd=="read":q.add_argument("--start-line",type=int);q.add_argument("--end-line",type=int)
    q=sub.add_parser("links");q.add_argument("path");q.add_argument("--match");q.add_argument("--offset",type=int,default=0);q.add_argument("--limit",type=int,default=15)
    q=sub.add_parser("source");q.add_argument("source_id")
    return p
def encode_result(result,budget):
    def encode():return json.dumps(result,ensure_ascii=False,separators=(",",":"))
    result["output_budget_chars"]=budget
    if len(encode())<=budget:return encode()
    result["output_reduced"]=True
    for key in ("records","headings","links"):
        if key in result:
            while len(result[key])>1 and len(encode())>budget:
                result[key].pop()
                result["next_offset"]=result.get("offset",0)+len(result[key])
            if key=="records":
                result["returned"]=len(result[key])
                if len(encode())>budget and result[key]:
                    r=result[key][0]
                    result[key][0]={k:v for k,v in r.items() if k in ("path","title","kind","domain","message_id","namespace","review_status")}
                    result[key][0]["details_omitted"]="Use read and metadata for this reference; search result exceeded budget."
    if "text" in result:
        if len(encode())>budget and len(json.dumps(result.get("metadata",{})))>800:
            result["metadata"]={"metadata_fields_truncated":["all"],"metadata_continuation":"Use metadata for this reference."}
        text=result["text"]
        if len(encode())>budget:
            original_next=result.get("next_offset")
            low=0;high=len(text)
            while low<high:
                mid=(low+high+1)//2;result["text"]=text[:mid]
                if len(encode())<=budget-180:low=mid
                else:high=mid-1
            end=low
            split=text.rfind("\n",0,end)
            if split>end//2:end=split+1
            result["text"]=text[:end]
            result["next_offset"]=result.get("offset",0)+end
            result["selection_complete"]=False
            result["contains_entire_selection"]=False
            result["partial_line"]=result.get("partial_line",False) or (end<len(text) and (end==0 or text[end-1]!="\n"))
            result["source_line_end"]=result["source_line_start"]+result["text"].count("\n") if isinstance(result.get("source_line_start"),int) else None
            result["warning"]="Continue this selection before asserting complete evidence."
    if len(encode())>budget:
        # Never silently truncate arbitrary structured facts.
        return json.dumps({"snapshot_id":result.get("snapshot_id"),"error":"Structured result exceeds budget",
                           "action":"Narrow the query or increase --budget; no complete result is being reported."},separators=(",",":"))
    return encode()

def main():
    args=parser().parse_args();corpus=None
    try:
        corpus=Corpus(args.root,args.snapshot);args.budget=args.budget if args.budget is not None else corpus.config.get("retrieval_budget_chars",12000)
        if not isinstance(args.budget,int) or isinstance(args.budget,bool) or not 3000<=args.budget<=60000:raise ValueError("Budget must be 3000 to 60000 characters")
        if hasattr(args,"limit") and not 1<=args.limit<=100:raise ValueError("Limit must be 1 to 100")
        if hasattr(args,"offset") and args.offset<0:raise ValueError("Offset must be nonnegative")
        cmd=args.command
        if cmd=="info":result=corpus.info()
        elif cmd=="resolve":result=corpus.resolve(args.identifier,args.offset,args.limit)
        elif cmd=="search":result=corpus.search(args.query,args)
        elif cmd=="outline":result=corpus.outline(args.path,args.offset,args.limit)
        elif cmd in ("read","metadata"):result=corpus.read(args.path,args,cmd=="metadata")
        elif cmd=="links":result=corpus.links(args.path,args.match,args.offset,args.limit)
        else:result=corpus.source(args.source_id)
        print(encode_result(result,args.budget))
    except (ValueError,OSError,sqlite3.Error,KeyError) as e:
        print(json.dumps({"error":str(e),"action":"Use a valid local snapshot or management; no automatic rebuild or download."},ensure_ascii=False));return 2
    finally:
        if corpus:corpus.close()
    return 0
if __name__=="__main__":raise SystemExit(main())
