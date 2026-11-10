from pathlib import Path
import sys,io,zipfile,copy,json,lxml.etree as E
sys.path.insert(0,'tools');import kb
root=Path('.').resolve();s=next(x for x in kb.sources(root) if x['source_id']=='src-000374');z=zipfile.ZipFile(io.BytesIO(kb.read_source(root,s)));doc=E.fromstring(z.read('word/document.xml'));ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','mc':'http://schemas.openxmlformats.org/markup-compatibility/2006','wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'};body=doc.find('w:body',ns);srcp=body.findall('w:p',ns)[54];runs=[r for r in srcp.findall('w:r',ns) if r.find('mc:AlternateContent',ns) is not None];out=root/'work/documents/src-000374/native-canvases';out.mkdir(exist_ok=True);records=[]
for i,r in enumerate(runs,1):
 d=copy.deepcopy(doc);b=d.find('w:body',ns);sec=copy.deepcopy(b.find('w:sectPr',ns));b.clear();p=E.SubElement(b,'{'+ns['w']+'}p');rr=copy.deepcopy(r);p.append(rr)
 for a in rr.findall('.//wp:anchor',ns):
  for tag in ['positionH','positionV']:
   el=a.find('wp:'+tag,ns);el.set('relativeFrom','margin');el.find('wp:posOffset',ns).text='0'
 b.append(sec);target=out/f'canvas-{i}.docx'
 with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED) as dest:
  for info in z.infolist():dest.writestr(copy.copy(info),z.read(info.filename) if info.filename!='word/document.xml' else E.tostring(d,xml_declaration=True,encoding='UTF-8',standalone=True))
 records.append({'canvas':i,'source_id':s['source_id'],'source_locator':f'P55 /w:r containing mc:AlternateContent[{i}]','working_copy':target.relative_to(root).as_posix(),'derivation':'Isolated original anchor canvas into a one-paragraph working document; changed only outer anchor offsets to zero at page margins. Source shapes, connectors, labels and package assets remain unchanged.','source_labels':rr.xpath('.//w:t/text()',namespaces=ns)})
kb.dump(out/'derivation.json',records);print(json.dumps(records,ensure_ascii=True))

