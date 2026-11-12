---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.11 RemittanceInformation <RmtInf>", "4.4.3.8.9.11.2 Structured <Strd>", "4.4.3.8.9.11.2.6 TaxRemittance <TaxRmt>", "4.4.3.8.9.11.2.6.11 Record <Rcrd>", "4.4.3.8.9.11.2.6.11.8 TaxAmount <TaxAmt>"]
file_pages: [378]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.11.2.6.11.8 TaxAmount <TaxAmt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 378 to 378.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 378

```text
4.4.3.8.9.11.2.6.11.8  TaxAmount <TaxAmt>
Presence: [0..1]
Definition: Set of elements used to provide information on the amount of the tax record.
TaxAmount <TaxAmt> contains the following TaxAmount3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Rate <Rate> [0..1] Rate 378
   TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C9 378
   TotalAmount <TtlAmt> [0..1] Amount C2, C9 378
   Details <Dtls> [0..*]  379
     Period <Prd> [0..1]  379
       Year <Yr> [0..1] Year 379
       Type <Tp> [0..1] CodeSet 380
       FromToDate <FrToDt> [0..1] ± 380
     Amount <Amt> [1..1] Amount C2, C9 381
4.4.3.8.9.11.2.6.11.8.1  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 606
4.4.3.8.9.11.2.6.11.8.2  TaxableBaseAmount <TaxblBaseAmt>
Presence: [0..1]
Definition: Amount of money on which the tax is based.
Impacted by: C2 "ActiveOrHistoricCurrency", C9 "CurrencyAmount"
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
4.4.3.8.9.11.2.6.11.8.3  TotalAmount <TtlAmt>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 378 March 2026
```

