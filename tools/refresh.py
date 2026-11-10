"""Scoped source discovery and refresh bookkeeping; never a conversion pipeline."""
from __future__ import annotations
import copy, datetime, hashlib, io, json, re, zipfile
from pathlib import Path, PurePosixPath
import kb

SCHEMA_VERSION = 1
MID = re.compile(r"^[a-z]{4}\.\d{3}\.\d{3}\.\d{2,}$")
ROUTE_FIELDS = ("collection", "domain", "set_slug", "set_title", "source_edition",
                "edition_basis", "edition_locator", "edition_slug", "set_path")
def digest_bytes(data): return hashlib.sha256(data).hexdigest()
def fingerprint(path): return digest_bytes(path.read_bytes()) if path.exists() else None
def json_hash(value): return digest_bytes(json.dumps(value, sort_keys=True, ensure_ascii=False).encode())
def read_json(path, default=None):
    return json.loads(path.read_text(encoding="utf-8-sig")) if path.exists() else copy.deepcopy(default)
def safe_path(root, relative):
    root = Path(root).resolve()
    p = (root / relative).resolve()
    if not p.is_relative_to(root): raise ValueError("Path escapes repository: " + str(relative))
    return p
def baseline(root):
    return {key: fingerprint(root / path) for key, path in (
        ("sources", "catalog/sources.json"), ("jobs", "tracking/jobs.json"),
        ("issues", "tracking/issues.md"), ("conversion_status", "tracking/conversion-status.md"),
        ("checkpoint", "tracking/checkpoint.json"))}
def location(o):
    return (o["path"], o.get("archive_member"), o.get("archive_sha256"))
def old_sources(root): return read_json(root/"catalog/sources.json", {"sources":[]})["sources"]
def route_from_source(s): return {k: copy.deepcopy(s[k]) for k in ROUTE_FIELDS if k in s}
def default_route(path, member=None):
    parts = PurePosixPath(path).parts
    collection = parts[1] if len(parts) > 1 else None
    known = kb.COLLECTIONS.get(collection)
    if not known: return {"collection":collection, "domain":None, "set_slug":None,
                          "set_title":collection, "source_edition":None,
                          "edition_basis":"Collection routing requires evidence"}
    domain, slug, title, _ = known
    if member:
        for name, (d, _, _) in kb.T2S.items():
            if "_" + name + "_MessageSet/" in member:
                domain, slug, title = d, "t2s-"+kb.slug(name), "T2S "+name
                break
    return {"collection":collection, "domain":domain, "set_slug":slug, "set_title":title,
            "source_edition":None, "edition_basis":"No publication edition established for these bytes"}
def scan(root, paths=None):
    """Complete internal scan; bounded presentation is handled by the CLI."""
    root = Path(root).resolve(); prior = old_sources(root)
    by_hash = {s["sha256"]:s for s in prior}
    by_location = {}
    for s in prior:
        for o in s.get("occurrences", []):
            by_location.setdefault((o["path"],o.get("archive_member")), []).append(s)
    candidates = {}; exclusions = []; errors = []; scanned_paths = []
    def add(stream, path, member=None, parent_sha=None):
        h=hashlib.sha256(); size=0; chunks=[]
        fmt=Path(member or path).suffix.lower().lstrip(".")
        for block in iter(lambda:stream.read(1024*1024), b""):
            h.update(block);size+=len(block)
            if fmt=="xsd":chunks.append(block)
        sha=h.hexdigest(); previous=by_hash.get(sha)
        occ={"path":path,"archive_member":member,"sha256":sha,"size_bytes":size,"availability":"current"}
        if parent_sha:occ["archive_sha256"]=parent_sha
        existing=by_location.get((path,member),[])
        identical_location=next((s for s in existing if s["sha256"]==sha),None)
        route=route_from_source(identical_location) if identical_location else default_route(path,member)
        occ["membership"]=route
        c=candidates.setdefault(sha,{"key":sha,"source_id":previous["source_id"] if previous else None,
            "sha256":sha,"format":fmt,"size_bytes":size,"message_ids":copy.deepcopy(previous.get("message_ids",[])) if previous else [],
            "namespace":previous.get("namespace") if previous else None,"roots":previous.get("roots",[]) if previous else [],
            "occurrences":[],"routing":route,"status":"unchanged" if previous else "new-content",
            "replaces_source_ids":[],"limitations":[]})
        c["occurrences"].append(occ)
        c["replaces_source_ids"]=sorted(set(c["replaces_source_ids"]+[s["source_id"] for s in existing if s["sha256"]!=sha]))
        if c["replaces_source_ids"]:c["status"]="changed-location"
        elif previous and not identical_location:c["status"]="added-occurrence"
        if fmt=="xsd":
            try:
                from lxml import etree as E
                tr=E.fromstring(b"".join(chunks), E.XMLParser(resolve_entities=False,no_network=True))
                ns=tr.get("targetNamespace");tail=(ns or "").rsplit(":",1)[-1]
                c.update(namespace=ns,message_ids=[tail] if MID.fullmatch(tail) else [],
                         roots=[e.get("name") for e in tr.findall("{"+kb.XS+"}element")],
                         schema_attributes=dict(tr.attrib),
                         schema_dependencies=[{"kind":E.QName(e).localname,**dict(e.attrib)}
                             for e in tr if isinstance(e.tag,str) and E.QName(e).localname in ("import","include","redefine","override")])
            except Exception as exc:c["limitations"].append("Cannot inspect schema: "+str(exc))
        elif not previous and fmt in ("pdf","docx","xlsx","json"):
            c["limitations"].append("Publication/message coverage needs source inspection and evidence-backed routing.")
        return sha
    raw=root/"raw-input"
    for p in sorted(raw.rglob("*")) if raw.exists() else []:
        if not p.is_file():continue
        rel=p.relative_to(root).as_posix()
        if paths and not any(rel==x.rstrip("/") or rel.startswith(x.rstrip("/")+"/") for x in paths):continue
        if p.name.lower()=="readme.md":
            exclusions.append({"path":rel,"reason":"Workspace navigation"});continue
        safe_path(raw,p.relative_to(raw))
        scanned_paths.append(rel)
        try:
            with p.open("rb") as f:sha=add(f,rel)
            if p.suffix.lower()==".zip":
                with zipfile.ZipFile(p) as z:
                    for info in sorted(z.infolist(),key=lambda x:x.filename):
                        name=info.filename
                        if info.is_dir():continue
                        pp=PurePosixPath(name.replace("\\","/"))
                        if pp.is_absolute() or ".." in pp.parts or re.match(r"^[A-Za-z]:",name):
                            errors.append({"path":rel,"member":name,"error":"Unsafe archive member"});continue
                        with z.open(info) as f:add(f,rel,name,sha)
        except Exception as exc:errors.append({"path":rel,"error":str(exc)})
    def in_scope(path):
        return not paths or any(path==x.rstrip("/") or path.startswith(x.rstrip("/")+"/") for x in paths)
    observed_locations={(o["path"],o.get("archive_member")) for c in candidates.values() for o in c["occurrences"]}
    missing=[]
    for s in prior:
        absent=[o for o in s.get("occurrences",[]) if in_scope(o["path"]) and (o["path"],o.get("archive_member")) not in observed_locations]
        if absent:
            missing.append({"source_id":s["source_id"],"sha256":s["sha256"],"occurrences":absent})
            if s["sha256"] not in candidates:
                candidates[s["sha256"]]={"key":s["sha256"],"source_id":s["source_id"],"sha256":s["sha256"],
                    "format":s["format"],"size_bytes":s.get("size_bytes"),"message_ids":s.get("message_ids",[]),
                    "namespace":s.get("namespace"),"roots":s.get("roots",[]),"occurrences":[],
                    "routing":route_from_source(s),"status":"missing","replaces_source_ids":[],
                    "limitations":["Previously registered content is unavailable in the scanned scope."]}
    rows=sorted(candidates.values(),key=lambda c:(c.get("source_id") or "z",c["key"]))
    evidence=sorted([{"key":c["key"],"occurrences":[{k:v for k,v in o.items() if k not in ("membership","availability")} for o in c["occurrences"]]} for c in rows],key=lambda x:x["key"])
    return {"schema_version":1,"kind":"refresh-scan","root":str(root),"baseline":baseline(root),
            "scan_fingerprint":json_hash(evidence),"scanned_scope":paths or ["raw-input"],
            "candidates":rows,"total":len(rows),"truncated":False,"missing_occurrences":missing,
            "excluded":exclusions,"errors":errors,
            "limitations":["New document publication/coverage metadata must be verified before targeting it."]}
