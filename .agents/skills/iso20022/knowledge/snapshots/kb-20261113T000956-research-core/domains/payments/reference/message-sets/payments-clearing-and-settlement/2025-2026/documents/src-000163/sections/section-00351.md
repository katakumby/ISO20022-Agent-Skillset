---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.23 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "4.4.3.27.23.29 Tax <Tax>", "4.4.3.27.23.29.11 Record <Rcrd>", "4.4.3.27.23.29.11.8 TaxAmount <TaxAmt>", "4.4.3.27.23.29.11.8.4 Details <Dtls>"]
file_pages: [486]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.23.29.11.8.4 Details <Dtls>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 486 to 486.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 486

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
4.4.3.27.23.29.11.8.4  Details <Dtls>
Presence: [0..*]
Definition: Set of elements used to provide details on the tax period and amount.
Details <Dtls> contains the following TaxRecordDetails3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Period <Prd> [0..1]  486
     Year <Yr> [0..1] Year 486
     Type <Tp> [0..1] CodeSet 487
     FromToDate <FrToDt> [0..1] ± 487
   Amount <Amt> [1..1] Amount C2, C12 488
4.4.3.27.23.29.11.8.4.1  Period <Prd>
Presence: [0..1]
Definition: Set of elements used to provide details on the period of time related to the tax payment.
Period <Prd> contains the following TaxPeriod3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Year <Yr> [0..1] Year 486
   Type <Tp> [0..1] CodeSet 487
   FromToDate <FrToDt> [0..1] ± 487
4.4.3.27.23.29.11.8.4.1.1  Year <Yr>
Presence: [0..1]
Definition: Year related to the tax payment.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
486 March 2026
```

