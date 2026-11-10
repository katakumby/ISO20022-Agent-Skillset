---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.20 ConsentTypeFormat4Choice", "16.1.15.20.2 Proprietary <Prtry>"]
file_pages: [920]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.20.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 920 to 920.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 920

```text
16.1.15.20.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the consent type.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.21  FractionDispositionType25Choice
Definition: Choice between a standard code or a proprietary code to specify the type of fraction
disposition.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 920
Or}   Proprietary <Prtry> [1..1] ± 920
16.1.15.21.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify how fractions resulting from derived securities will be processed or
how prorated decisions will be rounding, if provided with a pro ration rate.
Datatype: "FractionDispositionType9Code" on page 1212
CodeName Name Definition
DIST IssueFraction Take distribution of fractions in the form
of securities.
RDDN RoundDown Round the entitlement down to the last
full unit/minimum nominal quantity,
fractions are discarded.
STAN RoundToNearest If the fraction is greater than or equal to
0.5 of the resulting security then round
up, else round down as specified in the
respective RDUP and RDDN codes.
RDUP RoundUp Round up to the next full unit/minimum
nominal quantity at no cost.
UKWN Unknown Characteristics of the disposition of
fractions are unknown.
16.1.15.21.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of fraction disposition.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 920 February 2026
```

