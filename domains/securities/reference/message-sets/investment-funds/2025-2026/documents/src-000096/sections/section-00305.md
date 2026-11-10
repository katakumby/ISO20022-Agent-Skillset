---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02", "22.4 Message Building Blocks", "22.4.8 SubAccountDetails <SubAcctDtls>", "22.4.8.3 TransactionOnSubAccount <TxOnSubAcct>"]
file_pages: [422]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.006.001.02"]
---

# 22.4.8.3 TransactionOnSubAccount <TxOnSubAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 422 to 422.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 422

```text
• Meaning When True: Yes
• Meaning When False: No
22.4.8.3  TransactionOnSubAccount <TxOnSubAcct>
Presence: [0..*]
Definition: Creation/cancellation of investment units on the books of the fund or its designated agent, as
a result of executing an investment fund order.
TransactionOnSubAccount <TxOnSubAcct> contains the following
InvestmentFundTransactionsByFund2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 422
   Name <Nm> [0..1] Text 423
   SupplementaryIdentification <SplmtryId> [0..1] Text 423
   SecuritiesForm <SctiesForm> [0..1] CodeSet 423
   ClassType <ClssTp> [0..1] Text 424
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 424
   TransactionDetails <TxDtls> [1..*] ± C9, C10 424
   BalanceByPage <BalByPg> [0..1] ± 426
22.4.8.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a security by an ISIN.
Approved by the Securities SEG on 27 January 2026 semt.006.001.02
StatementOfInvestmentFundTransactionsV02
Investment Funds - Maintenance 2025 - 2026 422 May 2026
```

