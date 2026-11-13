---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.4 Payment <Pmt>", "5.4.2.1.3.2.1.4.16 Parties <Pties>", "5.4.2.1.3.2.1.4.16.9 IntermediaryAgent2 <IntrmyAgt2>"]
file_pages: [308]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.4.16.9 IntermediaryAgent2 <IntrmyAgt2>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 308 to 308.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 308

```text
IntermediaryAgent1 <IntrmyAgt1> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 803 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  804
     BICFI <BICFI> [0..1] IdentifierSet C2 804
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 805
     LEI <LEI> [0..1] IdentifierSet 805
     Name <Nm> [0..1] Text 805
     PostalAddress <PstlAdr> [0..1] ± 805
     Other <Othr> [0..1] ± 806
   BranchIdentification <BrnchId> [0..1]  807
     Identification <Id> [0..1] Text 807
     LEI <LEI> [0..1] IdentifierSet 807
     Name <Nm> [0..1] Text 807
     PostalAddress <PstlAdr> [0..1] ± 807
5.4.2.1.3.2.1.4.16.9  IntermediaryAgent2 <IntrmyAgt2>
Presence: [0..1]
Definition: Agent between the debtor's agent and the creditor's agent.
Usage: If more than two intermediary agents are present, then IntermediaryAgent2 identifies the agent
between the IntermediaryAgent1 and the IntermediaryAgent3.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 308 February 2025
```