def bounded(report,limit=20):
    result=copy.deepcopy(report); limit=max(1,min(limit,1000))
    rows=sorted(result.get("candidates",[]),key=lambda c:(c["status"]=="unchanged",c["status"],c["key"]));result["candidates"]=rows[:limit]
    import collections
    result["counts_by_status"]=dict(collections.Counter(c["status"] for c in rows))
    result["total"]=len(rows);result["truncated"]=len(rows)>limit
    return result
def canonical_schemas(root, sources=None):
    """Existing coverage binds identity; ambiguous new candidates are not selected."""
    ss=old_sources(root) if sources is None else sources
    byid={s["source_id"]:s for s in ss}; groups={};chosen={};conflicts=[]
    for s in ss:
        if s.get("format")=="xsd":
            for mid in s.get("message_ids",[]):groups.setdefault(mid,[]).append(s)
    for pattern in ("shared/reference/messages/*/schema-coverage.json","domains/*/reference/messages/*/schema-coverage.json"):
        for p in root.glob(pattern):
            c=read_json(p);s=byid.get(c.get("source_id"));mid=c.get("message_id")
            if not s or s["sha256"]!=c.get("sha256") or s.get("namespace")!=c.get("namespace"):
                conflicts.append({"message_id":mid,"reason":"Canonical coverage binding is unavailable or inconsistent","path":p.relative_to(root).as_posix()});continue
            if mid in chosen and chosen[mid]["source_id"]!=s["source_id"]:
                conflicts.append({"message_id":mid,"reason":"Multiple existing canonical bindings"});chosen.pop(mid,None);continue
            chosen[mid]=s
    for mid,group in groups.items():
        distinct={s["sha256"] for s in group}
        if mid not in chosen and len(distinct)==1 and not any(x["message_id"]==mid for x in conflicts):chosen[mid]=group[0]
        if len(distinct)>1:
            conflicts.append({"message_id":mid,"canonical_source_id":chosen.get(mid,{}).get("source_id"),
                              "candidate_source_ids":[s["source_id"] for s in group],
                              "reason":"Different supplied bytes claim the same exact definition; no automatic replacement"})
    return chosen,conflicts
def routing_valid(route):
    if route.get("domain") not in ("shared","payments","securities","cards","trade-finance","fx"):return False
    if not route.get("set_slug") or not route.get("collection"):return False
    if route.get("source_edition") and not route.get("edition_basis"):return False
    return True
