---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["60 reda.043.001.02 PartyAuditTrailReportV02", "60.4 Message Building Blocks", "60.4.2 ReportOrError <RptOrErr>", "60.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "60.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "60.4.2.1.1.2 BusinessError <BizErr>"]
file_pages: [2331]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 60.4.2.1.1.2 BusinessError <BizErr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2331 to 2331.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2331

```text
Definition: User who approved the change instructed by the instructing user.
Datatype: "Max256Text" on page 3327
60.4.2.1.1.2  BusinessError <BizErr>
Presence: [1..*]
Definition: Business error resulting from a rejection.
BusinessError <BizErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  2331
{Or     Code <Cd> [1..1] CodeSet 2331
Or}     Proprietary <Prtry> [1..1] Text 2331
   Description <Desc> [0..1] Text 2331
60.4.2.1.1.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2331
Or}   Proprietary <Prtry> [1..1] Text 2331
60.4.2.1.1.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 3246
60.4.2.1.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 3328
60.4.2.1.1.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 3326
60.4.2.1.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Period in dates for which the audit trail is provided.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2331 August 2026
```

