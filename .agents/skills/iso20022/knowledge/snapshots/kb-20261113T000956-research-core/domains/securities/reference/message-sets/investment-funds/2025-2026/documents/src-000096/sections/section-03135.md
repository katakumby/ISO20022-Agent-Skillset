---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.4 AggregateBalancePerSafekeepingPlace4", "66.1.5.4.1 AggregateBalance <AggtBal>"]
file_pages: [4363]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.4.1 AggregateBalance <AggtBal>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4363 to 4363.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4363

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AggregateBalance <AggtBal> [1..1] ± 4363
   DaysAccrued <DaysAcrd> [0..1] Quantity 4363
   HoldingValue <HldgVal> [1..*] Amount C2, C10 4363
   PreviousHoldingValue <PrvsHldgVal> [0..1] Amount C2, C10 4364
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] Amount C2, C10 4364
   AccruedInterestAmountSign <AcrdIntrstAmtSgn> [0..1] Indicator 4365
   BookValue <BookVal> [0..1] Amount C2, C10 4365
   SafekeepingPlace <SfkpgPlc> [1..1] ± 4365
   PriceDetails <PricDtls> [1..*] ± C15 4366
   ForeignExchangeDetails <FXDtls> [0..1] ± 4366
   BalanceBreakdownDetails <BalBrkdwnDtls> [0..*] ± 4367
   AdditionalBalanceBreakdownDetails
<AddtlBalBrkdwnDtls>
[0..*] ± 4367
Constraints
• AccruedInterestAmountSignRule
If AccruedInterestAmount is present, then AccruedInterestAmountSign must be present. If
AccruedInterestAmount is not present, then AccruedInterestAmountSign may not be present.
66.1.5.4.1  AggregateBalance <AggtBal>
Presence: [1..1]
Definition: Total quantity of financial instrument for the referenced holding.
AggregateBalance <AggtBal> contains one of the following elements (see "BalanceQuantity1Choice"
on page 4345 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 4346
Or}   QuantityAsDSS <QtyAsDSS> [1..1] ± 4346
66.1.5.4.2  DaysAccrued <DaysAcrd>
Presence: [0..1]
Definition: Specifies the number of days used for calculating the accrued interest amount.
Datatype: "Number" on page 5400
66.1.5.4.3  HoldingValue <HldgVal>
Presence: [1..*]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4363 May 2026
```

