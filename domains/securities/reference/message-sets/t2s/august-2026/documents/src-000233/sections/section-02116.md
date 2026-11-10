---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.16 Balance30", "82.1.5.16.2 BalanceForAccount <BalForAcct>", "82.1.5.16.2.5 ValuationHaircutDetails <ValtnHrcutDtls>"]
file_pages: [2874]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.16.2.5 ValuationHaircutDetails <ValtnHrcutDtls>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2874 to 2874.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2874

```text
InvestmentFundsFinancialInstrumentAttributes <InvstmtFndsFinInstrmAttrbts> contains the
following elements (see "FinancialInstrument21" on page 2947 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClassType <ClssTp> [0..1] Text 2948
   SecuritiesForm <SctiesForm> [0..1] CodeSet 2948
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 2948
   ProductGroup <PdctGrp> [0..1] Text 2949
   UmbrellaName <UmbrllNm> [0..1] Text 2949
   BaseCurrency <BaseCcy> [0..1] CodeSet C1 2949
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C1 2949
   RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C1 2950
   DualFundIndicator <DualFndInd> [0..1] Indicator 2950
   CountryOfDomicile <CtryOfDmcl> [0..1] CodeSet C3 2950
   RegisteredDistributionCountry <RegdDstrbtnCtry> [0..*] CodeSet C3 2950
82.1.5.16.2.5  ValuationHaircutDetails <ValtnHrcutDtls>
Presence: [0..1]
Definition: Elements used to calculate the valuation haircut.
ValuationHaircutDetails <ValtnHrcutDtls> contains the following elements (see
"BasicCollateralValuation1Details" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValuationHaircut <ValtnHrcut> [1..1] Rate 2953
   HaircutSource <HrcutSrc> [0..1] ± 2953
82.1.5.16.2.6  AggregateBalance <AggtBal>
Presence: [0..1]
Definition: Total quantity of financial instruments of the balance.
AggregateBalance <AggtBal> contains the following elements (see "Balance6" on page 2857 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [1..1] CodeSet 2857
   Quantity <Qty> [1..1] ± 2858
82.1.5.16.2.7  AvailableBalance <AvlblBal>
Presence: [0..1]
Definition: Total quantity of financial instruments of the balance that is available.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2874 August 2026
```

