---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.12 Financial Instrument", "7.1.12.3 SecurityIdentification19", "7.1.12.3.2 OtherIdentification <OthrId>", "7.1.12.3.2.3 Type <Tp>"]
file_pages: [341]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.12.3.2.3 Type <Tp>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 341 to 341.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 341

```text
Datatype: "Max16Text" on page 556
7.1.12.3.2.3  Type <Tp>
Presence: [1..1]
Definition: Type of the identification.
Type <Tp> contains one of the following elements (see "IdentificationSource3Choice" on page 351 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 351
Or}   Proprietary <Prtry> [1..1] Text 351
7.1.12.3.3  Description <Desc>
Presence: [0..1]
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 556
7.1.12.4  BasicCollateralValuation1Details
Definition: Basic valuation details of a collateral position.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValuationHaircut <ValtnHrcut> [1..1] Rate 341
   HaircutSource <HrcutSrc> [0..1] ± 341
7.1.12.4.1  ValuationHaircut <ValtnHrcut>
Presence: [1..1]
Definition: Haircut percentage applied to the market value of underlying assets used as collateral as a
risk control measure. The institution valuating the collateral calculates the value of underlying assets
based on its market value less a certain percentage (the haircut).
Datatype: "PercentageRate" on page 555
7.1.12.4.2  HaircutSource <HrcutSrc>
Presence: [0..1]
Definition: Place where the valuation haircut was calculated.
HaircutSource <HrcutSrc> contains the following elements (see "PartyIdentification15" on page 430
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [0..1] CodeSet C3 430
   Identification <Id> [1..1] Text 431
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 341 March 2026
```

