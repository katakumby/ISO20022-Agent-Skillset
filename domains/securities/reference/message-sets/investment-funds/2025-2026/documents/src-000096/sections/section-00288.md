---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["20 semt.004.001.02 CustodyStatementOfHoldingsCancellationV02", "20.4 Message Building Blocks", "20.4.5 StatementToBeCancelled <StmtToBeCanc>"]
file_pages: [402]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.004.001.02"]
---

# 20.4.5 StatementToBeCancelled <StmtToBeCanc>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 402 to 402.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 402

```text
20.4.5 StatementToBeCancelled <StmtToBeCanc>
Presence: [0..1]
Definition: The Custody Statement of Holdings message to cancel.
Impacted by: C9 "BalanceForAccountOrSubAccountDetailsRule"
StatementToBeCancelled <StmtToBeCanc> contains the following elements (see
"CustodyStatementOfHoldings2" on page 4382 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatementGeneralDetails <StmtGnlDtls> [0..1]  4383
     Reference <Ref> [1..1] Text 4384
     StatementDateTime <StmtDtTm> [1..1] ± 4384
     CreationDateTime <CreDtTm> [0..1] ± 4384
     Frequency <Frqcy> [1..1] ± 4384
     UpdateType <UpdTp> [1..1] ± 4385
     ActivityIndicator <ActvtyInd> [1..1] Indicator 4385
     StatementBasis <StmtBsis> [1..1] ± 4385
     ReportNumber <RptNb> [0..1] Text 4385
   AccountDetails <AcctDtls> [0..1] ± 4386
   BalanceForAccount <BalForAcct> [0..*] ± C1, C8,
C5
4386
   SubAccountDetails <SubAcctDtls> [0..*] ± 4388
   TotalValues <TtlVals> [0..1] ± 4388
   Extension <Xtnsn> [0..*] ± C16 4388
Constraints
• BalanceForAccountOrSubAccountDetailsRule
If StatementGeneralDetails/ActivityIndicator is "true" or "1" (Yes), then either BalanceForAccount or
SubAccountDetails is mandatory. If StatementGeneralDetails/ActivityIndicator is "false" or "0" (No),
then BalanceForAccount and SubAccountDetails may be present.
Approved by the Securities SEG on 27 January 2026 semt.004.001.02
CustodyStatementOfHoldingsCancellationV02
Investment Funds - Maintenance 2025 - 2026 402 May 2026
```

