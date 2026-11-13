---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.3 Pagination1", "6.1.15.3.2 LastPageIndicator <LastPgInd>"]
file_pages: [845]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.3.2 LastPageIndicator <LastPgInd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 845 to 845.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 845

```text
Definition: Page number.
Datatype: "Max5NumericText" on page 917
6.1.15.3.2  LastPageIndicator <LastPgInd>
Presence: [1..1]
Definition: Indicates the last page.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 911):
• Meaning When True: Yes
• Meaning When False: No
6.1.15.4  ReportingSource1Choice
Definition: Specifies the source used to generate the reporting.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 845
Or}   Proprietary <Prtry> [1..1] Text 845
6.1.15.4.1  Code <Cd>
Presence: [1..1]
Definition: Reporting source, as published in an external reporting source code list.
Datatype: "ExternalReportingSource1Code" on page 899
6.1.15.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reporting source, in a proprietary form.
Datatype: "Max35Text" on page 916
6.1.15.5  TotalTransactions6
Definition: Set of elements used to provide summary information on entries.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
845 March 2026
```

