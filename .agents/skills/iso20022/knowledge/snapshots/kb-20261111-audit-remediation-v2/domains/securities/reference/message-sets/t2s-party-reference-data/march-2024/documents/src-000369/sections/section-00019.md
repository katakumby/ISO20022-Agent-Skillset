---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 reda.015.001.01 PartyQueryV01", "3.4 Message Building Blocks", "3.4.2 SearchCriteria <SchCrit>", "3.4.2.2 ClosingDate <ClsgDt>", "3.4.2.2.4 EqualDate <EQDt>"]
file_pages: [25]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 3.4.2.2.4 EqualDate <EQDt>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 25 to 25.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 25

```text
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 158 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 158
   ToDate <ToDt> [1..1] Date 158
3.4.2.2.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 184
3.4.2.2.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 184
3.4.2.3  Type <Tp>
Presence: [0..1]
Definition: Specifies the type classification of the party.
Type <Tp> contains one of the following SystemPartyType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 25
Or}   Proprietary <Prtry> [1..1] Text 25
3.4.2.3.1  Code <Cd>
Presence: [1..1]
Definition: System party type, in a coded format.
Datatype: "ExternalSystemPartyType1Code" on page 182
3.4.2.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: System party type, in a proprietary format.
Datatype: "Max35Text" on page 188
3.4.2.4  ResponsiblePartyIdentification <RspnsblPtyId>
Presence: [0..1]
Definition: Unique identification of the party responsible for the maintenance of the party reference data.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.015.001.01 PartyQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
25 March 2024
```

