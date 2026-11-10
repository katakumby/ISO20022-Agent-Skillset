---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.11 ModificationScope41", "66.1.26.11.2 InvestmentPlan <InvstmtPlan>", "66.1.26.11.2.11 ModifiedCashSettlement <ModfdCshSttlm>"]
file_pages: [4750]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.11.2.11 ModifiedCashSettlement <ModfdCshSttlm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4750 to 4750.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4750

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
66.1.26.11.2.11  ModifiedCashSettlement <ModfdCshSttlm>
Presence: [0..8]
Definition: Cash settlement standing instruction associated to the investment plan and to be either
inserted or deleted.
ModifiedCashSettlement <ModfdCshSttlm> contains the following elements (see "CashSettlement4"
on page 5146 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 5147
   CashAccountDetails <CshAcctDtls> [0..*]  5147
     SettlementCurrency <SttlmCcy> [1..1] CodeSet C1 5148
     Identification <Id> [1..1] ± 5148
     AccountOwner <AcctOwnr> [0..1] ± 5148
     AccountServicer <AcctSvcr> [0..1] ± 5148
     AccountServicerBranch <AcctSvcrBrnch> [0..1] ± 5149
     AccountOwnerOtherIdentification <AcctOwnrOthrId> [0..*] ± 5149
     InvestmentAccountType <InvstmtAcctTp> [0..1] ± 5150
     CreditDebit <CdtDbt> [0..1] CodeSet 5150
     SettlementInstructionReason <SttlmInstrRsn> [0..1]  5150
{Or       Code <Cd> [1..1] CodeSet 5151
Or}       Proprietary <Prtry> [1..1] ± 5151
     CashAccountPurpose <CshAcctPurp> [0..1]  5152
{Or       Code <Cd> [1..1] CodeSet 5152
Or}       Proprietary <Prtry> [1..1] ± 5152
     CashAccountDesignation <CshAcctDsgnt> [0..1]  5153
{Or       Code <Cd> [1..1] CodeSet 5153
Or}       Proprietary <Prtry> [1..1] ± 5153
     DividendPercentage <DvddPctg> [0..1] Rate 5153
   OtherCashSettlementDetails <OthrCshSttlmDtls> [0..*] ± 5153
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4750 May 2026
```

