---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01"]
file_pages: [17]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.046.001.01"]
---

# 3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01

Source: [src-000366](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 17 to 17.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 17

```text
3 reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
3.1 MessageDefinition Functionality
SCOPE
An instructing party sends a SecurityCSDLinkMaintenanceRequest message to an executing/servicing
party to request the maintenance of the link between a financial instrument and a CSD in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified a gap in the security CSD Link coverage of the
executing/servicing party. The instructing party needs this security to be maintained at the executing /
servicing party to perform its activities.
Initiator: instructing party.
Outline
The SecurityCSDLinkMaintenanceRequestV01 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SecurityCSDLinkIdentification
Provides a unique and unambiguous identification for the Security CSD Link.
C. Update
Provides data that needs to be maintained.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 21 November 2024. reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
Target2-Securities - Link Reference Data 17 December 2024
```

