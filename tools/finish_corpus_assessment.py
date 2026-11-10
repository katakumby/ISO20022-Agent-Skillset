"""Publish a dated corpus assessment only after the recorded validation gates pass.

This reports processing to documented limits, never promotes reference review status,
and deliberately distinguishes that result from complete internal/visual review.
"""
import argparse,collections,hashlib,json
from pathlib import Path
import kb,checkpoint

def finish(root):
 def read(path):return json.loads((root/path).read_text(encoding='utf-8'))
 ss=kb.sources(root);summary=read('catalog/coverage-summary.json')
 validation=read('tracking/validation.json');retrieval=read('tracking/retrieval-validation.json')
 roles=read('tracking/reviews/message-role-audit.json');docx=read('tracking/reviews/docx-coverage-reconciliation.json')
 diagrams=read('tracking/reviews/diagram-record-audit.json');pdf=read('catalog/pdf-structural-review.json')
 workbook=read('tracking/reviews/workbook-status-audit.json');native=read('catalog/native-object-dispositions.json')
 workbook_counts=collections.Counter()
 for item in read('work/workbook-results.json'):
  if item['format']=='xlsx':workbook_counts.update(item.get('counts',{}))
 fingerprints={s['source_id']:s['sha256'] for s in ss}
 fingerprint_digest=hashlib.sha256(json.dumps(fingerprints,sort_keys=True).encode()).hexdigest()
 assert validation.get('pass') and validation.get('source_fingerprints_sha256')==fingerprint_digest,'Full current source validation required'
 assert validation['checks'].get('source_occurrences')==sum(len(s['occurrences']) for s in ss),'Every source occurrence must be checked'
 assert retrieval.get('pass') and roles.get('result')=='pass','Retrieval and role evidence checks must pass'
 assert roles.get('catalog_snapshot_sha256')==hashlib.sha256((root/'catalog/message-roles.json').read_bytes()).hexdigest(),'Role audit must match the current catalog'
 assert validation['checks'].get('reference_pages')==summary['pages'],'Validation and catalog must cover the same reference set'
 assert not docx['gaps'] and not diagrams['errors'],'Unresolved destination/render evidence errors'
 assert summary['diagram_pages']==diagrams['canonical_diagrams'],'Rebuild catalog after diagram changes'
 code_evidence=read('tracking/reviews/diagram-code-evidence-audit.json')['summary']
 assert code_evidence['canonical_diagrams']==diagrams['canonical_diagrams']==code_evidence['diagrams_all_blocks_match_input']==code_evidence['diagrams_with_dated_existing_render_evidence']
 assert code_evidence['diagrams_with_unmatched_hash_claim']==0 and code_evidence['unassociated_hash_claims']==0
 assert summary['messages']==len(read('catalog/messages.json')['records'])
 for s in ss:
  assert s.get('canonical_output_paths') and all((root/p).exists() for p in s['canonical_output_paths']),s['source_id']
  assert s.get('disposition') not in [None,'queued'],s['source_id']
 evidence_paths=['tracking/validation.json','tracking/retrieval-validation.json','tracking/reviews/message-role-audit.json','tracking/reviews/message-role-coverage.json','tracking/reviews/docx-coverage-reconciliation.json','tracking/reviews/diagram-record-audit.json','tracking/reviews/diagram-code-evidence-audit.json','catalog/pdf-structural-review.json','tracking/reviews/workbook-status-audit.json','catalog/native-object-dispositions.json','tracking/reviews/navigation-retrieval-usability.json']
 limitations=[
  'All supplied sources have destinations and processing dispositions. Complete internal/semantic/visual review is not claimed.',
  '65 binary Visio objects retain undecoded internal pages/layers. Eight unique VSDX objects have static package/page evidence, but inherited/native visual semantics remain qualified.',
  'The 24 Part2 PDFs have complete grid-cell and painted-object reconciliation; direct visual review covers 29 named pages, not every one of their 20,396 pages. Text-only diagram completeness is outside the painted-object audit.',
  'All 24 workbooks have independent cell/range checks and every drawing has a disposition; complete whole-worksheet visual formatting review is not claimed.',
  'Source contradictions, historical example/version mismatches, missing MDR context for schema-only collections, two documentation-only messages without XSD, and 23 external-code definitions without supplied enumerations remain explicit.',
  'A passing schema, text, link, or render check does not resolve a source business-rule conflict. Qualified and partial visual comparisons remain qualified.'
 ]
 report={'date':kb.DATE,'status':'needs-review','source_fingerprints':fingerprints,'all_supplied_sources_have_disposition':True,'all_supplied_sources_processed_to_recorded_limits':True,'all_supplied_material_processed':False,'all_desired_knowledge_available':False,'completion_meaning':'Corpus-wide extraction, focused reference creation and validation finished to the documented evidence/tooling limits; uninspected internal content and unresolved source facts remain open.','coverage':{k:summary[k] for k in ['unique_sources','source_occurrences','input_collections','domains','message_sets','message_set_editions','archive_message_sets','code_publication_groups','messages','families','messages_with_supplied_schema','documentation_only_messages','participants','flows','business_concepts','schema_components','diagram_pages','pages','reference_kind_counts']},'docx_tables':docx['table_destinations'],'docx_figure_destinations':docx['figure_destinations'],'pdf_structural_coverage':{k:pdf[k] for k in ['source_count','pages','grid_table_candidates','physical_cells','supplemental_warning_panels','direct_visual_page_count']},'native_objects':native['summary'],'limitations':limitations,'validation_evidence':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in evidence_paths},'remaining_action':'Start with the issue register and native-object dispositions. Resolve only affected source ambiguities or unavailable native/whole-layout review; compare fingerprints and reuse unchanged references rather than reconverting the corpus.'}
 kb.dump(root/'tracking/corpus-assessment.json',report)
 checkpoint.checkpoint(root,'All supplied collections processed to documented evidence and tooling limits',report['remaining_action'])
 cp=read('tracking/checkpoint.json');cp.update(status='needs-review',all_supplied_sources_have_disposition=True,all_supplied_sources_processed_to_recorded_limits=True,all_supplied_material_processed=False,all_desired_knowledge_available=False,corpus_assessment='tracking/corpus-assessment.json');kb.dump(root/'tracking/checkpoint.json',cp)
 for key in ['all_supplied_material_processed','all_desired_knowledge_available','all_supplied_sources_processed_to_recorded_limits']:summary[key]=report[key]
 summary['corpus_assessment']='tracking/corpus-assessment.json';kb.dump(root/'catalog/coverage-summary.json',summary)
 page=root/'tracking/completion-report.md'
 text='# Corpus processing assessment\n\nAll supplied collections have been processed to the documented evidence and tooling limits. This is not a claim that every source statement is correct or every native internal object has been reviewed. Reference statuses and unresolved issues remain visible.\n\n'
 text+=kb.table(['Output area','Exact message definitions'],[[area,count] for area,count in summary['domains'].items()])
 rows=[['Supplied input collections',summary['input_collections']],['Unique source contents / occurrences',str(len(ss))+' / '+str(sum(len(s['occurrences']) for s in ss))],['Message sets / publication groups',str(summary['message_sets'])+' / '+str(summary['message_set_editions'])],['T2S archive message-set boundaries',summary['archive_message_sets']],['Exact messages / families',str(summary['messages'])+' / '+str(summary['families'])],['Messages with XSD / documentation only',str(summary['messages_with_supplied_schema'])+' / '+str(summary['documentation_only_messages'])],['Shared participant records',summary['participants']],['Business flows',summary['flows']],['Business concepts',summary['business_concepts']],['Schema declaration/type pages',summary['schema_components']],['Canonical diagram pages',summary['diagram_pages']],['DOCX tables / figure destinations',str(docx['table_destinations'])+' / '+str(docx['figure_destinations'])],['Part2 PDF grid-table parts / recovered warning panels',str(pdf['grid_table_candidates'])+' / '+str(pdf['supplemental_warning_panels'])],['Workbook table parts / source rows',str(workbook_counts['table_parts'])+' / '+format(workbook_counts['data_rows'],',')]]
 text+=kb.table(['Coverage','Count'],rows)
 table_pages=sum(summary['reference_kind_counts'].get(kind,0) for kind in ['table','extracted-table'])
 text+=str(table_pages)+' focused table or table-part pages are indexed in total. This is an output-page count, not a claim that every page corresponds to a separate logical source table.\n\n'
 text+='The three separately versioned code-publication groups are additional to the message-set counts. No supplied collection is routed to cards, trade finance or foreign exchange in this inventory.\n\n'
 text+='Source tables, page-level table parts, drawing occurrences and canonical reconstructions are different counts. Header PDFs have additional separately reviewed tables/figures. Detailed counts and source scopes are in '+kb.link(page,root/'catalog/coverage-summary.json','the catalog summary')+'.\n\n'
 text+='## Validation\n\n'+kb.table(['Check','Recorded result'],[['Original occurrences rehashed',validation['checks']['source_occurrences']],['Reference pages / local links',str(validation['checks']['reference_pages'])+' / '+str(validation['checks']['relative_links'])],['Exact schemas / literal declaration fragments',str(validation['checks']['schema_definitions'])+' / '+str(validation['checks']['schema_fragments'])],['Mechanical validation errors',len(validation['errors'])],['Retrieval scenarios passed',sum(x['pass'] for x in retrieval['checks'])],['Canonical diagram evidence errors',len(diagrams['errors'])],['DOCX destination gaps',len(docx['gaps'])]])
 text+='All checks are scoped. '+kb.link(page,root/'tracking/validation.json','Mechanical validation')+'; '+kb.link(page,root/'tracking/retrieval-validation.json','retrieval evidence')+'; '+kb.link(page,root/'tracking/reviews/message-role-audit.json','exact role quotes and direction checks')+'.\n\n## Remaining limits\n\n'+'\n'.join('- '+x for x in limitations)+'\n\n'+kb.link(page,root/'tracking/issues.md','Issue register')+' · '+kb.link(page,root/'shared/reference/native-assets/index.md','Native-object evidence')+' · '+kb.link(page,root/'tracking/corpus-assessment.json','Machine-readable assessment')+'\n\n## Retrieval and resumption\n\nStart with '+kb.link(page,root/'catalog/README.md','the entry guide and lookup commands')+', then follow a focused reference, its detailed type/table/diagram, and the original source where needed. '+kb.link(page,root/'tracking/checkpoint.json','The durable checkpoint')+' preserves the exact next action and source identities. No skills were created or installed.\n'
 kb.put(page,text)
 print(json.dumps({'status':report['status'],'sources':len(ss),'messages':summary['messages'],'participants':summary['participants'],'flows':summary['flows'],'diagrams':summary['diagram_pages'],'report':page.relative_to(root).as_posix()}))

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();finish(a.root.resolve())
