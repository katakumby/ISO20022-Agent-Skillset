"""Curated BAH MUG diagram reconstructions and complete table normalization.
Source locators and original artwork are authoritative; no source file is modified.
"""
from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from extract_workbooks import fm,write,relative,esc
ROOT=Path(__file__).resolve().parents[1];JOB='job-000001';SID='src-000012'
WORK=ROOT/'work/documents'/SID;A=json.loads((WORK/'pdf-assets.json').read_text('utf-8'));IM={v['figure_id']:v for v in A['image_occurrences']}
BASE=Path('shared/reference/message-sets/business-application-header/2021-11-03-v3.0')
DOC=BASE/'documents'/SID;OUT=ROOT/'work/mug-diagrams';OUT.mkdir(parents=True,exist_ok=True)
def seq(actors,messages):
 t='sequenceDiagram\n'
 for ident,label in actors:t+='participant '+ident+' as '+label+'\n'
 for sender,arrow,receiver,label in messages:t+=sender+arrow+receiver+': '+label+'\n'
 return t
D={}
def add(i,title,code,meaning,flows=None,limitations=None):
 fid='fig-%04d'%i;D[fid]=dict(figure_id=fid,title=title,mermaid=code,meaning=meaning,flows=flows or [],limitations=limitations or [],review_status='needs-review')
 addpath=OUT/(fid+'.mmd');write(ROOT,addpath,code,JOB)
