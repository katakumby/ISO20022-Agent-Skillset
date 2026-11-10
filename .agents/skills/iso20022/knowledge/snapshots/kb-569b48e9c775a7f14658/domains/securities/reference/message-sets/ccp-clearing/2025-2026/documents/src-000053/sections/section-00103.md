---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.2 Pagination <Pgntn>"]
file_pages: [134]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.2 Pagination <Pgntn>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 134 to 134.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 134

```text
StatementParameters <StmtParams> contains the following elements (see Statement86 on page 438
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatementIdentification <StmtId> [1..1] Text 438
   StatementDateAndTime <StmtDtAndTm> [1..1] ± 438
   UpdateType <UpdTp> [1..1] CodeSet 439
   Frequency <Frqcy> [1..1] CodeSet 439
   ReportNumber <RptNb> [0..1] Text 439
   ActivityIndicator <ActvtyInd> [1..1] Indicator 439
Constraints
• ReportNumberRule
(Rule)
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002, etc.
4.4.2 Pagination <Pgntn>
Presence: [1..1]
Definition: Page number of the message (within a statement) and continuation indicator to indicate that
the statement is to continue or that the message is the last page of the statement.
Pagination <Pgntn> contains the following elements (see Pagination1 on page 439 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 440
   LastPageIndicator <LastPgInd> [1..1] Indicator 440
4.4.3 ClearingMember <ClrMmb>
Presence: [1..1]
Definition: Provides the identification of the account owner, that is the clearing member (individual
clearing member or general clearing member).
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 134
```

