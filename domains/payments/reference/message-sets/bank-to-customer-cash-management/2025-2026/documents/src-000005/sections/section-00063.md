---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.7 Charges <Chrgs>", "2.4.2.15.18.2.7.2 Record <Rcrd>", "2.4.2.15.18.2.7.2.1 Amount <Amt>"]
file_pages: [128]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.7.2.1 Amount <Amt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 128 to 128.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 128

```text
Record <Rcrd> contains the following ChargesRecord8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C6 128
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 128
   ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 129
   Type <Tp> [0..1]  129
{Or     Code <Cd> [1..1] CodeSet 129
Or}     Proprietary <Prtry> [1..1] ± 129
   Rate <Rate> [0..1] Rate 129
   Bearer <Br> [0..1] CodeSet 130
   Agent <Agt> [0..1] ± 130
   Tax <Tax> [0..1]  131
     Identification <Id> [0..1] Text 131
     Rate <Rate> [0..1] Rate 131
     Amount <Amt> [0..1] Amount C2, C6 131
2.4.2.15.18.2.7.2.1  Amount <Amt>
Presence: [1..1]
Definition: Transaction charges to be paid by the charge bearer.
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
2.4.2.15.18.2.7.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the charges amount is a credit or a debit amount.
Usage: A zero amount is considered to be a credit.
Datatype: "CreditDebitCode" on page 892
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
128 March 2026
```

