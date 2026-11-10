---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["50 reda.030.001.01 SecurityDeletionStatusAdviceV01"]
file_pages: [2208]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.030.001.01"]
---

# 50 reda.030.001.01 SecurityDeletionStatusAdviceV01

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2208 to 2208.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2208

```text
50 reda.030.001.01
SecurityDeletionStatusAdviceV01
50.1 MessageDefinition Functionality
SCOPE
An executing/servicing party sends a SecurityDeletionStatusAdvice message to an instructing party to
report the status of a SecurityDeletionRequest message previously sent by the instructing party.
The SecurityDeletionStatusAdvice message is sent as a response to the request of the instructing
party.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
Initiator: executing/servicing party.
Outline
The SecurityDeletionStatusAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
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
reda.030.001.01 SecurityDeletionStatusAdviceV01
Target2-Securities 2208 August 2026
```

