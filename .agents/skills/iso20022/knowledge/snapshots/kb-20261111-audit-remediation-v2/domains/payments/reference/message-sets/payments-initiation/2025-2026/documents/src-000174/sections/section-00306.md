---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.1 PaymentIdentification <PmtId>"]
file_pages: [444]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.1 PaymentIdentification <PmtId>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 444 to 444.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 444

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Date <Dt> [0..1] Date 524
         RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 524
         FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 524
         EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 524
       SecuritiesData <SctiesData> [0..*]  524
         UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 525
         Amount <Amt> [0..1] Amount C1, C13 525
       AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 525
   SupplementaryData <SplmtryData> [0..*] ± C21 525
Constraints
• UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
• UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
5.4.2.18.1  PaymentIdentification <PmtId>
Presence: [1..1]
Definition: Set of elements used to reference a payment instruction.
PaymentIdentification <PmtId> contains the following elements (see "PaymentIdentification6" on
page 548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionIdentification <InstrId> [0..1] Text 548
   EndToEndIdentification <EndToEndId> [1..1] Text 549
   UETR <UETR> [0..1] IdentifierSet 549
5.4.2.18.2  PaymentTypeInformation <PmtTpInf>
Presence: [0..1]
Definition: Set of elements used to further specify the type of transaction.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 444 March 2026
```

