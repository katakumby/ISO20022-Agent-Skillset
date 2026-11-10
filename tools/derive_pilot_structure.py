"""Create a labelled XSD-derived ordered top-level view, without inventing a source figure."""
from pathlib import Path
from lxml import etree
import argparse,json,os
P=argparse.ArgumentParser();P.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);A=P.parse_args();R=A.root.resolve();BASE=R/'domains/securities/reference/messages/sese.023.001.13';D=BASE/'diagrams';D.mkdir(parents=True,exist_ok=True)
SOURCE=R/'raw-input/settlement_and_reconciliation/sese.023.001.13.xsd';XS='{http://www.w3.org/2001/XMLSchema}';schema=etree.parse(str(SOURCE)).getroot();ns=schema.get('targetNamespace');name='SecuritiesSettlementTransactionInstructionV13'
t=schema.find(XS+'complexType[@name="'+name+'"]');seq=t.find(XS+'sequence');els=list(seq);assert len(els)==19
coverage=json.loads((BASE/'schema-coverage.json').read_text());types={x['name']:R/x['path'] for x in coverage['components'] if x['kind'] in ['complexType','simpleType']}
p=D/'fig-0001.md'
def lk(path,label):return '['+label+'](<'+os.path.relpath(path,p.parent).replace('\\','/')+'>)'
code='flowchart TB\n  DOC["Document root"] --> PAY["SctiesSttlmTxInstr [1..1]"]\n  PAY --> TYPE["SecuritiesSettlementTransactionInstructionV13"]\n  TYPE --> SEQ["sequence [1..1] effective defaults"]\n'
for i,e in enumerate(els,1):
 card=e.get('minOccurs','1')+'..'+e.get('maxOccurs','1').replace('unbounded','*');code+='  E'+str(i)+'["'+str(i).zfill(2)+' '+e.get('name')+' ['+card+']"]\n'
code+='  SEQ --> E1\n'+'\n'.join('  E'+str(i)+' --> E'+str(i+1) for i in range(1,19))+'\n'
meta={'template':False,'document_kind':'diagram','review_status':'needs-review','domain':'securities','message_ids':['sese.023.001.13'],'diagram_id':'fig-0001','diagram_kind':'flowchart','content_origin':'xsd-derived','source_ids':['src-000214'],'source_editions':[],'namespace':ns,'source_locations':[{'source_id':'src-000214','qname':'{'+ns+'}'+name,'schema_path':'/xs:schema/xs:complexType[@name="'+name+'"]/xs:sequence','line':seq.sourceline}],'original_image':None,'mermaid_renderer':None,'mermaid_version':None,'render_status':'not-run','visual_review':'not-run','limitations':['Only the top-level ordered sequence is shown; nested types and choices remain linked through the complete type reference.']}
text='---\n'+'\n'.join(k+': '+json.dumps(v) for k,v in meta.items())+'\n---\n\n# sese.023.001.13 ordered top-level structure\n\n'
text+='This is an **XSD-derived** view. There is no original source image. It represents XML declaration order, not a business flow, ownership model or database schema. Optional blocks may be absent; repeatable blocks may repeat at their declared sequence position.\n\nSource: '+lk(SOURCE,'src-000214')+'; namespace `'+ns+'`; `Document` root declaration line4; type `Document` contains `SctiesSttlmTxInstr`; type `{'+ns+'}'+name+'` lines'+str(t.sourceline)+'–1306, `xs:sequence` line'+str(seq.sourceline)+'.\n\n## Mermaid\n\n```mermaid\n'+code+'```\n\n## Exact sequence and type navigation\n\nThe enclosing `xs:sequence` omits minOccurs and maxOccurs: both are effective defaults 1. The root payload element also has effective [1..1]. Explicit source particle attributes are distinguished below from defaults. Nested choices are not expanded into independent required fields.\n\n| Position | XML element | Member cardinality | Source min/max attributes | Type | Source line |\n| --- | --- | --- | --- | --- | --- |\n'
for i,e in enumerate(els,1):
 card=e.get('minOccurs','1')+'..'+e.get('maxOccurs','1').replace('unbounded','*');attrs='minOccurs='+e.get('minOccurs')+', maxOccurs='+e.get('maxOccurs') if e.get('minOccurs') is not None else 'Both omitted; effective defaults 1'
 text+='| '+' | '.join([str(i),e.get('name'),card,attrs,lk(types[e.get('type')],e.get('type')),str(e.sourceline)])+' |\n'
text+='\n## Textual interpretation\n\nNineteen member declarations occur in the shown order. TxId, SttlmTpAndAddtlParams, TradDtls, FinInstrmId, QtyAndAcctDtls and SttlmParams each have effective [1..1]. Lnkgs and SplmtryData allow [0..unbounded], DgtlPmtSttlm permits [0..2], and the remaining ten members permit [0..1]. Cardinalities here apply within one instance of the enclosing sequence. Type references preserve reused types, nested compositors and restrictions.\n\n## Review evidence\n\nMermaid parse/render and direct comparison against the nineteen declarations are pending.\n\n'+lk(BASE/'structure.md','Complete schema reference')+'\n'
p.write_text(text,encoding='utf8');p.with_suffix('.mmd').write_text(code,encoding='utf8')
(D/'index.md').write_text('# sese.023.001.13 diagrams\n\n- [XSD-derived ordered top-level structure](fig-0001.md)\n',encoding='utf8')
print(str(p))
