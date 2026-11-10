"""Audit current canonical Mermaid code against retained inputs and dated review hashes.
No renderer invocation and no new visual approval. Raw-byte and documented UTF8/LF
hashes are distinguished. Markdown fence terminal newlines are not semantic edits.
"""
from pathlib import Path
import argparse,collections,hashlib,json,re,subprocess,os
from urllib.parse import unquote
import kb
sha=lambda b:hashlib.sha256(b).hexdigest()
def norm(s):return s.replace('\r\n','\n').replace('\r','\n').strip('\n')
def pathstr(v):return v.replace('\\','/') if isinstance(v,str) else ''
def local_paths(x):
 if isinstance(x,dict):
  for k,v in x.items():
   if isinstance(v,str) and (v.startswith(('domains/','shared/','work/')) or v.startswith(('domains\\','shared\\','work\\'))):yield k,pathstr(v)
   elif isinstance(v,(dict,list)):yield from local_paths(v)
 elif isinstance(x,list):
  for y in x:yield from local_paths(y)
def main(root):
 names=subprocess.run(['rg','-l','--glob','*.md','--regexp','^document_kind: "diagram"\\r?$','domains','shared'],cwd=root,capture_output=True,text=True,check=True).stdout.splitlines();diags={};artmap=collections.defaultdict(set);codemap=collections.defaultdict(set);mmds={};nh=collections.defaultdict(list)
 for folder in ['domains','shared','work']:
  for p in (root/folder).rglob('*.mmd'):
   raw=p.read_bytes();t=raw.decode('utf-8-sig');rp=p.relative_to(root).as_posix();v={'raw_bytes':sha(raw),'utf8_lf':sha(t.replace('\r\n','\n').replace('\r','\n').encode('utf-8'))};mmds[rp]={'path':rp,'text':t,'hashes':v};nh[sha(norm(t).encode())].append(rp)
 for name in names:
  p=root/name;m,b=kb.metadata(p);blocks=re.findall(r'```mermaid[^\n]*\n(.*?)\n```',b,re.S);rp=p.relative_to(root).as_posix();br=[]
  for i,code in enumerate(blocks):
   matches=nh[sha(norm(code).encode())];sibling=p.with_suffix('.mmd').relative_to(root).as_posix();near=[x for x in matches if Path(x).parent==Path(rp).parent];selected=near or matches
   br.append({'block':i+1,'markdown_lf_sha256':sha(code.encode()),'matching_mmd':selected,'current_mmd_hashes':{x:mmds[x]['hashes'] for x in selected},'sibling_exists':sibling in mmds,'sibling_matches':sibling in matches,'input_hash_evidence':[]})
   for x in selected:
    for v in mmds[x]['hashes'].values():codemap[v].add(rp)
  arts=set(v for k,v in local_paths(m) if v.endswith(('.svg','.png')))
  for target in re.findall(r'\]\(([^)]+)\)',b):
   target=unquote(target.split('#')[0]).strip('<>');q=(p.parent/target).resolve()
   if target.endswith(('.svg','.png')) and q.is_relative_to(root):arts.add(q.relative_to(root).as_posix())
  for a in arts:artmap[a].add(rp)
  diags[rp]={'path':rp,'blocks':br,'source_ids':m.get('source_ids',[]),'review_status':m.get('review_status'),'artifacts':sorted(arts),'hash_claims':[],'render_hash_claims':[]}
 claims=[];unassociated=[];auxiliary=[]
 files=sorted((root/'tracking/reviews').glob('*.json'))
 for p in files:
  if p.name in ['diagram-code-evidence-audit.json']:continue
  text=p.read_text(encoding='utf-8-sig')
  if not any(k in text for k in ['mermaid_sha256','mmd_sha256','rendered_png_sha256','svg_sha256','png_sha256']):continue
  doc=json.loads(text);report=p.relative_to(root).as_posix()
  def walk(x,anc,jp):
   if isinstance(x,dict):
    hs=[(k,v) for k,v in x.items() if isinstance(v,str) and re.fullmatch('[0-9a-f]{64}',v) and k in ['mermaid_sha256','mmd_sha256','auxiliary_mermaid_sha256','rendered_png_sha256','svg_sha256','png_sha256','auxiliary_png_sha256']]
    if hs:
     chain=[x]+list(reversed(anc));nearest={};targets=set();assoc=None
     for obj in chain:
      direct=[pathstr(v) for k,v in obj.items() if isinstance(v,str) and k in ['path','diagram','canonical_path','canonical_diagram','markdown','mermaid']]
      hit={q if q.endswith('.md') else str(Path(q).with_suffix('.md')).replace('\\','/') for q in direct if q.endswith(('.md','.mmd'))}&diags.keys()
      if hit:targets=hit;assoc='explicit reference path';nearest=obj;break
     explicit=pathstr(x.get('path',''))
     if explicit.endswith('.md') and explicit not in diags and (root/explicit).exists() and any(k in ['mermaid_sha256','mmd_sha256'] for k,v in hs):
      am,ab=kb.metadata(root/explicit);ac=re.findall(r'```mermaid[^\n]*\n(.*?)\n```',ab,re.S);amp=pathstr(x.get('mermaid')) or str(Path(explicit).with_suffix('.mmd')).replace('\\','/');av=mmds.get(amp);checks=[]
      for hk,hv in hs:
       if hk in ['mermaid_sha256','mmd_sha256']:checks.append({'field':hk,'recorded_sha256':hv,'result':'pass' if av and hv in av['hashes'].values() else 'mismatch'})
       elif hk in ['rendered_png_sha256','png_sha256','svg_sha256']:
        ap=pathstr(x.get('svg' if 'svg' in hk else 'png',''));checks.append({'field':hk,'artifact':ap,'result':'pass' if ap and (root/ap).exists() and sha((root/ap).read_bytes())==hv else 'mismatch'})
      auxiliary.append({'path':explicit,'document_kind':am.get('document_kind'),'report':report,'json_path':jp,'date':x.get('date',doc.get('date') if isinstance(doc,dict) else None),'canonical_diagram':am.get('canonical_diagram'), 'markdown_matches_mmd':None if am.get('document_kind')=='diagram-occurrence' else bool(av and len(ac)==1 and norm(ac[0])==norm(av['text'])),'checks':checks});hs=[]
     arts=[v for k,v in local_paths(x) if v.endswith(('.svg','.png'))]
     if not targets:
      hit=set().union(*(artmap[a] for a in arts)) if arts else set()
      if hit:targets=hit;assoc='named render artifact';nearest=x
     if not targets:
      values=[v for k,v in hs if k in ['mermaid_sha256','mmd_sha256','auxiliary_mermaid_sha256']];hit=set().union(*(codemap[v] for v in values)) if values else set()
      if len(hit)==1:targets=hit;assoc='unique retained Mermaid hash';nearest=x
     dates=[]
     for obj in chain:
      for k,v in obj.items():
       if k in ['date','visual_review_date','review_date','render_date','render_date_utc'] and isinstance(v,str):dates.append(v)
     for k,v in hs:
      claim={'report':report,'json_path':jp,'field':k,'recorded_sha256':v,'association':assoc,'dated_evidence':sorted(set(dates))}
      if not targets:unassociated.append(claim);continue
      for rp in targets:
       cc={**claim};d=diags[rp]
       if k in ['mermaid_sha256','mmd_sha256','auxiliary_mermaid_sha256']:
        matches=[]
        for br in d['blocks']:
         for mp in br['matching_mmd']:
          modes=[mode for mode,h in mmds[mp]['hashes'].items() if h==v]
          if modes:matches.append({'block':br['block'],'mmd':mp,'hash_conventions':modes});br['input_hash_evidence'].append({**claim,'mmd':mp,'hash_conventions':modes})
        cc.update(matches=matches,result='pass' if matches else 'mismatch');d['hash_claims'].append(cc)
       else:
        field='auxiliary_png' if k=='auxiliary_png_sha256' else ('svg' if 'svg' in k else 'png');candidates=[]
        for obj in [x,nearest]:
         if isinstance(obj.get(field),str):candidates.append(pathstr(obj[field]))
         if isinstance(obj.get('render'),dict) and isinstance(obj['render'].get(field),str):candidates.append(pathstr(obj['render'][field]))
        if not candidates:candidates=[a for a in d['artifacts'] if a.endswith('.'+field)]
        existing=[a for a in set(candidates) if (root/a).exists()];matched=[a for a in existing if sha((root/a).read_bytes())==v];cc.update(candidate_artifacts=existing,matching_artifacts=matched,result='pass' if matched else 'mismatch');d['render_hash_claims'].append(cc)
    for k,y in x.items():
     if isinstance(y,(dict,list)):walk(y,anc+[x],jp+'/'+k)
   elif isinstance(x,list):
    for i,y in enumerate(x):walk(y,anc,jp+'/'+str(i))
  walk(doc,[],'')
 renderdocs=[];renderfiles=set(files);renderfiles.update((root/'work/documents').glob('*/*render*.json'))
 for current,dirs,fs in os.walk(root/'work'):
  dirs[:]=[x for x in dirs if x not in ['documents','docx-render','native-cfb','native-vsdx','renderer','node_modules','pdf-table-workers','tables']]
  for fn in fs:
   if fn.endswith('.json'):
    fp=Path(current)/fn
    if fp.stat().st_size<15000000:renderfiles.add(fp)
 def collect_render(x,report,jp):
  if isinstance(x,dict):
   status=x.get('result',x.get('render_result',x.get('render_status')));date=x.get('date',x.get('render_date_utc',x.get('render_date')))
   if status in ['pass','passed'] and date and isinstance(x.get('svg'),str) and isinstance(x.get('png'),str):
    paths=[pathstr(x['svg']),pathstr(x['png'])];targets=set().union(*(artmap[a] for a in paths));record={'report':report,'json_path':jp,'date':date,'renderer':x.get('renderer'),'version':x.get('version',x.get('renderer_version')),'svg':paths[0],'png':paths[1],'artifacts_exist':all((root/a).exists() for a in paths)}
    for target in targets:diags[target].setdefault('dated_render_evidence',[]).append(record)
   for k,y in x.items():
    if isinstance(y,(dict,list)):collect_render(y,report,jp+'/'+k)
  elif isinstance(x,list):
   for i,y in enumerate(x):collect_render(y,report,jp+'/'+str(i))
 for fp in sorted(renderfiles):
  if fp.name in ['diagram-code-evidence-audit.json']:continue
  tx=fp.read_text(encoding='utf-8-sig')
  if '"svg"' not in tx or '"png"' not in tx:continue
  try:collect_render(json.loads(tx),fp.relative_to(root).as_posix(),'')
  except json.JSONDecodeError:continue
 for rp in diags:
  meta,_=kb.metadata(root/rp)
  if isinstance(meta.get('render_evidence'),dict):collect_render(meta['render_evidence'],rp,'/metadata/render_evidence')
 for d in diags.values():
  d['all_blocks_match_retained_input']=all(b['matching_mmd'] for b in d['blocks']);d['all_blocks_have_dated_input_hash']=all(any(e['dated_evidence'] for e in b['input_hash_evidence']) for b in d['blocks']);d['has_matching_render_hash']=any(c['result']=='pass' for c in d['render_hash_claims']);d['unmatched_hash_claims']=[c for c in d['hash_claims']+d['render_hash_claims'] if c['result']=='mismatch']
 summary={'canonical_diagrams':len(diags),'mermaid_blocks':sum(len(d['blocks']) for d in diags.values()),'retained_mmd_files':len(mmds),'diagrams_all_blocks_match_input':sum(d['all_blocks_match_retained_input'] for d in diags.values()),'diagrams_all_blocks_have_dated_input_hash':sum(d['all_blocks_have_dated_input_hash'] for d in diags.values()),'diagrams_with_matching_render_hash':sum(d['has_matching_render_hash'] for d in diags.values()),'diagrams_with_unmatched_hash_claim':sum(bool(d['unmatched_hash_claims']) for d in diags.values()),'unassociated_hash_claims':len(unassociated),'auxiliary_detail_views':sum(a['document_kind']=='diagram-detail' for a in auxiliary),'auxiliary_detail_hash_failures':sum(any(c['result']!='pass' for c in a['checks']) or not a['markdown_matches_mmd'] for a in auxiliary if a['document_kind']=='diagram-detail'),'delegated_occurrences':sum(a['document_kind']=='diagram-occurrence' for a in auxiliary),'delegated_occurrence_retained_input_failures':sum(any(c['result']!='pass' for c in a['checks']) for a in auxiliary if a['document_kind']=='diagram-occurrence'),'diagrams_with_dated_existing_render_evidence':sum(any(e['artifacts_exist'] for e in d.get('dated_render_evidence',[])) for d in diags.values())}
 out={'date':'2026-11-09','scope':'Independent current Markdown versus retained Mermaid inputs and recorded dated code/render hashes. No renderer or visual review performed. Raw-byte and UTF8/LF digests are distinguished; fence terminal newlines are excluded only in code comparison, not evidence hashing.','summary':summary,'records':list(diags.values()),'unassociated_claims':unassociated,'auxiliary_detail_views':auxiliary};kb.dump(root/'tracking/reviews/diagram-code-evidence-audit.json',out);print(json.dumps(summary));print(json.dumps({'no_input':[d['path'] for d in diags.values() if not d['all_blocks_match_retained_input']],'unmatched_claims':[{'path':d['path'],'claims':d['unmatched_hash_claims']} for d in diags.values() if d['unmatched_hash_claims']]},ensure_ascii=True)[:15000])
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();main(a.root.resolve())
