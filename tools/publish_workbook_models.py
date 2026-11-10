"""Publish explicitly reviewed workbook model transcriptions; does not infer review success."""
from pathlib import Path
import json,sys,re,collections,argparse
sys.path.insert(0,str(Path(__file__).resolve().parent));import kb
from extract_workbooks import fm,write,relative,esc
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--models',type=Path,required=True);ap.add_argument('--render-report',type=Path,required=True);args=ap.parse_args();ROOT=args.root.resolve();JOB='job-000001';FENCE=chr(96)*3
models=json.loads((ROOT/args.models).read_text('utf-8'));renders={r['diagram']:r for r in json.loads((ROOT/args.render_report).read_text('utf-8'))};sources={s['source_id']:s for s in kb.sources(ROOT)};results=json.loads((ROOT/'work/workbook-results.json').read_text('utf-8'))
def put(p,b):write(ROOT,ROOT/p,b,JOB)
def link(p,t,label):return '['+label+']('+relative(ROOT/p,ROOT/t)+')'
def table(h,rows):return '| '+' | '.join(esc(x) for x in h)+' |\n| '+' | '.join('---' for x in h)+' |\n'+''.join('| '+' | '.join(esc(x) for x in row)+' |\n' for row in rows)
reports=[]
for m in models:
 sid=m['source_id'];s=sources[sid];base=Path(s['set_path']);wb=base/'workbooks'/sid;wpath=Path('work/workbooks')/sid/'workbook.json';w=json.loads((ROOT/wpath).read_text('utf-8'));sh=next(x for x in w['sheets'] if x['name']=='FullBusinessModel');rows=collections.defaultdict(dict)
 for cell in sh['cells']:
  a=re.match('([A-Z]+)([0-9]+)',cell['cell']);rows[int(a[2])][a[1]]=cell['value']
 defs={row['A']:(n,row) for n,row in rows.items() if row.get('A') and not row.get('B')};fid=m['id'];d=m['source'];p=Path(d['page']);r=renders[m['render_prefix']];v=m.get('visual_review')
 if not v or v.get('result') not in ['pass','pass-with-limitations']:raise ValueError('Explicit visual-review evidence required for '+fid)
 if r['result']!='pass':raise ValueError('Render failed '+fid)
 status=m.get('review_status','needs-review');loc=d['sheet']+'!'+d['from_cell']+(':'+d['to_cell'] if d.get('to_cell') else '')+'; '+d['drawing_part']+'; anchor '+str(d['anchor_id']);meta=fm(domain=s['domain'],document_kind='diagram',review_status=status,curated=True,source_ids=[sid],source_edition=s['source_edition'],source_locations=[loc]+m.get('extra_source_locations',[]),figure_id=fid,diagram_kind='class',content_origin='source-reconstruction',message_sets=[s['set_slug']],concepts=sorted(set(n['name'] for n in m['nodes'])),participants=m.get('participants',[]),flows=m.get('flows',[]),render_status='passed',visual_review=v,limitations=m.get('limitations',[]),issues=m.get('issues',[]))
 b=meta+'# '+m['title']+'\n\n'+kb.source_link(ROOT,ROOT/p,s)+', '+loc+'. Original image SHA-256: '+d['sha256']+'.\n\n'+link(p,Path(d['asset']),'Original complete figure')+' · '+link(p,Path(r['svg']),'Rendered Mermaid SVG')+' · '+link(p,Path(r['png']),'Rendered Mermaid PNG')+'\n\n## Source reconstruction\n\n'+FENCE+'mermaid\n'+m['mermaid'].rstrip()+'\n'+FENCE+'\n\n## Entities and relationships\n\n'+m['meaning']+'\n\nAll '+str(len(m['nodes']))+' visible node occurrences and '+str(len(m['edges']))+' relationship lines are retained. '+m.get('multiplicity_note','No numeric multiplicity is shown in this source view, so none is inferred.')+' '+m.get('package_note','Namespaces group the source’s printed “from” package labels for readability; the source did not draw those enclosing package boxes.')+' Association labels retain literal +/− prefixes and combined end names. Their re-layout position is not additional navigability evidence. The native class inheritance marker is reserved for the source’s hollow-triangle generalizations. Source editor/navigation icons are omitted as interface decoration; no business entity or relationship is excluded.\n\n## Complete relationship register\n\n'+table(['From node','To node','Source relationship kind','Visible source label(s)','From-end multiplicity','To-end multiplicity'],[[e['a'],e['b'],e.get('kind_label') or ('generalization: subtype to supertype' if e['kind']=='--|>' else 'directed association' if e['kind']=='-->' else 'composition at from node, directed to to node' if e['kind']=='*-->' else 'composition at from node' if e['kind']=='*--' else 'association'),e['label'] or '(unlabelled in source)',e.get('a_card','not printed'),e.get('b_card','not printed')] for e in m['edges']])+'\n## Entity definitions and precise workbook locators\n\n'
 b+='| Visible label | Source package / stereotype | Definition evidence |\n| --- | --- | --- |\n'
 for n in m['nodes']:
  name=n['name'];found=defs.get(name)
  if found:
   rownum,row=found;tp=next(x for x in sh['table_pages'] if x['row_start']<=rownum<=x['row_end']);evidence=link(p,Path(tp['path']),'FullBusinessModel!A'+str(rownum)+':D'+str(rownum))+' — '+esc(row.get('D') or '')
  else:evidence='Label/type is shown by this figure; no independent component definition is asserted from the FullBusinessModel sheet.'
  b+='| '+esc(name)+' | '+esc(n['package']+' / '+(n.get('stereotype') or '(stereotype not printed)'))+' | '+evidence+' |\n'
 b+='\n## Participant and flow navigation\n\nThis is a conceptual entity model, not a message exchange diagram. A business component or relationship label is not automatically a functional participant or institution. '+link(p,base/'participants.md','Message-set participant references')+' and '+link(p,base/'flows/index.md','Message-set business flows')+' provide the independently sourced actor/process context. These references are navigational; source figure associations do not establish message direction.\n\n## Rendering and visual review\n\n'+v['date']+': Mermaid '+r['version']+' parsed and rendered successfully with '+r['renderer']+'. '+v['method']+' '+link(p,args.render_report,'Renderer evidence')+'.\n\n'
 if m.get('limitations'):b+='Remaining limitations: '+' '.join(m['limitations'])+'\n'
 put(p,b)
 update={'review_status':status,'disposition':'converted','render_status':'passed','visual_review':v,'content_origin':'source-reconstruction','node_occurrences':len(m['nodes']),'relationship_count':len(m['edges'])}
 for record in results:
  if record['source_id']==sid:
   for item in record['diagrams']:
    if item['figure_id']==fid:item.update(update)
 for sheet in w['sheets']:
  for item in sheet.get('drawings',[]):
   if item.get('figure_id')==fid:item.update(update)
 put(wpath,json.dumps(w,ensure_ascii=False,indent=2));reports.append({'source_id':sid,'figure_id':fid,'output':p.as_posix(),**update})
put(Path('work/workbook-results.json'),json.dumps(results,ensure_ascii=False,indent=2));put(args.models.parent/'review-report.json',json.dumps(reports,ensure_ascii=False,indent=2));print(json.dumps(reports,ensure_ascii=False))
