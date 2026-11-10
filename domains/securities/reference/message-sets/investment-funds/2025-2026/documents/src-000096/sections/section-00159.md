---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.6 CancellationIdentification <CxlId>"]
file_pages: [232]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.6 CancellationIdentification <CxlId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 232 to 232.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 232

```text
14.4.3 PreviousReference <PrvsRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
14.4.4 MessagePagination <MsgPgntn>
Presence: [1..1]
Definition: Pagination of the message.
MessagePagination <MsgPgntn> contains the following elements (see "Pagination1" on page 4817 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 4817
   LastPageIndicator <LastPgInd> [1..1] Indicator 4817
14.4.5 PriceReportIdentification <PricRptId>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the price report, as assigned by the reporting party.
Datatype: "Max35Text" on page 5403
14.4.6 CancellationIdentification <CxlId>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the cancellation of the previous price report, as
assigned by the reporting party.
Datatype: "Max35Text" on page 5403
14.4.7 CancellationReason <CxlRsn>
Presence: [0..1]
Definition: Reason for the cancellation.
Datatype: "Max350Text" on page 5403
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 232 May 2026
```

