---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.9 InvestmentAccount73", "66.1.24.9.14 LetterIntentDetails <LttrInttDtls>"]
file_pages: [4624]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.9.14 LetterIntentDetails <LttrInttDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4624 to 4624.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4624

```text
TaxReporting <TaxRptg> contains the following elements (see "TaxReporting3" on page 5213 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxationCountry <TaxtnCtry> [1..1] CodeSet C12 5214
   TaxRate <TaxRate> [0..1] Rate 5215
   TaxPayer <TaxPyer> [0..1] ± 5215
   TaxRecipient <TaxRcpt> [0..1] ± 5215
   CashAccountDetails <CshAcctDtls> [0..1]  5215
     SettlementCurrency <SttlmCcy> [1..1] CodeSet C1 5216
     Identification <Id> [1..1] ± 5216
     AccountOwner <AcctOwnr> [0..1] ± 5217
     AccountServicer <AcctSvcr> [0..1] ± 5217
     AccountServicerBranch <AcctSvcrBrnch> [0..1] ± 5217
     AccountOwnerOtherIdentification <AcctOwnrOthrId> [0..*] ± 5218
     InvestmentAccountType <InvstmtAcctTp> [0..1] ± 5218
     CreditDebit <CdtDbt> [0..1] CodeSet 5218
     SettlementInstructionReason <SttlmInstrRsn> [0..1]  5219
{Or       Code <Cd> [1..1] CodeSet 5219
Or}       Proprietary <Prtry> [1..1] ± 5220
     CashAccountPurpose <CshAcctPurp> [0..1]  5220
{Or       Code <Cd> [1..1] CodeSet 5220
Or}       Proprietary <Prtry> [1..1] ± 5220
     CashAccountDesignation <CshAcctDsgnt> [0..1]  5221
{Or       Code <Cd> [1..1] CodeSet 5221
Or}       Proprietary <Prtry> [1..1] ± 5221
     DividendPercentage <DvddPctg> [0..1] Rate 5221
   Description <Desc> [0..1] Text 5222
66.1.24.9.14  LetterIntentDetails <LttrInttDtls>
Presence: [0..1]
Definition: Details of the letter of intent.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4624 May 2026
```

