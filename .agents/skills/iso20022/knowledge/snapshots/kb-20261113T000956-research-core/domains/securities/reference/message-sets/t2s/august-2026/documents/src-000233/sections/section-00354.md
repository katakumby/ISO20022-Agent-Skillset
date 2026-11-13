---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["19 camt.081.001.02 IntraBalanceMovementModificationReportV02", "19.4 Message Building Blocks", "19.4.4 ReportOrError <RptOrErr>", "19.4.4.1 Modifications <Mods>", "19.4.4.1.5 Modification <Mod>", "19.4.4.1.5.4 ProcessingStatus <PrcgSts>"]
file_pages: [459]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 19.4.4.1.5.4 ProcessingStatus <PrcgSts>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 459 to 459.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 459

```text
CashAccountServicer <CshAcctSvcr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 2919 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  2920
     BICFI <BICFI> [0..1] IdentifierSet C3 2920
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 2920
     LEI <LEI> [0..1] IdentifierSet 2920
     Name <Nm> [0..1] Text 2921
     PostalAddress <PstlAdr> [0..1] ± 2921
     Other <Othr> [0..1] ± 2921
   BranchIdentification <BrnchId> [0..1]  2922
     Identification <Id> [0..1] Text 2922
     LEI <LEI> [0..1] IdentifierSet 2922
     Name <Nm> [0..1] Text 2922
     PostalAddress <PstlAdr> [0..1] ± 2923
19.4.4.1.5.4  ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Status and status reason of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus71Choice" on page 3152 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3152
Or   Pending <Pdg> [1..1] ± 3153
Or   Rejected <Rjctd> [1..1] ± 3153
Or   Repair <Rpr> [1..1] ± 3153
Or   Denied <Dnd> [1..1] ± 3154
Or   Completed <Cmpltd> [1..1] ± C6 3154
Or}   Proprietary <Prtry> [1..1] ± 3155
19.4.4.1.5.5  RequestReference <ReqRef>
Presence: [1..1]
Definition: Unambiguous identification of the modification request.
Datatype: "Max35Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 459 August 2026
```

