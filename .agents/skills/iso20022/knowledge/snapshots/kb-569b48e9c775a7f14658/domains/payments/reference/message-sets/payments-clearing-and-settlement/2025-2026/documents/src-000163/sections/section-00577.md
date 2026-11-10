---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.45 Tax <Tax>", "6.4.2.45.11 Record <Rcrd>", "6.4.2.45.11.8 TaxAmount <TaxAmt>", "6.4.2.45.11.8.4 Details <Dtls>"]
file_pages: [782]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.45.11.8.4 Details <Dtls>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 782 to 782.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 782

```text
Definition: Total amount that is the result of the calculation of the tax for the record.
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
6.4.2.45.11.8.4  Details <Dtls>
Presence: [0..*]
Definition: Set of elements used to provide details on the tax period and amount.
Details <Dtls> contains the following TaxRecordDetails3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Period <Prd> [0..1]  782
     Year <Yr> [0..1] Year 782
     Type <Tp> [0..1] CodeSet 783
     FromToDate <FrToDt> [0..1] ± 783
   Amount <Amt> [1..1] Amount C2, C12 784
6.4.2.45.11.8.4.1  Period <Prd>
Presence: [0..1]
Definition: Set of elements used to provide details on the period of time related to the tax payment.
Period <Prd> contains the following TaxPeriod3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Year <Yr> [0..1] Year 782
   Type <Tp> [0..1] CodeSet 783
   FromToDate <FrToDt> [0..1] ± 783
6.4.2.45.11.8.4.1.1  Year <Yr>
Presence: [0..1]
Definition: Year related to the tax payment.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
782 March 2026
```

