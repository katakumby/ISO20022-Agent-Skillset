---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.7 CustodyStatementOfHoldings2", "66.1.5.7.4 SubAccountDetails <SubAcctDtls>"]
file_pages: [4388]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.7.4 SubAccountDetails <SubAcctDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4388 to 4388.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4388

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AdditionalBalanceBreakdownDetails
<AddtlBalBrkdwnDtls>
[0..*] ± 4382
Constraints
• AccruedInterestAmountSignRule
if AccruedInterestAmount is present, then AccruedInterestAmountSign must be present. If
AccruedInterestAmount is not present, then AccruedInterestAmountSign may not be present.
• AggregateQuantityGuideline
The AggregateQuantity should be the sum of AvailableQuantity and NotAvailableQuantity if
AvailableQuantity and NotAvailableQuantity are both present.
• BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
66.1.5.7.4  SubAccountDetails <SubAcctDtls>
Presence: [0..*]
Definition: Sub-account of the safekeeping or investment account.
SubAccountDetails <SubAcctDtls> contains the following elements (see "SubAccountIdentification5"
on page 4332 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4332
   FungibleIndicator <FngbInd> [1..1] Indicator 4333
   ActivityIndicator <ActvtyInd> [1..1] Indicator 4333
   BalanceForSubAccount <BalForSubAcct> [0..*] ± C1, C8,
C5
4333
66.1.5.7.5  TotalValues <TtlVals>
Presence: [0..1]
Definition: Value of total holdings reported.
TotalValues <TtlVals> contains the following elements (see "TotalValueInPageAndStatement" on
page 4390 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] Amount C1, C13 4391
   TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] Amount C1, C13 4391
66.1.5.7.6  Extension <Xtnsn>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4388 May 2026
```

