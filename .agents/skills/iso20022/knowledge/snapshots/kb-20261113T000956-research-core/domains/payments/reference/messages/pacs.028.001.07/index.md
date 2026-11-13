---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "payments"
message_id: "pacs.028.001.07"
message_family: "pacs.028"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07"
source_ids: ["src-000163", "src-000172"]
source_editions: ["2025-2026", "March 2026"]
message_name: "FIToFIPaymentStatusRequestV07"
business_area: "pacs"
message_version: "07"
message_sets: ["payments-clearing-and-settlement"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000163", "file_pages": [1049, 1160], "heading": "9 pacs.028.001.07 FIToFIPaymentStatusRequestV07"}]
---

# pacs.028.001.07 — FIToFIPaymentStatusRequestV07

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `FIToFIPaymentStatusRequestV07`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | pacs.028.001.07 | [src-000172](../../../../../raw-input/payments_clearing_and_settlement/pacs.028.001.07.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Payments Clearing and Settlement | raw-input/payments_clearing_and_settlement/pacs.028.001.07.xsd |

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


<!-- CLEARING-FLOW-292 -->
[Debtor Agent sends FIToFIPaymentStatusRequest — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p292-debtor-agent-sends-fito-fipayment-status-request.md)
<!-- /CLEARING-FLOW-292 -->

<!-- CLEARING-FLOW-463 -->
[Debtor sends FIToFIPaymentStatusRequest — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p463-debtor-sends-fito-fipayment-status-request.md)
<!-- /CLEARING-FLOW-463 -->

<!-- CLEARING-FLOW-575 -->
[Creditor Agent sends FIToFIPaymentStatusRequest — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p575-creditor-agent-sends-fito-fipayment-status-request.md)
<!-- /CLEARING-FLOW-575 -->

<!-- CLEARING-FLOW-645 -->
[Creditor sends FIToFIPaymentStatusRequest — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p645-creditor-sends-fito-fipayment-status-request.md)
<!-- /CLEARING-FLOW-645 -->

<!-- CLEARING-EXAMPLES -->
[Source162 business examples, literal tables/XML and source limitations](../../message-sets/payments-clearing-and-settlement/2025-2026/examples/index.md)
<!-- /CLEARING-EXAMPLES -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
