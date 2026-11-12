---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "payments"
message_id: "pain.007.001.13"
message_family: "pain.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:pain.007.001.13"
source_ids: ["src-000174", "src-000178"]
source_editions: ["2025-2026", "March 2026"]
message_name: "CustomerPaymentReversalV13"
business_area: "pain"
message_version: "13"
message_sets: ["payments-initiation"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000174", "file_pages": [272, 402], "heading": "4 pain.007.001.13 CustomerPaymentReversalV13"}]
---

# pain.007.001.13 — CustomerPaymentReversalV13

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `CustomerPaymentReversalV13`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | pain.007.001.13 | [src-000178](../../../../../raw-input/payments_initiation/pain.007.001.13.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:pain.007.001.13 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Payments Initiation | raw-input/payments_initiation/pain.007.001.13.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/payments-initiation/2025-2026/index.md)
- [Source extraction coverage](../../message-sets/payments-initiation/2025-2026/coverage.md)
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


<!-- INITIATION-FLOW-298 -->
[Customer Payment Reversal with Direct Debit — source173 Part1 business flow; exact schema definition remains separately scoped.](../../message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p298-customer-payment-reversal-with-direct-debit.md)
<!-- /INITIATION-FLOW-298 -->

<!-- CLEARING-FLOW-556 -->
[FIToFIPaymentReversal with Direct Debit — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit.md)
<!-- /CLEARING-FLOW-556 -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
