---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>", "5.4.2.18.17.2 Structured <Strd>", "5.4.2.18.17.2.7 GarnishmentRemittance <GrnshmtRmt>", "5.4.2.18.17.2.7.5 Date <Dt>"]
file_pages: [524]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17.2.7.5 Date <Dt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 524 to 524.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 524

```text
5.4.2.18.17.2.7.5  Date <Dt>
Presence: [0..1]
Definition: Date of payment which garnishment was taken from.
Datatype: "ISODate" on page 603
5.4.2.18.17.2.7.6  RemittedAmount <RmtdAmt>
Presence: [0..1]
Definition: Amount of money remitted for the referred document.
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 585
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
5.4.2.18.17.2.7.7  FamilyMedicalInsuranceIndicator <FmlyMdclInsrncInd>
Presence: [0..1]
Definition: Indicates if the person to whom the garnishment applies (that is, the ultimate debtor) has
family medical insurance coverage available.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 605):
• Meaning When True: True
• Meaning When False: False
5.4.2.18.17.2.7.8  EmployeeTerminationIndicator <MplyeeTermntnInd>
Presence: [0..1]
Definition: Indicates if the employment of the person to whom the garnishment applies (that is, the
ultimate debtor) has been terminated.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 605):
• Meaning When True: True
• Meaning When False: False
5.4.2.18.17.2.8  SecuritiesData <SctiesData>
Presence: [0..*]
Definition: Provides information on the securities trades that make up the payment.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 524 March 2026
```

