---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["60 reda.043.001.02 PartyAuditTrailReportV02", "60.4 Message Building Blocks", "60.4.2 ReportOrError <RptOrErr>", "60.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "60.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "60.4.2.1.1.1 AuditTrail <AudtTrl>", "60.4.2.1.1.1.1 Record <Rcrd>", "60.4.2.1.1.1.1.11 Restriction <Rstrctn>", "60.4.2.1.1.1.1.11.1 Old <Od>", "60.4.2.1.1.1.1.11.1.1 RestrictionType <RstrctnTp>"]
file_pages: [2328]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 60.4.2.1.1.1.1.11.1.1 RestrictionType <RstrctnTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2328 to 2328.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2328

```text
60.4.2.1.1.1.1.11.1.1  RestrictionType <RstrctnTp>
Presence: [1..1]
Definition: Type of the restriction.
RestrictionType <RstrctnTp> contains one of the following CodeOrProprietary1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] Text 2328
Or}   Proprietary <Prtry> [1..1] ± 2328
60.4.2.1.1.1.1.11.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Element expressed as an ISO 20022 code from an external list.
Datatype: "Max4Text" on page 3329
60.4.2.1.1.1.1.11.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Element expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification13" on page 2968 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2969
   SchemeName <SchmeNm> [0..1] Text 2969
   Issuer <Issr> [1..1] Text 2969
60.4.2.1.1.1.1.11.1.2  ValidFrom <VldFr>
Presence: [1..1]
Definition: Date from when the restriction is valid.
Datatype: "ISODateTime" on page 3320
60.4.2.1.1.1.1.11.1.3  ValidUntil <VldUntil>
Presence: [0..1]
Definition: Date until when the restriction is valid.
Datatype: "ISODateTime" on page 3320
60.4.2.1.1.1.1.11.2  New <New>
Presence: [1..1]
Definition: New value after the update.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2328 August 2026
```

