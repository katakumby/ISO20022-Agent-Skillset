---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.10 AggregateBalanceInformation3", "66.1.5.10.1 AggregateQuantity <AggtQty>"]
file_pages: [4392]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.10.1 AggregateQuantity <AggtQty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4392 to 4392.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4392

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AggregateQuantity <AggtQty> [1..1] ± 4392
   DaysAccrued <DaysAcrd> [0..1] Quantity 4392
   HoldingValue <HldgVal> [1..*] Amount C2, C10 4393
   PreviousHoldingValue <PrvsHldgVal> [0..1] Amount C2, C10 4393
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] Amount C2, C10 4393
   AccruedInterestAmountSign <AcrdIntrstAmtSgn> [0..1] Indicator 4394
   BookValue <BookVal> [0..1] Amount C2, C10 4394
   SafekeepingPlace <SfkpgPlc> [0..1] ± 4394
   FinancialInstrumentDetails <FinInstrmDtls> [1..1] ± C12 4395
   PriceDetails <PricDtls> [1..*] ± C15 4395
   ForeignExchangeDetails <FXDtls> [0..1] ± 4396
   BalanceBreakdownDetails <BalBrkdwnDtls> [0..*] ± 4396
   AdditionalBalanceBreakdownDetails
<AddtlBalBrkdwnDtls>
[0..*] ± 4397
   BalanceAtSafekeepingPlace <BalAtSfkpgPlc> [0..*] ± C2 4397
Constraints
• AccruedInterestAmountSignRule
If AccruedInterestAmount is present, then AccruedInterestAmountSign must be present. If
AccruedInterestAmount is not present, then AccruedInterestAmountSign may not be present.
• BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
66.1.5.10.1  AggregateQuantity <AggtQty>
Presence: [1..1]
Definition: Total quantity of financial instrument for the referenced holding.
AggregateQuantity <AggtQty> contains one of the following elements (see "BalanceQuantity1Choice"
on page 4345 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 4346
Or}   QuantityAsDSS <QtyAsDSS> [1..1] ± 4346
66.1.5.10.2  DaysAccrued <DaysAcrd>
Presence: [0..1]
Definition: Specifies the number of days used for calculating the accrued interest amount.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4392 May 2026
```

