---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 reda.015.001.01 PartyQueryV01", "3.4 Message Building Blocks", "3.4.2 SearchCriteria <SchCrit>", "3.4.2.1 OpeningDate <OpngDt>"]
file_pages: [23]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 3.4.2.1 OpeningDate <OpngDt>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 23 to 23.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 23

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ResidenceType <ResTp> [0..1] CodeSet 29
   LockStatus <LckSts> [0..1]  29
     ValidFrom <VldFr> [0..1] Date 30
     Status <Sts> [1..1] CodeSet 30
     LockReason <LckRsn> [0..*] Text 30
3.4.2.1  OpeningDate <OpngDt>
Presence: [0..1]
Definition: Specifies the opening date of the party.
OpeningDate <OpngDt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 23
Or   ToDate <ToDt> [1..1] Date 23
Or   FromToDate <FrToDt> [1..1] ± 23
Or   EqualDate <EQDt> [1..1] Date 24
Or}   NotEqualDate <NEQDt> [1..1] Date 24
3.4.2.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 184
3.4.2.1.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 184
3.4.2.1.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 158 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 158
   ToDate <ToDt> [1..1] Date 158
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.015.001.01 PartyQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
23 March 2024
```

