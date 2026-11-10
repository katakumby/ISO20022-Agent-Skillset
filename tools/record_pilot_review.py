"""Record the pilot diagrams actually inspected in this session; hash-bound evidence."""
import argparse,json,re,hashlib,os
from pathlib import Path
P=argparse.ArgumentParser();P.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);A=P.parse_args();R=A.root.resolve()
D=R/'domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/pilot'
report=json.loads((R/'work/pilot-evidence/render-report.json').read_text())
notes={
'01-typical-sequence':'Compared both actors, instruction direction, two separate optional status boxes, confirmation and message labels.',
'02-partial-sequence':'Compared both actors, six message arrows, first two statuses in one optional box, second optional status, Partial and Remaining quantity notes.',
'03-cancellation-sequence':'Compared original instruction and cancellation request directions, optional intermediate status, final status and all labels.',
'04-cancellation-advice-sequence':'Compared both arrows and corrected exact AnyAdviceOrAnyStatement label before final render.',
'05-reversal-sequence':'Compared two servicer-to-instructing-party arrows, confirmation then reversal, exact labels.',
'06-business-processes':'Compared all 11 process nodes and 15 directed edges with Windows System.Drawing rasterization of unchanged EMF; no actors/include/extend semantics invented.',
'07-typical-activity':'Compared responsible-party boundaries, start/end points, both settlement decisions, successful/unsuccessful validation, pending loops and cross-party status paths to EMF preview; omitted successful-validation update remains explicitly stated in text.',
'08-role-model':'High-priority explicit review: compared 11 labels, 10 relationships, 4 hollow-triangle generalizations and 6 directed associations. Actor glyphs represented by class boxes; limitation documented; no cardinalities added.'}
expected_hashes={'01-typical-sequence': 'c80cd83d7fd61fa35cd11eb75ce8791b05d2456959f8ef3d5a07c578a6aa5272', '02-partial-sequence': 'e66f08302f0969783d20573d98e7ba76c32f5f2b55a0fa03178407088b1161f5', '03-cancellation-sequence': '8cf404add9f906a9c20755883b3768aa6df932c7e8eabc0347b3a370984036a4', '04-cancellation-advice-sequence': 'ca62d9cf2452a24a29f02129e65eb9e59ff4a239b0bdf67918803d5fb4557bd2', '05-reversal-sequence': 'f6c31260508e1f8f363f4b9ab523a3f148e2e3b7484d461b6a4174b3ad313588', '06-business-processes': '485abb0d67fec6bc66f50ac764b74b80cc4dc192b2fbb529a8a6ec6257437003', '07-typical-activity': '5768abb04be9673049bde40a347cfbaba4e7bdd46ba4108b9e840266ea25fb68', '08-role-model': '15adc0d3e280faeb445575e642aa85a0966ab3277c5dcf7fb9422b2e14918a3a'}
for x in report:
 p=D/(x['diagram']+'.md');mmd=D/(x['diagram']+'.mmd')
 assert hashlib.sha256(mmd.read_bytes()).hexdigest()==expected_hashes[x['diagram']], 'Diagram changed: a fresh visual review is required' 
 x.update(visual_review='pass',review_date='2026-11-08',source_comparison=notes[x['diagram']],mmd_sha256=hashlib.sha256(mmd.read_bytes()).hexdigest())
 text=p.read_text(encoding='utf8').replace('mermaid_renderer: null','mermaid_renderer: '+json.dumps(x['renderer'])).replace('mermaid_version: null','mermaid_version: "12.3.0"').replace('render_status: "not-run"','render_status: "pass"').replace('visual_review: "not-run"','visual_review: "pass"')
 text=text.replace('limitations: ["Required renderer and rendered-output visual review pending."]','limitations: ["Source and reconstructed layouts differ; semantics and notation differences are documented below."]')
 text=text.replace('| Original figure inspection | pending | Requires image inspection |','| Original figure inspection | performed | Original inspected on 2026-11-08 |')
 text=text.replace('| Mermaid parse/render | not-run | Renderer check pending |','| Mermaid parse/render | pass | Mermaid 12.3.0; Chromium 156.0.8078.81; 2026-11-08 |')
 text=text.replace('| Rendered reconstruction compared with original | not-run | Required before reviewed |','| Rendered reconstruction compared with original | pass | '+notes[x['diagram']]+' |')
 target=os.path.relpath(R/x['svg'],p.parent).replace('\\','/');png=os.path.relpath(R/x['png'],p.parent).replace('\\','/')
 text+='\n[Validated SVG](<'+target+'>) · [Readable rendered PNG](<'+png+'>)\n\nVisual review applies to this reconstructed view; it does not claim complete source-wide figure coverage or resolve source semantic defects.\n'
 p.write_text(text,encoding='utf8')
out=R/'tracking/reviews/pilot-diagrams.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps({'reviewed_diagrams':len(report),'evidence':str(out)},indent=2))
