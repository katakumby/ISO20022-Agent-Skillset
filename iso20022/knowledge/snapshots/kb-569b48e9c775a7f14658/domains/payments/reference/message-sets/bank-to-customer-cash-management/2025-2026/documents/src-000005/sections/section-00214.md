---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.14 Charges <Chrgs>", "3.4.2.15.14.2 Record <Rcrd>"]
file_pages: [335]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.14.2 Record <Rcrd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 335 to 335.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 335

```text
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
3.4.2.15.14.2  Record <Rcrd>
Presence: [0..*]
Definition: Provides details of the individual charges record.
Record <Rcrd> contains the following ChargesRecord8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C6 335
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 336
   ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 336
   Type <Tp> [0..1]  336
{Or     Code <Cd> [1..1] CodeSet 336
Or}     Proprietary <Prtry> [1..1] ± 337
   Rate <Rate> [0..1] Rate 337
   Bearer <Br> [0..1] CodeSet 337
   Agent <Agt> [0..1] ± 337
   Tax <Tax> [0..1]  338
     Identification <Id> [0..1] Text 338
     Rate <Rate> [0..1] Rate 338
     Amount <Amt> [0..1] Amount C2, C6 339
3.4.2.15.14.2.1  Amount <Amt>
Presence: [1..1]
Definition: Transaction charges to be paid by the charge bearer.
Impacted by: C2 "ActiveOrHistoricCurrency", C6 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 886
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
335 March 2026
```

