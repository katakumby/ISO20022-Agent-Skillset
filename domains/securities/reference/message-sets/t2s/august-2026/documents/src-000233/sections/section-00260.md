---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.2 CancellationReport <CxlRpt>", "15.4.2.2.6 CancellationReason <CxlRsn>", "15.4.2.2.6.1 Code <Cd>"]
file_pages: [339]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.2.6.1 Code <Cd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 339 to 339.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 339

```text
CancellationReason <CxlRsn> contains one of the following CancellationReason16Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] Text 339
Or}   Proprietary <Prtry> [1..1] Text 339
15.4.2.2.6.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the cancellation request, in a coded form.
Datatype: "Max4AlphaNumericText" on page 3328
15.4.2.2.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the cancellation request, in a proprietary form.
Datatype: "Max35Text" on page 3328
15.4.2.3  OperationalError <OprlErr>
Presence: [1..*]
Definition: Indicates that an operational error has been issued during the processing of the related
request.
OperationalError <OprlErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  339
{Or     Code <Cd> [1..1] CodeSet 339
Or}     Proprietary <Prtry> [1..1] Text 340
   Description <Desc> [0..1] Text 340
15.4.2.3.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 339
Or}   Proprietary <Prtry> [1..1] Text 340
15.4.2.3.1.1  Code <Cd>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 339 August 2026
```

