---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "7.4 Message Building Blocks", "7.4.2 ReportGeneralDetails <RptGnlDtls>", "7.4.2.2 QueryReference <QryRef>"]
file_pages: [151]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 7.4.2.2 QueryReference <QryRef>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 151 to 151.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 151

```text
ReportNumber <RptNb> contains one of the following elements (see "Number3Choice" on page 228
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 229
Or}   Long <Lng> [1..1] Text 229
7.4.2.2  QueryReference <QryRef>
Presence: [0..1]
Definition: Identification of the settlement and intra-position query message sent to request this report.
Datatype: "Max35Text" on page 345
7.4.2.3  ReportIdentification <RptId>
Presence: [0..1]
Definition: Reference common to all pages of a statement.
Datatype: "Max35Text" on page 345
7.4.2.4  ReportDateTime <RptDtTm>
Presence: [0..1]
Definition: Date and time when the report was created.
ReportDateTime <RptDtTm> contains one of the following elements (see "DateAndDateTime2Choice"
on page 204 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 204
Or}   DateTime <DtTm> [1..1] DateTime 204
7.4.2.5  ReportPeriod <RptPrd>
Presence: [0..1]
Definition: Period for the statement.
ReportPeriod <RptPrd> contains one of the following elements (see "Period7Choice" on page 200 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 200
Or}   FromDateToDate <FrDtToDt> [1..1] ± 201
7.4.2.6  QueryType <QryTp>
Presence: [0..1]
Definition: Defines the type of query.
Approved by the Securities SEG on 21 August 2025 semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities - Settlement Restrictions 151 September 2025
```

