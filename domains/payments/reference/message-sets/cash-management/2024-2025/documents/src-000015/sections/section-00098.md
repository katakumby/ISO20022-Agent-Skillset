---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.19 Parties <Pties>", "4.4.2.2.2.2.3.19.1 InstructingAgent <InstgAgt>"]
file_pages: [168]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.19.1 InstructingAgent <InstgAgt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 168 to 168.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 168

```text
Parties <Pties> contains the following PaymentTransactionParty4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructingAgent <InstgAgt> [0..1] ± 168
   InstructedAgent <InstdAgt> [0..1] ± 169
   UltimateDebtor <UltmtDbtr> [0..1]  170
{Or     Party <Pty> [1..1] ± 170
Or}     Agent <Agt> [1..1] ± 171
   Debtor <Dbtr> [0..1]  172
{Or     Party <Pty> [1..1] ± 172
Or}     Agent <Agt> [1..1] ± 173
   DebtorAgent <DbtrAgt> [0..1] ± 174
   InstructingReimbursementAgent <InstgRmbrsmntAgt> [0..1] ± 175
   InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 176
   IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 176
   IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 177
   IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 178
   CreditorAgent <CdtrAgt> [0..1] ± 179
   Creditor <Cdtr> [0..1]  180
{Or     Party <Pty> [1..1] ± 180
Or}     Agent <Agt> [1..1] ± 181
   UltimateCreditor <UltmtCdtr> [0..1]  182
{Or     Party <Pty> [1..1] ± 182
Or}     Agent <Agt> [1..1] ± 183
4.4.2.2.2.2.3.19.1  InstructingAgent <InstgAgt>
Presence: [0..1]
Definition: Agent that instructs the next party in the chain to carry out the (set of) instruction(s).
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 168 February 2025
```

