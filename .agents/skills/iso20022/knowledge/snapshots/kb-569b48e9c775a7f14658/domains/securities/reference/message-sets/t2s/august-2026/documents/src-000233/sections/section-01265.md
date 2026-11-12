---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01"]
file_pages: [1784]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32 reda.012.001.01 SecurityReportV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1784 to 1784.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1784

```text
32 reda.012.001.01
SecurityReportV01
32.1 MessageDefinition Functionality
SCOPE
An executing/servicing party sends a SecurityReport message to an instructing party to advise the last
known image of securities data's.
The report may be sent upon request (for example a query) of the instructing party or push by the
executing/servicing party.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
Initiator: executing/servicing party.
Outline
The SecurityReportV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Point to point reference elements, as assigned by the instructing party, to unambiguously identify
the report message.
B. Pagination
Provides details on the page number of the message.
C. SecurityReportOrError
Provides the financial instruments details or error raised during the generation of the report.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1784 August 2026
```

