---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["10 reda.030.001.01 SecurityDeletionStatusAdviceV01"]
file_pages: [124]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.030.001.01"]
---

# 10 reda.030.001.01 SecurityDeletionStatusAdviceV01

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 124 to 124.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 124

```text
10 reda.030.001.01
SecurityDeletionStatusAdviceV01
10.1 MessageDefinition Functionality
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.030.001.01 SecurityDeletionStatusAdviceV01
Target2-Securities - Securities Reference Data 124 March 2024
```

