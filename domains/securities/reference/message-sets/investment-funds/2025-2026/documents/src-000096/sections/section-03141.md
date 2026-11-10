---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.5 AdditionalBalanceInformation2", "66.1.5.5.3 ExtendedSubBalanceType <XtndedSubBalTp>"]
file_pages: [4369, 4370]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.5.3 ExtendedSubBalanceType <XtndedSubBalTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4369 to 4370.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4369

```text
66.1.5.5.3  ExtendedSubBalanceType <XtndedSubBalTp>
Presence: [1..1]
Warning   Either SubBalanceType or ExtendedSubBalanceType must be present, but not both.
Definition: Reason a security is not available or additional information about the financial instrument for
which the balance is given, for example, unregistered, registered in nominee name.
Datatype: "Extended350Code" on page 5402
66.1.5.6  AggregateBalanceInformation4
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account. A securities balance is calculated from the sum of securities' receipts minus the sum
of securities' deliveries.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4369 May 2026
```

## File page 4370

```text
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
     AdditionalBalanceBreakdownDetails
<AddtlBalBrkdwnDtls>
[0..*] ± 4382
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4370 May 2026
```

