"""Source-inspected communication overviews and activity diagrams for src-000196."""
import argparse,hashlib,json,re
from pathlib import Path
import kb

SID='src-000196';DATE='2026-11-09'

def activity(instruction,monitor,process,decision,finish,partial=False,bar=False):
 code='flowchart TB\n  subgraph I["Instructing Party"]\n'
 code+='    IS@{shape: sm-circ, label: " "}\n    IF@{shape: framed-circle, label: " "}\n'
 code+='    IA("'+instruction+'")\n    IM("'+monitor+'")\n    ID{"'+decision+'"}\n    IU("Update Status")\n    IX(["'+finish+'"])\n'
 code+='    IS --> IA\n    IM --> ID\n    ID -->|No| IU\n    IU --> IM\n'
 if partial:code+='    IP{"Partially Settled?"}\n    IPart(["Partially Settle"])\n    ID -->|Yes| IP\n    IP -->|No| IX\n    IP -->|Yes| IPart\n    IPart --> IM\n'
 else:code+='    ID -->|Yes| IX\n'
 if bar or partial:code+='    IJ@{shape: fork, label: " "}\n    IJ --> IM\n'
 code+='    IX --> IF\n  end\n  subgraph E["Executing/Servicing Party"]\n    EP("'+('Process cancellation request' if bar else 'Process instruction')+'")\n    ED{"Processed?"}\n    EU("Update Status")\n    EM("'+process+'")\n    ES{"'+decision+'"}\n    UP("Update Status")\n    EX(["'+finish+'"])\n    EF@{shape: framed-circle, label: " "}\n    EP --> ED\n    ED -->|No| EU\n    ED -->|Yes| EM\n    EM --> ES\n    ES -->|No| UP\n    UP --> EM\n'
 if partial:code+='    EPartDecision{"Partially Settled?"}\n    EPart(["Partially Settle"])\n    EJ@{shape: fork, label: " "}\n    ES -->|Yes| EPartDecision\n    EPartDecision -->|No| EX\n    EPartDecision -->|Yes| EPart\n    EPart --> EM\n    EPart --> EJ\n    EX --> EJ\n'
 else:code+='    ES -->|Yes| EX\n'
 code+='    EX --> EF\n  end\n  IA --> EP\n  EU --> IA\n'
 if partial:code+='  UP --> IJ\n  EJ --> IJ\n'
 elif bar:code+='  UP --> IJ\n  EX --> IJ\n'
 else:code+='  UP --> IM\n  EX --> IM\n'
 code+='  classDef main fill:#d1d8b8,stroke:#111,color:#111\n  classDef status fill:#c0d1e5,stroke:#111,color:#111\n  class IA,IM,ID,IX,EP,ED,EM,ES,EX main\n  class IU,EU,UP status\n'
 code+='  classDef start fill:#4472c4,stroke:#4472c4\n  classDef terminal fill:#fff,stroke:#111,stroke-width:3px\n  classDef synchronization fill:#111,stroke:#111\n  class IS start\n  class IF,EF terminal\n'
 if bar or partial:code+='  class IJ synchronization\n'
 if partial:code+='  class EJ synchronization\n'
 if partial:code+='  class IP,IPart,EPartDecision,EPart main\n'
 return code

