"""Offline ISO 20022 retrieval. Python 3.10+, standard library only."""
import sys
sys.dont_write_bytecode = True
import argparse, hashlib, html, json, re, sqlite3, zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit
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
    if not re.fullmatch(r"[a-z]{4}\.\d{3}(?:\.\d{3}\.\d{2,})?",s):raise ValueError("Use an exact message ID or family; use resolve or --namespace for a full namespace")
    return s

def _unescape(value):
    return html.unescape(re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\]\\^_`{|}~])",r"\1",value))

def _label(value):
    return " ".join(_unescape(value).split()).casefold()

def _code_mask(text):
    """Keep source positions while hiding fenced/indented blocks and code spans."""
    chars=list(text);fence=None;position=0;blank=True;indented=False;list_indent=None
    for line in text.splitlines(keepends=True):
        content=re.sub(r"^(?: {0,3}>[ \t]?)+","",line)
        indent=len(content)-len(content.lstrip(' '))
        item=re.match(r'^( *)(?:[-+*]|[0-9]+[.)])([ \t]+)',content)
        if not fence and item:list_indent=item.end()
        elif not fence and content.strip() and list_indent is not None and indent<list_indent:list_indent=None
        relative=content[list_indent:] if list_indent is not None and indent>=list_indent else content
        marker=re.match(r"^ {0,3}(`{3,}|~{3,})(.*?)[\r\n]*$",relative)
        hide=False
        if fence:
            hide=True
            if marker and marker[1][0]==fence[0] and len(marker[1])>=fence[1] and not marker[2].strip():fence=None
        elif marker and (marker[1][0]!='`' or '`' not in marker[2]):
            fence=(marker[1][0],len(marker[1]));hide=True
        elif (blank or indented) and (relative.startswith('    ') or relative.startswith('\t')):
            indented=True;hide=True
        elif content.strip():indented=False
        if hide:
            for k in range(position,position+len(line)):
                if chars[k] not in '\r\n':chars[k]=' '
        blank=not content.strip();position+=len(line)
    masked=''.join(chars);i=0
    while i<len(masked):
        if masked[i]=='\\':i+=2;continue
        if masked[i]!='`':i+=1;continue
        end=i
        while end<len(masked) and masked[end]=='`':end+=1
        close=re.search(r'(?<!`)`{'+str(end-i)+r'}(?!`)',masked[end:])
        if close:
            last=end+close.end()
            for k in range(i,last):
                if chars[k] not in '\r\n':chars[k]=' '
            i=last
        else:i=end
    for comment in re.finditer(r'<!--(?:[\s\S]*?-->|[\s\S]*$)',''.join(chars)):
        for k in range(comment.start(),comment.end()):
            if chars[k] not in '\r\n':chars[k]=' '
    # XML declarations and JSON-valued table cells are evidence literals,
    # even when an author omitted a Markdown code fence around them.
    visible=''.join(chars)
    for literal in re.finditer(r'<([A-Za-z_][\w.-]*:[\w.-]+)\b[^>]*>[\s\S]*?</\1\s*>',visible):
        for k in range(literal.start(),literal.end()):
            if chars[k] not in '\r\n':chars[k]=' '
    visible=''.join(chars);i=0
    while i<len(visible):
        if visible[i]!='{':i+=1;continue
        depth=0;quoted=False;escaped=False;end=i
        while end<len(visible):
            c=visible[end]
            if quoted:
                if escaped:escaped=False
                elif c=='\\':escaped=True
                elif c=='"':quoted=False
            elif c=='"':quoted=True
            elif c=='{':depth+=1
            elif c=='}':
                depth-=1
                if depth==0:break
            end+=1
        if end<len(visible):
            try:value=json.loads(visible[i:end+1].replace('\\|','|'))
            except ValueError:value=None
            if isinstance(value,dict):
                for k in range(i,end+1):
                    if chars[k] not in '\r\n':chars[k]=' '
                i=end+1;continue
        i+=1
    return ''.join(chars)

