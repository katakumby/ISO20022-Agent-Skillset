---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["66 reda.050.001.01 AccountLinkMaintenanceRequestV01"]
file_pages: [2375]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.050.001.01"]
---

# 66 reda.050.001.01 AccountLinkMaintenanceRequestV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2375 to 2375.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2375

```text
66 reda.050.001.01
AccountLinkMaintenanceRequestV01
66.1 MessageDefinition Functionality
SCOPE:
The AccountLinkMaintenanceRequest message is sent by the instructing party to the executing/
servicing party to request for the maintenance of an account link in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish account link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE:
The request is sent when the instructing party identified a gap in the account link coverage of the
executing/servicing party. The instructing party needs this account link to be maintained at the
executing /servicing party to perform its activities.
Initiator: instructing party.
Outline
The AccountLinkMaintenanceRequestV01 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. AccountLinkIdentification
Provides a unique and unambiguous identification for the account link.
C. Update
Provides data that needs to be maintained.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.050.001.01
AccountLinkMaintenanceRequestV01
Target2-Securities 2375 August 2026
```

