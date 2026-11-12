---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.47 RemittanceInformation <RmtInf>", "6.4.2.47.2 Structured <Strd>", "6.4.2.47.2.6 TaxRemittance <TaxRmt>", "6.4.2.47.2.6.11 Record <Rcrd>", "6.4.2.47.2.6.11.8 TaxAmount <TaxAmt>"]
file_pages: [819]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.47.2.6.11.8 TaxAmount <TaxAmt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 819 to 819.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 819

```text
6.4.2.47.2.6.11.8  TaxAmount <TaxAmt>
Presence: [0..1]
Definition: Set of elements used to provide information on the amount of the tax record.
TaxAmount <TaxAmt> contains the following TaxAmount3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Rate <Rate> [0..1] Rate 819
   TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 819
   TotalAmount <TtlAmt> [0..1] Amount C2, C12 819
   Details <Dtls> [0..*]  820
     Period <Prd> [0..1]  820
       Year <Yr> [0..1] Year 820
       Type <Tp> [0..1] CodeSet 821
       FromToDate <FrToDt> [0..1] ± 821
     Amount <Amt> [1..1] Amount C2, C12 822
6.4.2.47.2.6.11.8.1  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 1243
6.4.2.47.2.6.11.8.2  TaxableBaseAmount <TaxblBaseAmt>
Presence: [0..1]
Definition: Amount of money on which the tax is based.
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
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
6.4.2.47.2.6.11.8.3  TotalAmount <TtlAmt>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
819 March 2026
```

