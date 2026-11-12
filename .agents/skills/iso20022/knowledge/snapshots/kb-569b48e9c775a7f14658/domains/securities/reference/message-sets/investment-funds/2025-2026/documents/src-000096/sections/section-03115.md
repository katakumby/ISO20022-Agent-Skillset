---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.2 Account Identification", "66.1.2.11 CashAccountIdentification8Choice"]
file_pages: [4339]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.2.11 CashAccountIdentification8Choice

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4339 to 4339.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4339

```text
Impacted by: C1 "AccruedInterestAmountSignRule", C6 "BalanceAtSafekeepingPlaceRule"
BalanceForSubAccount <BalForSubAcct> contains the following elements (see
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
66.1.2.11  CashAccountIdentification8Choice
Definition: Specifies the unique identification of an account as assigned by the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Other <Othr> [1..1] ± 4339
Or}   IBAN <IBAN> [1..1] IdentifierSet C19 4340
66.1.2.11.1  Other <Othr>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4339 May 2026
```

