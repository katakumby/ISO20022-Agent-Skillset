---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["67 reda.051.001.01 AccountLinkStatusAdviceV01"]
file_pages: [2381]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.051.001.01"]
---

# 67 reda.051.001.01 AccountLinkStatusAdviceV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2381 to 2381.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2381

```text
67 reda.051.001.01
AccountLinkStatusAdviceV01
67.1 MessageDefinition Functionality
SCOPE:
The AccountLinkStatusAdvice message is sent by the executing/servicing party to the instructing party
to provide details about the processing of a request on account link reference data (create or update).
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish account link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE:
Initiator: executing/servicing party
When processing information is negative - a failure occurred in applying the changes the message
accordingly also delivers information about the reason why the creation or update could not be
processed.
When the processing is successfully performed, the message includes the related account link
identification.
Outline
The AccountLinkStatusAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. AccountLinkStatus
Represents the processing status.
C. AccountLinkIdentification
Provides a unique and unambiguous identification for the account link.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.051.001.01 AccountLinkStatusAdviceV01
Target2-Securities 2381 August 2026
```