AB=[('A','Business Application A'),('B','Business Application B')]
add(1,'Business Message comprises BAH and ISO 20022 message','''flowchart TB
subgraph BM["Business Message"]
direction TB
H["ISO 20022 Business Appl. Header: AppHdr"]
M["ISO 20022 Message: Document"]
end
''','The source brackets group AppHdr and Document as one Business Message. The figure establishes this packaging relationship, not a business-entity model, transport protocol, mandatory envelope order or database composition. No additional multiplicity is inferred. The identical semantic illustration also appears as Figure1 on page29.',['business-message-exchange'])
add(2,'Technical middle man forwards the same business message',seq([('A','Business Application A'),('T',"'technical' middle man"),('B','Business Application B')],[('A','->>','T','Business Message A'),('T','->>','B','Business Message A')]),'Both source arrows carry Business Message A. The technical middle man forwards without processing or changing the business content. It is not promoted to a business sender/receiver by transport alone.',['business-message-exchange'])
add(3,'Business intermediary creates a different business message',seq([('A','Business Application A'),('P','Business Application A′'),('B','Business Application B')],[('A','->>','P','Business Message A'),('P','->>','B','Business Message A′')]),'A business application in the middle receives A and sends a different Business Message A′. The prime in both labels is preserved.',['business-message-exchange'])
add(4,'Direct Business Message exchange',seq(AB,[('A','->>','B','Business Message A')]),'The source has one directed Business Message A from Business Application A to B. Icon artwork is replaced with labelled participant lifelines; no institution class is inferred.',['business-message-exchange'])
add(10,'Basic exchange from Business Application A to B',seq(AB,[('A','->>','B','Business Message A')]),'The direct exchange diagram is repeated byte-for-byte in the implementation-specification and processing-date scenarios on pages13 and14. Each occurrence is retained.',['business-message-exchange','market-practice','business-processing-date'])
add(11,'Forwarding without a new business message',D['fig-0002']['mermaid'],D['fig-0002']['meaning'],['business-message-exchange'])
add(12,'Liquidity Transfer Order forwarded through a settlement platform',seq([('A','System Member A'),('S','Securities Settlement Platform'),('B','System Member B')],[('A','->>','S','Liquidity Transfer Order'),('S','->>','B','Liquidity Transfer Order')]),'The source example uses the Securities Settlement Platform as a technical middle man. Both arrows remain Liquidity Transfer Order; this illustration does not declare a particular exact liquidity-transfer schema version or require every settlement platform to be purely technical.',['business-message-exchange'])
add(13,'Business Application C processes and creates a new message',seq([('A','Business Application A'),('C','Business Application C'),('B','Business Application B')],[('A','->>','C','Business Message A'),('C','->>','B','Business Message B')]),'Business Application C is recipient of Message A and sender of a different Message B. This role differs from the technical-forwarder example on the same page.',['business-message-exchange'])
add(22,'Original message and a copy to another recipient',seq([('A','Business Application A'),('B','Business Application B'),('C','Business Application C')],[('A','-->>','B','Business Message 1 (Original)'),('A','->>','C','Business Message 2 (Copy)')]),'The original goes from A to B; the copy goes from A to C. The dashed original and solid copy arrows are preserved. The p16 usage table nevertheless prints To=B; the diagram and table claims are retained separately.',['copy'],['Source diagram/table receiver discrepancy: issue-000003.'])
add(23,'Original message followed by duplicate',seq(AB,[('A','-->>','B','BusinessMessage 1'),('A','->>','B','BusinessMessage2')]),'Both source arrows go A→B. The earlier message is dashed; the second is solid. §2.8 and its table identify the second as a duplicate using DUPL; that semantic comes from the surrounding source rather than an added arrow label.',['duplicate'])
add(24,'Requested resend by Securities Settlement Platform',seq([('M','System Member'),('S','Securities Settlement Platform')],[('S','-->>','M','BusinessMessage 1'),('M','->>','S','(Resend Message Request)'),('S','->>','M','Resend BusinessMessage1')]),'The platform sent the original to the member. The member requests a resend, then the platform resends to the member. This is the source example of a requested duplicate; the figure gives no exact schema IDs for these exchanges.',['duplicate'])
add(25,'Duplicate of a previously sent copy',seq([('A','Business Application A'),('B','Business Application B'),('C','Business Application C')],[('A','-->>','B','Business Message 1 (Original)'),('A','-->>','C','Business Message 2 (Copy)'),('A','->>','C','Business Message 3 (DUPL)')]),'Original message goes to B. The prior copy and its duplicate go to C. The source table uses CODU; the last drawn arrow is labelled DUPL. Both facts are retained, and the source table receiver B conflicts with C in the illustration.',['duplicate-of-copy'],['Source diagram/table receiver and copy-duplicate label discrepancy: issue-000003.'])
add(26,'Possible duplicate after a lost return path',seq(AB,[('A','-->>','B','BusinessMessage 1'),('B','--x','A','Unlabelled return path shown lost'),('A','->>','B','BusinessMessage1′')]),'The source has a dashed original A→B, a dashed B→A return path marked by a red cross, and solid resend A→B. The source does not label the return path; the Mermaid label explicitly describes that absence. §2.10 supplies the receiver decision: ignore if original was received, otherwise process as original.',['possible-duplicate'])
add(27,'Related new message through a business intermediary',seq([('A','Business Application A'),('B','Business Application B'),('C','Business Application C')],[('A','->>','B','Business Message A'),('B','->>','C','Business Message B')]),'The drawn sequence is A→B→C, and Business Message B is different from A. Related carries prior BAH context; CopyDuplicate and PossibleDuplicate are not used. The usage table on the page repeats From A / To B, so this source-direction discrepancy remains explicit.',['related-message'],['Source diagram/table direction discrepancy: issue-000003.'])
add(28,'Subscription confirmation cancellation links to earlier messages','''flowchart LR
subgraph X["SubscriptionOrderConfirmationCancellationInstructionV02"]
direction LR
ROOT["SbcptOrdrConfCxlInstr"] --> SEQ["source sequence"]
SEQ --> MID["MsgId"]
SEQ -.-> POOL["PoolRef"]
SEQ -.-> PREV["PrvsRef: 0..∞"]
SEQ -.-> REL["RltdRef"]
SEQ --> AMEND["AmdmntInd"]
SEQ -.-> MASTER["MstrRef"]
SEQ --> ORDERS["OrdrRefs: 1..∞"]
SEQ -.-> COPY["CpyDtls"]
end
PREV --> CONF["setr.012.001.04; SubscriptionOrderConfirmationV04"]
REL --> ORDER["setr.010.001.04; SubscriptionOrderV04"]
''','The source XML-tree illustration lists MsgId, PoolRef, PrvsRef, RltdRef, AmdmntInd, MstrRef, OrdrRefs and CpyDtls in that order. Its visible cardinalities are PrvsRef 0..∞ and OrdrRefs 1..∞. Green arrows map PrvsRef to setr.012.001.04 and RltdRef to setr.010.001.04. Dashed/solid source outlines are retained using dashed/solid branch lines; missing multiplicities are not filled with guessed schema defaults. This is a source illustration of earlier definitions, not a supplied XSD or the complete current message structure.',['related-message'],['Diagram is a source XML-tree excerpt; no complete schema coverage is asserted.'])
add(29,'Resolution of investigation refers to cancellation request and payment','''flowchart LR
R["RsltnOfInvstgtn"] --> C["CxlDtls: 0..∞"]
C -.-> G["OrgnlGrpInfAndSts"]
C -.-> P["OrgnlPmtInfAndSts: 0..∞"]
G --> GMID["OrgnlMsgId"]
G --> GMNAME["OrgnlMsgNmId"]
G -.-> CDT["OrgnlCreDtTm"]
G -.-> N["OrgnlNbOfTxs"]
G -.-> SUM["OrgnlCtrlSum"]
G -.-> STATUS["GrpCxlSts"]
G -.-> REASON["CxlStsRsnInf: 0..∞"]
G -.-> NSTATUS["NbOfTxsPerCxlSts: 0..∞"]
GMID --> CANC["camt.056.001.07; FIToFIPaymentCancellationRequestV07"]
subgraph TX["PaymentTransaction85: visible source type frame"]
CS["CxlStsId"]
CASE["RslvdCase"]
OG["OrgnlGrpInf"] --> OMID["OriginalGroupInformation29 / OrgnlMsgId"]
OG --> ONAME["OriginalGroupInformation29 / OrgnlMsgNmId"]
end
OMID --> PAYMENT["pacs.008.001.07; FIToFICustomerCreditTransferV07"]
''','The upper green arrow maps OrgnlGrpInfAndSts/OrgnlMsgId to the cancellation request camt.056.001.07. The lower green arrow maps OrgnlGrpInf/OrgnlMsgId within the visible PaymentTransaction85 excerpt to pacs.008.001.07. All visible field labels and printed 0..∞ marks are retained. The source image is an excerpt whose frame/connector continues beyond the shown region; the reconstruction does not invent the unshown connecting element or complete structural cardinalities. No cancellation-versus-reversal semantics are inferred merely from containment.',['related-message'],['Source screenshot is a cropped XML-tree excerpt; unshown connecting structure and defaults are not inferred.'])
add(31,'XML digital-signature signing and verification processes','''flowchart TB
subgraph SIGN["XML Digital Signature Signing Process"]
direction LR
M["Message"] --> CM["Canonicalize Message"] --> DG["Digest"] --> SI["SignedInfo containing Digest"] --> CSI["Canonicalize SignedInfo"] --> SG["Sign"] --> SV["SignatureValue"]
PK["Private Key"] --> SG
end
M --> SEND["Construct signed message and send"]
SV --> SEND
SEND --> NET["Any network"] --> RECEIVE["Receive signed message"]
subgraph VERIFY["XML Digital Signature Verification Process"]
direction LR
VSI["SignedInfo containing Digest"] --> VCSI["Canonicalize SignedInfo"] --> CRYPTO["Verify crypto algorithm"]
PUB["Public Key"] --> CRYPTO
VSV["SignatureValue"] --> CRYPTO
CRYPTO -->|KO| FAIL1["Verification failure"]
CRYPTO -->|OK| VM["Message"] --> VCM["Canonicalize Message"] --> VD["Digest"] --> COMP["Compare digests"]
OLD["SignedInfo containing Digest"] --> COMP
COMP -->|KO| FAIL2["Verification failure"]
COMP -->|OK| OK["Signature OK"]
end
RECEIVE -. "received signed content" .-> VSI
RECEIVE -. "received signed content" .-> VSV
RECEIVE -. "received message" .-> VM
''','Figure2 depicts signing with a private key and verification with a public key. The signing process canonicalizes the message, obtains its digest, canonicalizes SignedInfo and signs it. The signed message passes over any network. Verification checks the cryptographic signature and then compares message digests; either KO branch fails. The dotted links from the receive node clarify the source grouping of received content; they are editorial connectors for the bracketed source layout. The source gives no institution-specific sender/receiver roles.',['signed-message'])
add(32,'XML Signature elements mapped to processing steps','''flowchart LR
subgraph PROC["Processing steps"]
direction TB
GET(["Get (XML) data"]) --> TRANS(["Apply transformations: C14N, XSLT, XPath, ..."]) --> DIG(["Generate digest"]) --> CAN(["Canonicalize SignedInfo"]) --> SIGN(["Sign SignedInfo"])
DIG -->|"repeat for another Reference"| GET
end
subgraph XML["Signature"]
direction TB
SI["SignedInfo"]
CM["CanonicalizationMethod Algorithm=..."]
SM["SignatureMethod Algorithm=..."]
REF["Reference URI=..."]
TR["Transforms / Transform Algorithm=...; another Transform Algorithm=..."]
DM["DigestMethod Algorithm=..."]
DV["DigestValue"]
R2["Another Reference URI=..."]
SV["SignatureValue"]
KI["KeyInfo / KeyValue"]
SI --- CM
SI --- SM
SI --- REF
REF --- TR
REF --- DM
REF --- DV
SI --- R2
end
GET -.-> REF
TRANS -.-> TR
DIG -.-> DM
DIG -.-> DV
CAN -.-> CM
SIGN -.-> SM
SIGN -.-> SV
''','The red process path iterates get-data, transform and digest for references, then canonicalizes and signs SignedInfo. Grey source mapping arrows connect data selection to Reference URI, transforms to Transform entries, digest generation to DigestMethod and DigestValue, canonicalization to CanonicalizationMethod, and signing to SignatureMethod and SignatureValue. The shown Signature also contains KeyInfo/KeyValue. XML attribute placeholders and sample digest/signature bytes remain in the original artwork; the graph labels describe XML locations, not executable XML.',['signed-message'])
add(33,'Signing a BAH and mapping generated values','''flowchart TB
GET["Get Business Message"] --> B["Extract BAH from Message"]
GET --> M["Extract ISO 20022 Message From Message"]
GET --> K["Construct KeyInfo"]
B --> ENV["Perform Enveloped Transform"] --> BC["Perform c14n Transform"] --> BD["Digest"] --> BR["Insert in Reference"]
M --> MC["Perform c14n Transform"] --> MD["Digest"] --> MR["Insert in Reference"]
K --> KC["Perform c14n Transform"] --> KD["Digest"] --> KR["Insert in Reference"]
BR --> SCI["Perform c14n on SignedInfo"]
MR --> SCI
KR --> SCI
SCI --> ALG["Perform sign algorithm"] --> VAL["Insert in SignatureValue"]
subgraph XML["ds:Signature source XML frame"]
SI["ds:SignedInfo: CanonicalizationMethod and SignatureMethod"]
RKEY["Reference URI=#Unique-id-to-KeyInfo; c14n transform; DigestMethod; DigestValue"]
RBAH["Reference URI=empty string; enveloped-signature and c14n transforms; DigestMethod; DigestValue"]
RDOC["Reference with no URI attribute; c14n transform; DigestMethod; DigestValue"]
XV["ds:SignatureValue"]
XK["ds:KeyInfo Id=Unique-id-to-KeyInfo; X509Data / X509Certificate"]
SI --- RKEY
SI --- RBAH
SI --- RDOC
end
BR -. "source blue connector" .-> RBAH
MR -. "source blue connector appears to target this Reference" .-> RKEY
KR -. "source blue connector appears to target this Reference" .-> RDOC
VAL --> XV
K --> XK
''','Figure4 has three digest branches: BAH (with enveloped-signature transform), ISO message and constructed KeyInfo. All feed canonicalized SignedInfo, signing and SignatureValue. Orange arrows map SignatureValue and constructed KeyInfo to the corresponding XML elements. The drawn blue reference connectors appear to cross the ISO-document and KeyInfo destinations relative to §§4.2.7–4.2.10 and Figure5. The reconstruction retains the apparent drawn destinations, with explicit uncertainty, rather than silently correcting them. The text-defined URI rules remain separate: KeyInfo uses #id, BAH uses empty URI, ISO message omits URI.',['signed-message'],['Open source connector discrepancy: issue-000017.'])
add(34,'Verifying a BAH signature','''flowchart TB
GET["Get Business Message"] --> B["Extract BAH from Message"]
GET --> M["Extract ISO 20022 Message From Message"]
GET --> K["Extract KeyInfo from Signature"]
B --> ENV["Perform Enveloped Transform"] --> BC["Perform c14n Transform"] --> BD["Digest"] --> BR["Compare With Reference"]
M --> MC["Perform c14n Transform"] --> MD["Digest"] --> MR["Compare With Reference"]
K --> KC["Perform c14n Transform"] --> KD["Digest"] --> KR["Compare With Reference"]
BR --> D1{"OK?"}
MR --> D1
KR --> D1
D1 -->|No| F1(["Verification failed"])
D1 -->|Yes| SV["Get SignatureValue"]
D1 -->|Yes| SI["Get SignedInfo"]
D1 -->|Yes| CERT["Get certificate"]
SV --> ALG["Perform verify algorithm"]
SI --> ALG
CERT --> ALG
ALG --> D2{"OK?"}
D2 -->|No| F2(["Verification failed"])
D2 -->|Yes| OK(["Verification successful"])
subgraph XML["ds:Signature source XML frame"]
XSI["ds:SignedInfo: CanonicalizationMethod and SignatureMethod"]
RKEY["Reference URI=#Unique-id-to-KeyInfo; c14n transform; DigestMethod; DigestValue"]
RBAH["Reference URI=empty string; enveloped-signature and c14n transforms; DigestMethod; DigestValue"]
RDOC["Reference with no URI attribute; c14n transform; DigestMethod; DigestValue"]
XSV["ds:SignatureValue"]
XK["ds:KeyInfo Id=Unique-id-to-KeyInfo"]
XC["ds:X509Data / ds:X509Certificate"]
XSI --- RKEY
XSI --- RBAH
XSI --- RDOC
XK --- XC
end
RBAH -.-> BR
RDOC -.-> MR
RKEY -.-> KR
XK --> K
XSV --> SV
XSI --> SI
XC -.-> CERT
''','Figure5 extracts BAH, ISO message and KeyInfo, transforms and digests them, then compares all three references. Any failed comparison ends in verification failed. If references pass, SignatureValue, SignedInfo and certificate feed the verification algorithm. Its No branch fails; Yes is verification successful. Blue source connectors map the empty-URI reference to BAH, URI-absent reference to ISO message, and #KeyInfo-id reference to KeyInfo. Orange and green data-source arrows from Signature, SignedInfo and certificate are retained by labelled nodes and arrows.',['signed-message'])
write(ROOT,ROOT/'work/mug-diagram-curation.json',json.dumps(D,ensure_ascii=False,indent=2),JOB)
print('Prepared '+str(len(D))+' canonical Mermaid reconstructions.')
