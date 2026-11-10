---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.11 Frequency", "9.1.11.1 Frequency22Choice", "9.1.11.1.2 Proprietary <Prtry>"]
file_pages: [223]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.11.1.2 Proprietary <Prtry>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 223 to 223.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 223

```text
9.1.11.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Frequency expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.11.2  Frequency23Choice
Definition: Choice of format for a frequency, for example, a payment frequency.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 223
Or}   Proprietary <Prtry> [1..1] ± 223
9.1.11.2.1  Code <Cd>
Presence: [1..1]
Definition: Frequency expressed as an ISO 20022 code.
Datatype: "EventFrequency3Code" on page 325
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
MNTH Monthly Event takes place every month or once a
month.
QUTR Quarterly Event takes place every three months or
four times a year.
SEMI SemiAnnual Event takes place every six months or
two times a year.
WEEK Weekly Event takes place once a week.
9.1.11.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Frequency expressed as a proprietary code.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 223 September 2025
```

