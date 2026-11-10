---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["33 reda.013.001.01 SecurityDeletionRequestV01"]
file_pages: [2039]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.013.001.01"]
---

# 33 reda.013.001.01 SecurityDeletionRequestV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2039 to 2039.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2039

```text
33 reda.013.001.01
SecurityDeletionRequestV01
33.1 MessageDefinition Functionality
SCOPE
An instructing party sends a SecurityDeletionRequest message to an executing/servicing party to
advice the complete removal of a financial instrument entry from their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified that a security is wrongly created in the
securities coverage of the executing/servicing party. The instructing party needs this security to be
removed from the executing /servicing party database.
This message can be used when a security identification code was issued too quickly or if a security
identification code needs to be reused (for example, in case of money market instrument). The result of
this message is a complete removal of the security identification from the executing/servicing party's
database.
Initiator: instructing party.
Outline
The SecurityDeletionRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. FinancialInstrumentIdentification
Identification of the financial instrument.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.013.001.01 SecurityDeletionRequestV01
Target2-Securities 2039 August 2026
```

