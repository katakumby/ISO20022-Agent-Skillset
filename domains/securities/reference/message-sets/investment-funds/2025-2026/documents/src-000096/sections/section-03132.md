---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.2 StatementOfInvestmentFundTransactions2", "66.1.5.2.4 SubAccountDetails <SubAcctDtls>", "66.1.5.2.4.3 TransactionOnSubAccount <TxOnSubAcct>", "66.1.5.2.4.3.8 BalanceByPage <BalByPg>"]
file_pages: [4359]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.2.4.3.8 BalanceByPage <BalByPg>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4359 to 4359.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4359

```text
Constraints
• TransactionTypeLegExecutionIdentificationRule
If TransactionType is SWII or SWIO, then LegExecutionIdentification is optional. If TransactionType
is neither SWII nor SWIO, then LegExecutionIdentification is not allowed.
• TransactionTypeLegIdentificationRule
If TransactionType is SWII or SWIO, then LegIdentification is optional. If TransactionType is neither
SWII nor SWIO, then LegIdentification is not allowed.
66.1.5.2.4.3.8  BalanceByPage <BalByPg>
Presence: [0..1]
Definition: Balance of the financial instrument for this specific statement page.
BalanceByPage <BalByPg> contains the following elements (see "PaginationBalance1" on page 4400
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FirstOpeningBalance <FrstOpngBal> [0..1] ± 4400
Or}   IntermediaryOpeningBalance <IntrmyOpngBal> [0..1] ± 4400
{Or   FinalClosingBalance <FnlClsgBal> [0..1] ± 4401
Or}   IntermediaryClosingBalance <IntrmyClsgBal> [0..1] ± 4401
66.1.5.2.5  Extension <Xtnsn>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C16 "ExtensionRule"
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
66.1.5.3  SubBalanceInformation2
Definition: Net position of a segregated holding of a single security within the overall position held in the
securities account, eg, sub-balance per status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4359 May 2026
```

