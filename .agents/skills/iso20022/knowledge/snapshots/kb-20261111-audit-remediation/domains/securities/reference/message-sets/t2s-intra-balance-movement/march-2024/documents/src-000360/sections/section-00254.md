---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["14 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "14.4 Message Building Blocks", "14.4.1 Identification <Id>", "14.4.1.5 MessageRecipient <MsgRcpt>"]
file_pages: [307]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 14.4.1.5 MessageRecipient <MsgRcpt>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 307 to 307.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 307

```text
14.4.1.5  MessageRecipient <MsgRcpt>
Presence: [0..1]
Definition: Party that is the final destination of the message, if other than the receiver.
MessageRecipient <MsgRcpt> contains the following elements (see "PartyIdentification136" on
page 417 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 418
   LEI <LEI> [0..1] IdentifierSet 418
14.4.2 Pagination <Pgntn>
Presence: [1..1]
Definition: Pagination of the message.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 412 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 412
   LastPageIndicator <LastPgInd> [1..1] Indicator 412
14.4.3 ReportGeneralDetails <RptGnlDtls>
Presence: [1..1]
Definition: General characteristics related to the report information.
Impacted by: C21 "ReportNumberRule"
ReportGeneralDetails <RptGnlDtls> contains the following IntraBalanceReport5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportNumber <RptNb> [0..1] ± 308
   QueryReference <QryRef> [0..1] Text 308
   ReportIdentification <RptId> [0..1] Text 308
   ReportDateTime <RptDtTm> [0..1] ± 308
   ReportPeriod <RptPrd> [0..1] ± 309
   QueryType <QryTp> [0..1] CodeSet 309
   Frequency <Frqcy> [0..1] ± 309
   UpdateType <UpdTp> [1..1] ± 309
   ActivityIndicator <ActvtyInd> [1..1] Indicator 310
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
307 March 2024
```

