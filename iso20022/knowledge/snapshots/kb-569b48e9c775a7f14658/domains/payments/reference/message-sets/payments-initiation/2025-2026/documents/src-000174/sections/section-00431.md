---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.17 Regulatory Reporting", "6.1.17.1 RegulatoryReporting10", "6.1.17.1.3 Details <Dtls>", "6.1.17.1.3.4 ReportingCode <RptgCd>"]
file_pages: [582]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.17.1.3.4 ReportingCode <RptgCd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 582 to 582.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 582

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
6.1.17.1.3.4  ReportingCode <RptgCd>
Presence: [0..1]
Definition: Specifies the nature, purpose, and reason for the transaction to be reported for regulatory
and statutory requirements in a coded form.
Datatype: "Max10Text" on page 607
6.1.17.1.3.5  Amount <Amt>
Presence: [0..1]
Definition: Amount of money to be reported for regulatory and statutory requirements.
Impacted by: C2 "ActiveOrHistoricCurrency", C19 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 585
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
6.1.17.1.3.6  Information <Inf>
Presence: [0..*]
Definition: Additional details that cater for specific domestic regulatory requirements.
Datatype: "Max35Text" on page 609
6.1.18 System Identification
6.1.18.1  ClearingSystemIdentification2Choice
Definition: Choice of a clearing system identifier.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 583
Or}   Proprietary <Prtry> [1..1] Text 583
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 582 March 2026
```

