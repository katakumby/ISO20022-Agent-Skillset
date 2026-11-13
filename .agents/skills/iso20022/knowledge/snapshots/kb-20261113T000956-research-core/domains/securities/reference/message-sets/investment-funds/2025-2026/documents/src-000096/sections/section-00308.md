---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02", "22.4 Message Building Blocks", "22.4.8 SubAccountDetails <SubAcctDtls>", "22.4.8.3 TransactionOnSubAccount <TxOnSubAcct>", "22.4.8.3.8 BalanceByPage <BalByPg>"]
file_pages: [426]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.006.001.02"]
---

# 22.4.8.3.8 BalanceByPage <BalByPg>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 426 to 426.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 426

```text
Constraints
• TransactionTypeLegExecutionIdentificationRule
If TransactionType is SWII or SWIO, then LegExecutionIdentification is optional. If TransactionType
is neither SWII nor SWIO, then LegExecutionIdentification is not allowed.
• TransactionTypeLegIdentificationRule
If TransactionType is SWII or SWIO, then LegIdentification is optional. If TransactionType is neither
SWII nor SWIO, then LegIdentification is not allowed.
22.4.8.3.8  BalanceByPage <BalByPg>
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
22.4.9 Extension <Xtnsn>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C5 "ExtensionRule"
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
Approved by the Securities SEG on 27 January 2026 semt.006.001.02
StatementOfInvestmentFundTransactionsV02
Investment Funds - Maintenance 2025 - 2026 426 May 2026
```

