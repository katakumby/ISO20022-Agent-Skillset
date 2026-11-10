---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.42 Settlement Instruction", "66.1.42.2 CashSettlement3", "66.1.42.2.1 CashAccountDetails <CshAcctDtls>"]
file_pages: [5155]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.42.2.1 CashAccountDetails <CshAcctDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5155 to 5155.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5155

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccountDetails <CshAcctDtls> [0..*]  5155
     SettlementCurrency <SttlmCcy> [1..1] CodeSet C1 5156
     Identification <Id> [1..1] ± 5156
     AccountOwner <AcctOwnr> [0..1] ± 5157
     AccountServicer <AcctSvcr> [0..1] ± 5157
     AccountServicerBranch <AcctSvcrBrnch> [0..1] ± 5157
     AccountOwnerOtherIdentification <AcctOwnrOthrId> [0..*] ± 5158
     InvestmentAccountType <InvstmtAcctTp> [0..1] ± 5158
     CreditDebit <CdtDbt> [0..1] CodeSet 5158
     SettlementInstructionReason <SttlmInstrRsn> [0..1]  5159
{Or       Code <Cd> [1..1] CodeSet 5159
Or}       Proprietary <Prtry> [1..1] ± 5160
     CashAccountPurpose <CshAcctPurp> [0..1]  5160
{Or       Code <Cd> [1..1] CodeSet 5160
Or}       Proprietary <Prtry> [1..1] ± 5160
     CashAccountDesignation <CshAcctDsgnt> [0..1]  5161
{Or       Code <Cd> [1..1] CodeSet 5161
Or}       Proprietary <Prtry> [1..1] ± 5161
     DividendPercentage <DvddPctg> [0..1] Rate 5161
   OtherCashSettlementDetails <OthrCshSttlmDtls> [0..*] ± 5162
66.1.42.2.1  CashAccountDetails <CshAcctDtls>
Presence: [0..*]
Definition: Account to credit or debit. When this is an account to debit, this is for the payment of a
subscription to an investment fund, a savings plan payment, the purchase of securities or the payment
of charges. When this is an account to credit, this is for the payment of an amount as a result of a
redemption of investment fund units, the sale of securities, interest and dividend payments. A single
account may be specified for all cash movements on the account or cash accounts may be specified for
specific types of transactions on the account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5155 May 2026
```

