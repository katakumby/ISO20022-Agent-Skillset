---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 reda.016.001.01 PartyStatusAdviceV01"]
file_pages: [35]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.016.001.01"]
---

# 4 reda.016.001.01 PartyStatusAdviceV01

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 35 to 35.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 35

```text
4 reda.016.001.01
PartyStatusAdviceV01
4.1 MessageDefinition Functionality
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.016.001.01 PartyStatusAdviceV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
35 March 2024
```

