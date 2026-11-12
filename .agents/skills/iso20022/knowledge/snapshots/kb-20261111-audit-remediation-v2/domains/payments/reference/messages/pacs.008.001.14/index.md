---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "payments"
message_id: "pacs.008.001.14"
message_family: "pacs.008"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14"
source_ids: ["src-000163", "src-000169"]
source_editions: ["2025-2026", "March 2026"]
message_name: "FIToFICustomerCreditTransferV14"
business_area: "pacs"
message_version: "14"
message_sets: ["payments-clearing-and-settlement"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000163", "file_pages": [702, 829], "heading": "6 pacs.008.001.14 FIToFICustomerCreditTransferV14"}]
---

# pacs.008.001.14 — FIToFICustomerCreditTransferV14

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `FIToFICustomerCreditTransferV14`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | pacs.008.001.14 | [src-000169](../../../../../raw-input/payments_clearing_and_settlement/pacs.008.001.14.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Payments Clearing and Settlement | raw-input/payments_clearing_and_settlement/pacs.008.001.14.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/payments-clearing-and-settlement/2025-2026/index.md)
- [Source extraction coverage](../../message-sets/payments-clearing-and-settlement/2025-2026/coverage.md)
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


<!-- INITIATION-FLOW-170 -->
[One Actor plays roles of Initiating Party, Debtor and Ultimate Debtor, Second actor plays roles of Creditor and Ultimate Creditor — source173 Part1 business flow; exact schema definition remains separately scoped.](../../message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p170-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor-s.md)
<!-- /INITIATION-FLOW-170 -->

<!-- INITIATION-FLOW-173 -->
[One actor plays roles of Initiating Party and Debtor, second actor plays role of Ultimate Debtor — source173 Part1 business flow; exact schema definition remains separately scoped.](../../message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p173-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play.md)
<!-- /INITIATION-FLOW-173 -->

<!-- INITIATION-FLOW-176 -->
[Three Different actors play the roles of Initiating Party, Debtor and Ultimate Debtor: — source173 Part1 business flow; exact schema definition remains separately scoped.](../../message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p176-three-different-actors-play-the-roles-of-initiating-party-debtor-and-u.md)
<!-- /INITIATION-FLOW-176 -->

<!-- INITIATION-FLOW-189 -->
[One actor plays roles of Initiating Party, Debtor and Ultimate Debtor — source173 Part1 business flow; exact schema definition remains separately scoped.](../../message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p189-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor.md)
<!-- /INITIATION-FLOW-189 -->

<!-- INITIATION-FLOW-192 -->
[One actor plays roles of Initiating Party and Debtor, Second Actor plays role of Ultimate Debtor — source173 Part1 business flow; exact schema definition remains separately scoped.](../../message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p192-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play.md)
<!-- /INITIATION-FLOW-192 -->

<!-- INITIATION-FLOW-195 -->
[One actor plays roles of Initiating Party and Ultimate Debtor, Second Actor plays role of Debtor — source173 Part1 business flow; exact schema definition remains separately scoped.](../../message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p195-one-actor-plays-roles-of-initiating-party-and-ultimate-debtor-second-a.md)
<!-- /INITIATION-FLOW-195 -->

<!-- CLEARING-FLOW-177 -->
[Debtor Agent and Creditor Agent are Correspondents — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p177-debtor-agent-and-creditor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-177 -->

<!-- CLEARING-FLOW-186 -->
[Debtor Agent and Creditor Agent are not Correspondents - 1 — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p186-debtor-agent-and-creditor-agent-are-not-correspondents-1.md)
<!-- /CLEARING-FLOW-186 -->

<!-- CLEARING-FLOW-198 -->
[Debtor Agent and Creditor Agent are not Correspondents - 2 — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p198-debtor-agent-and-creditor-agent-are-not-correspondents-2.md)
<!-- /CLEARING-FLOW-198 -->

<!-- CLEARING-FLOW-214 -->
[Debtor Agent and Creditor Agent are Direct Correspondents — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p214-debtor-agent-and-creditor-agent-are-direct-correspondents.md)
<!-- /CLEARING-FLOW-214 -->

<!-- CLEARING-FLOW-221 -->
[Debtor Agent and Creditor Agent are not Correspondents - 1 — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p221-debtor-agent-and-creditor-agent-are-not-correspondents-1.md)
<!-- /CLEARING-FLOW-221 -->

<!-- CLEARING-FLOW-236 -->
[Debtor Agent and Creditor Agent are not Correspondents - 2 — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p236-debtor-agent-and-creditor-agent-are-not-correspondents-2.md)
<!-- /CLEARING-FLOW-236 -->

<!-- CLEARING-FLOW-249 -->
[Debtor Agent and the Creditor Agent are Correspondents — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p249-debtor-agent-and-the-creditor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-249 -->

<!-- CLEARING-FLOW-260 -->
[Debtor Agent and Creditor Agent are not Correspondents - 1 — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p260-debtor-agent-and-creditor-agent-are-not-correspondents-1.md)
<!-- /CLEARING-FLOW-260 -->

<!-- CLEARING-FLOW-277 -->
[Debtor Agent and Creditor Agent are not Correspondents - 2 — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p277-debtor-agent-and-creditor-agent-are-not-correspondents-2.md)
<!-- /CLEARING-FLOW-277 -->

<!-- CLEARING-FLOW-292 -->
[Debtor Agent sends FIToFIPaymentStatusRequest — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p292-debtor-agent-sends-fito-fipayment-status-request.md)
<!-- /CLEARING-FLOW-292 -->

<!-- CLEARING-FLOW-353 -->
[Debtor and Creditor are Correspondents — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p353-debtor-and-creditor-are-correspondents.md)
<!-- /CLEARING-FLOW-353 -->

<!-- CLEARING-FLOW-360 -->
[Debtor and Creditor Agent are Correspondents — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p360-debtor-and-creditor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-360 -->

<!-- CLEARING-FLOW-367 -->
[Debtor Agent and Creditor are Correspondents — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p367-debtor-agent-and-creditor-are-correspondents.md)
<!-- /CLEARING-FLOW-367 -->

<!-- CLEARING-FLOW-379 -->
[Debtor Agent and Creditor Agent are Correspondents — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p379-debtor-agent-and-creditor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-379 -->

<!-- CLEARING-FLOW-391 -->
[Debtor Agent and Creditor Agent Not Correspondents — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p391-debtor-agent-and-creditor-agent-not-correspondents.md)
<!-- /CLEARING-FLOW-391 -->

<!-- CLEARING-EXAMPLES -->
[Source162 business examples, literal tables/XML and source limitations](../../message-sets/payments-clearing-and-settlement/2025-2026/examples/index.md)
<!-- /CLEARING-EXAMPLES -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
