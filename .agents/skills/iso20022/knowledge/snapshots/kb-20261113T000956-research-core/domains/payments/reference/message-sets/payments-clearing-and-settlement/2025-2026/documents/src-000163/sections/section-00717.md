---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.30 RemittanceInformation <RmtInf>", "7.4.2.40.30.2 Structured <Strd>", "7.4.2.40.30.2.6 TaxRemittance <TaxRmt>", "7.4.2.40.30.2.6.11 Record <Rcrd>", "7.4.2.40.30.2.6.11.8 TaxAmount <TaxAmt>"]
file_pages: [973]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.30.2.6.11.8 TaxAmount <TaxAmt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 973 to 973.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 973

```text
7.4.2.40.30.2.6.11.8  TaxAmount <TaxAmt>
Presence: [0..1]
Definition: Set of elements used to provide information on the amount of the tax record.
TaxAmount <TaxAmt> contains the following TaxAmount3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Rate <Rate> [0..1] Rate 973
   TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C9 973
   TotalAmount <TtlAmt> [0..1] Amount C2, C9 973
   Details <Dtls> [0..*]  974
     Period <Prd> [0..1]  974
       Year <Yr> [0..1] Year 974
       Type <Tp> [0..1] CodeSet 975
       FromToDate <FrToDt> [0..1] ± 975
     Amount <Amt> [1..1] Amount C2, C9 976
7.4.2.40.30.2.6.11.8.1  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 1243
7.4.2.40.30.2.6.11.8.2  TaxableBaseAmount <TaxblBaseAmt>
Presence: [0..1]
Definition: Amount of money on which the tax is based.
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
7.4.2.40.30.2.6.11.8.3  TotalAmount <TtlAmt>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
973 March 2026
```

