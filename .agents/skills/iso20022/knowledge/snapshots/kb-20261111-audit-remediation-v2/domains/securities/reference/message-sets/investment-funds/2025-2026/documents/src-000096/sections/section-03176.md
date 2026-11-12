---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.13 AccountingStatementOfHoldings2", "66.1.5.13.4 SubAccountDetails <SubAcctDtls>"]
file_pages: [4406]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.13.4 SubAccountDetails <SubAcctDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4406 to 4406.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4406

```text
BalanceForAccount <BalForAcct> contains the following elements (see
"AggregateBalanceInformation3" on page 4391 for details)
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
66.1.5.13.4  SubAccountDetails <SubAcctDtls>
Presence: [0..*]
Definition: The sub-account of the safekeeping or investment account.
SubAccountDetails <SubAcctDtls> contains the following elements (see "SubAccountIdentification3"
on page 4337 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4338
   FungibleIndicator <FngbInd> [1..1] Indicator 4338
   ActivityIndicator <ActvtyInd> [1..1] Indicator 4338
   BalanceForSubAccount <BalForSubAcct> [0..*] ± C1, C6 4338
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4406 May 2026
```

