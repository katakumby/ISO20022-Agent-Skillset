---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks"]
file_pages: [186]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4 Message Building Blocks

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 186 to 186.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 186

```text
C15 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
6.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
6.4.1 ReportPagination <RptPgntn>
Presence: [0..1]
Definition: Provides details on the page number of the report.
Usage: The pagination of the report is only allowed when agreed between the parties.
ReportPagination <RptPgntn> contains the following elements (see "Pagination1" on page 363 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 363
   LastPageIndicator <LastPgInd> [1..1] Indicator 363
6.4.2 ReportGeneralDetails <RptGnlDtls>
Presence: [1..1]
Definition: Provides general information on the report.
Impacted by: C14 "ReportDatePeriodPresenceRule"
ReportGeneralDetails <RptGnlDtls> contains the following PenaltyReport1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportIdentification <RptId> [1..1] Text 187
   ReportDate <RptDt> [0..1] ± 187
   ReportPeriod <RptPrd> [0..1] ± 187
   Frequency <Frqcy> [0..1] ± 187
   PenaltyListType <PnltyListTp> [0..1]  188
{Or     Code <Cd> [1..1] CodeSet 188
Or}     Proprietary <Prtry> [1..1] ± 188
   UpdateType <UpdTp> [0..1] ± 189
   ActivityIndicator <ActvtyInd> [1..1] Indicator 189
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 186 March 2026
```

