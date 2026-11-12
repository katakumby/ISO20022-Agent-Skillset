---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.49 SecuritiesFinancing12", "7.1.19.49.1 RateChangeDate <RateChngDt>"]
file_pages: [360]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.49.1 RateChangeDate <RateChngDt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 360 to 360.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 360

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
7.1.19.49.1  RateChangeDate <RateChngDt>
Presence: [0..1]
Definition: Date/Time at which rate change has taken place.
Datatype: "ISODateTime" on page 662
7.1.19.49.2  RateType <RateTp>
Presence: [0..1]
Definition: Specifies whether the rate is fixed or variable.
RateType <RateTp> contains one of the following elements (see "RateType35Choice" on page 516 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 516
Or}   Proprietary <Prtry> [1..1] ± 516
7.1.19.49.3  Revaluation <Rvaltn>
Presence: [0..1]
Definition: Specifies whether the collateral position should be subject to automatic revaluation by the
account servicer.
Revaluation <Rvaltn> contains one of the following elements (see "Revaluation3Choice" on page 303
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 304
Or}   Proprietary <Prtry> [1..1] ± 304
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 360 February 2025
```

