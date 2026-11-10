---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["19 semt.003.001.02 AccountingStatementOfHoldingsV02", "19.4 Message Building Blocks", "19.4.7 BalanceForAccount <BalForAcct>"]
file_pages: [395]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.02"]
---

# 19.4.7 BalanceForAccount <BalForAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 395 to 395.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 395

```text
AccountDetails <AcctDtls> contains the following elements (see "SafekeepingAccount2" on page 4643
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4643
   FungibleIndicator <FngbInd> [1..1] Indicator 4643
   Name <Nm> [0..1] Text 4644
   Designation <Dsgnt> [0..1] Text 4644
   IntermediaryInformation <IntrmyInf> [0..10] ± 4644
   AccountOwner <AcctOwnr> [0..1] ± 4644
   AccountServicer <AcctSvcr> [0..1] ± 4645
19.4.7 BalanceForAccount <BalForAcct>
Presence: [0..*]
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
Impacted by: C1 "AccruedInterestAmountSignRule", C6 "BalanceAtSafekeepingPlaceRule"
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
Approved by the Securities SEG on 27 January 2026 semt.003.001.02
AccountingStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 395 May 2026
```

