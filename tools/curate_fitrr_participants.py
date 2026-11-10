"""Reconcile only FITRR abbreviations explicitly defined by this source T2."""
import argparse,json,re
from pathlib import Path
import kb

SID='src-000320';ALIASES={'ca':('competent-authority','CA',6),'re':('reporting-entity','RE',26),'sa':('supervisory-authority','SA',29)}

def main(root):
    base=root/'domains/securities/reference/message-sets/fitrr/2025';parts=root/'shared/reference/participants';d=json.loads((root/'work/documents'/SID/'records.json').read_text(encoding='utf-8'));t2=d['tables'][1]['rows'];changes={}
    for short,(full,label,row) in ALIASES.items():
        old=parts/f'participant-{SID}-{short}.md';dest=parts/f'participant-{SID}-{full}.md';om,ob=kb.metadata(old);dm,db=kb.metadata(dest)
        matches=[(i+1,r) for i,r in enumerate(t2) if r[0].strip()==label];assert len(matches)==1,(label,matches);actualrow,values=matches[0];assert kb.slug(values[1])==full,(label,values)
        dm['aliases']=sorted(set(dm.get('aliases',[])+[label]));dm['source_labels']=sorted(set(dm.get('source_labels',[])+[label]));dm['alias_evidence']=[{'source_id':SID,'table_id':'T2','row':actualrow,'source_label':label,'expanded_label':values[1]}]
        db=re.sub(r'\n<!-- FITRR-ALIAS -->.*?<!-- /FITRR-ALIAS -->\n?','\n',db,flags=re.S);db+='\n<!-- FITRR-ALIAS -->\n## Source-supported abbreviation\n\n**'+label+'** is explicitly defined as **'+values[1]+'** in '+kb.link(dest,base/'documents'/SID/'tables/tbl-0002.md','T2')+', row '+str(actualrow)+'. This alias is scoped to this publication; it does not merge the functional participant with an institution or business role.\n<!-- /FITRR-ALIAS -->\n';kb.put(dest,kb.front(dm)+db.strip()+'\n')
        am={'template':False,'document_kind':'participant-alias','review_status':'reviewed','title':label+' — source-defined alias','domain':'securities','source_ids':[SID],'source_editions':['July 2025'],'message_sets':['fitrr'],'canonical_participant_id':dest.stem,'canonical_path':dest.relative_to(root).as_posix(),'source_locations':[{'source_id':SID,'table_id':'T2','row':actualrow,'xml_path':f'/w:document/w:body/w:tbl[2]/w:tr[{actualrow}]'}],'limitations':['Alias equivalence is limited to this source definition; business roles such as NCA and ESMA remain separate.']}
        kb.put(old,kb.front(am)+'# '+label+'\n\nUse '+kb.link(old,dest,values[1])+' as the canonical scoped participant. T2 row '+str(actualrow)+' explicitly establishes this abbreviation. Prior extracted content is retained in local version history.\n');changes[old.stem]=dest.stem
    edited=0
    for page in list(base.rglob('*.md'))+[p for p in parts.glob(f'participant-{SID}-*.md') if p.stem not in changes]:
        text=page.read_text(encoding='utf-8');new=text
        for old,newid in changes.items():new=re.sub(re.escape(old)+r'(?=["\s./,)\]])',newid,new)
        if new!=text:kb.put(page,new);edited+=1
    # Consolidate responsibilities by exact source abbreviation, retaining the
    # original table's initiator even where it conflicts with prose/diagram.
    for abbreviation,slug in [('RE','reporting-entity'),('CA','competent-authority'),('SA','supervisory-authority'),('Relevant CA','relevant-ca')]:
        p=parts/f'participant-{SID}-{slug}.md';m,b=kb.metadata(p);rows=[]
        for t in d['tables'][22:31]:
            for ordinal,row in enumerate(t['rows'][1:],2):
                if len(row)>=3 and row[2].strip()==abbreviation:rows.append([row[0],row[1],kb.link(p,base/'documents'/SID/'tables'/(t['table_id']+'.md'),t['source_table_id']+' row '+str(ordinal))])
        b=re.sub(r'\n<!-- FITRR-RESPONSIBILITIES -->.*?<!-- /FITRR-RESPONSIBILITIES -->\n?','\n',b,flags=re.S);b+='\n<!-- FITRR-RESPONSIBILITIES -->\n## Source-assigned activities\n\n'+kb.table(['Activity','Source responsibility','Precise evidence'],rows)+'\nThe source Initiator cells govern this table. T26 assigns Receive Message to SA while its description and diagram identify CA; '+kb.link(p,root/'tracking/issues.md#issue-000036','issue-000036')+' preserves the conflict. T18 has a separate calculation-result role conflict, '+kb.link(p,root/'tracking/issues.md#issue-000032','issue-000032')+'.\n'
        if slug=='reporting-entity':b+='\nIdentifier context: P207 says a reminder should be at the Reporting Entity identifier level, for example Segment MIC. This is a reminder-routing example, not a universal identifier requirement for every participant or flow.\n'
        b+='<!-- /FITRR-RESPONSIBILITIES -->\n';kb.put(p,kb.front(m)+b.strip()+'\n')
    print(json.dumps({'source_supported_aliases':len(changes),'references_updated':edited}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();main(a.root.resolve())
