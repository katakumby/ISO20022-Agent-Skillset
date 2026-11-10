---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 reda.043.001.02 PartyAuditTrailReportV02", "10.4 Message Building Blocks", "10.4.2 ReportOrError <RptOrErr>", "10.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "10.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "10.4.2.1.1.1 AuditTrail <AudtTrl>", "10.4.2.1.1.1.1 Record <Rcrd>", "10.4.2.1.1.1.1.4 ClosingDate <ClsgDt>"]
file_pages: [141]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 10.4.2.1.1.1.1.4 ClosingDate <ClsgDt>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 141 to 141.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 141

```text
Definition: New value after the update.
Datatype: "ISODate" on page 184
10.4.2.1.1.1.1.4  ClosingDate <ClsgDt>
Presence: [1..1]
Definition: Specifies the closing date of the party.
ClosingDate <ClsgDt> contains the following UpdateLogDate1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1] Date 141
   New <New> [1..1] Date 141
10.4.2.1.1.1.1.4.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Datatype: "ISODate" on page 184
10.4.2.1.1.1.1.4.2  New <New>
Presence: [1..1]
Definition: New value after the update.
Datatype: "ISODate" on page 184
10.4.2.1.1.1.1.5  Type <Tp>
Presence: [1..1]
Definition: Specifies the type classification of the party.
Type <Tp> contains the following UpdateLogSystemPartyType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1]  141
{Or     Code <Cd> [1..1] CodeSet 142
Or}     Proprietary <Prtry> [1..1] Text 142
   New <New> [1..1]  142
{Or     Code <Cd> [1..1] CodeSet 142
Or}     Proprietary <Prtry> [1..1] Text 142
10.4.2.1.1.1.1.5.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
141 March 2024
```

