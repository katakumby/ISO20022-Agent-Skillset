---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.14 Miscellaneous", "9.1.14.9 RegistrationReason5", "9.1.14.9.2 AdditionalInformation <AddtlInf>"]
file_pages: [240]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.14.9.2 AdditionalInformation <AddtlInf>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 240 to 240.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 240

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.14.9.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 344
9.1.14.10  OptionStyle8Choice
Definition: Choice of format for the option style.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 240
Or}   Proprietary <Prtry> [1..1] ± 240
9.1.14.10.1  Code <Cd>
Presence: [1..1]
Definition: Option style expressed as an ISO 20022 code.
Datatype: "OptionStyle2Code" on page 331
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
EURO European Option that can be exercised on expiry
date only.
9.1.14.10.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Option style expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 240 September 2025
```

