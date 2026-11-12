---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 reda.043.001.02 PartyAuditTrailReportV02", "10.4 Message Building Blocks", "10.4.2 ReportOrError <RptOrErr>", "10.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "10.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "10.4.2.1.1.1 AuditTrail <AudtTrl>", "10.4.2.1.1.1.1 Record <Rcrd>", "10.4.2.1.1.1.1.1 Address <Adr>"]
file_pages: [136]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 10.4.2.1.1.1.1.1 Address <Adr>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 136 to 136.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 136

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       RestrictionType <RstrctnTp> [1..1]  152
{Or         Code <Cd> [1..1] Text 152
Or}         Proprietary <Prtry> [1..1] ± 152
       ValidFrom <VldFr> [1..1] DateTime 152
       ValidUntil <VldUntil> [0..1] DateTime 153
Or}   Other <Othr> [1..*]  153
     FieldName <FldNm> [1..1] Text 153
     OldFieldValue <OdFldVal> [1..1] Text 153
     NewFieldValue <NewFldVal> [1..1] Text 153
10.4.2.1.1.1.1.1  Address <Adr>
Presence: [1..1]
Definition: Information that locates and identifies a specific address.
Address <Adr> contains the following UpdateLogAddress2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1] ± 136
   New <New> [1..1] ± 137
10.4.2.1.1.1.1.1.1  Old <Od>
Presence: [1..1]
Definition: Old value before change
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
136 March 2024
```

