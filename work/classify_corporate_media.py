from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();p=root/'tracking/reviews/docx-media-classification.json';data=json.loads(p.read_text(encoding='utf-8')) if p.exists() else {'records':[]};records=[x for x in data['records'] if x['source_id']!='src-000079']
inv=json.loads((root/'work/documents/src-000079/media-review-inventory.json').read_text(encoding='utf-8'))
for media in inv['media']:
 name=Path(media['original']).name;legend=name in [f'image{i}.png' for i in range(4,8)]
 row={'source_id':'src-000079','original':media['original'],'sha256':media['original_sha256'],'disposition':'preserved-legend-symbol' if legend else 'substantive-diagram','classification_review':'pass','classification_review_date':'2026-11-09','classification_review_scope':'All four labelled contact sheets visually inspected. T20 legend checked against extracted table and source media. This is classification, not full-size relationship/label or reconstruction review.','classification_reason':'Activity notation legend symbol embedded in T20; preserved with the substantive legend table. A standalone symbol is not a separate business diagram.' if legend else 'Source business-role, process, timeline, activity, sequence, or message-routing diagram with substantive labels and relationships.'}
 records.append(row)
 if legend:
  for oc in media['occurrences']:
   ep=root/oc['evidence_page'];em,eb=kb.metadata(ep);em.update(disposition='preserved-legend-symbol',diagram_kind='notation-legend-symbol',classification_review='pass',classification_review_date='2026-11-09');eb+='\n## Classification\n\nThis is a substantive notation symbol within source table T20, not a standalone business diagram or decorative image. Its meaning is preserved in '+kb.link(ep,ep.parent.parent/'tables/tbl-0020.md','the complete activity legend')+'. A Mermaid business diagram is not appropriate for this isolated legend symbol.\n';kb.put(ep,kb.front(em)+eb)
kb.dump(p,{'updated':'2026-11-09','records':records})
f=root/'tools/docx_contact_sheets.py';t=f.read_text(encoding='utf-8-sig');
if "override_file=root/" not in t:t=t.replace("font=load_font(14)", "override_file=root/'tracking/reviews/docx-media-classification.json';overrides={x['original']:x for x in json.loads(override_file.read_text(encoding='utf-8')).get('records',[])} if override_file.exists() else {}\n font=load_font(14)")
t=t.replace("items.append({**m,'dimensions':dims,'occurrences':occurrences,'disposition':'pending-visual-classification','complete_composite_review':'not-run'})", "items.append({**m,'dimensions':dims,'occurrences':occurrences,'disposition':'pending-visual-classification','complete_composite_review':'not-run',**{k:v for k,v in overrides.get(m['original'],{}).items() if k not in ['source_id','original','sha256']}})")
t=t.replace("'updated':'2026-11-08'", "'updated':'2026-11-09'")
f.write_text(t,encoding='utf-8')
