---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["41 reda.021.001.01 SecuritiesAccountReportV01", "41.4 Message Building Blocks", "41.4.3 ReportOrError <RptOrErr>", "41.4.3.1 SecuritiesAccountReport <SctiesAcctRpt>", "41.4.3.1.2 SecuritiesAccountOrError <SctiesAcctOrErr>", "41.4.3.1.2.2 BusinessError <BizErr>", "41.4.3.1.2.2.1 Error <Err>", "41.4.3.1.2.2.1.1 Code <Cd>"]
file_pages: [2138]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.021.001.01"]
---

# 41.4.3.1.2.2.1.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2138 to 2138.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2138

```text
41.4.3.1.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 3246
41.4.3.1.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 3328
41.4.3.1.2.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 3326
41.4.3.2  OperationalError <OprlErr>
Presence: [1..*]
Definition: Operational error resulting from a rejection.
OperationalError <OprlErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  2138
{Or     Code <Cd> [1..1] CodeSet 2138
Or}     Proprietary <Prtry> [1..1] Text 2139
   Description <Desc> [0..1] Text 2139
41.4.3.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2138
Or}   Proprietary <Prtry> [1..1] Text 2139
41.4.3.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 3246
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.021.001.01 SecuritiesAccountReportV01
Target2-Securities 2138 August 2026
```

