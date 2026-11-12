---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.22 Price", "7.1.22.2 OtherPrices5"]
file_pages: [507]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.22.2 OtherPrices5

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 507 to 507.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 507

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.22.2  OtherPrices5
Definition: Specifies the type of price and information about the price.
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
7.1.22.2.1  Maximum <Max>
Presence: [0..1]
Definition: Specifies the maximum price.
Maximum <Max> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 507 February 2025
```