def impact(root,message=None,set_slug=None,edition=None,scan_report=None,routing=None):
    root=Path(root).resolve()
    if bool(message)==bool(set_slug):raise ValueError("Select an exact message OR a publication set and edition")
    if message and not MID.fullmatch(message):raise ValueError("A full exact message identifier is required; select a family member first")
    if set_slug and not edition:raise ValueError("A publication edition must be selected explicitly")
    report=copy.deepcopy(scan_report) if scan_report else scan(root)
    if report.get("truncated"):raise ValueError("A truncated scan cannot establish scope; omit --scan to scan completely")
    if report.get("baseline")!=baseline(root):raise ValueError("Stale scan baseline; scan again")
    routing=routing or {}
    for c in report["candidates"]:
        override=routing.get(c["key"],routing.get(c.get("source_id"),{}))
        if override:
            c["routing"].update({k:v for k,v in override.items() if k in ROUTE_FIELDS})
            if override.get("message_ids"):
                if c["format"]=="xsd" and override["message_ids"]!=c["message_ids"]:raise ValueError("Schema identity is established by its namespace")
                if not override.get("edition_locator"):raise ValueError("Message coverage override requires a precise source locator")
                c["message_ids"]=override["message_ids"]
    def match(c):
        r=c["routing"]
        if message:return message in c.get("message_ids",[])
        return r.get("set_slug")==set_slug and edition in (r.get("source_edition"),r.get("edition_slug"),PurePosixPath(r.get("set_path","")).name)
    selected={c["key"]:c for c in report["candidates"] if match(c)}
    if not selected:raise ValueError("No evidence-mapped source matches the target; inspect sources and supply --routing metadata")
    import catalog
    rr=list(catalog.records(root));by_path={r["path"]:r for r in rr}
    sid_to_key={c["source_id"]:c["key"] for c in report["candidates"] if c.get("source_id")}
    candidate_map={c["key"]:c for c in report["candidates"]}
    affected={};queue=[];limits=list(report.get("limitations",[]))
    def affect(r,why):
        if r["path"] not in affected:affected[r["path"]]={"path":r["path"],"reasons":[why]};queue.append(r)
        elif why not in affected[r["path"]]["reasons"]:affected[r["path"]]["reasons"].append(why)
    selected_ids={c.get("source_id") for c in selected.values()}-{None}
    for r in rr:
        ids=set(r.get("message_ids",[]))|({r["message_id"]} if r.get("message_id") else set())
        if message and message in ids:affect(r,{"kind":"exact-message","message_id":message})
        if not message and selected_ids & set(r.get("source_ids",[])):affect(r,{"kind":"selected-source","source_ids":sorted(selected_ids & set(r.get("source_ids",[])))})
    # Explicit ID references establish graph edges. Navigation links and equal labels do not.
    identities={}
    for r in rr:
        for k in ("participant_id","flow_id","concept_id","component_id"):
            if r.get(k):identities.setdefault(r[k],[]).append(r)
    def ref_ids(r):
        values=[]
        for k in ("participant_ids","participants","flow_ids","flows","concept_ids","component_ids","depends_on"):
            for v in r.get(k,[]) if isinstance(r.get(k,[]),list) else []:
                if isinstance(v,str):values.append(v)
        for rel in r.get("relationships",[]) if isinstance(r.get("relationships",[]),list) else []:
            if isinstance(rel,dict) and rel.get("target_id"):values.append(rel["target_id"])
        return set(values)
    reverse={}
    for r in rr:
        for key in ref_ids(r):reverse.setdefault(key,[]).append(r)
    while queue:
        r=queue.pop(0)
        for sid in r.get("source_ids",[]):
            if sid in sid_to_key:selected[sid_to_key[sid]]=candidate_map[sid_to_key[sid]]
            else:limits.append("Affected reference "+r["path"]+" names an unavailable/unscanned source "+sid)
        for key in ref_ids(r):
            for dep in identities.get(key,[]):affect(dep,{"kind":"explicit-reference","from":r["path"],"identifier":key})
        for k in ("participant_id","flow_id","concept_id","component_id"):
            if r.get(k):
                for consumer in reverse.get(r[k],[]):affect(consumer,{"kind":"shared-consumer","from":r["path"],"identifier":r[k]})
    # Supplied schema dependencies and parent archives are necessary selected provenance.
    changed=True
    while changed:
        changed=False
        for c in list(selected.values()):
            for o in c["occurrences"]:
                parent=o.get("archive_sha256")
                if parent in candidate_map and parent not in selected:selected[parent]=candidate_map[parent];changed=True
            for dep in c.get("schema_dependencies",[]):
                loc=dep.get("schemaLocation");matches=[]
                if loc and not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:",loc):
                    for o in c["occurrences"]:
                        base=PurePosixPath(o.get("archive_member") or o["path"]).parent
                        target=str(base / loc)
                        import posixpath
                        target=posixpath.normpath(target)
                        for x in report["candidates"]:
                            if x.get("format")!="xsd":continue
                            if any((xo["path"]==o["path"] and xo.get("archive_member")==target) if o.get("archive_member")
                                   else (not xo.get("archive_member") and xo["path"]==target) for xo in x["occurrences"]):matches.append(x)
                if not loc and dep.get("namespace"):
                    matches=[x for x in report["candidates"] if x.get("format")=="xsd" and x.get("namespace")==dep["namespace"]]
                matches={x["key"]:x for x in matches}
                if len(matches)==1:
                    key,x=next(iter(matches.items()))
                    if key not in selected:selected[key]=x;changed=True
                else:limits.append("Unresolved or ambiguous local schema dependency for "+c["key"]+": "+str(dep))
    for c in selected.values():
        if not routing_valid(c["routing"]):limits.append("Unresolved routing for selected source "+c["key"])
    source_keys=set(selected)
    deferred=[{"key":c["key"],"source_id":c.get("source_id"),"status":c["status"],"message_ids":c["message_ids"],
               "paths":sorted({o["path"] for o in c["occurrences"]})} for c in report["candidates"] if c["key"] not in source_keys and c["status"]!="unchanged"]
    return {"schema_version":1,"kind":"refresh-selection","root":str(root),
            "target":{"message":message} if message else {"set":set_slug,"edition":edition},
            "baseline":report["baseline"],"scan_fingerprint":report["scan_fingerprint"],
            "scanned_scope":report.get("scanned_scope",["raw-input"]),"candidates":list(selected.values()),
            "verified_routing":{key:c["routing"] for key,c in selected.items()},
            "affected":list(affected.values()),
            "reference_fingerprints":{p:fingerprint(root/p) for p in affected},
            "deferred":deferred,"limitations":sorted(set(limits)),
            "scope":"Selected evidence and explicit dependencies only; not all raw inputs."}
def selection_sources(root,selection):
    keys={c["key"] for c in selection["candidates"]}
    return [s for s in old_sources(root) if s["sha256"] in keys]
