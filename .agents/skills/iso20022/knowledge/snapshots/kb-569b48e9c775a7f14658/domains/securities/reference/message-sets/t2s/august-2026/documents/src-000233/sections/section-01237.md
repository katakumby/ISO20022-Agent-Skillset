---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["29 reda.008.001.01 SecurityCreationStatusAdviceV01"]
file_pages: [1753]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.008.001.01"]
---

# 29 reda.008.001.01 SecurityCreationStatusAdviceV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1753 to 1753.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1753

```text
29 reda.008.001.01
SecurityCreationStatusAdviceV01
29.1 MessageDefinition Functionality
SCOPE
An executing/servicing party sends a SecurityCreationStatusAdvice message to an instructing party to
report the status of a SecurityCreationRequest message previously sent by the instructing party.
The SecurityCreationStatusAdvice message may be sent as a response to the request of the instructing
party or not.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
Initiator: executing/servicing party.
Outline
The SecurityCreationStatusAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. FinancialInstrumentIdentification
Identification of the financial instrument.
C. ProcessingStatus
Represents the processing status.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.008.001.01 SecurityCreationStatusAdviceV01
Target2-Securities 1753 August 2026
```

