---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["36 reda.016.001.01 PartyStatusAdviceV01"]
file_pages: [2072]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.016.001.01"]
---

# 36 reda.016.001.01 PartyStatusAdviceV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2072 to 2072.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2072

```text
36 reda.016.001.01
PartyStatusAdviceV01
36.1 MessageDefinition Functionality
Scope:
The PartyStatusAdvice message is sent by the executing party to the instructing party to provide details
about the processing of a request on party reference data (create or update).
Usage:
When processing information is negative - a failure occurred in applying the changes the message
accordingly also delivers information about the reason why the creation or update could not be
processed.
When processing is successfully performed, the message includes the related party identification.
Outline
The PartyStatusAdviceV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. PartyStatus
Status of the party involved in the originating message.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.016.001.01 PartyStatusAdviceV01
Target2-Securities 2072 August 2026
```

