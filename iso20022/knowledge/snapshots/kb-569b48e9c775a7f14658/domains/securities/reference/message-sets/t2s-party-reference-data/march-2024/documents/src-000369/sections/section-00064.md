---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["7 reda.031.001.01 PartyDeletionRequestV01"]
file_pages: [76]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.031.001.01"]
---

# 7 reda.031.001.01 PartyDeletionRequestV01

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 76 to 76.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 76

```text
7 reda.031.001.01
PartyDeletionRequestV01
7.1 MessageDefinition Functionality
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
7.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyDeltnReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 77
   SystemPartyIdentification <SysPtyId> [1..1] ± 77
   SupplementaryData <SplmtryData> [0..*] ± C3 77
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.031.001.01 PartyDeletionRequestV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
76 March 2024
```