def _bracket_end(text,start):
    depth=1;i=start+1
    while i<len(text):
        if text[i]=='\\':i+=2;continue
        if text[i]=='[':depth+=1
        elif text[i]==']':
            depth-=1
            if not depth:return i
        i+=1
    return None

def _destination(text,start):
    """Read an angle or balanced bare destination; return raw value and end."""
    i=start
    if i<len(text) and text[i]=='<':
        i+=1;begin=i
        while i<len(text):
            if text[i]=='\\':i+=2;continue
            if text[i] in '\r\n<':return None
            if text[i]=='>':return text[begin:i],i+1
            i+=1
        return None
    begin=i;depth=0
    while i<len(text):
        c=text[i]
        if c=='\\' and i+1<len(text):i+=2;continue
        if c.isspace():break
        if c=='(':
            depth+=1
        elif c==')':
            if depth==0:break
            depth-=1
        elif c=='<':return None
        i+=1
    return (text[begin:i],i) if depth==0 else None

def _title_end(text,start):
    if start>=len(text) or text[start] not in "\"'(":return None
    close=')' if text[start]=='(' else text[start];i=start+1
    while i<len(text):
        if text[i]=='\\':i+=2;continue
        if text[i]==close:return i+1
        if close==')' and text[i]=='(':return None
        i+=1
    return None

def _inline_destination(text,start):
    i=start
    while i<len(text) and text[i].isspace():i+=1
    parsed=_destination(text,i)
    if parsed is None:return None
    href,i=parsed;end=i
    while i<len(text) and text[i].isspace():i+=1
    if i<len(text) and text[i]==')':return href,i+1
    if i==end:return None
    title=_title_end(text,i)
    if title is None:return None
    i=title
    while i<len(text) and text[i].isspace():i+=1
    return (href,i+1) if i<len(text) and text[i]==')' else None