def check_selection(root,selection,allow_applied=False):
    if selection.get("kind")!="refresh-selection" or selection.get("schema_version")!=1:raise ValueError("Unsupported selection manifest")
    if Path(selection["root"]).resolve()!=Path(root).resolve():raise ValueError("Selection belongs to another repository")
    if not allow_applied and selection["baseline"]!=baseline(root):raise ValueError("Stale selection baseline; rescan before writing")
    fresh=scan(root, None if selection.get("scanned_scope")==["raw-input"] else selection.get("scanned_scope"))
    if fresh["scan_fingerprint"]!=selection["scan_fingerprint"]:raise ValueError("Raw inputs changed since selection; rescan before writing")
    selected_paths={o["path"] for c in selection["candidates"] for o in c.get("occurrences",[])}
    relevant_errors=[e for e in fresh["errors"] if e["path"] in selected_paths]
    if relevant_errors:raise ValueError("Selected source scan incomplete: "+str(relevant_errors))
    if not allow_applied:
        for path,sha in selection.get("reference_fingerprints",{}).items():
            if fingerprint(safe_path(root,path))!=sha:raise ValueError("Affected reference changed since selection: "+path)
    return fresh
def route_path(route,sid):
    if route.get("set_path"):return route["set_path"]
    edition=route.get("edition_slug") or (kb.slug(route["source_edition"]) if route.get("source_edition") else "edition-unknown-"+sid)
    return kb.area(route["domain"])+"/reference/message-sets/"+route["set_slug"]+"/"+edition
def source_register(root,ss):
    page=root/"tracking/source-register.md"
    rows=[[s["source_id"],kb.source_link(root,page,s),s["format"],s["sha256"],
           len(s.get("occurrences",[])),s.get("set_title","Unresolved"),", ".join(s.get("message_ids",[])),s.get("disposition","queued")] for s in ss]
    kb.put(page,"# Source register\n\nDerived from maintained source identities. Historical occurrences retain provenance; current copies are verified by checksum.\n\n"+
           kb.table(["ID","Original","Format","SHA-256","Occurrences","Collection","Exact IDs","Disposition"],rows))
