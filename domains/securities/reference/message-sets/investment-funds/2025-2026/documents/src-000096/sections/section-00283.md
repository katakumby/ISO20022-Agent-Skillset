---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["19 semt.003.001.02 AccountingStatementOfHoldingsV02", "19.4 Message Building Blocks", "19.4.8 SubAccountDetails <SubAcctDtls>"]
file_pages: [396, 397]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.02"]
---

# 19.4.8 SubAccountDetails <SubAcctDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 396 to 397.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 396

```text
Constraints
• AccruedInterestAmountSignRule
If AccruedInterestAmount is present, then AccruedInterestAmountSign must be present. If
AccruedInterestAmount is not present, then AccruedInterestAmountSign may not be present.
• BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
19.4.8 SubAccountDetails <SubAcctDtls>
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
19.4.9 TotalValues <TtlVals>
Presence: [0..1]
Definition: Value of total holdings reported.
TotalValues <TtlVals> contains the following elements (see "TotalValueInPageAndStatement" on
page 4390 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] Amount C1, C13 4391
   TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] Amount C1, C13 4391
19.4.10 Extension <Xtnsn>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C11 "ExtensionRule"
Approved by the Securities SEG on 27 January 2026 semt.003.001.02
AccountingStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 396 May 2026
```

## File page 397

```text
Extension <Xtnsn> contains the following elements (see "Extension1" on page 4835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [1..1] Text 4836
   Text <Txt> [1..1] Text 4836
Constraints
• ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
Approved by the Securities SEG on 27 January 2026 semt.003.001.02
AccountingStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 397 May 2026
```

