---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02", "22.4 Message Building Blocks", "22.4.8 SubAccountDetails <SubAcctDtls>", "22.4.8.1 Identification <Id>"]
file_pages: [421]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.006.001.02"]
---

# 22.4.8.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 421 to 421.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 421

```text
SubAccountDetails <SubAcctDtls> contains the following SubAccountIdentification6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 421
   ActivityIndicator <ActvtyInd> [1..1] Indicator 421
   TransactionOnSubAccount <TxOnSubAcct> [0..*]  422
     Identification <Id> [1..1] ± 422
     Name <Nm> [0..1] Text 423
     SupplementaryIdentification <SplmtryId> [0..1] Text 423
     SecuritiesForm <SctiesForm> [0..1] CodeSet 423
     ClassType <ClssTp> [0..1] Text 424
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 424
     TransactionDetails <TxDtls> [1..*] ± C9, C10 424
     BalanceByPage <BalByPg> [0..1] ± 426
Constraints
• TransactionOnSubAccountRule
If ActivityIndicator is "true" or "1" (Yes), then TransactionOnSubAccount must be present. If
ActivityIndicator is "false" or "0" (No), then TransactionOnSubAccount is not allowed.
22.4.8.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
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
22.4.8.2  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
Approved by the Securities SEG on 27 January 2026 semt.006.001.02
StatementOfInvestmentFundTransactionsV02
Investment Funds - Maintenance 2025 - 2026 421 May 2026
```

