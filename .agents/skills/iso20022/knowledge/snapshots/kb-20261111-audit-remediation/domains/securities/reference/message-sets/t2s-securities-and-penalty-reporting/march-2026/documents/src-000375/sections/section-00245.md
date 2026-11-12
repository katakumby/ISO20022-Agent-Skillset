---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.9 Date Time", "7.1.9.5 SettlementDateCode7Choice", "7.1.9.5.1 Code <Cd>"]
file_pages: [321]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.9.5.1 Code <Cd>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 321 to 321.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 321

```text
7.1.9.5.1  Code <Cd>
Presence: [1..1]
Definition: Settlement date expressed as an ISO 20022 code.
Datatype: "SettlementDate4Code" on page 538
CodeName Name Definition
WISS WhenIssued Settlement is to be done when the
security is issued.
7.1.9.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement date expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.9.6  DateAndDateTime2Choice
Definition: Choice between a date or a date and time format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 321
Or}   DateTime <DtTm> [1..1] DateTime 321
7.1.9.6.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Datatype: "ISODate" on page 550
7.1.9.6.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
Datatype: "ISODateTime" on page 551
7.1.9.7  SettlementDate19Choice
Definition: Choice of format for the settlement date.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 321 March 2026
```

