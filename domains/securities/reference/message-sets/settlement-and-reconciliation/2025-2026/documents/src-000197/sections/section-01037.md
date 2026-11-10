---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.6 SecurityIdentification19", "35.1.11.6.2 OtherIdentification <OthrId>", "35.1.11.6.2.3 Type <Tp>"]
file_pages: [1476]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.6.2.3 Type <Tp>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1476 to 1476.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1476

```text
35.1.11.6.2.3  Type <Tp>
Presence: [1..1]
Definition: Type of the identification.
Type <Tp> contains one of the following elements (see "IdentificationSource3Choice" on page 1497 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1498
Or}   Proprietary <Prtry> [1..1] Text 1498
35.1.11.6.3  Description <Desc>
Presence: [0..1]
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 2191
35.1.11.7  BasicCollateralValuation1Details
Definition: Basic valuation details of a collateral position.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValuationHaircut <ValtnHrcut> [1..1] Rate 1476
   HaircutSource <HrcutSrc> [0..1] ± 1476
35.1.11.7.1  ValuationHaircut <ValtnHrcut>
Presence: [1..1]
Definition: Haircut percentage applied to the market value of underlying assets used as collateral as a
risk control measure. The institution valuating the collateral calculates the value of underlying assets
based on its market value less a certain percentage (the haircut).
Datatype: "PercentageRate" on page 2190
35.1.11.7.2  HaircutSource <HrcutSrc>
Presence: [0..1]
Definition: Place where the valuation haircut was calculated.
HaircutSource <HrcutSrc> contains the following elements (see "PartyIdentification15" on page 1683
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [0..1] CodeSet C7 1683
   Identification <Id> [1..1] Text 1684
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1476 March 2026
```

