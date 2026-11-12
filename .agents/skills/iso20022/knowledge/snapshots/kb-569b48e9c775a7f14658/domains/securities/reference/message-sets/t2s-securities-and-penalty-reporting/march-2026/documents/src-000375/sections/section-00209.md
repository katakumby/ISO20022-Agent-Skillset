---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.14 Balance30", "7.1.5.14.2 BalanceForAccount <BalForAcct>", "7.1.5.14.2.5 ValuationHaircutDetails <ValtnHrcutDtls>"]
file_pages: [282]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.14.2.5 ValuationHaircutDetails <ValtnHrcutDtls>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 282 to 282.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 282

```text
InvestmentFundsFinancialInstrumentAttributes <InvstmtFndsFinInstrmAttrbts> contains the
following elements (see "FinancialInstrument21" on page 336 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClassType <ClssTp> [0..1] Text 336
   SecuritiesForm <SctiesForm> [0..1] CodeSet 337
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 337
   ProductGroup <PdctGrp> [0..1] Text 337
   UmbrellaName <UmbrllNm> [0..1] Text 337
   BaseCurrency <BaseCcy> [0..1] CodeSet C1 337
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C1 338
   RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C2 338
   DualFundIndicator <DualFndInd> [0..1] Indicator 338
   CountryOfDomicile <CtryOfDmcl> [0..1] CodeSet C3 338
   RegisteredDistributionCountry <RegdDstrbtnCtry> [0..*] CodeSet C3 339
7.1.5.14.2.5  ValuationHaircutDetails <ValtnHrcutDtls>
Presence: [0..1]
Definition: Elements used to calculate the valuation haircut.
ValuationHaircutDetails <ValtnHrcutDtls> contains the following elements (see
"BasicCollateralValuation1Details" on page 341 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValuationHaircut <ValtnHrcut> [1..1] Rate 341
   HaircutSource <HrcutSrc> [0..1] ± 341
7.1.5.14.2.6  AggregateBalance <AggtBal>
Presence: [0..1]
Definition: Total quantity of financial instruments of the balance.
AggregateBalance <AggtBal> contains the following elements (see "Balance6" on page 267 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [1..1] CodeSet 268
   Quantity <Qty> [1..1] ± 268
7.1.5.14.2.7  AvailableBalance <AvlblBal>
Presence: [0..1]
Definition: Total quantity of financial instruments of the balance that is available.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 282 March 2026
```

