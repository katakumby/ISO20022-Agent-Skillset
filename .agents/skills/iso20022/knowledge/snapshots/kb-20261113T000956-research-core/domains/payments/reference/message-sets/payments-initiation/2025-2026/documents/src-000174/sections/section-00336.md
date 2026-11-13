---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.15 Tax <Tax>", "5.4.2.18.15.11 Record <Rcrd>", "5.4.2.18.15.11.8 TaxAmount <TaxAmt>"]
file_pages: [478]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.15.11.8 TaxAmount <TaxAmt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 478 to 478.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 478

```text
5.4.2.18.15.11.8  TaxAmount <TaxAmt>
Presence: [0..1]
Definition: Set of elements used to provide information on the amount of the tax record.
TaxAmount <TaxAmt> contains the following TaxAmount3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Rate <Rate> [0..1] Rate 478
   TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 478
   TotalAmount <TtlAmt> [0..1] Amount C2, C12 478
   Details <Dtls> [0..*]  479
     Period <Prd> [0..1]  479
       Year <Yr> [0..1] Year 479
       Type <Tp> [0..1] CodeSet 480
       FromToDate <FrToDt> [0..1] ± 480
     Amount <Amt> [1..1] Amount C2, C12 481
5.4.2.18.15.11.8.1  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 606
5.4.2.18.15.11.8.2  TaxableBaseAmount <TaxblBaseAmt>
Presence: [0..1]
Definition: Amount of money on which the tax is based.
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
5.4.2.18.15.11.8.3  TotalAmount <TtlAmt>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 478 March 2026
```