def markdown_links(text,destination_spans=False):
    """Extract inline/image and full/collapsed/shortcut reference links.

    This scanner never evaluates source text. Code, comments and tag attributes
    are not navigation. Destination escaping, titles and parentheses are kept
    separate from hrefs; fragment resolution is performed by the caller.
    """
    masked=_code_mask(text);definitions={};chars=list(masked);position=0;spans=[]
    frontmatter=re.match(r'\A---[ \t]*\r?\n[\s\S]*?\r?\n---[ \t]*(?:\r?\n|$)',text)
    if frontmatter:
        for k in range(frontmatter.end()):
            if chars[k] not in '\r\n':chars[k]=' '
        masked=''.join(chars)
    for line in masked.splitlines(keepends=True):
        m=re.match(r'^(?: {0,3}>[ \t]?)* {0,3}\[',line)
        if m:
            start=position+m.end()-1;end=_bracket_end(masked,start)
            if end is not None and masked[end+1:end+2]==':':
                i=end+2
                while i<len(masked) and masked[i].isspace():i+=1
                parsed=_destination(masked,i) if masked[end+2:i].count('\n')<=1 else None
                if parsed and parsed[0]:
                    href,last=parsed;line_end=masked.find('\n',last)
                    if line_end<0:line_end=len(masked)
                    rest=masked[last:line_end].strip();valid=not rest;finish=line_end
                    title_start=last
                    while title_start<len(masked) and masked[title_start].isspace():title_start+=1
                    if masked[last:title_start].count('\n')<=1:
                        title_end=_title_end(masked,title_start)
                        if title_end is not None:
                            title_line_end=masked.find('\n',title_end)
                            if title_line_end<0:title_line_end=len(masked)
                            if not masked[title_end:title_line_end].strip():valid=True;finish=title_line_end
                    if valid:
                        begin=i+(1 if masked[i:i+1]=='<' else 0)
                        spans.append((begin,begin+len(href),_unescape(href)))
                        definitions.setdefault(_label(text[start+1:end]),_unescape(href))
                        for k in range(position,finish):
                            if chars[k] not in '\r\n':chars[k]=' '
        position+=len(line)
    masked=''.join(chars);i=0
    while i<len(masked):
        if masked[i]=='\\':i+=2;continue
        if masked.startswith('<!--',i):
            end=masked.find('-->',i+4);i=len(masked) if end<0 else end+3;continue
        if masked[i]=='<':
            auto=re.match(r'<((?:https?://|mailto:)[^<>\s]+)>',masked[i:])
            if auto:
                href=_unescape(auto[1]);spans.append((i+1,i+1+len(auto[1]),href))
                if not destination_spans:yield href,href
                i+=auto.end();continue
            tag=re.match(r'</?[A-Za-z][A-Za-z0-9:_-]*(?:\s|/?>)',masked[i:])
            if tag:
                if masked[i+tag.end()-1]=='>':i+=tag.end();continue
                end=i+tag.end();quote=None
                while end<len(masked):
                    c=masked[end]
                    if quote:
                        if c==quote:quote=None
                    elif c in "\"'":quote=c
                    elif c=='>':end+=1;break
                    end+=1
                # The opening regex may already have consumed the final >.
                i=i+tag.end() if masked[i+tag.end()-1]=='>' else end;continue
        if masked[i]!='[':i+=1;continue
        end=_bracket_end(masked,i)
        if end is None:i+=1;continue
        label=text[i+1:end];after=end+1;href=None;finish=after
        if after<len(masked) and masked[after]=='(':
            parsed=_inline_destination(masked,after+1)
            if parsed:
                href,finish=parsed;begin=after+1
                while masked[begin:begin+1].isspace():begin+=1
                if masked[begin:begin+1]=='<':begin+=1
                spans.append((begin,begin+len(href),_unescape(href)));href=_unescape(href)
        if href is None and after<len(masked) and masked[after]=='[':
            refend=_bracket_end(masked,after)
            if refend is not None:
                key=masked[after+1:refend] or label
                href=definitions.get(_label(key));finish=refend+1
        if href is None:href=definitions.get(_label(label))
        if href is not None:
            if not destination_spans:yield _unescape(label),href
            i=finish
        else:i+=1
    if destination_spans:yield from sorted(set(spans))

def markdown_destinations(text):
    """Return source spans of hrefs only, including reference definitions.

    Start/end are Python character offsets in the original text. The third
    value is Markdown/entity-unescaped href text; source slices retain their
    original escapes. A publisher must preserve the surrounding syntax.
    """
    yield from markdown_links(text,destination_spans=True)

