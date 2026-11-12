---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["26 head.002.001.01 BusinessFileHeaderV01"]
file_pages: [614]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.002.001.01"]
---

# 26 head.002.001.01 BusinessFileHeaderV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 614 to 614.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 614

```text
26 head.002.001.01
BusinessFileHeaderV01
26.1 MessageDefinition Functionality
The Business File Header contains information about the parties involved in the file exchange, as well
as information about the content and its structure.
The Business File headers has four major functions:
- Provides information about the sender of the file.
- Identifies the file exchanged: each file must have a unique File Identifier.
- Describes the type of message(s) exchanged: by default, the type of messages contained in a file will
be ISO 20022 message definitions.
- Provides processing information to the receiving party: that would be, for instance, the total number of
messages included in the file.
Usage: The Business File Header (head.002) is to be used exclusively in existing implementations,
such as the Eurosystem, and will be replaced for general use by the upcoming next version defined as
the Business File Envelope (nvlp.002). The Business File Header (head.002) will therefore not be
maintained in the future and any new implementation must use the Business File Envelope (nvlp.002).
Outline
The BusinessFileHeaderV01 MessageDefinition is composed of 2 MessageBuildingBlocks:
A. PayloadDescription
Contains information about the payload.
B. Payload
File Payload is used to include the exchanged documents within the file structure.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
head.002.001.01 BusinessFileHeaderV01
Target2-Securities 614 August 2026
```

