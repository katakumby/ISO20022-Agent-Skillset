---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.5 Balance", "6.1.5.1 CreditLine3", "6.1.5.1.2 Type <Tp>"]
file_pages: [816]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.5.1.2 Type <Tp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 816 to 816.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 816

```text
• Meaning When True: True
• Meaning When False: False
6.1.5.1.2  Type <Tp>
Presence: [0..1]
Definition: Type of the credit line provided when multiple credit lines may be provided.
Type <Tp> contains one of the following CreditLineType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 816
Or}   Proprietary <Prtry> [1..1] Text 816
6.1.5.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Type of the credit line, as published in an external purpose code list.
Datatype: "ExternalCreditLineType1Code" on page 895
6.1.5.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of the credit line, in a proprietary form.
Datatype: "Max35Text" on page 916
6.1.5.1.3  Amount <Amt>
Presence: [0..1]
Definition: Amount of money of the credit line.
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
6.1.5.1.4  Date <Dt>
Presence: [0..1]
Definition: Date of the credit line provided when multiple credit lines may be provided.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
816 March 2026
```

