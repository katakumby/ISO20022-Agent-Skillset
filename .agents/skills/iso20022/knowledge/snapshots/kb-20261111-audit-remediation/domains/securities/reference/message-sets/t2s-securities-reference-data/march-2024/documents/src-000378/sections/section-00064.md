---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["7 reda.012.001.01 SecurityReportV01", "7.4 Message Building Blocks", "7.4.3 SecurityReportOrError <SctyRptOrErr>", "7.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "7.4.3.1.2 BusinessError <BizErr>", "7.4.3.1.2.2 BusinessError <BizErr>", "7.4.3.1.2.2.1 Error <Err>", "7.4.3.1.2.2.1.2 Proprietary <Prtry>"]
file_pages: [113]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 7.4.3.1.2.2.1.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 113 to 113.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 113

```text
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 514
7.4.3.1.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 534
7.4.3.1.2.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 533
7.4.3.2  OperationalError <OprlErr>
Presence: [1..*]
Definition: Provides the operational error details.
OperationalError <OprlErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  113
{Or     Code <Cd> [1..1] CodeSet 113
Or}     Proprietary <Prtry> [1..1] Text 113
   Description <Desc> [0..1] Text 114
7.4.3.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 113
Or}   Proprietary <Prtry> [1..1] Text 113
7.4.3.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 514
7.4.3.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 113 March 2024
```

