---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.2 Account Identification", "66.1.2.7 SubAccountIdentification5", "66.1.2.7.2 FungibleIndicator <FngbInd>"]
file_pages: [4333, 4334]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.2.7.2 FungibleIndicator <FngbInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4333 to 4334.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4333

```text
Identification <Id> contains one of the following elements (see "AccountIdentificationFormatChoice" on
page 4335 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SimpleIdentification <SmplId> [1..1] ± 4335
Or   IdentificationAndPurpose <IdAndPurp> [1..1]  4335
     Identification <Id> [1..1] ± 4336
     Purpose <Purp> [1..1] CodeSet 4336
Or}   IdentificationAsDSS <IdAsDSS> [1..1] ± 4336
66.1.2.7.2  FungibleIndicator <FngbInd>
Presence: [1..1]
Definition: Indicates whether the securities in the account are fungible, ie, interchangeable.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.2.7.3  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.2.7.4  BalanceForSubAccount <BalForSubAcct>
Presence: [0..*]
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
Impacted by: C1 "AccruedInterestAmountSignRule", C8 "BalanceAtSafekeepingPlaceRule", C5
"AggregateQuantityGuideline"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4333 May 2026
```

## File page 4334

```text
BalanceForSubAccount <BalForSubAcct> contains the following elements (see
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4334 May 2026
```

