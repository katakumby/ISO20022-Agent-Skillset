---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.6 Date Time", "9.1.6.3 SettlementDateCode7Choice", "9.1.6.3.1 Code <Cd>"]
file_pages: [204]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.6.3.1 Code <Cd>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 204 to 204.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 204

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 204
Or}   Proprietary <Prtry> [1..1] ± 204
9.1.6.3.1  Code <Cd>
Presence: [1..1]
Definition: Settlement date expressed as an ISO 20022 code.
Datatype: "SettlementDate4Code" on page 339
CodeName Name Definition
WISS WhenIssued Settlement is to be done when the
security is issued.
9.1.6.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement date expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.6.4  DateAndDateTime2Choice
Definition: Choice between a date or a date and time format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 204
Or}   DateTime <DtTm> [1..1] DateTime 204
9.1.6.4.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Datatype: "ISODate" on page 340
9.1.6.4.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
Datatype: "ISODateTime" on page 340
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 204 September 2025
```

