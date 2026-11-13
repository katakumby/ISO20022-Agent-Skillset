---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.7 SettlementInformation <SttlmInf>", "4.4.3.8.9.7.3 ClearingSystem <ClrSys>", "4.4.3.8.9.7.3.1 Code <Cd>"]
file_pages: [326]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.7.3.1 Code <Cd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 326 to 326.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 326

```text
ClearingSystem <ClrSys> contains one of the following ClearingSystemIdentification3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 326
Or}   Proprietary <Prtry> [1..1] Text 326
4.4.3.8.9.7.3.1  Code <Cd>
Presence: [1..1]
Definition: Infrastructure through which the payment instruction is processed, as published in an
external clearing system identification code list.
Datatype: "ExternalCashClearingSystem1Code" on page 591
4.4.3.8.9.7.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Clearing system identification in a proprietary form.
Datatype: "Max35Text" on page 609
4.4.3.8.9.7.4  InstructingReimbursementAgent <InstgRmbrsmntAgt>
Presence: [0..1]
Definition: Agent through which the instructing agent will reimburse the instructed agent.
Usage: If InstructingAgent and InstructedAgent have the same reimbursement agent, then only
InstructingReimbursementAgent must be used.
InstructingReimbursementAgent <InstgRmbrsmntAgt> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 539 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  540
     BICFI <BICFI> [0..1] IdentifierSet C4 540
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 541
     LEI <LEI> [0..1] IdentifierSet 541
     Name <Nm> [0..1] Text 541
     PostalAddress <PstlAdr> [0..1] ± 541
     Other <Othr> [0..1] ± 542
   BranchIdentification <BrnchId> [0..1]  543
     Identification <Id> [0..1] Text 543
     LEI <LEI> [0..1] IdentifierSet 543
     Name <Nm> [0..1] Text 543
     PostalAddress <PstlAdr> [0..1] ± 543
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 326 March 2026
```

