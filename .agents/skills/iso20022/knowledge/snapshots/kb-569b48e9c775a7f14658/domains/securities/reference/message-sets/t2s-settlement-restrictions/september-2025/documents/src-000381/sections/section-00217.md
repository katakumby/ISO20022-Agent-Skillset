---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.18 Quantity", "9.1.18.1 QuantityBreakdown32", "9.1.18.1.1 LotNumber <LotNb>"]
file_pages: [263]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.18.1.1 LotNumber <LotNb>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 263 to 263.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 263

```text
9.1.18.1.1  LotNumber <LotNb>
Presence: [0..1]
Definition: Identification, for tax purposes, of a lot of identical securities that are bought at a certain date
and at a certain price.
LotNumber <LotNb> contains the following elements (see "GenericIdentification37" on page 225 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 226
   Issuer <Issr> [0..1] Text 226
9.1.18.1.2  LotQuantity <LotQty>
Presence: [0..1]
Definition: Quantity of financial instruments that is part of the lot described.
LotQuantity <LotQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 220 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 221
Or   FaceAmount <FaceAmt> [1..1] Amount 221
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 221
9.1.18.1.3  SecuritiesSubBalanceType <SctiesSubBalTp>
Presence: [0..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
SecuritiesSubBalanceType <SctiesSubBalTp> contains the following elements (see
"GenericIdentification30" on page 224 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.18.2  QuantityBreakdown31
Definition: Details of breakdown of a quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [1..1] ± 264
   LotQuantity <LotQty> [0..1] ± 264
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 263 September 2025
```

