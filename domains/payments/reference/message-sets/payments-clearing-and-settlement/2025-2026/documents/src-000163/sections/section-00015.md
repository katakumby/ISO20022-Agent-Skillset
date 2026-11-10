---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.1 StatusIdentification <StsId>"]
file_pages: [32]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.1 StatusIdentification <StsId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 32 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 32

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           RemittedAmount <RmtdAmt> [0..1] Amount C2, C8 115
           FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 115
           EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 115
         SecuritiesData <SctiesData> [0..*]  115
           UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 116
           Amount <Amt> [0..1] Amount C1, C9 116
         AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 116
     UltimateDebtor <UltmtDbtr> [0..1]  116
{Or       Party <Pty> [1..1] ± 117
Or}       Agent <Agt> [1..1] ± 118
     Debtor <Dbtr> [0..1]  119
{Or       Party <Pty> [1..1] ± 119
Or}       Agent <Agt> [1..1] ± 120
     DebtorAccount <DbtrAcct> [0..1] ± C16,
C15
121
     DebtorAgent <DbtrAgt> [0..1] ± 122
     DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C16,
C15
122
     CreditorAgent <CdtrAgt> [0..1] ± 123
     CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C16,
C15
124
     Creditor <Cdtr> [0..1]  125
{Or       Party <Pty> [1..1] ± 125
Or}       Agent <Agt> [1..1] ± 126
     CreditorAccount <CdtrAcct> [0..1] ± C16,
C15
127
     UltimateCreditor <UltmtCdtr> [0..1]  128
{Or       Party <Pty> [1..1] ± 128
Or}       Agent <Agt> [1..1] ± 129
     Purpose <Purp> [0..1] ± 130
   SupplementaryData <SplmtryData> [0..*] ± C31 130
2.4.3.1  StatusIdentification <StsId>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
32 March 2026
```

