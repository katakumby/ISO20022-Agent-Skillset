---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.4 Payment <Pmt>", "5.4.2.1.3.2.1.4.16 Parties <Pties>", "5.4.2.1.3.2.1.4.16.1 InstructingAgent <InstgAgt>"]
file_pages: [299]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.4.16.1 InstructingAgent <InstgAgt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 299 to 299.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 299

```text
Parties <Pties> contains the following PaymentTransactionParty4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructingAgent <InstgAgt> [0..1] ± 299
   InstructedAgent <InstdAgt> [0..1] ± 300
   UltimateDebtor <UltmtDbtr> [0..1]  301
{Or     Party <Pty> [1..1] ± 301
Or}     Agent <Agt> [1..1] ± 302
   Debtor <Dbtr> [0..1]  303
{Or     Party <Pty> [1..1] ± 303
Or}     Agent <Agt> [1..1] ± 304
   DebtorAgent <DbtrAgt> [0..1] ± 305
   InstructingReimbursementAgent <InstgRmbrsmntAgt> [0..1] ± 306
   InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 307
   IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 307
   IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 308
   IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 309
   CreditorAgent <CdtrAgt> [0..1] ± 310
   Creditor <Cdtr> [0..1]  311
{Or     Party <Pty> [1..1] ± 311
Or}     Agent <Agt> [1..1] ± 312
   UltimateCreditor <UltmtCdtr> [0..1]  313
{Or     Party <Pty> [1..1] ± 313
Or}     Agent <Agt> [1..1] ± 314
5.4.2.1.3.2.1.4.16.1  InstructingAgent <InstgAgt>
Presence: [0..1]
Definition: Agent that instructs the next party in the chain to carry out the (set of) instruction(s).
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 299 February 2025
```

