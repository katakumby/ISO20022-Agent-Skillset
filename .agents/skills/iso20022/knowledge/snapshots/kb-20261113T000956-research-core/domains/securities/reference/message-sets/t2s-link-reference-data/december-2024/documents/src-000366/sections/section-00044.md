---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["7 reda.051.001.01 AccountLinkStatusAdviceV01"]
file_pages: [47]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.051.001.01"]
---

# 7 reda.051.001.01 AccountLinkStatusAdviceV01

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 47 to 47.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 47

```text
7 reda.051.001.01
AccountLinkStatusAdviceV01
7.1 MessageDefinition Functionality
SCOPE:
The AccountLinkStatusAdvice message is sent by the executing/servicing party to the instructing party
to provide details about the processing of a request on account link reference data (create or update).
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish account link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE:
Initiator: executing/servicing party
When processing information is negative - a failure occurred in applying the changes the message
accordingly also delivers information about the reason why the creation or update could not be
processed.
When the processing is successfully performed, the message includes the related account link
identification.
Outline
The AccountLinkStatusAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. AccountLinkStatus
Represents the processing status.
C. AccountLinkIdentification
Provides a unique and unambiguous identification for the account link.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 21 November 2024. reda.051.001.01 AccountLinkStatusAdviceV01
Target2-Securities - Link Reference Data 47 December 2024
```

