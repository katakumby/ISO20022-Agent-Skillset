---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07"]
file_pages: [291, 292]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15 reda.004.001.07 FundReferenceDataReportV07

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 291 to 292.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 291

```text
15 reda.004.001.07
FundReferenceDataReportV07
15.1 MessageDefinition Functionality
Scope
The FundReferenceDataReport message is sent by a report provider, for example, a fund promoter,
fund management company, transfer agent, or market data provider to the report recipient, for example,
a professional investor, investment fund distributor, market data provider, regulator or other interested
party, to provide the key reference data for financial instruments to facilitate trading. The message may
also include reporting data concerning product governance, such as target market data, and a
breakdown of the costs and fees.
Usage
A FundReferenceDataReport message should be prepared for each class of unit/share (for which an
individual ISIN should have been allocated), in respect of its "home" market. Each time the fund data
changes, the 'product provider' must provide the data to a product user, for example, the distributors, by
sending a new funds reference data report. A single message may contain more than one report. When
the FundReferenceDataReport message is sent to provide updated reference data, the message
overwrites the previously sent data.
The FundReferenceDataReport message may be used in various models or environments:
- in a standalone environment, for example, initiated by the Report Provider (fund promoter, fund
manager and / or reference data vendors) sent on a regular frequency, or when changes are needed.
- in a request / response environment, with the InvestmentFundReportRequest, for example, initiated by
report users (data vendors, professional investors, regulators or investment fund distributors) in
enabling the user to control the flow and updates of information.
- in a reference data vendor environment, for example, market infrastructure and reference data
providers may collate and store all fund reference data information centrally for access via database or
regular distribution information. A reference data vendor may assume the role of both report provider
and report user.
The FundReferenceDataReport message may be used to provide data concerning product governance,
such as target market data, and a breakdown of the costs and fees in the context of MiFID II, with
respect to the European MiFID Template (EMT).
Outline
The FundReferenceDataReportV07 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PreviousReference
Reference to a linked message that was previously sent.
C. RelatedReference
Reference to a linked message that was previously received.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 291 May 2026
```

## File page 292

```text
D. FundReferenceDataReportIdentification
Unique and unambiguous identifier for the fund reference data report, as assigned by the issuer of
the report.
E. Report
Fund reference data.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 292 May 2026
```

