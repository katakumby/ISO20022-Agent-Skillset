---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.13 Financial Instrument", "82.1.13.5 SecurityIdentification19", "82.1.13.5.3 Description <Desc>"]
file_pages: [2953]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.13.5.3 Description <Desc>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2953 to 2953.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2953

```text
82.1.13.5.3  Description <Desc>
Presence: [0..1]
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 3326
82.1.13.6  BasicCollateralValuation1Details
Definition: Basic valuation details of a collateral position.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValuationHaircut <ValtnHrcut> [1..1] Rate 2953
   HaircutSource <HrcutSrc> [0..1] ± 2953
82.1.13.6.1  ValuationHaircut <ValtnHrcut>
Presence: [1..1]
Definition: Haircut percentage applied to the market value of underlying assets used as collateral as a
risk control measure. The institution valuating the collateral calculates the value of underlying assets
based on its market value less a certain percentage (the haircut).
Datatype: "PercentageRate" on page 3325
82.1.13.6.2  HaircutSource <HrcutSrc>
Presence: [0..1]
Definition: Place where the valuation haircut was calculated.
HaircutSource <HrcutSrc> contains the following elements (see "PartyIdentification15" on page 3076
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [0..1] CodeSet C3 3076
   Identification <Id> [1..1] Text 3077
82.1.14 Financial Instrument Quantity
82.1.14.1  FinancialInstrumentQuantity1Choice
Definition: Choice between formats for the quantity of security.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2953 August 2026
```

