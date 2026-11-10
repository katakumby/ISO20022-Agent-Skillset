---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.7 UnderlyingFinancialInstrument <UndrlygFinInstrm>", "3.4.7.2 Attributes <Attrbts>", "3.4.7.2.52 FinancialInstrumentAttributeAdditionalDetails <FinInstrmAttrAddtlDtls>"]
file_pages: [94, 95]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.7.2.52 FinancialInstrumentAttributeAdditionalDetails <FinInstrmAttrAddtlDtls>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 94 to 95.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 94

```text
ContractSize <CtrctSz> contains one of the following elements (see
"FinancialInstrumentQuantity18Choice" on page 518 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 518
Or}   FaceAmount <FaceAmt> [1..1] Amount 518
3.4.7.2.52  FinancialInstrumentAttributeAdditionalDetails <FinInstrmAttrAddtlDtls>
Presence: [0..1]
Definition: Provides additional information about the financial instrument in narrative form.
Datatype: "Max350Text" on page 669
3.4.8 Stipulations <Stiptns>
Presence: [0..1]
Definition: Additional restrictions on the financial instrument, related to the stipulation.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 94 February 2025
```

## File page 95

```text
Stipulations <Stiptns> contains the following FinancialInstrumentStipulations4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Geographics <Geogcs> [0..1] Text 96
   YieldRange <YldRg> [0..1] ± 96
   Rating <Ratg> [0..1] ± 96
   CouponRange <CpnRg> [0..1] ± 97
   AmortisableIndicator <AmtsblInd> [0..1] Indicator 97
   Purpose <Purp> [0..1] Text 97
   AlternativeMinimumTaxIndicator <AltrntvMinTaxInd> [0..1] Indicator 97
   AutoReinvestment <AutoRinvstmt> [0..1] Rate 98
   TransactionConditions <TxConds> [0..1] CodeSet 98
   Currency <Ccy> [0..1] CodeSet C1 99
   CustomDate <CstmDt> [0..1] ± 99
   Haircut <Hrcut> [0..1] Rate 99
   InsuredIndicator <InsrdInd> [0..1] Indicator 99
   LookBack <LookBck> [0..1] Quantity 100
   MaturityDate <MtrtyDt> [0..1] YearMonth 100
   IssueDate <IsseDt> [0..1] YearMonth 100
   IssuerIdentification <IssrId> [0..1] IdentifierSet C9 100
   IssueSize <IsseSz> [0..1] Quantity 100
   MinimumDenomination <MinDnmtn> [0..1] ± 100
   MaximumSubstitution <MaxSbstitn> [0..1] Quantity 101
   MinimumIncrement <MinIncrmt> [0..1] ± 101
   PaymentFrequency <PmtFrqcy> [0..1] CodeSet 101
   MinimumQuantity <MinQty> [0..1] ± 102
   Production <Pdctn> [0..1] Text 102
   RestrictedIndicator <RstrctdInd> [0..1] Indicator 102
   PriceFrequency <PricFrqcy> [0..1] CodeSet 102
   Sector <Sctr> [0..1] Text 103
   SubstitutionFrequency <SbstitnFrqcy> [0..1] CodeSet 103
   SubstitutionLeft <SbstitnLft> [0..1] Quantity 103
   WholePoolIndicator <WhlPoolInd> [0..1] Indicator 104
   PriceSource <PricSrc> [0..1] Text 104
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 95 February 2025
```

