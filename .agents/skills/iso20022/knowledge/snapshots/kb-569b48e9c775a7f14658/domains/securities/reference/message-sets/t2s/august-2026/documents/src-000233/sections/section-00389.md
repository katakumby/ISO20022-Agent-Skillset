---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["21 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "21.4 Message Building Blocks", "21.4.1 Identification <Id>", "21.4.1.5 MessageRecipient <MsgRcpt>"]
file_pages: [498]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 21.4.1.5 MessageRecipient <MsgRcpt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 498 to 498.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 498

```text
21.4.1.5  MessageRecipient <MsgRcpt>
Presence: [0..1]
Definition: Party that is the final destination of the message, if other than the receiver.
MessageRecipient <MsgRcpt> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
21.4.2 Pagination <Pgntn>
Presence: [1..1]
Definition: Pagination of the message.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 2980 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 2980
   LastPageIndicator <LastPgInd> [1..1] Indicator 2980
21.4.3 ReportGeneralDetails <RptGnlDtls>
Presence: [1..1]
Definition: General characteristics related to the report information.
Impacted by: C21 "ReportNumberRule"
ReportGeneralDetails <RptGnlDtls> contains the following IntraBalanceReport5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportNumber <RptNb> [0..1] ± 499
   QueryReference <QryRef> [0..1] Text 499
   ReportIdentification <RptId> [0..1] Text 499
   ReportDateTime <RptDtTm> [0..1] ± 499
   ReportPeriod <RptPrd> [0..1] ± 500
   QueryType <QryTp> [0..1] CodeSet 500
   Frequency <Frqcy> [0..1] ± 500
   UpdateType <UpdTp> [1..1] ± 500
   ActivityIndicator <ActvtyInd> [1..1] Indicator 501
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 498 August 2026
```

