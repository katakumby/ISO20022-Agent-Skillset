---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.26 RemittanceInformation <RmtInf>", "2.4.2.19.26.2 Structured <Strd>", "2.4.2.19.26.2.6 TaxRemittance <TaxRmt>", "2.4.2.19.26.2.6.11 Record <Rcrd>", "2.4.2.19.26.2.6.11.8 TaxAmount <TaxAmt>", "2.4.2.19.26.2.6.11.8.4 Details <Dtls>"]
file_pages: [120]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.26.2.6.11.8.4 Details <Dtls>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 120 to 120.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 120

```text
Definition: Total amount that is the result of the calculation of the tax for the record.
Impacted by: C2 "ActiveOrHistoricCurrency", C19 "CurrencyAmount"
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
2.4.2.19.26.2.6.11.8.4  Details <Dtls>
Presence: [0..*]
Definition: Set of elements used to provide details on the tax period and amount.
Details <Dtls> contains the following TaxRecordDetails3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Period <Prd> [0..1]  120
     Year <Yr> [0..1] Year 120
     Type <Tp> [0..1] CodeSet 121
     FromToDate <FrToDt> [0..1] ± 121
   Amount <Amt> [1..1] Amount C2, C19 122
2.4.2.19.26.2.6.11.8.4.1  Period <Prd>
Presence: [0..1]
Definition: Set of elements used to provide details on the period of time related to the tax payment.
Period <Prd> contains the following TaxPeriod3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Year <Yr> [0..1] Year 120
   Type <Tp> [0..1] CodeSet 121
   FromToDate <FrToDt> [0..1] ± 121
2.4.2.19.26.2.6.11.8.4.1.1  Year <Yr>
Presence: [0..1]
Definition: Year related to the tax payment.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 120 March 2026
```

