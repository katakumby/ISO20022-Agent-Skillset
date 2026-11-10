---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.13 AccountingStatementOfHoldings2", "66.1.5.13.1 StatementGeneralDetails <StmtGnlDtls>"]
file_pages: [4402]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.13.1 StatementGeneralDetails <StmtGnlDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4402 to 4402.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4402

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatementGeneralDetails <StmtGnlDtls> [0..1]  4402
     Reference <Ref> [1..1] Text 4403
     StatementDateTime <StmtDtTm> [1..1] ± 4403
     CreationDateTime <CreDtTm> [0..1] ± 4403
     Frequency <Frqcy> [1..1] ± 4404
     UpdateType <UpdTp> [1..1] ± 4404
     ActivityIndicator <ActvtyInd> [1..1] Indicator 4404
     StatementBasis <StmtBsis> [1..1] ± 4404
     ReportNumber <RptNb> [0..1] Text 4404
     AuditedIndicator <AudtdInd> [1..1] Indicator 4405
   AccountDetails <AcctDtls> [0..1] ± 4405
   BalanceForAccount <BalForAcct> [0..*] ± C1, C6 4405
   SubAccountDetails <SubAcctDtls> [0..*] ± 4406
   TotalValues <TtlVals> [0..1] ± 4407
   Extension <Xtnsn> [0..*] ± C16 4407
Constraints
• BalanceForAccountOrSubAccountDetailsRule
If StatementGeneralDetails/ActivityIndicator is "true" or "1" (Yes), then either BalanceForAccount or
SubAccountDetails is mandatory. If StatementGeneralDetails/ActivityIndicator is "false" or "0" (No),
then BalanceForAccount and SubAccountDetails may be present.
66.1.5.13.1  StatementGeneralDetails <StmtGnlDtls>
Presence: [0..1]
Definition: General information related to the custody statement of holdings that is being cancelled.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4402 May 2026
```

