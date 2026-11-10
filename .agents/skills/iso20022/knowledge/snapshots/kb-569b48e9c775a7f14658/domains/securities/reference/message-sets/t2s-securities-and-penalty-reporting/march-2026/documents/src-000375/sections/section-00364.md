---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.22 Price", "7.1.22.7 TypeOfPrice28Choice", "7.1.22.7.2 Proprietary <Prtry>"]
file_pages: [451]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.22.7.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 451 to 451.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 451

```text
7.1.22.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of price expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.23 Quantity
7.1.23.1  QuantityBreakdown54
Definition: Details of breakdown of a quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 451
   LotQuantity <LotQty> [0..1] ± 451
   LotDateTime <LotDtTm> [0..1] ± 452
   LotPrice <LotPric> [0..1] ± 452
   TypeOfPrice <TpOfPric> [0..1] ± 452
7.1.23.1.1  LotNumber <LotNb>
Presence: [0..1]
Definition: Identification, for tax purposes, of a lot of identical securities that are bought at a certain date
and at a certain price.
LotNumber <LotNb> contains the following elements (see "GenericIdentification37" on page 351 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 351
   Issuer <Issr> [0..1] Text 351
7.1.23.1.2  LotQuantity <LotQty>
Presence: [0..1]
Definition: Quantity of financial instruments that is part of the lot described.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 451 March 2026
```

