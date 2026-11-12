---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["2 acmt.001.001.08 AccountOpeningInstructionV08", "2.4 Message Building Blocks", "2.4.13 ServiceLevelAgreement <SvcLvlAgrmt>"]
file_pages: [35]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.001.001.08"]
---

# 2.4.13 ServiceLevelAgreement <SvcLvlAgrmt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 35 to 35.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 35

```text
Definition: Cash settlement standing instruction associated to transactions on the account.
CashSettlement <CshSttlm> contains the following elements (see "CashSettlement3" on page 5154 for
details)
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
2.4.13 ServiceLevelAgreement <SvcLvlAgrmt>
Presence: [0..30]
Definition: Identifies documents to be provided for the account opening.
Approved by the Securities SEG on 27 January 2026 acmt.001.001.08 AccountOpeningInstructionV08
Investment Funds - Maintenance 2025 - 2026 35 May 2026
```

