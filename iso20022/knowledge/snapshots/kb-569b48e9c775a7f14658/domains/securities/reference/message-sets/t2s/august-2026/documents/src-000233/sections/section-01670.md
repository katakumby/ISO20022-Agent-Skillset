---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["60 reda.043.001.02 PartyAuditTrailReportV02", "60.4 Message Building Blocks", "60.4.2 ReportOrError <RptOrErr>", "60.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "60.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "60.4.2.1.1.1 AuditTrail <AudtTrl>", "60.4.2.1.1.1.1 Record <Rcrd>", "60.4.2.1.1.1.1.4 ClosingDate <ClsgDt>"]
file_pages: [2318]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 60.4.2.1.1.1.1.4 ClosingDate <ClsgDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2318 to 2318.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2318

```text
Definition: New value after the update.
Datatype: "ISODate" on page 3319
60.4.2.1.1.1.1.4  ClosingDate <ClsgDt>
Presence: [1..1]
Definition: Specifies the closing date of the party.
ClosingDate <ClsgDt> contains the following UpdateLogDate1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1] Date 2318
   New <New> [1..1] Date 2318
60.4.2.1.1.1.1.4.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Datatype: "ISODate" on page 3319
60.4.2.1.1.1.1.4.2  New <New>
Presence: [1..1]
Definition: New value after the update.
Datatype: "ISODate" on page 3319
60.4.2.1.1.1.1.5  Type <Tp>
Presence: [1..1]
Definition: Specifies the type classification of the party.
Type <Tp> contains the following UpdateLogSystemPartyType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1]  2318
{Or     Code <Cd> [1..1] CodeSet 2319
Or}     Proprietary <Prtry> [1..1] Text 2319
   New <New> [1..1]  2319
{Or     Code <Cd> [1..1] CodeSet 2319
Or}     Proprietary <Prtry> [1..1] Text 2319
60.4.2.1.1.1.1.5.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2318 August 2026
```

