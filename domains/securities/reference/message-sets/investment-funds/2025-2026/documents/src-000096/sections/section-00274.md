---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["18 semt.002.001.02 CustodyStatementOfHoldingsV02", "18.4 Message Building Blocks", "18.4.7 BalanceForAccount <BalForAcct>"]
file_pages: [383, 384]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.02"]
---

# 18.4.7 BalanceForAccount <BalForAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 383 to 384.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 383

```text
18.4.7 BalanceForAccount <BalForAcct>
Presence: [0..*]
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
Impacted by: C1 "AccruedInterestAmountSignRule", C8 "BalanceAtSafekeepingPlaceRule", C5
"AggregateQuantityGuideline"
Approved by the Securities SEG on 27 January 2026 semt.002.001.02 CustodyStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 383 May 2026
```

## File page 384

```text
BalanceForAccount <BalForAcct> contains the following elements (see
"AggregateBalanceInformation4" on page 4369 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AggregateQuantity <AggtQty> [1..1] ± 4371
   AvailableQuantity <AvlblQty> [0..1] ± 4371
   NotAvailableQuantity <NotAvlblQty> [0..1] ± 4371
   DaysAccrued <DaysAcrd> [0..1] Quantity 4372
   HoldingValue <HldgVal> [0..*] Amount C2, C10 4372
   PreviousHoldingValue <PrvsHldgVal> [0..1] Amount C2, C10 4372
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] Amount C2, C10 4372
   AccruedInterestAmountSign <AcrdIntrstAmtSgn> [0..1] Indicator 4373
   BookValue <BookVal> [0..1] Amount C2, C10 4373
   SafekeepingPlace <SfkpgPlc> [0..1] ± 4373
   FinancialInstrumentDetails <FinInstrmDtls> [1..1] ± C12 4374
   PriceDetails <PricDtls> [0..*] ± C15 4374
   ForeignExchangeDetails <FXDtls> [0..1] ± 4375
   BalanceBreakdownDetails <BalBrkdwnDtls> [0..*] ± 4375
   AdditionalBalanceBreakdownDetails
<AddtlBalBrkdwnDtls>
[0..*] ± 4376
   BalanceAtSafekeepingPlace <BalAtSfkpgPlc> [0..*]  C2, C6 4376
     AggregateQuantity <AggtQty> [1..1] ± 4377
     AvailableQuantity <AvlblQty> [0..1] ± 4378
     NotAvailableQuantity <NotAvlblQty> [0..1] ± 4378
     DaysAccrued <DaysAcrd> [0..1] Quantity 4378
     HoldingValue <HldgVal> [0..*] Amount C2, C10 4378
     PreviousHoldingValue <PrvsHldgVal> [0..1] Amount C2, C10 4379
     AccruedInterestAmount <AcrdIntrstAmt> [0..1] Amount C2, C10 4379
     AccruedInterestAmountSign <AcrdIntrstAmtSgn> [0..1] Indicator 4379
     BookValue <BookVal> [0..1] Amount C2, C10 4380
     SafekeepingPlace <SfkpgPlc> [1..1] ± 4380
     PriceDetails <PricDtls> [0..*] ± C15 4380
     ForeignExchangeDetails <FXDtls> [0..1] ± 4381
     BalanceBreakdownDetails <BalBrkdwnDtls> [0..*] ± 4381
Approved by the Securities SEG on 27 January 2026 semt.002.001.02 CustodyStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 384 May 2026
```

