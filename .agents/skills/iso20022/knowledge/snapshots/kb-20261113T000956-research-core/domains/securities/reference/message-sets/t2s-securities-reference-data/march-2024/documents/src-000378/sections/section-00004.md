---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["2 reda.006.001.01 SecurityCreationRequestV01"]
file_pages: [8]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 2 reda.006.001.01 SecurityCreationRequestV01

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 8 to 8.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 8

```text
2 reda.006.001.01
SecurityCreationRequestV01
2.1 MessageDefinition Functionality
SCOPE
An instructing party sends a SecurityCreationRequest message to an executing/servicing party to
request the creation of financial instrument static details in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified a gap in the securities coverage of the
executing/servicing party. The instructing party needs this security to be set-up at the executing /
servicing party to perform its activities.
Initiator: instructing party.
Outline
The SecurityCreationRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. Security
Represents the financial instruments details.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities - Securities Reference Data 8 March 2024
```

