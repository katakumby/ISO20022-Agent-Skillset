---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["60 reda.043.001.02 PartyAuditTrailReportV02", "60.4 Message Building Blocks", "60.4.2 ReportOrError <RptOrErr>", "60.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "60.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "60.4.2.1.1.1 AuditTrail <AudtTrl>", "60.4.2.1.1.1.1 Record <Rcrd>", "60.4.2.1.1.1.1.11 Restriction <Rstrctn>", "60.4.2.1.1.1.1.11.2 New <New>", "60.4.2.1.1.1.1.11.2.3 ValidUntil <VldUntil>"]
file_pages: [2330]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 60.4.2.1.1.1.1.11.2.3 ValidUntil <VldUntil>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2330 to 2330.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2330

```text
60.4.2.1.1.1.1.11.2.3  ValidUntil <VldUntil>
Presence: [0..1]
Definition: Date until when the restriction is valid.
Datatype: "ISODateTime" on page 3320
60.4.2.1.1.1.1.12  Other <Othr>
Presence: [1..*]
Definition: Specifies a proprietary update type.
Other <Othr> contains the following UpdateLogProprietary1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FieldName <FldNm> [1..1] Text 2330
   OldFieldValue <OdFldVal> [1..1] Text 2330
   NewFieldValue <NewFldVal> [1..1] Text 2330
60.4.2.1.1.1.1.12.1  FieldName <FldNm>
Presence: [1..1]
Definition: Name of the field whose value has been changed.
Datatype: "Max35Text" on page 3328
60.4.2.1.1.1.1.12.2  OldFieldValue <OdFldVal>
Presence: [1..1]
Definition: Value of the field before the change.
Datatype: "Max350Text" on page 3328
60.4.2.1.1.1.1.12.3  NewFieldValue <NewFldVal>
Presence: [1..1]
Definition: Value of the field after the change.
Datatype: "Max350Text" on page 3328
60.4.2.1.1.1.2  OperationTimeStamp <OprTmStmp>
Presence: [1..1]
Definition: Timestamp of the change.
Datatype: "ISODateTime" on page 3320
60.4.2.1.1.1.3  InstructingUser <InstgUsr>
Presence: [1..1]
Definition: User who instructed the change.
Datatype: "Max256Text" on page 3327
60.4.2.1.1.1.4  ApprovingUser <ApprvgUsr>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2330 August 2026
```

