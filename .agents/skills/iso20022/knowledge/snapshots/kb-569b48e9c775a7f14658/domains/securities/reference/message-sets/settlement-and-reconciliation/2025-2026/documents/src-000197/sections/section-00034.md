---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.9 SubAccountDetails <SubAcctDtls>", "2.4.9.5 BalanceForSubAccount <BalForSubAcct>", "2.4.9.5.4 ValuationHaircutDetails <ValtnHrcutDtls>"]
file_pages: [62]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.9.5.4 ValuationHaircutDetails <ValtnHrcutDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 62 to 62.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 62

```text
InvestmentFundsFinancialInstrumentAttributes <InvstmtFndsFinInstrmAttrbts> contains the
following elements (see "FinancialInstrument21" on page 1457 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClassType <ClssTp> [0..1] Text 1458
   SecuritiesForm <SctiesForm> [0..1] CodeSet 1458
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 1458
   ProductGroup <PdctGrp> [0..1] Text 1459
   UmbrellaName <UmbrllNm> [0..1] Text 1459
   BaseCurrency <BaseCcy> [0..1] CodeSet C1 1459
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C1 1459
   RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C2 1460
   DualFundIndicator <DualFndInd> [0..1] Indicator 1460
   CountryOfDomicile <CtryOfDmcl> [0..1] CodeSet C7 1460
   RegisteredDistributionCountry <RegdDstrbtnCtry> [0..*] CodeSet C7 1460
2.4.9.5.4  ValuationHaircutDetails <ValtnHrcutDtls>
Presence: [0..1]
Definition: Elements used to calculate the valuation haircut.
ValuationHaircutDetails <ValtnHrcutDtls> contains the following elements (see
"BasicCollateralValuation1Details" on page 1476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValuationHaircut <ValtnHrcut> [1..1] Rate 1476
   HaircutSource <HrcutSrc> [0..1] ± 1476
2.4.9.5.5  AggregateBalance <AggtBal>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
AggregateBalance <AggtBal> contains the following elements (see "Balance17" on page 1431 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [1..1] CodeSet 1432
   Quantity <Qty> [1..1] ± 1432
2.4.9.5.6  AvailableBalance <AvlblBal>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 62 March 2026
```

