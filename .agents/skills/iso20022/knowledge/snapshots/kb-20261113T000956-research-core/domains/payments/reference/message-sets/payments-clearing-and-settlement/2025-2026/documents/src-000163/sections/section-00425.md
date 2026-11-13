---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.1 GroupHeader <GrpHdr>", "5.4.1.10 SettlementInformation <SttlmInf>", "5.4.1.10.3 ClearingSystem <ClrSys>", "5.4.1.10.3.1 Code <Cd>"]
file_pages: [584]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.1.10.3.1 Code <Cd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 584 to 584.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 584

```text
ClearingSystem <ClrSys> contains one of the following ClearingSystemIdentification3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 584
Or}   Proprietary <Prtry> [1..1] Text 584
5.4.1.10.3.1  Code <Cd>
Presence: [1..1]
Definition: Infrastructure through which the payment instruction is processed, as published in an
external clearing system identification code list.
Datatype: "ExternalCashClearingSystem1Code" on page 1227
5.4.1.10.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Clearing system identification in a proprietary form.
Datatype: "Max35Text" on page 1246
5.4.1.10.4  InstructingReimbursementAgent <InstgRmbrsmntAgt>
Presence: [0..1]
Definition: Agent through which the instructing agent will reimburse the instructed agent.
Usage: If InstructingAgent and InstructedAgent have the same reimbursement agent, then only
InstructingReimbursementAgent must be used.
InstructingReimbursementAgent <InstgRmbrsmntAgt> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 1173 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  1174
     BICFI <BICFI> [0..1] IdentifierSet C5 1174
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1175
     LEI <LEI> [0..1] IdentifierSet 1175
     Name <Nm> [0..1] Text 1175
     PostalAddress <PstlAdr> [0..1] ± 1175
     Other <Othr> [0..1] ± 1176
   BranchIdentification <BrnchId> [0..1]  1177
     Identification <Id> [0..1] Text 1177
     LEI <LEI> [0..1] IdentifierSet 1177
     Name <Nm> [0..1] Text 1177
     PostalAddress <PstlAdr> [0..1] ± 1177
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
584 March 2026
```

