"""Persist the explicit 2026-11-09 visual comparison of FITRR figures17–36.

Not an automatic visual validator. Reuse is allowed only while the inspected
original, Mermaid and rendered PNG fingerprints still match the first record.
"""
import argparse,hashlib,json,re
from pathlib import Path
import kb

def main(root):
    manifest=json.loads((root/'work/fitrr-sequences.json').read_text(encoding='utf-8'))
    renders={x['diagram']:x for x in json.loads((root/'work/fitrr-sequences-render.json').read_text(encoding='utf-8'))}
    report=root/'tracking/reviews/fitrr-sequences.json';prior={x['figure_id']:x for x in json.loads(report.read_text(encoding='utf-8'))['records']} if report.exists() else {}
    inventory_path=root/'work/documents/src-000320/media-review-inventory.json';inv=json.loads(inventory_path.read_text(encoding='utf-8'));records=[]
    for item in manifest['outputs']:
        fid=item['figure_id'];n=int(fid[4:]);page=root/item['path'];rr=renders[fid];assert rr['result']=='pass'
        hashes={'mermaid_sha256':hashlib.sha256(page.with_suffix('.mmd').read_bytes()).hexdigest(),'original_sha256':hashlib.sha256((root/item['original']).read_bytes()).hexdigest(),'rendered_png_sha256':hashlib.sha256((root/rr['png']).read_bytes()).hexdigest()}
        assert hashes['mermaid_sha256']==item['mermaid_sha256'] and hashes['original_sha256']==item['original_sha256']
        if fid in prior:assert all(prior[fid][k]==v for k,v in hashes.items()),'Fresh visual review required for '+fid
        result='pass-with-documented-notation-limitations' if n in (19,22,23,28,31,35) else 'pass'
        status='needs-review' if n in (19,22,23,28,31,32,35) else 'reviewed'
        rec={**item,**hashes,'date':'2026-11-09','timezone':'Europe/Warsaw','render_result':'pass','renderer':rr['renderer'],'renderer_version':rr['version'],'svg':rr['svg'],'png':rr['png'],'visual_review':result,'review_status':status,'checks':['Original full-size source preview and final Mermaid PNG directly viewed.','All actor labels, arrow endpoints, order, repeated arrows and conditional branches compared.','OR alternatives, source success/failure wording and generic transaction labels retained.','Source34 first open arrowhead and source23 out-of-scope dashed arrows preserved.','Source23 final two arrows terminate at Public; the idle Reporting Entity lifeline remains.','Crossing-frame geometry and unsupported consider operator explicitly documented; no invented opt semantics.'],'scope':'Visible source sequence fidelity only; whole-publication tables, native hidden content and unresolved source conflicts remain separate.'};records.append(rec)
        m,b=kb.metadata(page);m.update(review_status=status,render_status='pass',visual_review=result,visual_review_date='2026-11-09',renderer='Mermaid '+rr['version'],rendered_svg=rr['svg'],rendered_png=rr['png'])
        if n==32:m['issue_ids']=['issue-000032']
        b=re.sub(r'## Rendering and visual review\n.*','## Rendering and visual review\n\nMermaid '+rr['version']+' with '+rr['renderer']+' parsed and rendered this reconstruction. The original and rendered PNG were directly compared on 2026-11-09 (Europe/Warsaw), checking labels, endpoints, order, branches and repeated exchanges. Result: **'+result+'**.\n\n'+kb.link(page,root/rr['svg'],'Rendered SVG')+' · '+kb.link(page,root/rr['png'],'Rendered PNG')+' · '+kb.link(page,report,'Hash-bound visual-review evidence')+'\n\nThis review does not resolve conflicting source statements or native hidden-content coverage.\n',b,flags=re.S);kb.put(page,kb.front(m)+b)
        for media in inv['media']:
            for occurrence in media['occurrences']:
                if occurrence['figure_id']==fid:
                    occurrence['canonical_diagram']=item['path'];media.update(disposition='source-reconstruction',canonical_diagram=item['path'],visual_review=result,review_status=status,complete_composite_review='source-preview-compared; full-Word-page-context-separate')
                    ep=root/occurrence['evidence_page'];em,eb=kb.metadata(ep);em.update(review_status=status,disposition='source-reconstruction',canonical_diagram=item['path'],render_status='pass',visual_review=result);kb.put(ep,kb.front(em)+eb.strip()+'\n')
    kb.dump(inventory_path,inv);kb.dump(report,{'source_id':manifest['source_id'],'source_sha256':manifest['source_sha256'],'date':'2026-11-09','records':records,'render_pass':len(records),'direct_visual_comparisons':len(records),'reviewed':sum(r['review_status']=='reviewed' for r in records),'needs_review':sum(r['review_status']=='needs-review' for r in records)});print(json.dumps({'diagrams':len(records),'reviewed':sum(r['review_status']=='reviewed' for r in records)}))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();main(a.root.resolve())
