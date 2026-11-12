---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "sese.043.001.02"
message_family: "sese.043"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.043.001.02"
source_ids: ["src-000096", "src-000136"]
source_editions: ["2025-2026", "May 2026"]
message_name: "PortfolioTransferCompletionV02"
business_area: "sese"
message_version: "02"
message_sets: ["investment-funds"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000096", "file_pages": [1489, 1684], "heading": "40 sese.043.001.02 PortfolioTransferCompletionV02"}]
---

# sese.043.001.02 — PortfolioTransferCompletionV02

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `PortfolioTransferCompletionV02`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | sese.043.001.02 | [src-000136](../../../../../raw-input/investment_funds/sese.043.001.02.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:sese.043.001.02 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Investment Funds | raw-input/investment_funds/sese.043.001.02.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/investment-funds/2025-2026/index.md)
- [Source extraction coverage](../../message-sets/investment-funds/2025-2026/coverage.md)
- [Shared participants](../../../../../catalog/participants.md)
- [Business flows](../../../../../catalog/flows.md)
- [Source identities and original occurrences](../../../../../tracking/source-register.md)
- [Known gaps and review requirements](../../../../../tracking/issues.md)

## Review

Complete supplied schema declarations have focused pages with literal XML, qualified references and nested paths. Automated schema compilation: **pass**. Extraction is **needs-review**; this does not claim that source documentation, tables or diagrams have passed visual review.


<!-- MDR-NAV-START -->
## Supplied business evidence

[Purpose, usage, actors and detailed MDR evidence](mdr-evidence.md)
<!-- MDR-NAV-END -->



<!-- FUNDS-FLOW-0108-START -->
[Portfolio transfer instruction and completion](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p768-portfolio-transfer-instruction.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0108-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
