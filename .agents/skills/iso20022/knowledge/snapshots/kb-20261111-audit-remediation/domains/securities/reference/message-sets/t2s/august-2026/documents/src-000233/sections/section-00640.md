---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01"]
file_pages: [825]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28 reda.007.001.01 SecurityMaintenanceRequestV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 825 to 825.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 825

```text
28 reda.007.001.01
SecurityMaintenanceRequestV01
28.1 MessageDefinition Functionality
SCOPE
An instructing party sends a SecurityMaintenanceRequest message to an executing/servicing party to
request the maintenance of financial instrument details in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified a gap in the security data within the executing/
servicing party system. The instructing party needs this security to be updated at the executing /
servicing party to perform its activities.
Initiator: instructing party.
Outline
The SecurityMaintenanceRequestV01 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. UpdateType
Request to maintain data's of a security.
C. UpdateReason
Reason for the update of a security.
D. FinancialInstrumentIdentification
Identification of the financial instrument.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 825 August 2026
```

