---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.50 Transfer Status"]
file_pages: [5257]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.50 Transfer Status

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5257 to 5257.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5257

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.50 Transfer Status
66.1.50.1  CancelledStatus13Choice
Definition: Reason for the cancelled status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5257
Or   Reason <Rsn> [1..1] CodeSet 5257
Or   ExtendedReason <XtndedRsn> [1..1] Text 5257
Or}   DataSourceScheme <DataSrcSchme> [1..1] ± 5258
66.1.50.1.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.50.1.2  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the cancelled status.
Datatype: "CancelledStatusReason3Code" on page 5281
CodeName Name Definition
CNTA CancelledByTransferAgent Transaction is cancelled by the transfer
agent.
CNCL CancelledByClient Transaction is cancelled by the client.
CNIN CancelledByIntermediary Transaction is cancelled by the
intermediary.
66.1.50.1.3  ExtendedReason <XtndedRsn>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5257 May 2026
```

