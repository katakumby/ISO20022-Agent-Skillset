---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.42 Settlement Instruction", "66.1.42.1 CashSettlement4", "66.1.42.1.1 ModificationScopeIndication <ModScpIndctn>"]
file_pages: [5147]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.42.1.1 ModificationScopeIndication <ModScpIndctn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5147 to 5147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5147

```text
66.1.42.1.1  ModificationScopeIndication <ModScpIndctn>
Presence: [1..1]
Definition: Specifies the type of modification to be applied.
Datatype: "DataModification2Code" on page 5293
CodeName Name Definition
INSE InsertNewDataSet Insert a new set of data.
DELT DeleteDataSet Delete an existing set of data.
66.1.42.1.2  CashAccountDetails <CshAcctDtls>
Presence: [0..*]
Definition: Account to credit or debit. When this is an account to debit, this is for the payment of a
subscription to an investment fund, a savings plan payment, the purchase of securities or the payment
of charges. When this is an account to credit, this is for the payment of an amount as a result of a
redemption of investment fund units, the sale of securities, interest and dividend payments. A single
account may be specified for all cash movements on the account or cash accounts may be specified for
specific types of transactions on the account.
CashAccountDetails <CshAcctDtls> contains the following CashAccount204 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementCurrency <SttlmCcy> [1..1] CodeSet C1 5148
   Identification <Id> [1..1] ± 5148
   AccountOwner <AcctOwnr> [0..1] ± 5148
   AccountServicer <AcctSvcr> [0..1] ± 5148
   AccountServicerBranch <AcctSvcrBrnch> [0..1] ± 5149
   AccountOwnerOtherIdentification <AcctOwnrOthrId> [0..*] ± 5149
   InvestmentAccountType <InvstmtAcctTp> [0..1] ± 5150
   CreditDebit <CdtDbt> [0..1] CodeSet 5150
   SettlementInstructionReason <SttlmInstrRsn> [0..1]  5150
{Or     Code <Cd> [1..1] CodeSet 5151
Or}     Proprietary <Prtry> [1..1] ± 5151
   CashAccountPurpose <CshAcctPurp> [0..1]  5152
{Or     Code <Cd> [1..1] CodeSet 5152
Or}     Proprietary <Prtry> [1..1] ± 5152
   CashAccountDesignation <CshAcctDsgnt> [0..1]  5153
{Or     Code <Cd> [1..1] CodeSet 5153
Or}     Proprietary <Prtry> [1..1] ± 5153
   DividendPercentage <DvddPctg> [0..1] Rate 5153
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5147 May 2026
```

