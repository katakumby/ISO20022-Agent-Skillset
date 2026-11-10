---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.7 Charges <Chrgs>", "2.4.2.15.18.2.7.1 TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt>"]
file_pages: [127]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.7.1 TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 127 to 127.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 127

```text
Charges <Chrgs> contains the following Charges15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt> [0..1] Amount C2, C6 127
   Record <Rcrd> [0..*]  127
     Amount <Amt> [1..1] Amount C2, C6 128
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 128
     ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 129
     Type <Tp> [0..1]  129
{Or       Code <Cd> [1..1] CodeSet 129
Or}       Proprietary <Prtry> [1..1] ± 129
     Rate <Rate> [0..1] Rate 129
     Bearer <Br> [0..1] CodeSet 130
     Agent <Agt> [0..1] ± 130
     Tax <Tax> [0..1]  131
       Identification <Id> [0..1] Text 131
       Rate <Rate> [0..1] Rate 131
       Amount <Amt> [0..1] Amount C2, C6 131
2.4.2.15.18.2.7.1  TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt>
Presence: [0..1]
Definition: Total of all charges and taxes applied to the entry.
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
2.4.2.15.18.2.7.2  Record <Rcrd>
Presence: [0..*]
Definition: Provides details of the individual charges record.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
127 March 2026
```

