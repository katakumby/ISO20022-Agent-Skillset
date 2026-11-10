---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.21 RegulatoryStipulations <RgltryStiptns>"]
file_pages: [138]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.21 RegulatoryStipulations <RgltryStiptns>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 138 to 138.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 138

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NumberOfDaysLendingBorrowing
<NbOfDaysLndgBrrwg>
[0..1] ± 368
   StandardCollateralAmount <StdCollAmt> [0..1] ± 368
   AccruedInterestTax <AcrdIntrstTax> [0..1] Indicator 369
   EndNumberOfDaysAccrued <EndNbOfDaysAcrd> [0..1] Quantity C25 369
   EndFactor <EndFctr> [0..1] Rate 369
   SecuritiesLendingType <SctiesLndgTp> [0..1] ± 369
   Reversible <Rvsbl> [0..1] ± 369
   MinimumDateForCallBack <MinDtForCallBck> [0..1] Date 370
   RollOver <RollOver> [0..1] Indicator 370
   PeriodicPayment <PrdcPmt> [0..1] Indicator 370
   ExCoupon <ExCpn> [0..1] Indicator 370
3.4.21 RegulatoryStipulations <RgltryStiptns>
Presence: [0..1]
Definition: Specifies regulatory stipulations that financial institutions must be compliant with in the
country, region, and/or area they conduct business.
RegulatoryStipulations <RgltryStiptns> contains the following RegulatoryStipulations1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [1..1] CodeSet C12 138
   Stipulations <Stiptns> [1..*] Text 138
3.4.21.1  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government, occupying a particular territory.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 622
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
3.4.21.2  Stipulations <Stiptns>
Presence: [1..*]
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 138 February 2025
```