def _register(root,selection,job):
    root=Path(root).resolve()
    if not re.fullmatch(r"job-\d{6,}",job):raise ValueError("Use a registered-format job ID")
    reportpath=root/"tracking/refresh"/job/"selection.json"
    previous=read_json(reportpath)
    if previous and previous.get("request_hash")==json_hash(selection):
        check_selection(root,selection,True)
        registered={s["source_id"]:s["sha256"] for s in old_sources(root)}
        selected_hashes={c["sha256"] for c in previous["candidates"]}
        if any(registered.get(sid) not in selected_hashes for sid in previous["selected_source_ids"]):
            raise ValueError("Registered selected identities changed; inspect the existing refresh job")
        return {"job_id":job,"selected_source_ids":previous["selected_source_ids"],"conflicts":previous.get("conflicts",[]),
                "report_path":reportpath.relative_to(root).as_posix(),"reused":True}
    fresh=check_selection(root,selection)
    ss=copy.deepcopy(old_sources(root));byhash={s["sha256"]:s for s in ss};nextid=max([int(s["source_id"][4:]) for s in ss] or [0])+1
    jobs=read_json(root/"tracking/jobs.json",{"jobs":[]})
    historical_ids={j["job_id"] for j in jobs["jobs"]}
    for tracked in ("conversion-status.md","issues.md","checkpoint.json"):
        file=root/"tracking"/tracked
        if file.exists():historical_ids.update(re.findall(r"job-\d{6,}",file.read_text(encoding="utf-8")))
    for directory in (root/"tracking/history",root/"tracking/refresh"):
        if directory.exists():historical_ids.update(p.name for p in directory.iterdir() if re.fullmatch(r"job-\d{6,}",p.name))
    if job in historical_ids:raise ValueError("Existing unrelated job ID; choose the next unused ID")
    if int(job[4:])<=max([int(j[4:]) for j in historical_ids] or [0]):raise ValueError("Job IDs cannot be recycled")
    chosen=[];selectedhashes={c["key"] for c in selection["candidates"]}
    all_now={c["key"]:c for c in fresh["candidates"]}
    for candidate in selection["candidates"]:
        c=copy.deepcopy(candidate);actual=all_now.get(c["key"])
        if not actual:raise ValueError("Selected content is absent from the fresh inventory")
        for field in ("key","sha256","format","size_bytes"):
            if c.get(field)!=actual.get(field):raise ValueError("Selection changed immutable source identity: "+field)
        if c["format"]=="xsd":
            for field in ("namespace","message_ids","roots","schema_attributes","schema_dependencies"):
                if c.get(field)!=actual.get(field):raise ValueError("Schema identity must come from supplied bytes: "+field)
        route=selection.get("verified_routing",{}).get(c["key"],{})
        if not routing_valid(route):raise ValueError("Resolve routing before registration: "+c["key"])
        # A changed source gets a new identity, never a modified old checksum.
        s=byhash.get(c["key"])
        if s is None:
            sid=f"src-{nextid:06d}";nextid+=1
            s={"source_id":sid,"sha256":c["key"],"format":c["format"],"size_bytes":c["size_bytes"],
               "occurrences":[],"publication":None,"message_ids":c.get("message_ids",[]),"review_status":"draft",
               "disposition":"queued","limitations":list(c.get("limitations",[]))}
            s.update({k:v for k,v in route.items() if k in ROUTE_FIELDS});s["set_path"]=route_path(route,sid)
            for k in ("namespace","roots","schema_attributes","schema_dependencies"):
                if k in c:s[k]=c[k]
            ss.append(s);byhash[c["key"]]=s
        sid=s["source_id"];chosen.append(sid)
        for historical in s.get("occurrences",[]):
            if historical.get("archive_member") and not historical.get("archive_sha256"):
                parents=[parent for parent in ss if parent.get("format")=="zip" and any(x["path"]==historical["path"] and not x.get("archive_member") for x in parent.get("occurrences",[]))]
                if len(parents)==1:
                    historical["archive_sha256"]=parents[0]["sha256"];historical["archive_source_id"]=parents[0]["source_id"]
        membership={**route,"set_path":route_path(route,sid)}
        safe_path(root,membership["set_path"])
        if not membership["set_path"].startswith(("shared/reference/","domains/")):raise ValueError("Invalid output route")
        current=all_now[c["key"]]["occurrences"]
        for old in s.get("occurrences",[]):
            if any(location(old)==location(o) for o in current):old["availability"]="current"
            elif any(old["path"]==o["path"] and old.get("archive_member")==o.get("archive_member") for x in fresh["candidates"] for o in x["occurrences"]):old["availability"]="changed"
            elif fresh["scanned_scope"]==["raw-input"] or any(old["path"]==p or old["path"].startswith(p.rstrip("/")+"/") for p in fresh["scanned_scope"]):old["availability"]="missing"
        for o in current:
            o=copy.deepcopy(o);o.pop("membership",None)
            old=next((x for x in s["occurrences"] if location(x)==location(o)),None)
            o["membership"]=copy.deepcopy(old.get("membership") or route_from_source(s)) if old else membership
            if old:old.update(o)
            else:s["occurrences"].append(o)
        s["current_occurrences_available"]=any(o.get("availability","current")=="current" for o in s["occurrences"])
        memberships=s.setdefault("memberships",[route_from_source(s)])
        if membership not in memberships:memberships.append(membership)
        s["job_ids"]=list(dict.fromkeys(s.get("job_ids",[])+[job]))
        if c.get("replaces_source_ids"):
            s["replaces_source_ids"]=sorted(set(s.get("replaces_source_ids",[])+c["replaces_source_ids"]))
            for oldid in c["replaces_source_ids"]:
                old=next(x for x in ss if x["source_id"]==oldid)
                old["replacement_candidates"]=sorted(set(old.get("replacement_candidates",[])+[sid]))
                for o in old.get("occurrences",[]):
                    if any(o["path"]==n["path"] and o.get("archive_member")==n.get("archive_member") for n in current):o["availability"]="changed"
                old["current_occurrences_available"]=any(o.get("availability","current")=="current" for o in old.get("occurrences",[]))
        if not s["current_occurrences_available"]:s["limitations"]=list(dict.fromkeys(s.get("limitations",[])+["Registered bytes are currently unavailable; historical evidence is retained."]))
    for s in ss:
        for o in s.get("occurrences",[]):
            if o.get("archive_sha256") in byhash:o["archive_source_id"]=byhash[o["archive_sha256"]]["source_id"]
    _,allconflicts=canonical_schemas(root,ss)
    conflicts=[c for c in allconflicts if set(c.get("candidate_source_ids",[])) & set(chosen) or c.get("canonical_source_id") in chosen]
    for c in conflicts:
        for sid in c.get("candidate_source_ids",[]):
            if sid in chosen and sid!=c.get("canonical_source_id"):next(s for s in ss if s["source_id"]==sid)["disposition"]="conflicting-candidate"
    if selection["baseline"]!=baseline(root):raise ValueError("Register changed while preparing the refresh; rescan before writing")
    kb.set_write_context(root,job)
    manifest=read_json(root/"catalog/sources.json",{"schema_version":1,"sources":[]})
    manifest.update(updated=kb.DATE,sources=sorted(ss,key=lambda s:s["source_id"]))
    kb.dump(root/"catalog/sources.json",manifest)
    jobrow={"job_id":job,"scope":selection["target"],"source_ids":chosen,"status":"in-progress",
            "last_updated":kb.DATE,"processing_complete_to_recorded_limits":False,
            "next_action":"Extract/reuse selected evidence, curate affected references, then validate and record actual review."}
    jobs["jobs"].append(jobrow);kb.dump(root/"tracking/jobs.json",jobs)
    progress_markdown(root,job,selection["target"],"in-progress",jobrow["next_action"])
    for c in conflicts:c["issue_id"]=append_issue(root,job,"Conflicting exact definition "+str(c.get("message_id")),c)
    applied=copy.deepcopy(selection);applied.update(job_id=job,selected_source_ids=chosen,conflicts=conflicts,
        request_hash=json_hash(selection),registered_manifest_sha256=fingerprint(root/"catalog/sources.json"))
    kb.dump(reportpath,applied)
    kb.dump(root/"tracking/refresh"/job/"report.json",{"date":kb.DATE,"job_id":job,"target":selection["target"],
        "status":"in-progress","selected_source_ids":chosen,"conflicts":conflicts,"deferred":selection.get("deferred",[]),
        "completed_work":[{"action":"registered-selected-source-identities","source_ids":chosen}],
        "known_gaps":selection.get("limitations",[]),"next_action":jobrow["next_action"],
        "scope":"Selected refresh only; substantive extraction/review remains."})
    source_register(root,ss)
    checkpoint(root,job,applied,jobrow["next_action"])
    return {"job_id":job,"selected_source_ids":chosen,"conflicts":conflicts,
            "report_path":reportpath.relative_to(root).as_posix(),"reused":False}
def append_issue(root,job,title,evidence):
    p=root/"tracking/issues.md";text=p.read_text(encoding="utf-8") if p.exists() else "# Issues\n"
    marker="refresh-evidence:"+json_hash(evidence)
    if marker in text:
        before=text[:text.index(marker)]
        found=re.findall(r"issue-\d+",before)
        return found[-1] if found else None
    number=max([int(x) for x in re.findall(r"issue-(\d+)",text)] or [0])+1
    body="\n\n<a id=\"issue-"+f"{number:06d}"+"\"></a>\n## issue-"+f"{number:06d}"+" - "+title+"\n\n"
    body+="Status: open. Job: "+job+". Recorded: "+kb.DATE+".\n\n"+json.dumps(evidence,ensure_ascii=False,indent=2)+"\n\n<!-- "+marker+" -->\n"
    kb.put(p,text+body)
    return "issue-"+f"{number:06d}"
def checkpoint(root,job,selection,next_action,validation=None):
    p=root/"tracking/checkpoint.json";cp=read_json(p,{})
    cp.update(updated=kb.DATE,status="needs-review",active_refresh_job=job,
              active_domain_message_set=selection["target"],exact_next_action=next_action)
    cp["refresh"]={"job_id":job,"selection":"tracking/refresh/"+job+"/selection.json",
                   "source_fingerprints":{c["key"]:c["sha256"] for c in selection["candidates"]},
                   "affected":selection.get("affected",[]),"conflicts":selection.get("conflicts",[]),
                   "deferred":selection.get("deferred",[]),"validation":validation}
    cp["unresolved_items"]=list(dict.fromkeys(cp.get("unresolved_items",[])+[c["issue_id"] for c in selection.get("conflicts",[]) if c.get("issue_id")]))
    cp["all_supplied_material_processed"]=False;cp["all_desired_knowledge_available"]=False
    cp["all_supplied_sources_processed_to_recorded_limits"]=False
    if selection.get("deferred"):cp["all_supplied_sources_have_disposition"]=False
    kb.dump(p,cp)
