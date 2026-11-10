---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.2 StatementOfInvestmentFundTransactions2", "66.1.5.2.3 TransactionOnAccount <TxOnAcct>", "66.1.5.2.3.8 BalanceByPage <BalByPg>"]
file_pages: [4354]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.2.3.8 BalanceByPage <BalByPg>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4354 to 4354.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4354

```text
Constraints
• TransactionTypeLegExecutionIdentificationRule
If TransactionType is SWII or SWIO, then LegExecutionIdentification is optional. If TransactionType
is neither SWII nor SWIO, then LegExecutionIdentification is not allowed.
• TransactionTypeLegIdentificationRule
If TransactionType is SWII or SWIO, then LegIdentification is optional. If TransactionType is neither
SWII nor SWIO, then LegIdentification is not allowed.
66.1.5.2.3.8  BalanceByPage <BalByPg>
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
66.1.5.2.4  SubAccountDetails <SubAcctDtls>
Presence: [1..1]
Definition: Sub-account of the safekeeping or investment account.
Impacted by: C8 "TransactionOnSubAccountRule"
SubAccountDetails <SubAcctDtls> contains the following SubAccountIdentification6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4355
   ActivityIndicator <ActvtyInd> [1..1] Indicator 4355
   TransactionOnSubAccount <TxOnSubAcct> [0..*]  4355
     Identification <Id> [1..1] ± 4356
     Name <Nm> [0..1] Text 4357
     SupplementaryIdentification <SplmtryId> [0..1] Text 4357
     SecuritiesForm <SctiesForm> [0..1] CodeSet 4357
     ClassType <ClssTp> [0..1] Text 4357
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4357
     TransactionDetails <TxDtls> [1..*] ± C9, C10 4357
     BalanceByPage <BalByPg> [0..1] ± 4359
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4354 May 2026
```

