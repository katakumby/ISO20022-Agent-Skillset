---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.2 BusinessError <BizErr>", "32.4.3.1.2.2 BusinessError <BizErr>", "32.4.3.1.2.2.1 Error <Err>"]
file_pages: [2036]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.2.2.1 Error <Err>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2036 to 2036.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2036

```text
BusinessError <BizErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  2036
{Or     Code <Cd> [1..1] CodeSet 2036
Or}     Proprietary <Prtry> [1..1] Text 2036
   Description <Desc> [0..1] Text 2036
32.4.3.1.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2036
Or}   Proprietary <Prtry> [1..1] Text 2036
32.4.3.1.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 3246
32.4.3.1.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 3328
32.4.3.1.2.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 3326
32.4.3.2  OperationalError <OprlErr>
Presence: [1..*]
Definition: Provides the operational error details.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 2036 August 2026
```