def complete(root,selection,job,next_action,status="needs-review"):
    """Persist actual work/review evidence; never infer completion from extraction."""
    kb.set_write_context(root,job)
    applied=read_json(root/"tracking/refresh"/job/"selection.json")
    if not applied:raise ValueError("No registered refresh job")
    check_selection(root,applied,True)
    jobs=read_json(root/"tracking/jobs.json",{"jobs":[]})
    item=next((j for j in jobs["jobs"] if j["job_id"]==job),None)
    if item is None:raise ValueError("Unknown job")
    if status not in ("in-progress","needs-review","blocked"):raise ValueError("Reviewed status requires explicit item-level review, not this bookkeeping command")
    item.update(status=status,last_updated=kb.DATE,next_action=next_action)
    kb.dump(root/"tracking/jobs.json",jobs)
    progress_markdown(root,job,applied["target"],status,next_action)
    validation=read_json(root/"tracking/refresh"/job/"validation.json")
    checkpoint(root,job,applied,next_action,validation)
    prior_report=read_json(root/"tracking/refresh"/job/"report.json",{})
    kb.dump(root/"tracking/refresh"/job/"report.json",{**prior_report,"date":kb.DATE,"job_id":job,"status":status,
        "selected_source_ids":item["source_ids"],"target":applied["target"],"validation":validation,"conflicts":applied.get("conflicts",[]),
        "deferred":applied.get("deferred",[]),"next_action":next_action,
        "scope":"Selected refresh only; extraction is not review; no whole-corpus completion claim."})

