---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.8 TransactionInterest4"]
file_pages: [852]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.8 TransactionInterest4

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 852 to 852.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 852

```text
6.1.15.8  TransactionInterest4
Definition: Provide further details on transaction specific interest information that applies to the
underlying transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalInterestAndTaxAmount <TtlIntrstAndTaxAmt> [0..1] Amount C1, C5 852
   Record <Rcrd> [0..*]  853
     Amount <Amt> [1..1] Amount C1, C5 853
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 854
     Type <Tp> [0..1]  854
{Or       Code <Cd> [1..1] CodeSet 854
Or}       Proprietary <Prtry> [1..1] Text 854
     Rate <Rate> [0..1]  854
       Type <Tp> [1..1] ± 855
       ValidityRange <VldtyRg> [0..1] ± 855
     FromToDate <FrToDt> [0..1] ± 855
     Reason <Rsn> [0..1] Text 855
     Tax <Tax> [0..1]  856
       Identification <Id> [0..1] Text 856
       Rate <Rate> [0..1] Rate 856
       Amount <Amt> [0..1] Amount C1, C5 856
6.1.15.8.1  TotalInterestAndTaxAmount <TtlIntrstAndTaxAmt>
Presence: [0..1]
Definition: Total amount of interests and taxes included in the entry amount.
Impacted by: C1 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
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
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
852 March 2026
```

