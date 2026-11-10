from pathlib import Path
import json,re,sys,lxml.etree as E
from pypdf import PdfReader
sys.path.insert(0,'tools');import kb
root=Path('.').resolve();sid='src-000374';records=json.loads((root/'work/documents'/sid/'records.json').read_text(encoding='utf-8'));ps={int(p['paragraph_id'][1:]):p['text'] for p in records['paragraphs']};ex=json.loads((root/'work/documents'/sid/'source-examples.json').read_text(encoding='utf-8'));pdf=PdfReader(root/'work/docx-render'/sid/'document.pdf');norm=lambda x:re.sub(r'\s+','',x);pages=[p.extract_text() for p in pdf.pages];sources=kb.sources(root)
for r,span in zip(ex,[(27,27),(28,28),(29,29),(30,30),(31,34),(34,38),(38,45),(45,47),(48,70)]):
 text=''.join(norm(pages[i-1]) for i in range(span[0],span[1]+1));lo,hi=r['payload_paragraphs'];missing=[{'paragraph':i,'text':ps[i]} for i in range(lo,hi+1) if ps[i].strip() and norm(ps[i]) not in text];r.update(word_pages=list(range(span[0],span[1]+1)),independent_word_text_comparison={'paragraphs_checked':hi-lo+1,'unmatched':missing})
 schema=next((s for s in sources if s['format']=='xsd' and r['message_id'] in s.get('message_ids',[])),None)
 if r['wellformedness']=='pass' and schema:
  try:
   x=E.fromstring(re.search(r'```xml\n(.*?)```',(root/r['path']).read_text(encoding='utf-8'),re.S).group(1).encode('utf-8'));ns=E.fromstring(kb.read_source(root,schema)).get('targetNamespace')
   for node in x.iter():node.tag='{'+ns+'}'+node.tag
   wrapper=E.Element('{'+ns+'}Document',nsmap={None:ns});wrapper.append(x);v=E.XMLSchema(E.fromstring(kb.read_source(root,schema)));valid=v.validate(wrapper);r['derived_envelope_xsd_check']={'result':'pass' if valid else 'fail','source_schema_id':schema['source_id'],'namespace':ns,'transform':'Assigned the supplied exact namespace to all payload tags and enclosed it in Document; interior values and structure unchanged. Original fragment retained.','errors':[str(e) for e in v.error_log]}
  except Exception as e:r['derived_envelope_xsd_check']={'result':'error','error':str(e)}
 else:r['derived_envelope_xsd_check']={'result':'not-run','reason':'Original XML malformed' if r['wellformedness']!='pass' else 'Matching exact schema not supplied'}
kb.dump(root/'work/documents'/sid/'source-examples.json',ex);print(json.dumps([{'path':r['path'].split('/')[-1],'unmatched':r['independent_word_text_comparison']['unmatched'],'schema':r['derived_envelope_xsd_check']} for r in ex],ensure_ascii=True))