ACTIVITIES={
 2:dict(title='Reporting communication overview',kind='flowchart',flow_slugs=['reporting-push','reporting-pull'],roles=['account-owner','account-servicer'],table=None,code='flowchart LR\n  A["Account Owner"] -->|Request For Statement Status Advice| B["Account Servicer"]\n  B -->|Statement Of Pending Transactions| A\n  B -->|Statement Of Transactions| A\n  B -->|Statement Of Holdings| A\n  B -->|Statement Of Allegements| A\n',notes=['This is a scope/communication overview, not an ordered sequence. Generic labels are retained, including the owner-to-servicer “Request For Statement Status Advice” label; they are not silently replaced with modern exact message names.']),
 3:dict(title='Intra-position communication overview',kind='flowchart',flow_slugs=['intra-position-instruction'],roles=['account-owner','account-servicer'],table=None,code='flowchart LR\n  A["Account Owner"] -->|Intra-Position Instruction| B["Account Servicer"]\n  B -->|Intra-Position Instruction Status Advice| A\n  B -->|Intra-Position Advice| A\n  B -->|Statement Of Intra-Position Advice| A\n',notes=['The source provides communication categories, not exact definition IDs or a required temporal sequence. All four original labels are preserved.']),
 11:dict(title='Intra-position instruction activity',kind='flowchart',flow_slugs=['intra-position-instruction'],roles=['instructing-party','executing-servicing-party'],table=29,code=activity('Instruct intra-position movement','Monitor Intra-position movement instruction','Intra-position movement process','Executed?','Move position'),notes=['The two swimlanes, processing/execution decisions, Yes/No branches, return-to-instruction path, status loops and both endpoints are retained.']),
 12:dict(title='Partial settlement activity',kind='flowchart',flow_slugs=['partial-settlement'],roles=['instructing-party','executing-servicing-party'],table=30,code=activity('Instruct settlement','Monitor Matching and Settlement Process','Matching and Settlement Process','Settled?','Settle instruction',partial=True),notes=['Both lanes contain a Settled? decision followed by Partially Settled?. Partial settlement loops back; full settlement reaches the end point.','The source has two synchronization bars joining outcome/status routes. Native fork/join shapes preserve their placement in the relationship graph; no additional requirement to wait for mutually exclusive outcomes is inferred.']),
 33:dict(title='Cancellation-request activity',kind='flowchart',flow_slugs=['cancellation-request'],roles=['instructing-party','executing-servicing-party'],table=45,code=activity('Request cancellation','Monitor Cancellation request','Cancellation process','Cancelled?','Cancel instruction',bar=True),notes=['The source includes a synchronization bar for status/outcome information returning to the instructing participant. A cancellation request does not itself establish completed cancellation.']),
 34:dict(title='Cancellation-advice activity',kind='flowchart',flow_slugs=['cancellation-advice'],roles=['instructing-party','executing-servicing-party'],table=46,code='flowchart TB\n  subgraph I["Instructing Party"]\n    IP("Process advice, confirm or report")\n    IC("Process cancellation")\n  end\n  subgraph E["Executing/Servicing Party"]\n    ST@{shape: sm-circ, label: " "}\n    EA("Advice, confirm or report")\n    EC("Advice cancellation")\n    ST --- EA\n    EA --> EC\n  end\n  EA --- IP\n  EC --- IC\n  classDef context fill:#bed0e9,stroke:#111,color:#111\n  classDef focus fill:#d1d8b8,stroke:#111,color:#111\n  class IP,EA context\n  class IC,EC focus\n',notes=['The visible horizontal source connectors have no clear arrowheads; they remain plain connections. The source activity table and narrative establish the participants’ communication responsibilities.','The source wording “Advice cancellation” is retained. Existing cancellation-advice/instruction-cancellation/status exclusions remain governed by the documented source conflicts, not resolved by this picture.']),
 35:dict(title='Settlement reversal-advice activity',kind='flowchart',flow_slugs=['reversal-advice'],roles=['instructing-party','executing-servicing-party'],table=47,code='flowchart TB\n  subgraph I["Instructing Party"]\n    IP("Process confirmation")\n    IR("Process reversal")\n  end\n  subgraph E["Executing/Servicing Party"]\n    ST@{shape: sm-circ, label: " "}\n    EC("Confirmation")\n    ER("Advice reversal")\n    ST --- EC\n    EC --> ER\n  end\n  EC --- IP\n  ER --- IR\n  classDef context fill:#bed0e9,stroke:#111,color:#111\n  classDef focus fill:#d1d8b8,stroke:#111,color:#111\n  class IP,EC context\n  class IR,ER focus\n',notes=['Horizontal source connections have no clearly visible arrowheads and remain plain connections. The vertical confirmation-to-reversal arrow is retained.','The picture supplies no post-reversal settlement outcome; the linked flow retains the source narrative on the underlying instruction remaining open.']),
}

