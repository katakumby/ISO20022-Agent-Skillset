---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.21 TransferUnmatchedStatus4Choice", "66.1.45.21.4 DataSourceScheme <DataSrcSchme>"]
file_pages: [5198]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.21.4 DataSourceScheme <DataSrcSchme>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5198 to 5198.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5198

```text
66.1.45.21.4  DataSourceScheme <DataSrcSchme>
Presence: [1..1]
Definition: Proprietary identification of the reason for the unmatched status.
DataSourceScheme <DataSrcSchme> contains the following elements (see "GenericIdentification1"
on page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.45.22  InRepairStatusReason4Choice
Definition: Choice of formats for the reason for an in repair status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5198
Or}   ReasonDetails <RsnDtls> [1..5]  5198
     Reason <Rsn> [1..1]  5199
{Or       Code <Cd> [1..1] CodeSet 5199
Or}       Proprietary <Prtry> [1..1] ± 5199
     AdditionalInformation <AddtlInf> [0..1] Text 5199
66.1.45.22.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: No reason available or to report for the in repair status.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.45.22.2  ReasonDetails <RsnDtls>
Presence: [1..5]
Definition: Reason for the in repair status, expressed as a code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5198 May 2026
```

