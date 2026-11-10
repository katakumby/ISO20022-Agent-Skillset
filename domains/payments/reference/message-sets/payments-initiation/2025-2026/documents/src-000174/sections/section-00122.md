---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.1 InterbankSettlementAmount <IntrBkSttlmAmt>"]
file_pages: [188]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.1 InterbankSettlementAmount <IntrBkSttlmAmt>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 188 to 188.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 188

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         RemittedAmount <RmtdAmt> [0..1] Amount C2, C8 255
         FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 255
         EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 255
       SecuritiesData <SctiesData> [0..*]  255
         UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 256
         Amount <Amt> [0..1] Amount C1, C9 256
       AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 256
   UltimateDebtor <UltmtDbtr> [0..1]  256
{Or     Party <Pty> [1..1] ± 257
Or}     Agent <Agt> [1..1] ± 258
   Debtor <Dbtr> [0..1]  259
{Or     Party <Pty> [1..1] ± 259
Or}     Agent <Agt> [1..1] ± 260
   DebtorAccount <DbtrAcct> [0..1] ± C16,
C15
261
   DebtorAgent <DbtrAgt> [0..1] ± 262
   DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C16,
C15
262
   CreditorAgent <CdtrAgt> [0..1] ± 263
   CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C16,
C15
264
   Creditor <Cdtr> [0..1]  265
{Or     Party <Pty> [1..1] ± 265
Or}     Agent <Agt> [1..1] ± 266
   CreditorAccount <CdtrAcct> [0..1] ± C16,
C15
267
   UltimateCreditor <UltmtCdtr> [0..1]  268
{Or     Party <Pty> [1..1] ± 268
Or}     Agent <Agt> [1..1] ± 269
   Purpose <Purp> [0..1] ± 270
3.4.3.7.12.1  InterbankSettlementAmount <IntrBkSttlmAmt>
Presence: [0..1]
Definition: Amount of money moved between the instructing agent and the instructed agent.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 188 March 2026
```

