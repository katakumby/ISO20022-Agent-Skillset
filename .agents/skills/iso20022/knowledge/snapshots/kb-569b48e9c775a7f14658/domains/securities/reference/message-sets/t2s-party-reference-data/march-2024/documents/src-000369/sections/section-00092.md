---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["9 reda.042.001.01 PartyAuditTrailQueryV01", "9.4 Message Building Blocks", "9.4.2 SearchCriteria <SchCrit>", "9.4.2.1 PartyIdentification <PtyId>"]
file_pages: [113]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.042.001.01"]
---

# 9.4.2.1 PartyIdentification <PtyId>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 113 to 113.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 113

```text
SearchCriteria <SchCrit> contains the following PartyAuditTrailSearchCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [0..1] ± 113
   DatePeriod <DtPrd> [0..1]  113
{Or     FromDate <FrDt> [1..1] Date 113
Or     ToDate <ToDt> [1..1] Date 114
Or     FromToDate <FrToDt> [1..1] ± 114
Or     EqualDate <EQDt> [1..1] Date 114
Or}     NotEqualDate <NEQDt> [1..1] Date 114
9.4.2.1  PartyIdentification <PtyId>
Presence: [0..1]
Definition: Describes party to be queried.
PartyIdentification <PtyId> contains the following elements (see "SystemPartyIdentification8" on
page 170 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 170
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 170
9.4.2.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Describes date period for querying information.
DatePeriod <DtPrd> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 113
Or   ToDate <ToDt> [1..1] Date 114
Or   FromToDate <FrToDt> [1..1] ± 114
Or   EqualDate <EQDt> [1..1] Date 114
Or}   NotEqualDate <NEQDt> [1..1] Date 114
9.4.2.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 184
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.042.001.01 PartyAuditTrailQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
113 March 2024
```

