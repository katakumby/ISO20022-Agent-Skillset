---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.10 RelatedAgents <RltdAgts>", "4.4.2.14.18.2.10.1 InstructingAgent <InstgAgt>"]
file_pages: [670]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.10.1 InstructingAgent <InstgAgt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 670 to 670.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 670

```text
RelatedAgents <RltdAgts> contains the following TransactionAgents6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructingAgent <InstgAgt> [0..1] ± 670
   InstructedAgent <InstdAgt> [0..1] ± 671
   DebtorAgent <DbtrAgt> [0..1] ± 672
   CreditorAgent <CdtrAgt> [0..1] ± 673
   IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 673
   IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 674
   IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 675
   ReceivingAgent <RcvgAgt> [0..1] ± 676
   DeliveringAgent <DlvrgAgt> [0..1] ± 677
   IssuingAgent <IssgAgt> [0..1] ± 678
   SettlementPlace <SttlmPlc> [0..1] ± 679
   Proprietary <Prtry> [0..*]  679
     Type <Tp> [1..1] Text 679
     Agent <Agt> [1..1] ± 679
4.4.2.14.18.2.10.1  InstructingAgent <InstgAgt>
Presence: [0..1]
Definition: Agent that instructs the next party in the chain to carry out the (set of) instruction(s).
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
670 March 2026
```

