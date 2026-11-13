---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.9 FractionDispositionType26Choice", "16.1.15.9.2 Proprietary <Prtry>"]
file_pages: [900]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.9.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 900 to 900.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 900

```text
Definition: Standard code to specify how fractions resulting from derived securities will be processed or
how prorated decisions will be rounding, if provided with a pro ration rate.
Datatype: "FractionDispositionType8Code" on page 1211
CodeName Name Definition
BUYU BuyUp Buy securities up to next whole number.
CINL CashInLieuOfFraction Fractional part of cash. Take cash in lieu
of fractions.
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
16.1.15.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of fraction disposition.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.10  NetDividendRateFormat40Choice
Definition: Choice between different formats to express a net dividend.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 900 February 2026
```

