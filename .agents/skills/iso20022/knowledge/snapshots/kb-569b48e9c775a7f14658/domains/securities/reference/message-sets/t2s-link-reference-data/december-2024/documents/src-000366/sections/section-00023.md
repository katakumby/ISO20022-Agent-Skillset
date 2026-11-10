---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01"]
file_pages: [25]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.047.001.01"]
---

# 4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 25 to 25.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 25

```text
4 reda.047.001.01
SecurityCSDLinkStatusAdviceV01
4.1 MessageDefinition Functionality
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
Approved by the Securities SEG on 21 November 2024. reda.047.001.01 SecurityCSDLinkStatusAdviceV01
Target2-Securities - Link Reference Data 25 December 2024
```

