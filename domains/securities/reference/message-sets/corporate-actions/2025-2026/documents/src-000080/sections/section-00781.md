---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.53 FractionDispositionType28Choice"]
file_pages: [974]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.53 FractionDispositionType28Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 974 to 974.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 974

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.53  FractionDispositionType28Choice
Definition: Choice between a standard code or a proprietary code to specify the type of fraction
disposition.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 974
Or}   Proprietary <Prtry> [1..1] ± 974
16.1.15.53.1  Code <Cd>
Presence: [1..1]
Definition: Specifies how fractions resulting from derived securities will be processed or how prorated
decisions will be rounding, if provided with a pro ration rate.
Datatype: "FractionDispositionType10Code" on page 1211
CodeName Name Definition
BUYU BuyUp Buy securities up to next whole number.
CINL CashInLieuOfFraction Fractional part of cash. Take cash in lieu
of fractions.
EXPI Expire Let fractions expire worthless.
DIST IssueFraction Take distribution of fractions in the form
of securities.
16.1.15.53.2  Proprietary <Prtry>
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 974 February 2026
```

