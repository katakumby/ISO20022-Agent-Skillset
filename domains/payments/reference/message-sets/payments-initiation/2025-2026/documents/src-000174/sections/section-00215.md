---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.1 InterbankSettlementAmount <IntrBkSttlmAmt>"]
file_pages: [319]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.1 InterbankSettlementAmount <IntrBkSttlmAmt>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 319 to 319.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 319

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         RemittedAmount <RmtdAmt> [0..1] Amount C2, C9 386
         FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 386
         EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 386
       SecuritiesData <SctiesData> [0..*]  386
         UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 387
         Amount <Amt> [0..1] Amount C1, C10 387
       AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 387
   UltimateDebtor <UltmtDbtr> [0..1]  387
{Or     Party <Pty> [1..1] ± 388
Or}     Agent <Agt> [1..1] ± 389
   Debtor <Dbtr> [0..1]  390
{Or     Party <Pty> [1..1] ± 390
Or}     Agent <Agt> [1..1] ± 391
   DebtorAccount <DbtrAcct> [0..1] ± C18,
C17
392
   DebtorAgent <DbtrAgt> [0..1] ± 393
   DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C18,
C17
393
   CreditorAgent <CdtrAgt> [0..1] ± 394
   CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C18,
C17
395
   Creditor <Cdtr> [0..1]  396
{Or     Party <Pty> [1..1] ± 396
Or}     Agent <Agt> [1..1] ± 397
   CreditorAccount <CdtrAcct> [0..1] ± C18,
C17
398
   UltimateCreditor <UltmtCdtr> [0..1]  399
{Or     Party <Pty> [1..1] ± 399
Or}     Agent <Agt> [1..1] ± 400
   Purpose <Purp> [0..1] ± 401
4.4.3.8.9.1  InterbankSettlementAmount <IntrBkSttlmAmt>
Presence: [0..1]
Definition: Amount of money moved between the instructing agent and the instructed agent.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 319 March 2026
```

