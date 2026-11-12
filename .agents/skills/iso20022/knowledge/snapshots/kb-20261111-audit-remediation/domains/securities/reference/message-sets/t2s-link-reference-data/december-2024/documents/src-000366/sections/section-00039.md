---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["6 reda.050.001.01 AccountLinkMaintenanceRequestV01"]
file_pages: [41]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.050.001.01"]
---

# 6 reda.050.001.01 AccountLinkMaintenanceRequestV01

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 41 to 41.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 41

```text
6 reda.050.001.01
AccountLinkMaintenanceRequestV01
6.1 MessageDefinition Functionality
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
Approved by the Securities SEG on 21 November 2024. reda.050.001.01
AccountLinkMaintenanceRequestV01
Target2-Securities - Link Reference Data 41 December 2024
```

