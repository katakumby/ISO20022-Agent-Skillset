---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.6 Date Time", "9.1.6.1 TradeDate8Choice", "9.1.6.1.1 Date <Dt>"]
file_pages: [202]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.6.1.1 Date <Dt>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 202 to 202.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 202

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 202
Or}   DateCode <DtCd> [1..1]  202
{Or     Code <Cd> [1..1] CodeSet 202
Or}     Proprietary <Prtry> [1..1] ± 202
9.1.6.1.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as an ISO date.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 204 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 204
Or}   DateTime <DtTm> [1..1] DateTime 204
9.1.6.1.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date expressed as a code.
DateCode <DtCd> contains one of the following TradeDateCode3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 202
Or}   Proprietary <Prtry> [1..1] ± 202
9.1.6.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Trade date expressed as an ISO 20022 code.
Datatype: "DateType3Code" on page 324
CodeName Name Definition
VARI Various Partial trades have occurred over a
period of two or more days.
9.1.6.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade date expressed as a proprietary code.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 202 September 2025
```

