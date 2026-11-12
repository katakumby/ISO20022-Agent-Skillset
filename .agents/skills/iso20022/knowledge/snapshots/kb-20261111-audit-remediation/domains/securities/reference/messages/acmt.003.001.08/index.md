---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "acmt.003.001.08"
message_family: "acmt.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08"
source_ids: ["src-000096", "src-000100"]
source_editions: ["2025-2026", "May 2026"]
message_name: "AccountModificationInstructionV08"
business_area: "acmt"
message_version: "08"
message_sets: ["investment-funds"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000096", "file_pages": [57, 76], "heading": "4 acmt.003.001.08 AccountModificationInstructionV08"}]
---

# acmt.003.001.08 — AccountModificationInstructionV08

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `AccountModificationInstructionV08`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | acmt.003.001.08 | [src-000100](../../../../../raw-input/investment_funds/acmt.003.001.08.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Investment Funds | raw-input/investment_funds/acmt.003.001.08.xsd |

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


<!-- FUNDS-EARLY-FLOW-262 -->
[Account Management / Account Modification / Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p262-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-262 -->

<!-- FUNDS-EARLY-FLOW-266 -->
[Account Management / Account Modification / Intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p266-intermediary.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-266 -->

<!-- FUNDS-EARLY-FLOW-269 -->
[Account Management / Account Modification / Rejection - Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p269-rejection-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-269 -->

<!-- FUNDS-EARLY-FLOW-274 -->
[Account Management / Account Modification / Rejection - Intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p274-rejection-intermediary.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-274 -->

<!-- FUNDS-EARLY-FLOW-284 -->
[Account Management / Status of Account Modification – Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p284-status-of-account-modification-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-284 -->

<!-- FUNDS-EARLY-FLOW-296 -->
[Account Management / Status of Account Modification - Intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p296-status-of-account-modification-intermediary.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-296 -->

<!-- FUNDS-EARLY-FLOW-308 -->
[Account Management / Account Closure - Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p308-account-closure-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-308 -->

<!-- FUNDS-EARLY-FLOW-311 -->
[Account Management / Account Closure and Reactivation - Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p311-account-closure-and-reactivation-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-311 -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