def validate_selection(root,selection,checksums=False,job=None):
    import catalog
    root=Path(root).resolve();errors=[];limits=list(selection.get("limitations",[]));counts={}
    try:fresh=check_selection(root,selection,True)
    except Exception as exc:return {"pass":False,"errors":[{"kind":"stale-selection","error":str(exc)}],"checks":{},"limitations":limits}
    ss=old_sources(root);chosen=selection_sources(root,selection);ids={s["source_id"] for s in chosen}
    missing={c["key"] for c in selection["candidates"]}-{s["sha256"] for s in chosen}
    for key in missing:errors.append({"kind":"selected-source-unregistered","key":key})
    current_checks=0
    if checksums:
        for s in chosen:
            active=[o for o in s.get("occurrences",[]) if o.get("availability","current")=="current"]
            if not active:limits.append("Source "+s["source_id"]+" has no current original; substantive review cannot be completed.")
            for o in active:
                try:kb.read_source(root,{"source_id":s["source_id"],"sha256":s["sha256"],"occurrences":[o]});current_checks+=1
                except Exception as exc:errors.append({"kind":"changed-source","source_id":s["source_id"],"error":str(exc)})
    counts["source_occurrences"]=current_checks
    rr=list(catalog.records(root));by_path={r["path"]:r for r in rr}
    paths={r["path"] for r in rr if set(r.get("source_ids",[]))&ids}
    paths.update(x["path"] for x in selection.get("affected",[]))
    identities={}
    for r in rr:
        for k in ("participant_id","flow_id"):
            if r.get(k):identities.setdefault((k,r[k]),[]).append(r["path"])
    for (kind,ident),locations in identities.items():
        if len(locations)>1 and paths&set(locations):errors.append({"kind":"duplicate-reference-identity","identity":ident,"paths":locations})
    from urllib.parse import unquote
    for path in sorted(paths):
        p=safe_path(root,path)
        if not p.exists():errors.append({"kind":"missing-reference","path":path});continue
        meta,text=kb.metadata(p)
        if meta.get("review_status") not in ("draft","needs-review","reviewed"):errors.append({"kind":"invalid-status","path":path})
        scan_text=catalog.template_scan_text(p.read_text(encoding="utf-8"))
        if "{{" in scan_text or "}}" in scan_text:errors.append({"kind":"placeholder","path":path})
        prose=re.sub(r"\x60\x60\x60.*?\x60\x60\x60","",text,flags=re.S)
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)",prose):
            value=target.split("#")[0].split(' "')[0].strip("<>")
            if not value or re.match(r"[a-z]+:",value,re.I):continue
            dest=(p.parent/unquote(value)).resolve()
            if not dest.is_relative_to(root) or not dest.exists():errors.append({"kind":"broken-link","path":path,"target":value})
        for k,index in (("participant_ids","participant_id"),("participants","participant_id"),("flow_ids","flow_id"),("flows","flow_id")):
            for ident in meta.get(k,[]) if isinstance(meta.get(k,[]),list) else []:
                if isinstance(ident,str) and ident.startswith(("participant-","flow-")) and (index,ident) not in identities:
                    errors.append({"kind":"unresolved-reference-id","path":path,"identifier":ident})
        if meta.get("document_kind")=="diagram":
            if meta.get("render_status")!="pass":limits.append("Diagram render verification remains: "+path)
            visual=meta.get("visual_review")
            visual_pass=visual in ("pass","passed","reviewed") if isinstance(visual,str) else isinstance(visual,dict) and visual.get("result",visual.get("status")) in ("pass","passed","reviewed")
            if not visual_pass:limits.append("Diagram visual review remains: "+path)
        if meta.get("review_status")!="reviewed":limits.append("Review is incomplete: "+path)
    counts["reference_pages"]=len(paths)
    canonical,conflicts=canonical_schemas(root,ss);schema_checks=0
    from lxml import etree as E
    from extract_schemas import path as schema_path
    def signature(n):
        return (n.tag,dict(n.attrib),(n.text or "").strip(),[(signature(x),(x.tail or "").strip()) for x in n if isinstance(x.tag,str)])
    for mid,s in canonical.items():
        if s["source_id"] not in ids:continue
        matches=[r for r in rr if r.get("document_kind")=="message-index" and r.get("message_id")==mid and r.get("namespace")==s.get("namespace")]
        if len(matches)!=1:errors.append({"kind":"canonical-reference-count","message_id":mid,"count":len(matches)})
        folder=root/kb.area(s["domain"])/"reference/messages"/mid;c=read_json(folder/"schema-coverage.json")
        if not c:errors.append({"kind":"missing-schema-coverage","message_id":mid});continue
        if c.get("source_id")!=s["source_id"] or c.get("sha256")!=s["sha256"]:errors.append({"kind":"schema-binding-mismatch","message_id":mid});continue
        try:
            tree=E.fromstring(kb.read_source(root,s),E.XMLParser(resolve_entities=False,no_network=True))
            nodes={schema_path(n):n for n in tree.iter() if isinstance(n.tag,str)}
            import collections
            actual_counts=dict(collections.Counter(E.QName(n).localname for n in tree.iter() if isinstance(n.tag,str)))
            if actual_counts!=c.get("counts"):errors.append({"kind":"schema-count-mismatch","message_id":mid})
            for comp in c.get("components",[]):
                pg=root/comp["path"]
                if not pg.exists():errors.append({"kind":"missing-schema-page","path":comp["path"]});continue
                found=re.search(r"\x60\x60\x60xml\n(.*?)\n\x60\x60\x60",pg.read_text(encoding="utf-8"),re.S)
                if not found:errors.append({"kind":"missing-schema-fragment","path":comp["path"]});continue
                n=nodes.get(comp["schema_path"])
                if n is None or signature(E.fromstring(found.group(1).encode()))!=signature(n):errors.append({"kind":"schema-fragment-mismatch","path":comp["path"]})
            if c.get("compile_result")!="pass":errors.append({"kind":"schema-dependency-or-compile-failure","message_id":mid,"error":c.get("compile_error")})
            resolver=SuppliedSchemaResolver(root,ss)
            for dep in c.get("dependencies",[]):
                attributes=dep.get("attributes",dep)
                resolved=resolver.dependency(s,attributes.get("schemaLocation"),attributes.get("namespace"))
                if not resolved:
                    errors.append({"kind":"missing-schema-dependency","message_id":mid,"dependency":dep})
                elif dep.get("kind")=="import" and attributes.get("namespace")!=resolved.get("namespace"):
                    errors.append({"kind":"schema-dependency-namespace-mismatch","message_id":mid,"dependency":dep})
            for dependency in c.get("dependency_coverage",[]):
                ds=next((x for x in ss if x["source_id"]==dependency["source_id"]),None)
                if not ds or ds["sha256"]!=dependency["sha256"]:
                    errors.append({"kind":"dependency-coverage-binding-mismatch","dependency":dependency.get("source_id")});continue
                dt=E.fromstring(kb.read_source(root,ds),E.XMLParser(resolve_entities=False,no_network=True))
                dn={schema_path(n):n for n in dt.iter() if isinstance(n.tag,str)}
                for comp in dependency.get("components",[]):
                    pg=root/comp["path"]
                    match=re.search(r"\x60\x60\x60xml\n(.*?)\n\x60\x60\x60",pg.read_text(encoding="utf-8"),re.S) if pg.exists() else None
                    node=dn.get(comp["schema_path"])
                    if not match or node is None or signature(E.fromstring(match.group(1).encode()))!=signature(node):
                        errors.append({"kind":"dependency-schema-fragment-mismatch","path":comp["path"]})
            schema_checks+=1
        except Exception as exc:errors.append({"kind":"schema-source-unavailable","message_id":mid,"error":str(exc)})
    counts["schema_definitions"]=schema_checks
    # Catalog integrity is checked against all maintained metadata; source scope remains bounded.
    for name,kinds in (("messages",["message-index"]),("participants",["participant","participant-reference","shared-participant"]),
                       ("flows",["business-flow","flow","flow-reference"]),("diagrams",["diagram"]),
                       ("concepts",["schema-type","concept","business-concept"])):
        index=read_json(root/"catalog"/(name+".json"),{"records":[]})["records"]
        indexed={r["path"]:r for r in index}
        expected={r["path"]:r for r in rr if r.get("document_kind") in kinds}
        for path in paths:
            if path not in expected:continue
            if path not in indexed:errors.append({"kind":"catalog-reference-omitted","index":name,"path":path});continue
            for key in ("review_status","source_ids","message_id","namespace","participant_id","flow_id"):
                if key in indexed[path] and indexed[path][key]!=expected[path].get(key):
                    errors.append({"kind":"catalog-metadata-mismatch","index":name,"path":path,"field":key})
    for s in chosen:
        if s["format"] in ("docx","pdf","xlsx","json") and not any(s["source_id"] in r.get("source_ids",[]) for r in rr):
            errors.append({"kind":"selected-document-unprocessed","source_id":s["source_id"]})
        if s["format"]!="zip" and s.get("review_status")!="reviewed":limits.append("Source-wide table/diagram/business review remains: "+s["source_id"])
    affected_conflicts=[c for c in conflicts if set(c.get("candidate_source_ids",[]))&ids]
    unregistered=[{"key":c["key"],"paths":sorted({o["path"] for o in c["occurrences"]})}
                  for c in fresh["candidates"] if c["key"] not in {s["sha256"] for s in ss}]
    out={"date":kb.DATE,"pass":not errors,"errors":errors,"checks":counts,"conflicts":affected_conflicts,
         "limitations":sorted(set(limits)),"deferred":selection.get("deferred",[]),
         "unregistered_outside_selection":unregistered,"all_supplied_material_processed":False,
         "selected_review_complete":not errors and not limits and not affected_conflicts,
         "scope":"Selected source/schema/reference checks; no automatic business, table, diagram or visual approval.",
         "source_fingerprints":{s["source_id"]:s["sha256"] for s in chosen}}
    if job:
        kb.set_write_context(root,job);path=root/"tracking/refresh"/job/"validation.json";kb.dump(path,out)
        out["report_path"]=path.relative_to(root).as_posix()
    return out

