---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["7 reda.012.001.01 SecurityReportV01"]
file_pages: [94]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 7 reda.012.001.01 SecurityReportV01

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 94 to 94.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 94

```text
7 reda.012.001.01
SecurityReportV01
7.1 MessageDefinition Functionality
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 94 March 2024
```

