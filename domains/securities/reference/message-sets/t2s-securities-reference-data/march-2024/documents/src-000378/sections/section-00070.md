---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["9 reda.029.001.01 SecurityMaintenanceStatusAdviceV01"]
file_pages: [119]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.029.001.01"]
---

# 9 reda.029.001.01 SecurityMaintenanceStatusAdviceV01

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 119 to 119.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 119

```text
9 reda.029.001.01
SecurityMaintenanceStatusAdviceV01
9.1 MessageDefinition Functionality
SCOPE
An executing/servicing party sends a SecurityMaintenanceStatusAdvice message to an instructing party
to report the status of a SecurityMaintencanceRequest message previously sent by the instructing
party.
The SecurityMaintenanceStatusAdvice message may be sent as a response to the request of the
instructing party or not.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
Initiator: executing/servicing party.
Outline
The SecurityMaintenanceStatusAdviceV01 MessageDefinition is composed of 4
MessageBuildingBlocks:
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
reda.029.001.01
SecurityMaintenanceStatusAdviceV01
Target2-Securities - Securities Reference Data 119 March 2024
```

