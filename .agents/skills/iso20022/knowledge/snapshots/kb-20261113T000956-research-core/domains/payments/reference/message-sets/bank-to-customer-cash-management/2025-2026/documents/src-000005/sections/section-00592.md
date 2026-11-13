---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.8 Cash Entry", "6.1.8.1 CashAvailability1", "6.1.8.1.1 Date <Dt>", "6.1.8.1.1.1 NumberOfDays <NbOfDays>"]
file_pages: [825]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.8.1.1.1 NumberOfDays <NbOfDays>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 825 to 825.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 825

```text
Date <Dt> contains one of the following CashAvailabilityDate1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NumberOfDays <NbOfDays> [1..1] Text 825
Or}   ActualDate <ActlDt> [1..1] Date 825
6.1.8.1.1.1  NumberOfDays <NbOfDays>
Presence: [1..1]
Definition: Indicates the number of float days attached to the balance.
Datatype: "Max15PlusSignedNumericText" on page 915
6.1.8.1.1.2  ActualDate <ActlDt>
Presence: [1..1]
Definition: Identifies the actual availability date.
Datatype: "ISODate" on page 908
6.1.8.1.2  Amount <Amt>
Presence: [1..1]
Definition: Identifies the available amount.
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
6.1.8.1.3  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether the availability balance is a credit or a debit balance.
Usage: A zero balance is considered to be a credit balance.
Datatype: "CreditDebitCode" on page 892
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
825 March 2026
```

