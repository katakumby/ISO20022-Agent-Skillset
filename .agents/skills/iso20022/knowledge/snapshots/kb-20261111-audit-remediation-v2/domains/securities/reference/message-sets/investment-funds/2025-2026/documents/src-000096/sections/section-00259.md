---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["16 reda.005.001.03 InvestmentFundReportRequestV03"]
file_pages: [365]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.005.001.03"]
---

# 16 reda.005.001.03 InvestmentFundReportRequestV03

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 365 to 365.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 365

```text
16 reda.005.001.03
InvestmentFundReportRequestV03
16.1 MessageDefinition Functionality
Scope
The InvestmentFundReportRequest message is sent by a report user, for example, a professional
investor, investment fund distributor, market data provider, regulator or other interested party to the
report provider, for example, a fund promoter, fund management company, transfer agent, or market
data provider to request a report.
The Investment Fund Report Request message can be used to request one or many fund reference
data report messages.
Usage
If the InvestmentFundReportRequest message is used to request a fund reference data report then the
request can specify the financial instrument for which the report is requested. Other appropriate
parameters can also be included. It is also possible to indicate that the request is an open request, that
is, there is no specific criteria for the report requested. For example, a request for a fund reference data
report that is specified as "no criteria" means that the request is a request for a reference data report
messages for all funds.
Outline
The InvestmentFundReportRequestV03 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PreviousReference
Reference to a linked message that was previously sent.
C. RelatedReference
Reference to a linked message that was previously received.
D. ReportRequest
Parameters for which the report is requested.
Approved by the Securities SEG on 27 January 2026 reda.005.001.03
InvestmentFundReportRequestV03
Investment Funds - Maintenance 2025 - 2026 365 May 2026
```

