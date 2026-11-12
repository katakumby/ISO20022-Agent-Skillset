---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.9 Date Time", "7.1.9.1 TradeDate8Choice", "7.1.9.1.1 Date <Dt>"]
file_pages: [318]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.9.1.1 Date <Dt>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 318 to 318.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 318

```text
7.1.9.1.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as an ISO date.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 321 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 321
Or}   DateTime <DtTm> [1..1] DateTime 321
7.1.9.1.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date expressed as a code.
DateCode <DtCd> contains one of the following TradeDateCode3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 318
Or}   Proprietary <Prtry> [1..1] ± 318
7.1.9.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Trade date expressed as an ISO 20022 code.
Datatype: "DateType3Code" on page 501
CodeName Name Definition
VARI Various Partial trades have occurred over a
period of two or more days.
7.1.9.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade date expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.9.2  SettlementDateCode8Choice
Definition: Choice of format for the settlement date code.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 318 March 2026
```