def verify_original(path,sha,size,source,sources):
    """Authenticate loose/extracted bytes or a registered ZIP's exact member."""
    occurrences=source.get('occurrences',[])
    if sha==source.get('sha256') and size==source.get('size_bytes'):
        return {'representation':'source-content','original_occurrences':occurrences}
    for occurrence in occurrences:
        member=occurrence.get('archive_member')
        if not member:continue
        container=next((s for s in sources if s.get('format')=='zip' and s.get('sha256')==sha and s.get('size_bytes')==size
            and any(o.get('path')==occurrence.get('path') and not o.get('archive_member') for o in s.get('occurrences',[]))),None)
        if container is None:continue
        try:
            with zipfile.ZipFile(path) as archive:
                matches=[info for info in archive.infolist() if info.filename==member]
                if len(matches)!=1:raise ValueError('Evidence archive member missing or ambiguous: '+member)
                h=hashlib.sha256();length=0
                with archive.open(matches[0]) as stream:
                    for block in iter(lambda:stream.read(1024*1024),b''):h.update(block);length+=len(block)
                if h.hexdigest()!=source.get('sha256') or length!=source.get('size_bytes'):
                    raise ValueError('Evidence archive member checksum or size mismatch: '+member)
                return {'representation':'archive-container','archive_source_id':container['source_id'],
                    'archive_member':member,'original_occurrences':occurrences}
        except (zipfile.BadZipFile,RuntimeError,NotImplementedError) as error:
            raise ValueError('Cannot verify evidence archive member: '+str(error)) from error
    raise ValueError('Evidence bytes do not match registered source '+str(source.get('source_id')))

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
        if self.config.get("evidence_pack") is not None and (not isinstance(self.config["evidence_pack"],str) or not re.fullmatch(r"[a-zA-Z0-9_-]{1,100}",self.config["evidence_pack"])):raise ValueError("Invalid evidence pack identifier")
        # A pinned reader does not depend on the current active pointer.
        if snapshot is None:
            active=load(safe_path(self.skill_root,"knowledge/active.json"))
            if not isinstance(active,dict) or type(active.get("format_version")) is not int or active["format_version"]!=1:
                raise ValueError("Unsupported or invalid active snapshot pointer")
            snapshot=active.get("snapshot_id")
        if not isinstance(snapshot,str) or not re.fullmatch(r"[a-zA-Z0-9_-]{1,100}",snapshot):
            raise ValueError("Invalid snapshot identifier")
        self.snapshot_id=snapshot
        self.root=safe_path(self.skill_root,"knowledge/snapshots/"+snapshot,must_exist=False)
        self.manifest=load(safe_path(self.root,"manifest.json"))
        if (not isinstance(self.manifest,dict) or type(self.manifest.get("format_version")) is not int
                or self.manifest["format_version"]!=1 or self.manifest.get("snapshot_id")!=self.snapshot_id):
            raise ValueError("Unsupported or mismatched manifest")
        index=safe_path(self.root,"index.sqlite")
        self.db=sqlite3.connect(index.as_uri()+"?mode=ro",uri=True);self.db.row_factory=sqlite3.Row
        self.db.execute("PRAGMA query_only=ON")
        try:
            info=dict(self.db.execute("SELECT key,value FROM info"))
            if info.get("snapshot_id")!=self.snapshot_id or info.get("format_version")!="1":raise ValueError("Index belongs to another snapshot")
        except Exception:
            self.db.close();raise
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
    def content(self,path):
        text=self.text(path);fallback,body,line=metadata(text)
        row=self.db.execute("SELECT metadata FROM documents WHERE path=?",(path,)).fetchone()
        # The publisher parses full YAML. Keep its typed metadata instead of
        # reparsing valid flow arrays or nested objects with a scalar fallback.
        if row and not isinstance(row[0],str):raise ValueError("Invalid indexed document metadata: "+path)
        meta=json.loads(row[0]) if row else fallback
        if not isinstance(meta,dict):raise ValueError("Invalid indexed document metadata: "+path)
        return text,meta,body,line
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
        supplied=identifier.strip()
        namespace_query=bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:",supplied))
        if namespace_query:
            key=supplied;exact=True
            rows=self.db.execute("SELECT d.* FROM documents d WHERE d.kind='message-index' AND EXISTS "
                "(SELECT 1 FROM tags t WHERE t.doc_id=d.id AND t.key='namespace' AND t.value=?) ORDER BY d.message_id",(key,)).fetchall()
            rows=[row for row in rows if json.loads(row["metadata"]).get("namespace")==key]
        else:
            key=normalize(supplied);exact=len(key.split("."))==4;column="message_id" if exact else "family"
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
            " ORDER BY CASE WHEN d.title=? COLLATE NOCASE THEN 0 ELSE 1 END,bm25(search,5.0,1.0),d.path LIMIT ? OFFSET ?",params+[query.strip(),args.limit,args.offset]).fetchall()
        records=[]
        for row in rows:
            _,_,body,body_line=self.content(row["path"])
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
        text,m,body,body_line=self.content(path);start_line=body_line
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
        for label,href in markdown_links(metadata(self.text(path))[1]):
            if match and match.casefold() not in (label+" "+href).casefold():continue
            item={"label":label}
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:",href) or href.startswith("//"):
                item["target"]=href
            else:
                parts=urlsplit(href)
                base=(self.root/Path(path).parent/unquote(parts.path)).resolve() if parts.path else self.root/Path(path)
                if self.root not in base.parents:
                    item["target"]="outside-package"
                else:
                    item["path"]=base.relative_to(self.root).as_posix()
                    item["target"]=(item["path"] if parts.path else "")+("?"+parts.query if parts.query else "")
                    if "#" in href:
                        item["fragment"]=parts.fragment;item["target"]+="#"+parts.fragment
                    if not item["target"]:item["target"]=item["path"]
            found.append(item)
        return self.envelope({"path":path,"total":len(found),"offset":offset,"links":found[offset:offset+limit],
            "next_offset":offset+limit if offset+limit<len(found) else None})
    def source(self,source_id):
        if not re.fullmatch(r"src-\d{6}",source_id):raise ValueError("Invalid source ID")
        path="evidence/sources/"+source_id+".md";self.file(path)
        result={"source_id":source_id,"provenance_path":path};attachment=self.config.get("evidence_pack")
        if attachment:
            ep=safe_path(self.skill_root,"evidence-packs/"+attachment,must_exist=False)
            man=load(safe_path(ep,"evidence-manifest.json"))
            if not isinstance(man,dict):raise ValueError("Invalid evidence manifest")
            if man.get("corpus_sources_sha256")!=self.manifest.get("corpus_sources_sha256"):
                result["evidence_limitation"]="Evidence pack belongs to another source register"
            else:
                register_path=self.file("catalog/sources.json")
                if digest(register_path)!=self.manifest.get("corpus_sources_sha256"):
                    raise ValueError("Snapshot source register fingerprint mismatch")
                register=json.loads(self.text("catalog/sources.json"))
                sources=register.get("sources") if isinstance(register,dict) else None
                if not isinstance(sources,list) or any(not isinstance(x,dict) for x in sources):
                    raise ValueError("Invalid packaged source register")
                by_id={x.get("source_id"):x for x in sources}
                if len(by_id)!=len(sources) or source_id not in by_id:raise ValueError("Unregistered source identity")
                entries=man.get("files")
                if not isinstance(entries,list):raise ValueError("Invalid evidence file inventory")
                originals=[];verified=[]
                for entry in entries:
                    if not isinstance(entry,dict) or not isinstance(entry.get("source_ids"),list) or any(not isinstance(x,str) for x in entry["source_ids"]):
                        raise ValueError("Invalid evidence source identities")
                    if source_id not in entry["source_ids"]:continue
                    if any(sid not in by_id for sid in entry["source_ids"]):raise ValueError("Unregistered evidence source identity")
                    original=safe_path(ep,entry.get("path"))
                    if (not isinstance(entry.get("sha256"),str) or not re.fullmatch(r"[0-9a-fA-F]{64}",entry["sha256"])
                            or type(entry.get("size")) is not int or entry["size"]<0):
                        raise ValueError("Invalid evidence fingerprint")
                    actual=digest(original);size=original.stat().st_size
                    if size!=entry["size"] or actual!=entry["sha256"].lower():
                        raise ValueError("Evidence file checksum or size mismatch: "+entry["path"])
                    identities={sid:verify_original(original,actual,size,by_id[sid],sources) for sid in set(entry["source_ids"])}
                    if str(original) not in originals:
                        originals.append(str(original));verified.append({"path":str(original),"sha256":actual,"size":size,
                            "source_id":source_id,"source_sha256":by_id[source_id]["sha256"],**identities[source_id]})
                result["local_originals"]=originals;result["local_original_evidence"]=verified
                if not originals:result["evidence_limitation"]="No verified local original supplied for this source"
        result["inspection_policy"]="Verified byte identity and locations only; content inspection requires an explicit request."
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
