---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["62 reda.045.001.01 SecurityCSDLinkCreationRequestV01"]
file_pages: [2340]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.045.001.01"]
---

# 62 reda.045.001.01 SecurityCSDLinkCreationRequestV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2340 to 2340.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2340

```text
62 reda.045.001.01
SecurityCSDLinkCreationRequestV01
62.1 MessageDefinition Functionality
SCOPE
An instructing party sends a SecurityCSDLinkCreationRequest message to an executing/servicing party
to request the creation of the link between a financial instrument and a CSD in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified a gap in the security CSD Link coverage of the
executing/servicing party. The instructing party needs this security CSD Link to be set-up at the
executing /servicing party to perform its activities.
Initiator: instructing party.
Outline
The SecurityCSDLinkCreationRequestV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SecurityCSDLink
This Securities CSD Link logical entity shall assign a security to a CSD in T2S in order to define the
eligibility of the instrument for settlement in that CSD. An attribute within this entity shall specify
which CSD is responsible for maintaining the instrument static data.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.045.001.01
SecurityCSDLinkCreationRequestV01
Target2-Securities 2340 August 2026
```

