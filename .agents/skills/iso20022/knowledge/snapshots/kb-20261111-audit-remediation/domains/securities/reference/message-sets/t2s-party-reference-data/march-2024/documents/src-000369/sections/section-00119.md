---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 reda.043.001.02 PartyAuditTrailReportV02", "10.4 Message Building Blocks", "10.4.2 ReportOrError <RptOrErr>", "10.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "10.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "10.4.2.1.1.1 AuditTrail <AudtTrl>", "10.4.2.1.1.1.1 Record <Rcrd>", "10.4.2.1.1.1.1.11 Restriction <Rstrctn>", "10.4.2.1.1.1.1.11.2 New <New>", "10.4.2.1.1.1.1.11.2.3 ValidUntil <VldUntil>"]
file_pages: [153]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 10.4.2.1.1.1.1.11.2.3 ValidUntil <VldUntil>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 153 to 153.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 153

```text
10.4.2.1.1.1.1.11.2.3  ValidUntil <VldUntil>
Presence: [0..1]
Definition: Date until when the restriction is valid.
Datatype: "ISODateTime" on page 185
10.4.2.1.1.1.1.12  Other <Othr>
Presence: [1..*]
Definition: Specifies a proprietary update type.
Other <Othr> contains the following UpdateLogProprietary1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FieldName <FldNm> [1..1] Text 153
   OldFieldValue <OdFldVal> [1..1] Text 153
   NewFieldValue <NewFldVal> [1..1] Text 153
10.4.2.1.1.1.1.12.1  FieldName <FldNm>
Presence: [1..1]
Definition: Name of the field whose value has been changed.
Datatype: "Max35Text" on page 188
10.4.2.1.1.1.1.12.2  OldFieldValue <OdFldVal>
Presence: [1..1]
Definition: Value of the field before the change.
Datatype: "Max350Text" on page 187
10.4.2.1.1.1.1.12.3  NewFieldValue <NewFldVal>
Presence: [1..1]
Definition: Value of the field after the change.
Datatype: "Max350Text" on page 187
10.4.2.1.1.1.2  OperationTimeStamp <OprTmStmp>
Presence: [1..1]
Definition: Timestamp of the change.
Datatype: "ISODateTime" on page 185
10.4.2.1.1.1.3  InstructingUser <InstgUsr>
Presence: [1..1]
Definition: User who instructed the change.
Datatype: "Max256Text" on page 187
10.4.2.1.1.1.4  ApprovingUser <ApprvgUsr>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
153 March 2024
```

