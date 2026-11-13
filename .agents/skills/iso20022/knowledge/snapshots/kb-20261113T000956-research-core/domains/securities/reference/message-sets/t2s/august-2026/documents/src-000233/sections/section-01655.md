---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["59 reda.042.001.01 PartyAuditTrailQueryV01", "59.4 Message Building Blocks", "59.4.2 SearchCriteria <SchCrit>", "59.4.2.1 PartyIdentification <PtyId>"]
file_pages: [2290]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.042.001.01"]
---

# 59.4.2.1 PartyIdentification <PtyId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2290 to 2290.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2290

```text
SearchCriteria <SchCrit> contains the following PartyAuditTrailSearchCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [0..1] ± 2290
   DatePeriod <DtPrd> [0..1]  2290
{Or     FromDate <FrDt> [1..1] Date 2290
Or     ToDate <ToDt> [1..1] Date 2291
Or     FromToDate <FrToDt> [1..1] ± 2291
Or     EqualDate <EQDt> [1..1] Date 2291
Or}     NotEqualDate <NEQDt> [1..1] Date 2291
59.4.2.1  PartyIdentification <PtyId>
Presence: [0..1]
Definition: Describes party to be queried.
PartyIdentification <PtyId> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
59.4.2.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Describes date period for querying information.
DatePeriod <DtPrd> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 2290
Or   ToDate <ToDt> [1..1] Date 2291
Or   FromToDate <FrToDt> [1..1] ± 2291
Or   EqualDate <EQDt> [1..1] Date 2291
Or}   NotEqualDate <NEQDt> [1..1] Date 2291
59.4.2.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 3319
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.042.001.01 PartyAuditTrailQueryV01
Target2-Securities 2290 August 2026
```

