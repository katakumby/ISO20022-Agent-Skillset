---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["21 semt.005.001.02 AccountingStatementOfHoldingsCancellationV02", "21.4 Message Building Blocks", "21.4.2 PreviousReference <PrvsRef>"]
file_pages: [406, 407]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.005.001.02"]
---

# 21.4.2 PreviousReference <PrvsRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 406 to 407.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 406

```text
21.4.2 PreviousReference <PrvsRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference2" on
page 4538 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4538
   ReferenceIssuer <RefIssr> [0..1] ± 4538
   MessageName <MsgNm> [0..1] Text 4538
21.4.3 RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference2" on
page 4538 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4538
   ReferenceIssuer <RefIssr> [0..1] ± 4538
   MessageName <MsgNm> [0..1] Text 4538
21.4.4 MessagePagination <MsgPgntn>
Presence: [1..1]
Definition: Pagination of the message.
MessagePagination <MsgPgntn> contains the following elements (see "Pagination" on page 4833 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 4833
   LastPageIndicator <LastPgInd> [1..1] Indicator 4833
21.4.5 StatementToBeCancelled <StmtToBeCanc>
Presence: [0..1]
Definition: The Accounting Statement of Holdings message to cancel.
Impacted by: C7 "BalanceForAccountOrSubAccountDetailsRule"
Approved by the Securities SEG on 27 January 2026 semt.005.001.02
AccountingStatementOfHoldingsCancellationV02
Investment Funds - Maintenance 2025 - 2026 406 May 2026
```

## File page 407

```text
StatementToBeCancelled <StmtToBeCanc> contains the following elements (see
"AccountingStatementOfHoldings2" on page 4401 for details)
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
Approved by the Securities SEG on 27 January 2026 semt.005.001.02
AccountingStatementOfHoldingsCancellationV02
Investment Funds - Maintenance 2025 - 2026 407 May 2026
```

