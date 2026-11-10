---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["60 reda.043.001.02 PartyAuditTrailReportV02", "60.4 Message Building Blocks", "60.4.2 ReportOrError <RptOrErr>", "60.4.2.2 OperationalError <OprlErr>"]
file_pages: [2333]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 60.4.2.2 OperationalError <OprlErr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2333 to 2333.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2333

```text
PartyIdentification <PtyId> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
60.4.2.2  OperationalError <OprlErr>
Presence: [1..*]
Definition: Operational error resulting from a rejection.
OperationalError <OprlErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  2333
{Or     Code <Cd> [1..1] CodeSet 2333
Or}     Proprietary <Prtry> [1..1] Text 2333
   Description <Desc> [0..1] Text 2333
60.4.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2333
Or}   Proprietary <Prtry> [1..1] Text 2333
60.4.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 3246
60.4.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 3328
60.4.2.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2333 August 2026
```

