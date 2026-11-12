---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["6 reda.022.001.02 PartyModificationRequestV02", "6.4 Message Building Blocks", "6.4.3 Modification <Mod>", "6.4.3.1 ScopeIndication <ScpIndctn>"]
file_pages: [66]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 6.4.3.1 ScopeIndication <ScpIndctn>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 66 to 66.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 66

```text
6.4.3.1  ScopeIndication <ScpIndctn>
Presence: [1..1]
Definition: Specifies the type of requested modification.
Datatype: "DataModification1Code" on page 181
CodeName Name Definition
INSE InsertNewDataSet Insert a new set of data.
UPDT UpdateDataSetDetails Update the details of an existing set of
data.
DELT DeleteDataSet Delete an existing set of data.
6.4.3.2  RequestedModification <ReqdMod>
Presence: [1..1]
Definition: Specifies the set of elements to be modified for the party reference data.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.022.001.02 PartyModificationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
66 March 2024
```

