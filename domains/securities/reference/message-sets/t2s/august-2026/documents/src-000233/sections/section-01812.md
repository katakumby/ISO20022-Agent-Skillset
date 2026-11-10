---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.2 ReportGeneralDetails <RptGnlDtls>", "72.4.2.1 ReportIdentification <RptId>"]
file_pages: [2487]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.2.1 ReportIdentification <RptId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2487 to 2487.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2487

```text
Constraints
• ReportIdentificationRule
If Long number (Exact5NumericText) is used, then the report must be a delta reports (UpdateType:
DELT).
If the report has multiple pages, then the ReportIdentification must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different report identifications. For example, a daily report sent on
day 1 would have ReportIdentification 001, on day 2, 002, etc.
72.4.2.1  ReportIdentification <RptId>
Presence: [0..1]
Definition: Reference common to all pages of a report.
Datatype: "Max35Text" on page 3328
72.4.2.2  QueryReference <QryRef>
Presence: [0..1]
Definition: Identification of the SecuritiesStatementQuery message sent to request this statement.
Datatype: "Max35Text" on page 3328
72.4.2.3  QueryType <QryTp>
Presence: [1..1]
Definition: Defines the type of query.
Datatype: "SettlementQueryType1Code" on page 3300
CodeName Name Definition
INST Instruction Queries settlement instructions based on
criteria excluding statuses.
STTS Status Queries settlement instructions based on
criteria that includes statuses.
STPD StatusPeriod Queries settlement instructions based on
criteria that includes statuses during a
period.
72.4.2.4  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2487 August 2026
```

