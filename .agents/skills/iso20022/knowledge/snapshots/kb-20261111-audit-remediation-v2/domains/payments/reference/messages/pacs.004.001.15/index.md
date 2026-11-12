---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "payments"
message_id: "pacs.004.001.15"
message_family: "pacs.004"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15"
source_ids: ["src-000163", "src-000167"]
source_editions: ["2025-2026", "March 2026"]
message_name: "PaymentReturnV15"
business_area: "pacs"
message_version: "15"
message_sets: ["payments-clearing-and-settlement"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000163", "file_pages": [246, 561], "heading": "4 pacs.004.001.15 PaymentReturnV15"}]
---

# pacs.004.001.15 — PaymentReturnV15

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `PaymentReturnV15`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | pacs.004.001.15 | [src-000167](../../../../../raw-input/payments_clearing_and_settlement/pacs.004.001.15.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Payments Clearing and Settlement | raw-input/payments_clearing_and_settlement/pacs.004.001.15.xsd |

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


<!-- INITIATION-FLOW-234 -->
[Negative CustomerPaymentStatusReport - Creditor Agent — source173 Part1 business flow; exact schema definition remains separately scoped.](../../message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p234-negative-customer-payment-status-report-creditor-agent.md)
<!-- /INITIATION-FLOW-234 -->

<!-- INITIATION-FLOW-239 -->
[Negative CustomerPaymentStatusReport - Clearing And Settlement Agent — source173 Part1 business flow; exact schema definition remains separately scoped.](../../message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p239-negative-customer-payment-status-report-clearing-and-settlement-agent.md)
<!-- /INITIATION-FLOW-239 -->

<!-- INITIATION-FLOW-249 -->
[Negative FIToFIPaymentStatusReport - Debtor Agent — source173 Part1 business flow; exact schema definition remains separately scoped.](../../message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p249-negative-fito-fipayment-status-report-debtor-agent.md)
<!-- /INITIATION-FLOW-249 -->

<!-- INITIATION-FLOW-266 -->
[Confirmation of Processability of CustomerDirectDebitInitiation — source173 Part1 business flow; exact schema definition remains separately scoped.](../../message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p266-confirmation-of-processability-of-customer-direct-debit-initiation.md)
<!-- /INITIATION-FLOW-266 -->

<!-- INITIATION-FLOW-280 -->
[PaymentReturn Initiated by Debtor Agent — source173 Part1 business flow; exact schema definition remains separately scoped.](../../message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p280-payment-return-initiated-by-debtor-agent.md)
<!-- /INITIATION-FLOW-280 -->

<!-- INITIATION-FLOW-298 -->
[Customer Payment Reversal with Direct Debit — source173 Part1 business flow; exact schema definition remains separately scoped.](../../message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p298-customer-payment-reversal-with-direct-debit.md)
<!-- /INITIATION-FLOW-298 -->

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

<!-- CLEARING-FLOW-409 -->
[Debtor and Creditor are direct Correspondents — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents.md)
<!-- /CLEARING-FLOW-409 -->

<!-- CLEARING-FLOW-420 -->
[Debtor Agent and Creditor are Correspondents — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p420-debtor-agent-and-creditor-are-correspondents.md)
<!-- /CLEARING-FLOW-420 -->

<!-- CLEARING-FLOW-433 -->
[Debtor Agent and Creditor Agent are Correspondents — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p433-debtor-agent-and-creditor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-433 -->

<!-- CLEARING-FLOW-445 -->
[Debtor Agent and Creditor Agent are Not Correspondents — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p445-debtor-agent-and-creditor-agent-are-not-correspondents.md)
<!-- /CLEARING-FLOW-445 -->

<!-- CLEARING-FLOW-499 -->
[CreditorNegative FIToFIPaymentStatusReport initiated by Clearing and Settlement Agent — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p499-creditor-negative-fito-fipayment-status-report-initiated-by-clearing-a.md)
<!-- /CLEARING-FLOW-499 -->

<!-- CLEARING-FLOW-509 -->
[Negative FIToFIPaymentStatusReport Initiated by Debtor Agent — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p509-negative-fito-fipayment-status-report-initiated-by-debtor-agent.md)
<!-- /CLEARING-FLOW-509 -->

<!-- CLEARING-FLOW-529 -->
[FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p529-fito-fipayment-status-report-to-confirm-processability-of-fito-ficusto.md)
<!-- /CLEARING-FLOW-529 -->

<!-- CLEARING-FLOW-539 -->
[PaymentReturn Initiated by Debtor Agent — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p539-payment-return-initiated-by-debtor-agent.md)
<!-- /CLEARING-FLOW-539 -->

<!-- CLEARING-FLOW-556 -->
[FIToFIPaymentReversal with Direct Debit — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit.md)
<!-- /CLEARING-FLOW-556 -->

<!-- CLEARING-FLOW-623 -->
[Payment Return in a FinancialInstitutionDirectDebit scenario — source162 Part1 family-level business context.](../../message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p623-payment-return-in-a-financial-institution-direct-debit-scenario.md)
<!-- /CLEARING-FLOW-623 -->

<!-- CLEARING-EXAMPLES -->
[Source162 business examples, literal tables/XML and source limitations](../../message-sets/payments-clearing-and-settlement/2025-2026/examples/index.md)
<!-- /CLEARING-EXAMPLES -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
