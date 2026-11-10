---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["51 reda.031.001.01 PartyDeletionRequestV01"]
file_pages: [2213]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.031.001.01"]
---

# 51 reda.031.001.01 PartyDeletionRequestV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2213 to 2213.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2213

```text
51 reda.031.001.01
PartyDeletionRequestV01
51.1 MessageDefinition Functionality
Scope:
The PartyDeletionRequest message is sent by the instructing party to the executing party to request a
deletion of a party defined in the executing system.
Usage:
It aims at instructing the deletion of an existing party by providing its identification.
Processing of the party deletion request message is provided via a party status advice.
Outline
The PartyDeletionRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SystemPartyIdentification
Unique identification, as assigned by the executing system, to unambiguously identify the party to
be deleted.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
51.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyDeltnReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2214
   SystemPartyIdentification <SysPtyId> [1..1] ± 2214
   SupplementaryData <SplmtryData> [0..*] ± C3 2214
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.031.001.01 PartyDeletionRequestV01
Target2-Securities 2213 August 2026
```

