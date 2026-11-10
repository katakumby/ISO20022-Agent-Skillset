---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.9 SubAccountDetails <SubAcctDtls>", "3.4.9.5 BalanceForSubAccount <BalForSubAcct>", "3.4.9.5.4 AdditionalDerivativeAttributes <AddtlDerivAttrbts>"]
file_pages: [119]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.9.5.4 AdditionalDerivativeAttributes <AddtlDerivAttrbts>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 119 to 119.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 119

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
3.4.9.5.4  AdditionalDerivativeAttributes <AddtlDerivAttrbts>
Presence: [0..1]
Definition: Details of the swap contract.
AdditionalDerivativeAttributes <AddtlDerivAttrbts> contains the following elements (see
"DerivativeBasicAttributes1" on page 1457 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NotionalCurrencyAndAmount <NtnlCcyAndAmt> [1..1] Amount C2, C8 1457
   InterestIncludedInPrice <IntrstInclInPric> [0..1] Indicator 1457
3.4.9.5.5  AggregateBalance <AggtBal>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
AggregateBalance <AggtBal> contains the following elements (see "Balance17" on page 1431 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [1..1] CodeSet 1432
   Quantity <Qty> [1..1] ± 1432
3.4.9.5.6  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 119 March 2026
```

