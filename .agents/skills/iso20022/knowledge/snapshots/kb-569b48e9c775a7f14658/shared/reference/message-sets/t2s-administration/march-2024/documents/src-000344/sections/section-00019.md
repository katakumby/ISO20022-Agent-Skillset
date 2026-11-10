---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.2 SearchCriteria <SchCrit>", "2.4.2.2.6 ResponsiblePartyIdentification <RspnsblPtyId>"]
file_pages: [23]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.2.6 ResponsiblePartyIdentification <RspnsblPtyId>

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 23 to 23.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 23

```text
2.4.2.2.6  ResponsiblePartyIdentification <RspnsblPtyId>
Presence: [0..1]
Definition: Responsible Party of the report owning party.
ResponsiblePartyIdentification <RspnsblPtyId> contains the following elements (see
"PartyIdentification136" on page 54 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 54
   LEI <LEI> [0..1] IdentifierSet 54
2.4.2.2.7  DateSearch <DtSch>
Presence: [0..1]
Definition: Date and time when the report was created.
DateSearch <DtSch> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 23
Or   ToDate <ToDt> [1..1] Date 23
Or   FromToDate <FrToDt> [1..1] ± 23
Or   EqualDate <EQDt> [1..1] Date 24
Or}   NotEqualDate <NEQDt> [1..1] Date 24
2.4.2.2.7.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 66
2.4.2.2.7.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 66
2.4.2.2.7.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.005.001.02 ReportQueryRequestV02
Target2-Securities - Administration - Maintenance 2023 -
2024
23 March 2024
```

