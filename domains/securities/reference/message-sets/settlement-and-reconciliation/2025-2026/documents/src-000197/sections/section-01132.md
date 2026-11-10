---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.41 RateOrName1Choice", "35.1.16.41.2 RateName <RateNm>"]
file_pages: [1577]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.41.2 RateName <RateNm>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1577 to 1577.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1577

```text
Rate <Rate> contains the following elements (see "Rate2" on page 1748 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 1748
   Rate <Rate> [1..1] Rate 1749
Constraints
• SignRule
When Sign is present, rate must not be zero.
35.1.16.41.2  RateName <RateNm>
Presence: [1..1]
Definition: Pricing expressed as a rate name.
RateName <RateNm> contains the following elements (see "RateName1" on page 1747 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [0..1] Text 1747
   RateName <RateNm> [1..1] Text 1747
35.1.16.42  Statement64
Definition: Characteristics of the statement.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportNumber <RptNb> [0..1] ± 1578
   QueryReference <QryRef> [0..1] Text 1578
   StatementIdentification <StmtId> [0..1] Text 1578
   StatementDateTime <StmtDtTm> [1..1] ± 1578
   Frequency <Frqcy> [0..1] ± 1578
   UpdateType <UpdTp> [0..1] ± 1579
   StatementStructure <StmtStr> [1..1] CodeSet 1579
   ActivityIndicator <ActvtyInd> [1..1] Indicator 1579
Constraints
• ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports (UpdateType:
DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1577 March 2026
```

