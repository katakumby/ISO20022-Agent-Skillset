---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.10 RelatedAgents <RltdAgts>", "2.4.2.15.18.2.10.1 InstructingAgent <InstgAgt>"]
file_pages: [152]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.10.1 InstructingAgent <InstgAgt>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 152 to 152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 152

```text
RelatedAgents <RltdAgts> contains the following TransactionAgents6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructingAgent <InstgAgt> [0..1] ± 152
   InstructedAgent <InstdAgt> [0..1] ± 153
   DebtorAgent <DbtrAgt> [0..1] ± 154
   CreditorAgent <CdtrAgt> [0..1] ± 155
   IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 155
   IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 156
   IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 157
   ReceivingAgent <RcvgAgt> [0..1] ± 158
   DeliveringAgent <DlvrgAgt> [0..1] ± 159
   IssuingAgent <IssgAgt> [0..1] ± 160
   SettlementPlace <SttlmPlc> [0..1] ± 161
   Proprietary <Prtry> [0..*]  161
     Type <Tp> [1..1] Text 161
     Agent <Agt> [1..1] ± 161
2.4.2.15.18.2.10.1  InstructingAgent <InstgAgt>
Presence: [0..1]
Definition: Agent that instructs the next party in the chain to carry out the (set of) instruction(s).
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
152 March 2026
```

