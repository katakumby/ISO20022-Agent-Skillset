---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.31 InvestmentPlan17", "66.1.26.31.11 CashSettlement <CshSttlm>"]
file_pages: [4797]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.31.11 CashSettlement <CshSttlm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4797 to 4797.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4797

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
66.1.26.31.11  CashSettlement <CshSttlm>
Presence: [0..8]
Definition: Cash settlement standing instruction associated to the investment plan.
CashSettlement <CshSttlm> contains the following elements (see "CashSettlement3" on page 5154
for details)
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
66.1.26.31.12  ContractReference <CtrctRef>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4797 May 2026
```

