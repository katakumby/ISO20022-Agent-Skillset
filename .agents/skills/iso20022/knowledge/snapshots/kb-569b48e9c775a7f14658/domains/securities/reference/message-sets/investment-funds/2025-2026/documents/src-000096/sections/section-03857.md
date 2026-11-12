---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.42 Settlement Instruction"]
file_pages: [5146]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.42 Settlement Instruction

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5146 to 5146.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5146

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.42 Settlement Instruction
66.1.42.1  CashSettlement4
Definition: Cash settlement parties and accounts.
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
Investment Funds - Maintenance 2025 - 2026 5146 May 2026
```

