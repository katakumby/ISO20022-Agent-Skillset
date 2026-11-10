---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000381-account-owner-request-literal"
title: "account owner/request — T2S SettlementRestrictions Functionality"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
source_labels: ["account owner/request"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["t2s-settlement-restrictions"]
message_ids: ["semt.034.001.01"]
message_families: ["semt.034"]
source_locations: [{"source_id": "src-000381", "heading": "8 semt.034.001.01 IntraPositionMovementPendingReportV01", "file_pages": [169], "evidence_id": "src-000381-semt.034.001.01-p169-c001"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
issue_ids: ["issue-000062"]
---





# account owner/request — T2S SettlementRestrictions Functionality

[src-000381](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`

## Definition and business context

Literal recipient label printed in IntraPositionMovementPendingReport. It reports pending instructions previously sent by the account owner. Whether request is intended to mean requestor is unresolved (issue-000062); no replacement is made.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000381-semt.034.001.01-p169-c001

src-000381, file page 169; 8 semt.034.001.01 IntraPositionMovementPendingReportV01.

> This IntraPositionMovementPendingReport message is sent from a settlement infrastructure to an account owner/request to report the intra-position movement instructions, previously sent by the account owner, that have a pending status.

## Applicable exact messages


- [semt.034.001.01](../../../domains/securities/reference/messages/semt.034.001.01/roles.md)

## Identity and unresolved scope

Source labels: account owner/request. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.

[Unresolved source wording: issue-000062](../../../tracking/issues.md)

## Original-page wording check

On2026-11-09, the original PDF file page169 (printed page169) was rendered with Poppler26.07 at110dpi and directly inspected. It visibly prints account owner/request. This is a source wording issue, not a text-extraction or glyph-display artifact. [Rendered source page](../../../domains/securities/assets/src-000381/participant-wording-review/wording.png).
