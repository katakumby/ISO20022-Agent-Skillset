---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.1 StatusRequestIdentification <StsReqId>"]
file_pages: [1068]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.1 StatusRequestIdentification <StsReqId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1068 to 1068.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1068

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C12,
C11
1151
     CreditorAgent <CdtrAgt> [0..1] ± 1152
     CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C12,
C11
1153
     Creditor <Cdtr> [0..1]  1154
{Or       Party <Pty> [1..1] ± 1154
Or}       Agent <Agt> [1..1] ± 1155
     CreditorAccount <CdtrAcct> [0..1] ± C12,
C11
1156
     UltimateCreditor <UltmtCdtr> [0..1]  1157
{Or       Party <Pty> [1..1] ± 1157
Or}       Agent <Agt> [1..1] ± 1158
     Purpose <Purp> [0..1] ± 1159
   SupplementaryData <SplmtryData> [0..*] ± C24 1159
9.4.3.1  StatusRequestIdentification <StsReqId>
Presence: [0..1]
Definition: Unique identification, as assigned by an instructing party for an instructed party, to
unambiguously identify the status request.
Usage: The instructing party is the party sending the request message and not the party that sent the
original instruction that is being reported on.
Datatype: "Max35Text" on page 1246
9.4.3.2  OriginalGroupInformation <OrgnlGrpInf>
Presence: [0..1]
Definition: Point to point reference, as assigned by the original instructing party, to unambiguously
identify the original message.
OriginalGroupInformation <OrgnlGrpInf> contains the following OriginalGroupInformation33
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 1068
   OriginalMessageNameIdentification <OrgnlMsgNmId> [1..1] Text 1069
   OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 1069
9.4.3.2.1  OriginalMessageIdentification <OrgnlMsgId>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1068 March 2026
```