from settlement_status_diagrams import STATUS
ACTIVITIES.update(STATUS)
from settlement_financing_activities import FINANCING
ACTIVITIES.update(FINANCING)
from settlement_remaining_activities import REMAINING
ACTIVITIES.update(REMAINING)
from settlement_scope_overview import SCOPE,participants as scope_participants
ACTIVITIES.update(SCOPE)

def main(root):
 source=next(s for s in kb.sources(root) if s['source_id']==SID);base=root/source['set_path'];out=base/'diagrams/settlement-activities';flowbase=base/'flows'
 inv=json.loads((root/'work/documents'/SID/'media-review-inventory.json').read_text(encoding='utf-8'))
 media={int(re.search(r'image(\d+)',m['original']).group(1)):m for m in inv['media']}
 scope_participants(root,source,out/'fig-0001.md')
 outputs=[]
 for number,data in ACTIVITIES.items():
  original=media[number];occ=original['occurrences'][0];page=out/f'fig-{number:04d}.md';mmd=page.with_suffix('.mmd')
  metadata={'template':False,'document_kind':'diagram','review_status':'needs-review','manual_curated':True,'diagram_id':f'fig-{number:04d}','title':data['title'],'domain':'securities','source_ids':[SID],'source_editions':['March 2026'],'message_sets':['settlement-and-reconciliation'],'content_origin':'source-reconstruction','diagram_kind':data['kind'],'source_locations':[{'source_id':SID,'locator':occ['source_locator'],'heading_path':occ['heading_path'],'xml_path':occ['xml_path'],'figure_id':occ['figure_id']}],'original_asset':original['original'],'source_preview':original['preview'],'participant_ids':['participant-settlement-reconciliation-'+x for x in data['roles']],'flow_ids':['flow-settlement-reconciliation-'+x for x in data['flow_slugs']],'render_status':'not-run','visual_review':'not-run','limitations':data['notes'],'updated':DATE}
  code='%%{init: {"themeVariables": {"edgeLabelBackground": "#ffffff"}, "themeCSS": ".edgeLabel rect { fill: #fff !important; opacity: 1 !important; }"}}%%\n'+re.sub(r'(shape|label):(?=\S)',r'\1: ',data['code']).replace('shape: sm-circ','shape: f-circ')
  text=kb.front(metadata)+'# '+data['title']+'\n\n'+kb.source_link(root,page,source)+'; '+occ['source_locator']+'; '+ ' / '.join(occ['heading_path'])+'; `'+occ['xml_path']+'`.\n\n'+kb.link(page,root/original['original'],'Unchanged original asset')+' · '+kb.link(page,root/original['preview'],'Readable original/complete vector preview')+'\n\n## Mermaid source reconstruction\n\n```mermaid\n'+code+'```\n\n## Participants and flow context\n\n'
  text+='\n'.join('- '+kb.link(page,root/'shared/reference/participants'/('settlement-reconciliation-'+x+'.md'),x.replace('-',' ')) for x in data['roles'])+'\n\n'
  text+='\n'.join('- '+kb.link(page,flowbase/(slug+'.md'),slug.replace('-',' ')) for slug in data['flow_slugs'])+'\n\n'
  if data['table']:
   table=base/'documents'/SID/'tables'/f'tbl-{data["table"]:04d}.md';text+=kb.link(page,table,'Activity table T'+str(data['table'])+' — all steps, definitions and Initiator values')+'. These source responsibilities are distinct from message sender/receiver assertions.\n\n'
  text+='## Semantics and limitations\n\n'+'\n'.join('- '+x for x in data['notes'])+'\n\n'
  if data['kind']=='flowchart' and number not in (1,2,3,19,20,21,22,23,24):text+='Swimlane ownership is represented by native flowchart subgraphs. Decisions retain their source labels and branch labels; start/end symbols and explicit source bars use native Mermaid shapes. The layout is reflowed without changing endpoints. Green/blue fills preserve the source’s distinction between the foreground activities and surrounding status/context activities where visible.\n\n'
  text+='## Rendering and visual review\n\nThe original was directly inspected. Reconstruction parsing, rendering and final visual comparison remain pending.\n';kb.put(mmd,code);kb.put(page,text)
  ep=root/occ['evidence_page'];em,eb=kb.metadata(ep);em.update(canonical_diagram=page.relative_to(root).as_posix(),disposition='canonical-reconstruction-created-needs-review');eb=re.sub(r'\n<!-- CANONICAL-ACTIVITY-START -->.*?<!-- CANONICAL-ACTIVITY-END -->\n?','\n',eb,flags=re.S);kb.put(ep,kb.front(em)+eb.strip()+'\n\n<!-- CANONICAL-ACTIVITY-START -->\n'+kb.link(ep,page,'Canonical source reconstruction and review evidence')+'\n<!-- CANONICAL-ACTIVITY-END -->\n')
  for slug in data['flow_slugs']:
   fp=flowbase/(slug+'.md');fm,fb=kb.metadata(fp);tag=f'SOURCE-ACTIVITY-{number:04d}';fb=re.sub(r'\n<!-- '+tag+r'-START -->.*?<!-- '+tag+r'-END -->\n?','\n',fb,flags=re.S);fm['diagram_ids']=sorted(set(fm.get('diagram_ids',[]))|{f'fig-{number:04d}'});fb+='\n<!-- '+tag+'-START -->\n'+kb.link(fp,page,data['title']+' — source activity/communication diagram')+'\n<!-- '+tag+'-END -->\n';kb.put(fp,kb.front(fm)+fb.strip()+'\n')
  outputs.append({'source_id':SID,'source_figure_id':occ['figure_id'],'path':page.relative_to(root).as_posix(),'original':original['original'],'original_sha256':original['original_sha256'],'preview':original['preview'],'mermaid_sha256':hashlib.sha256(mmd.read_bytes()).hexdigest(),'flow_paths':[(flowbase/(slug+'.md')).relative_to(root).as_posix() for slug in data['flow_slugs']],'limitations':data['notes'],'visual_review':'pending-render-comparison'})
 # These four images are notation symbols inside a substantive table, not four
 # independent business diagrams. Preserve the originals and the exact legend.
 meanings={6:('Start Point','Shows where the lifecycle of the business process commences.'),7:('End Point','Shows where the lifecycle of the business process may ends.'),8:('Lozenge (or diamond)','Indicates that a choice between several actions can be made.'),9:('Bar','Indicates that several actions are initiated in parallel.')}
 for number,(name,meaning) in meanings.items():
  item=media[number];occ=item['occurrences'][0];ep=root/occ['evidence_page'];m,_=kb.metadata(ep);m.update(document_kind='notation-legend-evidence',disposition='retained-notation-legend',visual_review='classification-pass',render_status='not-applicable',limitations=['This asset is a symbol in the source notation legend, not an independent business diagram.']);kb.put(ep,kb.front(m)+'# '+name+' — notation legend\n\n'+kb.source_link(root,ep,source)+'; '+occ['source_locator']+'; `'+occ['xml_path']+'`.\n\n'+kb.link(ep,root/item['original'],'Original symbol')+' · '+kb.link(ep,base/'documents'/SID/'tables/tbl-0027.md','Complete source legend table T27')+'\n\n**Source definition:** '+meaning+'\n\nThe symbol and its source table definition were inspected together on 2026-11-09. The asset remains part of the substantive notation legend; it is not excluded as decoration or turned into a separate invented business flow.\n')
 kb.dump(root/'work/settlement-activities.json',{'date':DATE,'source_id':SID,'source_sha256':source['sha256'],'outputs':outputs})
 ix=out/'index.md';kb.put(ix,kb.front({'template':False,'document_kind':'diagram-index','review_status':'needs-review','domain':'securities','source_ids':[SID],'message_sets':['settlement-and-reconciliation']})+'# Settlement activity and scope diagrams\n\n'+kb.table(['Figure','Reference','Review'],[[x['source_figure_id'],kb.link(ix,root/x['path'],Path(x['path']).stem),x['visual_review']] for x in outputs]))
 if (root/'tracking/reviews/settlement-activities.json').exists():
  from record_settlement_activity_review import main as restore_review
  restore_review(root)
 print(json.dumps({'source_reconstructions':len(outputs),'legend_symbols_accounted_for':4}))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);main(p.parse_args().root.resolve())
