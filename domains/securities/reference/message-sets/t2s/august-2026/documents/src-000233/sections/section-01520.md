---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["42 reda.022.001.02 PartyModificationRequestV02"]
file_pages: [2140]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 42 reda.022.001.02 PartyModificationRequestV02

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2140 to 2140.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2140

```text
42 reda.022.001.02
PartyModificationRequestV02
42.1 MessageDefinition Functionality
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.022.001.02 PartyModificationRequestV02
Target2-Securities 2140 August 2026
```

