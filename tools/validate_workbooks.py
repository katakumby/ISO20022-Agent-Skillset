#!/usr/bin/env python3
"""Independently reconcile extracted workbook values against openpyxl.
No original workbook is saved or recalculated. Use --root, --source and --report.
"""
import argparse,datetime,io,json
from decimal import Decimal,InvalidOperation
from pathlib import Path
import openpyxl
from openpyxl.utils.datetime import from_excel
from kb import sources,read_source

def validate(root,source):
    sid=source['source_id'];m=json.loads((root/'work/workbooks'/sid/'workbook.json').read_text('utf-8'))
    w=openpyxl.load_workbook(io.BytesIO(read_source(root,source)),read_only=True,data_only=False)
    differences=[];count=0
    for sheet in m['sheets']:
        actual={c['cell']:c for c in sheet['cells'] if c['value'] is not None or 'formula' in c}
        independent={c.coordinate:c for row in w[sheet['name']] for c in row if c.value is not None}
        if actual.keys()!=independent.keys():differences.append({'sheet':sheet['name'],'cell_set_difference':len(actual.keys()^independent.keys())})
        for coordinate,c in independent.items():
            a=actual.get(coordinate);count+=1
            if not a:continue
            av=a['value'];bv=c.value
            if 'formula' in a:
                av='='+a['formula']
            elif isinstance(bv,(datetime.datetime,datetime.date,datetime.time)):
                try:av=from_excel(float(av),w.epoch)
                except (ValueError,TypeError):pass
            elif isinstance(bv,(float,int)) and not isinstance(bv,bool):
                try:av=Decimal(av);bv=Decimal(str(bv))
                except (InvalidOperation,TypeError):pass
            if av!=bv:differences.append({'sheet':sheet['name'],'cell':coordinate,'extracted':str(av),'independent':str(bv)})
        coverage=sheet['table_pages']
        for a,b in zip(coverage,coverage[1:]):
            if a['row_end']+1!=b['row_start']:differences.append({'sheet':sheet['name'],'split_gap':True})
    w.close()
    return {'source_id':sid,'nonempty_cells_compared':count,'differences':differences,'result':'pass' if not differences else 'fail','date':'2026-11-08','method':'Direct OOXML extraction compared to independent openpyxl parse; every nonempty cell coordinate and value; dates decoded with source epoch; table split continuity checked.','visual_review':'not performed by this validator'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--source',action='append');p.add_argument('--report');a=p.parse_args();root=a.root.resolve();results=[]
    for source in sources(root):
        if source['format']!='xlsx' or (a.source and source['source_id'] not in a.source):continue
        result=validate(root,source);results.append(result)
        print(json.dumps({k:result[k] for k in ['source_id','nonempty_cells_compared','result']}),flush=True)
    if a.report:
        report=(root/a.report).resolve()
        if not report.is_relative_to(root) or report.is_relative_to(root/'raw-input'):raise ValueError('Report must remain under repository and outside raw-input.')
        report.parent.mkdir(parents=True,exist_ok=True);report.write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    if any(r['differences'] for r in results):raise SystemExit(1)
if __name__=='__main__':main()
