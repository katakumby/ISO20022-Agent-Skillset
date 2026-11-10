---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.9 Date Time", "7.1.9.7 SettlementDate19Choice", "7.1.9.7.1 Date <Dt>"]
file_pages: [322]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.9.7.1 Date <Dt>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 322 to 322.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 322

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 322
Or}   DateCode <DtCd> [1..1] ± 322
7.1.9.7.1  Date <Dt>
Presence: [1..1]
Definition: Date in ISO format.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 321 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 321
Or}   DateTime <DtTm> [1..1] DateTime 321
7.1.9.7.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date and time at which the securities are to be delivered or received.
DateCode <DtCd> contains one of the following elements (see "SettlementDateCode8Choice" on
page 318 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 319
Or}   Proprietary <Prtry> [1..1] ± 319
7.1.9.8  Period2
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 322
   ToDate <ToDt> [1..1] Date 322
7.1.9.8.1  FromDate <FrDt>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODate" on page 550
7.1.9.8.2  ToDate <ToDt>
Presence: [1..1]
Definition: Date and time at which the range ends.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 322 March 2026
```

