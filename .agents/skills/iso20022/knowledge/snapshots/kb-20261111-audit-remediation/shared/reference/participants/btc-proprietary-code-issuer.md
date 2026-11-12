---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-proprietary-code-issuer"
source_labels: ["issuer of the proprietary bank transaction code"]
aliases: []
source_locations: ["T2 row 8; The Bank Transaction Code component", "T2 row 10; The Bank Transaction Code component"]
domains: ["payments"]
message_sets: ["external-code-sets"]
flows: []
relationships: []
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# issuer of the proprietary bank transaction code — Bank Transaction Code context

## Definition, role and business context

Defines the proprietary bank transaction code and may be identified in the optional Issuer field. This is a code-source role, distinct from a securities issuer.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T2 row 8](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0002.md): 1.2    Proprietary &lt;Prtry&gt; [0..1]  Proprietary identification of the bank transaction code, as defined by the issuer.
- [T2 row 10](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0002.md): 1.2.2       Issuer &lt;Issr&gt; [0..1] Max35Text Identification of the issuer of the proprietary bank transaction code.

## Relationships and reuse

No specific counterpart role is established by these cited definitions.

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
