---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.14 Charges <Chrgs>", "4.4.2.14.14.2 Record <Rcrd>"]
file_pages: [593]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.14.2 Record <Rcrd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 593 to 593.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 593

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
4.4.2.14.14.2  Record <Rcrd>
Presence: [0..*]
Definition: Provides details of the individual charges record.
Record <Rcrd> contains the following ChargesRecord8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C6 593
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 594
   ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 594
   Type <Tp> [0..1]  594
{Or     Code <Cd> [1..1] CodeSet 594
Or}     Proprietary <Prtry> [1..1] ± 595
   Rate <Rate> [0..1] Rate 595
   Bearer <Br> [0..1] CodeSet 595
   Agent <Agt> [0..1] ± 595
   Tax <Tax> [0..1]  596
     Identification <Id> [0..1] Text 596
     Rate <Rate> [0..1] Rate 596
     Amount <Amt> [0..1] Amount C2, C6 597
4.4.2.14.14.2.1  Amount <Amt>
Presence: [1..1]
Definition: Transaction charges to be paid by the charge bearer.
Impacted by: C2 "ActiveOrHistoricCurrency", C6 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 886
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
593 March 2026
```

