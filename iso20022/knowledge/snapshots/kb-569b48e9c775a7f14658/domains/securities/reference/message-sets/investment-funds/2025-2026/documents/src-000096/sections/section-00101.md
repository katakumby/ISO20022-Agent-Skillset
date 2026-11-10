---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["11 camt.044.001.03 FundConfirmedCashForecastReportCancellationV03"]
file_pages: [146]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.044.001.03"]
---

# 11 camt.044.001.03 FundConfirmedCashForecastReportCancellationV03

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 146 to 146.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 146

```text
11 camt.044.001.03
FundConfirmedCashForecastReportCancellat
ionV03
11.1 MessageDefinition Functionality
Scope
A report provider, such as a transfer agent, sends the FundConfirmedCashForecastReportCancellation
message to the report user, such as an investment manager or pricing agent, to cancel a previously
sent FundConfirmedCashForecastReport message.
Usage
The FundConfirmedCashForecastReportCancellation message is used to cancel an entire
FundConfirmedCashForecastReport message that was previously sent by the report provider. This
message must contain reference to the of the message being cancelled.
This message may also contain details of the message to be cancelled, but this is not recommended.
Outline
The FundConfirmedCashForecastReportCancellationV03 MessageDefinition is composed of 6
MessageBuildingBlocks:
A. MessageIdentification
Identifies the message.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. MessagePagination
Pagination of the message.
F. CashForecastReportToBeCancelled
The FundDetailedConfirmedCashForecastReport to be cancelled.
Approved by the Securities SEG on 27 January 2026 camt.044.001.03
FundConfirmedCashForecastReportCancellationV0
3
Investment Funds - Maintenance 2025 - 2026 146 May 2026
```

