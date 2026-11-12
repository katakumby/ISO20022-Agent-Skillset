---
template: false
document_kind: "participant"
review_status: "needs-review"
participant_id: "participant-src-000095-sub-level-account-owner"
title: "Sub-Level Account Owner"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
source_labels: ["Sub-Level Account Owner"]
aliases: []
role_type: "functional participant role; scoped custody-chain level"
message_sets: ["investment-funds"]
source_locations: [{"source_id": "src-000095", "locator": "BusinessTransactions / Statements / Transparency of Holdings Statement; P941–P943; fig-0138", "xml_path": "/w:document/w:body/w:p[943]"}]
identifier_schemes: []
limitations: ["This definition is scoped to the source diagram; it is not an institutional identity or a universal account-role equivalence.", "P941 describes the initial sender as an account servicer such as a custodian; the figure labels that endpoint Sub-Level Account Owner. Both contextual labels remain explicit."]
updated: "2026-11-09"
---

# Sub-Level Account Owner

## Definition and responsibilities

The left-hand account-owner role in the source transparency reporting chain. It sends a SecuritiesBalanceTransparencyReport to the Omnibus Account Owner and receives a SecuritiesBalanceTransparencyReportStatusAdvice from that party.

Evidence: src-000095, P941–P943, [source figure 138](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/diagrams/fig-0138.md).

## Relationships and business context

Investment Funds transparency-of-holdings reporting; related [adjacent contextual role](participant-src-000095-omnibus-account-owner.md). A participant can occupy different owner/servicer roles in different account relationships. No institution is permanently assigned to this role.

## Identifiers and unresolved distinctions

No identifier scheme is specified by P941–P943 for this functional role. No aliases or cross-source equivalence are asserted. The narrative and picture use different contextual labels for the first endpoint; see the flow for both.

<!-- FUNDS-CURATED-FLOW-0138-START -->
[Transparency holdings statement aggregation and status](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p940-transparency-of-holdings-statement.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0138.md)
<!-- FUNDS-CURATED-FLOW-0138-END -->
