---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.18 OtherPrices <OthrPrics>"]
file_pages: [126]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.18 OtherPrices <OthrPrics>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 126 to 126.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 126

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemunerationAmountRequest <RmnrtnAmtReq> [0..1] Indicator 242
   RemunerationAmount <RmnrtnAmt> [0..1] ± 242
   BorrowingInterestAmount <BrrwgIntrstAmt> [0..1] ± 242
   BorrowingFee <BrrwgFee> [0..1] ± 243
   NetMarketValue <NetMktVal> [0..1] ± 243
   RemainingFaceValue <RmngFaceVal> [0..1] ± 243
   RemainingBookValue <RmngBookVal> [0..1] ± 244
   ClearingBrokerCommission <ClrBrkrComssn> [0..1] ± 244
   DifferenceInPrice <DiffInPric> [0..1] ± 244
   OddLotFee <OddLotFee> [0..1] Indicator 245
3.4.18 OtherPrices <OthrPrics>
Presence: [0..*]
Definition: Other prices than the deal price.
OtherPrices <OthrPrics> contains the following elements (see "OtherPrices5" on page 507 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Maximum <Max> [0..1] ± 507
   Transaction <Tx> [0..1] ± 508
   MarketBrokerCommission <MktBrkrComssn> [0..1] ± 508
   MarkedUp <MrkdUp> [0..1] ± 508
   MarkedDown <MrkdDwn> [0..1] ± 508
   NetDisclosed <NetDscld> [0..1] ± 509
   NetUndisclosed <NetUdscld> [0..1] ± 509
   NotionalGross <NtnlGrss> [0..1] ± 509
   BenchmarkWeightedAverage <BchmkWghtdAvrg> [0..1] ± 509
   AllMarketsWeightedAverage <AllMktsWghtdAvrg> [0..1] ± 510
   Benchmark <Bchmk> [0..1] ± 510
   OtherPrice <OthrPric> [0..1] ± 510
   IndexPrice <IndxPric> [0..1] ± 510
   ReportedPrice <RptdPric> [0..1] ± 510
   ReferencePrice <RefPric> [0..1] ± 511
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 126 February 2025
```

