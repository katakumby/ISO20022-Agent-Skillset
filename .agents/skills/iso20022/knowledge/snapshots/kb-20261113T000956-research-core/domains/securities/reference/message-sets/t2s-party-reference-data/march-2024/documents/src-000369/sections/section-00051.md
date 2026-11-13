---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["6 reda.022.001.02 PartyModificationRequestV02"]
file_pages: [61]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 6 reda.022.001.02 PartyModificationRequestV02

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 61 to 61.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 61

```text
6 reda.022.001.02
PartyModificationRequestV02
6.1 MessageDefinition Functionality
Scope:
The PartyModificationRequest message is sent by the instructing party to the executing party to request
for an update of the party reference data of a party defined in the executing system.
Usage:
It aims at instructing the update of an existing party by amending its existing details or by providing
additional details.
Processing and confirmation of the party modification request message are provided via a party status
advice.
Outline
The PartyModificationRequestV02 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SystemPartyIdentification
Unique identification, as assigned by the executing system, to unambiguously identify the party to
be modified.
C. Modification
Identifies the list of requested modifications to be executed by the system.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.022.001.02 PartyModificationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
61 March 2024
```

