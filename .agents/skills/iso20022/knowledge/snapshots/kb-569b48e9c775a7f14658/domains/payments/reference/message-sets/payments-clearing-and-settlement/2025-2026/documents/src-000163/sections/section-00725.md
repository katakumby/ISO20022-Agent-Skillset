---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.30 RemittanceInformation <RmtInf>", "7.4.2.40.30.2 Structured <Strd>", "7.4.2.40.30.2.7 GarnishmentRemittance <GrnshmtRmt>", "7.4.2.40.30.2.7.5 Date <Dt>"]
file_pages: [981]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.30.2.7.5 Date <Dt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 981 to 981.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 981

```text
7.4.2.40.30.2.7.5  Date <Dt>
Presence: [0..1]
Definition: Date of payment which garnishment was taken from.
Datatype: "ISODate" on page 1239
7.4.2.40.30.2.7.6  RemittedAmount <RmtdAmt>
Presence: [0..1]
Definition: Amount of money remitted for the referred document.
Impacted by: C2 "ActiveOrHistoricCurrency", C9 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.4.2.40.30.2.7.7  FamilyMedicalInsuranceIndicator <FmlyMdclInsrncInd>
Presence: [0..1]
Definition: Indicates if the person to whom the garnishment applies (that is, the ultimate debtor) has
family medical insurance coverage available.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 1242):
• Meaning When True: True
• Meaning When False: False
7.4.2.40.30.2.7.8  EmployeeTerminationIndicator <MplyeeTermntnInd>
Presence: [0..1]
Definition: Indicates if the employment of the person to whom the garnishment applies (that is, the
ultimate debtor) has been terminated.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 1242):
• Meaning When True: True
• Meaning When False: False
7.4.2.40.30.2.8  SecuritiesData <SctiesData>
Presence: [0..*]
Definition: Provides information on the securities trades that make up the payment.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
981 March 2026
```

