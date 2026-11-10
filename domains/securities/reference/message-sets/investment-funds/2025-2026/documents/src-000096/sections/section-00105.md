---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03"]
file_pages: [153]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.045.001.03"]
---

# 12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 153 to 153.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 153

```text
12 camt.045.001.03
FundDetailedConfirmedCashForecastReport
CancellationV03
12.1 MessageDefinition Functionality
Scope
A report provider, such as a transfer agent, sends the
FundDetailedConfirmedCashForecastReportCancellation messages to the report user, such as an
investment manager, fund accountant or any other interested party, to cancel a previously sent
FundDetailedConfirmedCashForecastReport.
Usage
The FundDetailedConfirmedCashForecastReportCancellation message is used to cancel an entire
FundDetailedConfirmedCashForecastReport message that was previously sent. This message must
contain the reference of the message to be cancelled.
This message may also contain details of the message to be cancelled, but this is not recommended.
Outline
The FundDetailedConfirmedCashForecastReportCancellationV03 MessageDefinition is composed of 6
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
Approved by the Securities SEG on 27 January 2026 camt.045.001.03
FundDetailedConfirmedCashForecastReportCancell
ationV03
Investment Funds - Maintenance 2025 - 2026 153 May 2026
```

