---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01"]
file_pages: [2359]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.047.001.01"]
---

# 64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2359 to 2359.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2359

```text
64 reda.047.001.01
SecurityCSDLinkStatusAdviceV01
64.1 MessageDefinition Functionality
SCOPE
An executing/servicing party sends a SecurityCSDLinkStatusAdvice message to an instructing party to
report the status of a SecurityCSDLink Request message previously sent by the instructing party.
The SecurityCSDLinkStatusAdvice message may be sent as a response to the request of the
instructing party or not.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
Initiator: executing/servicing party.
Outline
The SecurityCSDLinkStatusAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SecurityCSDLinkStatus
Represents the processing status.
C. SecurityCSDLinkIdentification
Provides a unique and unambiguous identification for the Security CSD Link.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.047.001.01 SecurityCSDLinkStatusAdviceV01
Target2-Securities 2359 August 2026
```

