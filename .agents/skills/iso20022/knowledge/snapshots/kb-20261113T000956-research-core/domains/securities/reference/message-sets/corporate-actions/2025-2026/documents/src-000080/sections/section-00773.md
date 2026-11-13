---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.46 Statement72"]
file_pages: [966]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.46 Statement72

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 966 to 966.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 966

```text
16.1.15.46  Statement72
Definition: General characteristics related to a statement which reports information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatementType <StmtTp> [1..1] CodeSet 966
   ReportingType <RptgTp> [1..1] CodeSet 966
   StatementIdentification <StmtId> [1..1] Text 967
   InstructionAggregationPeriod <InstrAggtnPrd> [0..1] ± 967
   ReportNumber <RptNb> [0..1] Text 967
   StatementDateTime <StmtDtTm> [1..1] ± 967
   Frequency <Frqcy> [1..1] ± 967
   UpdateType <UpdTp> [1..1] ± 968
   ActivityIndicator <ActvtyInd> [1..1] Indicator 968
   NotificationDeadlinePeriod <NtfctnDdlnPrd> [0..1] ± 968
16.1.15.46.1  StatementType <StmtTp>
Presence: [1..1]
Definition: Indicates whether the statement is a balance only notification or if it includes missing
instructions only or all instructions.
Datatype: "CorporateActionStatementType2Code" on page 1204
CodeName Name Definition
MISS Missing Statement contains missing instructions.
ALLL All Statement contains all instructions.
BALO BalanceOnlyNotification Balance information with no instruction
details provided.
BALI BalanceInformation Balance information with instruction
details.
16.1.15.46.2  ReportingType <RptgTp>
Presence: [1..1]
Definition: Indicates whether the statement report on account holdings for corporate action events is for
single account/multiple events or multiple accounts/single event.
Datatype: "CorporateActionStatementReportingType1Code" on page 1204
CodeName Name Definition
MASE MultipleAccounts The reporting is for a single event and
for multiple accounts.
SAME MultipleEvents The reporting is for multiple events for a
single account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 966 February 2026
```

