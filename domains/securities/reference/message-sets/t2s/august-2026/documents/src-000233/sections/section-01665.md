---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["60 reda.043.001.02 PartyAuditTrailReportV02", "60.4 Message Building Blocks", "60.4.2 ReportOrError <RptOrErr>", "60.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "60.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "60.4.2.1.1.1 AuditTrail <AudtTrl>", "60.4.2.1.1.1.1 Record <Rcrd>", "60.4.2.1.1.1.1.1 Address <Adr>"]
file_pages: [2313]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 60.4.2.1.1.1.1.1 Address <Adr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2313 to 2313.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2313

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       RestrictionType <RstrctnTp> [1..1]  2329
{Or         Code <Cd> [1..1] Text 2329
Or}         Proprietary <Prtry> [1..1] ± 2329
       ValidFrom <VldFr> [1..1] DateTime 2329
       ValidUntil <VldUntil> [0..1] DateTime 2330
Or}   Other <Othr> [1..*]  2330
     FieldName <FldNm> [1..1] Text 2330
     OldFieldValue <OdFldVal> [1..1] Text 2330
     NewFieldValue <NewFldVal> [1..1] Text 2330
60.4.2.1.1.1.1.1  Address <Adr>
Presence: [1..1]
Definition: Information that locates and identifies a specific address.
Address <Adr> contains the following UpdateLogAddress2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1] ± 2313
   New <New> [1..1] ± 2314
60.4.2.1.1.1.1.1.1  Old <Od>
Presence: [1..1]
Definition: Old value before change
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2313 August 2026
```

