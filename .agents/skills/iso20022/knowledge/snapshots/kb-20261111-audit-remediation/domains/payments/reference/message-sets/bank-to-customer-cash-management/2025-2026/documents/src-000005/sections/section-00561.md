---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 camt.060.001.07 AccountReportingRequestV07", "5.4 Message Building Blocks", "5.4.2 ReportingRequest <RptgReq>", "5.4.2.8 RequestedTransactionType <ReqdTxTp>", "5.4.2.8.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [794]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.060.001.07"]
---

# 5.4.2.8.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 794 to 794.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 794

```text
5.4.2.8.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether the reporting request refers to credit or debit entries.
Datatype: "CreditDebitCode" on page 892
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
5.4.2.8.3  FloorLimit <FlrLmt>
Presence: [0..*]
Definition: Specifies the minimum value of entries to be reported in the requested message.
FloorLimit <FlrLmt> contains the following Limit2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 794
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 794
5.4.2.8.3.1  Amount <Amt>
Presence: [1..1]
Definition: Minimum transaction amount to be reported in the requested message.
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
5.4.2.8.3.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether the floor limit applies to credit, to debit or to both credit and debit entries.
Datatype: "FloorLimitType1Code" on page 901
CodeName Name Definition
CRED Credit Floor limit applies to credit entries.
Approved by the Payments SEG on 12 January 2026 camt.060.001.07 AccountReportingRequestV07
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
794 March 2026
```

