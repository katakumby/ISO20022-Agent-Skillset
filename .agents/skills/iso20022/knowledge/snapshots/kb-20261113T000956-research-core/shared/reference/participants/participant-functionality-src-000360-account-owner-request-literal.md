---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000360-account-owner-request-literal"
title: "account owner/request — T2S IntraBalanceMovement Functionality"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
source_labels: ["account owner/request"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["t2s-intra-balance-movement"]
message_ids: ["camt.085.001.02"]
message_families: ["camt.085"]
source_locations: [{"source_id": "src-000360", "heading": "16 camt.085.001.02 IntraBalanceMovementPendingReportV02", "file_pages": [358], "evidence_id": "src-000360-camt.085.001.02-p358-c001"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
issue_ids: ["issue-000062"]
---





# account owner/request — T2S IntraBalanceMovement Functionality

[src-000360](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`

## Definition and business context

Literal recipient label printed in IntraBalanceMovementPendingReport. It reports pending instructions previously sent by the account owner. Whether the truncated word request is intended to mean requestor is unresolved (issue-000062); no replacement is made.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000360-camt.085.001.02-p358-c001

src-000360, file page 358; 16 camt.085.001.02 IntraBalanceMovementPendingReportV02.

> This IntraBalanceMovementPendingReport message is sent from a settlement infrastructure to an account owner/request to report the intra-balance movement instructions, previously sent by the account owner, that have a pending status.

## Applicable exact messages


- [camt.085.001.02](../../../domains/securities/reference/messages/camt.085.001.02/roles.md)

## Identity and unresolved scope

Source labels: account owner/request. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.

[Unresolved source wording: issue-000062](../../../tracking/issues.md)

## Original-page wording check

On2026-11-09, the original PDF file page358 (printed page358) was rendered with Poppler26.07 at110dpi and directly inspected. It visibly prints account owner/request. This is a source wording issue, not a text-extraction or glyph-display artifact. [Rendered source page](../../../evidence/omitted/20fd76e5849fdc070e84d959.md).
