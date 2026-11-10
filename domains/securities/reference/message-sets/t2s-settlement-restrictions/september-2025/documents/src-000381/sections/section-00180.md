---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.9 Financial Instrument", "9.1.9.2 FinancialInstrumentAttributes92", "9.1.9.2.38 MinimumNominalQuantity <MinNmnlQty>"]
file_pages: [219]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.9.2.38 MinimumNominalQuantity <MinNmnlQty>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 219 to 219.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 219

```text
9.1.9.2.38  MinimumNominalQuantity <MinNmnlQty>
Presence: [0..1]
Definition: Minimum nominal quantity of financial instrument.
MinimumNominalQuantity <MinNmnlQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 220 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 221
Or   FaceAmount <FaceAmt> [1..1] Amount 221
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 221
9.1.9.2.39  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a quantity.
ContractSize <CtrctSz> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 220 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 221
Or   FaceAmount <FaceAmt> [1..1] Amount 221
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 221
9.1.9.2.40  UnderlyingFinancialInstrumentIdentification <UndrlygFinInstrmId>
Presence: [0..*]
Definition: Identification of the underlying security.
Impacted by: C8 "DescriptionPresenceRule", C9 "DescriptionUsageRule", C11 "ISINGuideline", C12
"ISINPresenceRule", C14 "OtherIdentificationPresenceRule"
UnderlyingFinancialInstrumentIdentification <UndrlygFinInstrmId> contains the following elements
(see "SecurityIdentification19" on page 207 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 208
   OtherIdentification <OthrId> [0..*]  208
     Identification <Id> [1..1] Text 208
     Suffix <Sfx> [0..1] Text 208
     Type <Tp> [1..1] ± 208
   Description <Desc> [0..1] Text 208
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 219 September 2025
```

