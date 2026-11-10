---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["8 reda.013.001.01 SecurityDeletionRequestV01"]
file_pages: [115]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.013.001.01"]
---

# 8 reda.013.001.01 SecurityDeletionRequestV01

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 115 to 115.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 115

```text
8 reda.013.001.01
SecurityDeletionRequestV01
8.1 MessageDefinition Functionality
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.013.001.01 SecurityDeletionRequestV01
Target2-Securities - Securities Reference Data 115 March 2024
```

