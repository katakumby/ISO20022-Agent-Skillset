---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["19 camt.081.001.02 IntraBalanceMovementModificationReportV02", "19.4 Message Building Blocks", "19.4.2 Pagination <Pgntn>"]
file_pages: [444]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 19.4.2 Pagination <Pgntn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 444 to 444.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 444

```text
MessageRecipient <MsgRcpt> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
19.4.2 Pagination <Pgntn>
Presence: [1..1]
Definition: Pagination of the message.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 2980 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 2980
   LastPageIndicator <LastPgInd> [1..1] Indicator 2980
19.4.3 ReportGeneralDetails <RptGnlDtls>
Presence: [1..1]
Definition: General characteristics related to the report information.
Impacted by: C23 "ReportNumberRule"
ReportGeneralDetails <RptGnlDtls> contains the following IntraBalanceReport5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportNumber <RptNb> [0..1] ± 445
   QueryReference <QryRef> [0..1] Text 445
   ReportIdentification <RptId> [0..1] Text 445
   ReportDateTime <RptDtTm> [0..1] ± 445
   ReportPeriod <RptPrd> [0..1] ± 445
   QueryType <QryTp> [0..1] CodeSet 446
   Frequency <Frqcy> [0..1] ± 446
   UpdateType <UpdTp> [1..1] ± 446
   ActivityIndicator <ActvtyInd> [1..1] Indicator 446
Constraints
• ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports (UpdateType:
DELT).
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 444 August 2026
```