class SuppliedSchemaResolver:
    """Compile only exact local/archived dependencies already registered."""
    def __init__(self,root,ss):
        self.root=Path(root);self.ss=ss;self.byid={s["source_id"]:s for s in ss};self.cache={}
    def uri(self,s):return "kb-source://"+s["source_id"]+"/schema.xsd"
    def dependency(self,s,location,namespace=None):
        import posixpath
        candidates=[]
        if location and re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:",location):
            return None
        for o in s.get("occurrences",[]):
            if o.get("availability","current")!="current":continue
            target=posixpath.normpath(str(PurePosixPath(o.get("archive_member") or o["path"]).parent/(location or "")))
            for dep in self.ss:
                if dep.get("format")!="xsd":continue
                for x in dep.get("occurrences",[]):
                    if x.get("availability","current")!="current":continue
                    matches=(x["path"]==o["path"] and x.get("archive_member")==target) if o.get("archive_member") else (not x.get("archive_member") and x["path"]==target)
                    if location and matches:candidates.append(dep)
                    elif not location and namespace and dep.get("namespace")==namespace:candidates.append(dep)
        unique={d["sha256"]:d for d in candidates}
        return next(iter(unique.values())) if len(unique)==1 else None
    def prepare(self,s,seen=None):
        from lxml import etree as E
        seen=set() if seen is None else seen
        if s["source_id"] in seen:return
        seen.add(s["source_id"])
        tree=E.fromstring(kb.read_source(self.root,s),E.XMLParser(resolve_entities=False,no_network=True))
        for n in tree:
            if isinstance(n.tag,str) and E.QName(n).localname in ("import","include","redefine","override"):
                dep=self.dependency(s,n.get("schemaLocation"),n.get("namespace"))
                if not dep:
                    raise OSError("Missing or ambiguous supplied schema dependency: "+str(n.get("schemaLocation") or n.get("namespace")))
                if E.QName(n).localname=="import" and n.get("namespace")!=dep.get("namespace"):
                    raise OSError("Supplied import namespace does not match "+dep["source_id"])
                n.set("schemaLocation",self.uri(dep));self.prepare(dep,seen)
        self.cache[self.uri(s)]=E.tostring(tree)
    def compile(self,s):
        from lxml import etree as E
        self.prepare(s);outer=self
        class Resolver(E.Resolver):
            def resolve(self,url,pubid,context):
                if url not in outer.cache:raise OSError("Dependency is not a verified registered local source: "+url)
                return self.resolve_string(outer.cache[url],context,base_url=url)
        parser=E.XMLParser(resolve_entities=False,no_network=True);parser.resolvers.add(Resolver())
        tree=E.fromstring(self.cache[self.uri(s)],parser,base_url=self.uri(s))
        E.XMLSchema(tree)

def selected_messages(root,selection):
    ids={m for s in selection_sources(root,selection) for m in s.get("message_ids",[])}
    import catalog
    affected={x["path"] for x in selection.get("affected",[])}
    for record in catalog.records(root):
        if record["path"] in affected:
            ids.update(record.get("message_ids",[]))
            if record.get("message_id"):ids.add(record["message_id"])
    return ids

def output_fingerprints(root,source,result):
    """Generated outputs needed for reuse; preserve authored edits but detect absence."""
    output=result.get("output")
    if not output:return {}
    base=(root/output).parent
    paths=list(base.rglob("*")) if base.exists() else []
    assets=root/kb.area(source["domain"])/"assets"/source["source_id"]
    if assets.exists():paths+=list(assets.rglob("*"))
    return {p.relative_to(root).as_posix():fingerprint(p) for p in paths if p.is_file()}

def extraction_outputs_valid(root,source,result):
    if result.get("source_sha256")!=source["sha256"]:return False
    kb.read_source(root,source)
    files=result.get("output_fingerprints")
    if not files:return False
    # Curated output may legitimately differ from extraction. Existence and
    # source binding establish reuse; changed output never inherits review.
    return bool(result.get("output")) and (root/result["output"]).exists() and all(safe_path(root,p).is_file() for p in files)

def job_sources(root,job,requested):
    if not job:return requested
    selection=read_json(root/"tracking/refresh"/job/"selection.json")
    if not selection:raise ValueError("A refresh job needs its applied selection before extraction")
    check_selection(root,selection,True)
    allowed=set(selection["selected_source_ids"])
    if requested and not set(requested)<=allowed:raise ValueError("Requested source is outside this refresh job")
    return requested or sorted(allowed)

def progress_markdown(root,job,target,status,next_action):
    p=root/"tracking/conversion-status.md"
    text=p.read_text(encoding="utf-8") if p.exists() else "# Conversion status\n"
    start="<!-- REFRESH-JOB-"+job+"-START -->";end="<!-- REFRESH-JOB-"+job+"-END -->"
    block=start+"\n## "+job+" - selected refresh\n\nStatus: "+status+". Updated: "+kb.DATE+".\n\nScope: "+json.dumps(target)+".\n\nNext action: "+next_action+"\n\n[Applied selection](refresh/"+job+"/selection.json) · [Job report](refresh/"+job+"/report.json).\n"+end
    if start in text:
        text=re.sub(re.escape(start)+r".*?"+re.escape(end),lambda _:block,text,flags=re.S)
    else:text=text.rstrip()+"\n\n"+block+"\n"
    kb.put(p,text)

def register(root,selection,job):
    """Serialize registrations for one repository without touching discovery state."""
    import os,tempfile
    key=digest_bytes(str(Path(root).resolve()).casefold().encode())[:32]
    lock=Path(tempfile.gettempdir())/("iso20022-refresh-"+key+".lock")
    try:fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    except FileExistsError:raise ValueError("Another registration holds "+str(lock)+". Verify that run has ended before clearing a stale lock.")
    try:
        with os.fdopen(fd,"w",encoding="utf-8") as handle:
            json.dump({"pid":os.getpid(),"root":str(root),"job":job,"date":kb.DATE},handle)
        return _register(root,selection,job)
    finally:lock.unlink(missing_ok=True)
