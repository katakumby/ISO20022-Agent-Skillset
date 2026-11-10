---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.32 SupplementaryData1", "7.1.19.32.2 Envelope <Envlp>"]
file_pages: [322]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.32.2 Envelope <Envlp>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 322 to 322.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 322

```text
7.1.19.32.2  Envelope <Envlp>
Presence: [1..1]
Definition: Technical element wrapping the supplementary data.
Type: (External Schema)
Technical component that contains the validated supplementary data information. This technical
envelope allows to segregate the supplementary data information from any other information.
7.1.19.33  Number24Choice
Definition: Choice number format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NumberIdentification <NbId> [1..1] Text 322
Or}   Proprietary <Prtry> [1..1] ± 322
7.1.19.33.1  NumberIdentification <NbId>
Presence: [1..1]
Definition: Number of maximum 4 numeric text.
Datatype: "Max4NumericText" on page 669
7.1.19.33.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Number of maximum 35 text, with the possibility to provide an issuer for the number
identification.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 279 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 279
   Issuer <Issr> [1..1] Text 279
   SchemeName <SchmeNm> [0..1] Text 279
7.1.19.34  SpreadRate1
Definition: Margin over or under an index that determines the repurchase rate expressed as a rate or an
amount.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [1..1] Indicator 323
   RateOrAmount <RateOrAmt> [1..1]  323
{Or     Amount <Amt> [1..1] Amount C1, C9 323
Or}     Rate <Rate> [1..1] Rate 323
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 322 February 2025
```

