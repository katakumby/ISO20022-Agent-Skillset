---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks"]
file_pages: [2768]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2768 to 2768.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2768

```text
C15 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
81.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
81.4.1 ReportPagination <RptPgntn>
Presence: [0..1]
Definition: Provides details on the page number of the report.
Usage: The pagination of the report is only allowed when agreed between the parties.
ReportPagination <RptPgntn> contains the following elements (see "Pagination1" on page 2980 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 2980
   LastPageIndicator <LastPgInd> [1..1] Indicator 2980
81.4.2 ReportGeneralDetails <RptGnlDtls>
Presence: [1..1]
Definition: Provides general information on the report.
Impacted by: C14 "ReportDatePeriodPresenceRule"
ReportGeneralDetails <RptGnlDtls> contains the following PenaltyReport1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportIdentification <RptId> [1..1] Text 2769
   ReportDate <RptDt> [0..1] ± 2769
   ReportPeriod <RptPrd> [0..1] ± 2769
   Frequency <Frqcy> [0..1] ± 2769
   PenaltyListType <PnltyListTp> [0..1]  2770
{Or     Code <Cd> [1..1] CodeSet 2770
Or}     Proprietary <Prtry> [1..1] ± 2770
   UpdateType <UpdTp> [0..1] ± 2771
   ActivityIndicator <ActvtyInd> [1..1] Indicator 2771
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2768 August 2026
```

