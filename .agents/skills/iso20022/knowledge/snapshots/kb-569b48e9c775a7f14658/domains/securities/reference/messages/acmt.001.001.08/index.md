---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "acmt.001.001.08"
message_family: "acmt.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08"
source_ids: ["src-000096", "src-000098"]
source_editions: ["2025-2026", "May 2026"]
message_name: "AccountOpeningInstructionV08"
business_area: "acmt"
message_version: "08"
message_sets: ["investment-funds"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000096", "file_pages": [20, 37], "heading": "2 acmt.001.001.08 AccountOpeningInstructionV08"}]
---

# acmt.001.001.08 — AccountOpeningInstructionV08

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `AccountOpeningInstructionV08`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | acmt.001.001.08 | [src-000098](../../../../../raw-input/investment_funds/acmt.001.001.08.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Investment Funds | raw-input/investment_funds/acmt.001.001.08.xsd |

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


<!-- FUNDS-EARLY-FLOW-240 -->
[Account Management / Account Opening / Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p240-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-240 -->

<!-- FUNDS-EARLY-FLOW-245 -->
[Account Management / Account Opening / Intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p245-intermediary.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-245 -->

<!-- FUNDS-EARLY-FLOW-251 -->
[Account Management / Account Opening / Rejection - Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p251-rejection-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-251 -->

<!-- FUNDS-EARLY-FLOW-256 -->
[Account Management / Account Opening / Rejection - Intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p256-rejection-intermediary.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-256 -->

<!-- FUNDS-EARLY-FLOW-279 -->
[Account Management / Status of Account Opening - Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p279-status-of-account-opening-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-279 -->

<!-- FUNDS-EARLY-FLOW-290 -->
[Account Management / Status of Account Opening - Intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p290-status-of-account-opening-intermediary.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-290 -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
