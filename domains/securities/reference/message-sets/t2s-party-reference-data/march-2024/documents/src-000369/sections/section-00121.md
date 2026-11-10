---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 reda.043.001.02 PartyAuditTrailReportV02", "10.4 Message Building Blocks", "10.4.2 ReportOrError <RptOrErr>", "10.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "10.4.2.1.2 DatePeriod <DtPrd>", "10.4.2.1.2.1 FromDate <FrDt>"]
file_pages: [155]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 10.4.2.1.2.1 FromDate <FrDt>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 155 to 155.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 155

```text
DatePeriod <DtPrd> contains one of the following DatePeriod3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 155
Or   ToDate <ToDt> [1..1] Date 155
Or   FromToDate <FrToDt> [1..1] ± 155
Or}   Date <Dt> [1..1] Date 155
10.4.2.1.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 184
10.4.2.1.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 184
10.4.2.1.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Range of time between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 158 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 158
   ToDate <ToDt> [1..1] Date 158
10.4.2.1.2.4  Date <Dt>
Presence: [1..1]
Definition: Single date entry
Datatype: "ISODate" on page 184
10.4.2.1.3  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Identifies the party for which the audit trail is provided.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
155 March 2024
```

