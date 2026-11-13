---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "2.4.2.15.18.2.15.2 Structured <Strd>", "2.4.2.15.18.2.15.2.6 TaxRemittance <TaxRmt>", "2.4.2.15.18.2.15.2.6.11 Record <Rcrd>", "2.4.2.15.18.2.15.2.6.11.8 TaxAmount <TaxAmt>"]
file_pages: [198]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.15.2.6.11.8 TaxAmount <TaxAmt>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 198 to 198.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 198

```text
2.4.2.15.18.2.15.2.6.11.8  TaxAmount <TaxAmt>
Presence: [0..1]
Definition: Set of elements used to provide information on the amount of the tax record.
TaxAmount <TaxAmt> contains the following TaxAmount3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Rate <Rate> [0..1] Rate 198
   TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 198
   TotalAmount <TtlAmt> [0..1] Amount C2, C6 198
   Details <Dtls> [0..*]  199
     Period <Prd> [0..1]  199
       Year <Yr> [0..1] Year 199
       Type <Tp> [0..1] CodeSet 200
       FromToDate <FrToDt> [0..1] ± 200
     Amount <Amt> [1..1] Amount C2, C6 201
2.4.2.15.18.2.15.2.6.11.8.1  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 913
2.4.2.15.18.2.15.2.6.11.8.2  TaxableBaseAmount <TaxblBaseAmt>
Presence: [0..1]
Definition: Amount of money on which the tax is based.
Impacted by: C2 "ActiveOrHistoricCurrency", C6 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 886
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
2.4.2.15.18.2.15.2.6.11.8.3  TotalAmount <TtlAmt>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
198 March 2026
```

