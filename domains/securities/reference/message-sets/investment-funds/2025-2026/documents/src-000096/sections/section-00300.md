---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02", "22.4 Message Building Blocks", "22.4.7 TransactionOnAccount <TxOnAcct>"]
file_pages: [416]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.006.001.02"]
---

# 22.4.7 TransactionOnAccount <TxOnAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 416 to 416.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 416

```text
22.4.7 TransactionOnAccount <TxOnAcct>
Presence: [0..*]
Definition: Creation/cancellation of investment units on the books of the fund or its designated agent, as
a result of executing an investment fund order.
TransactionOnAccount <TxOnAcct> contains the following InvestmentFundTransactionsByFund2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 416
   Name <Nm> [0..1] Text 417
   SupplementaryIdentification <SplmtryId> [0..1] Text 417
   SecuritiesForm <SctiesForm> [0..1] CodeSet 417
   ClassType <ClssTp> [0..1] Text 418
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 418
   TransactionDetails <TxDtls> [1..*] ± C9, C10 418
   BalanceByPage <BalByPg> [0..1] ± 420
22.4.7.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a security by an ISIN.
Approved by the Securities SEG on 27 January 2026 semt.006.001.02
StatementOfInvestmentFundTransactionsV02
Investment Funds - Maintenance 2025 - 2026 416 May 2026
```

