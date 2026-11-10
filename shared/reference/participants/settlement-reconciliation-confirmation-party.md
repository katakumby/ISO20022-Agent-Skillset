---
template: false
document_kind: "participant"
review_status: "needs-review"
title: "Confirmation Party"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
participant_id: "participant-settlement-reconciliation-confirmation-party"
role_kind: "business role"
source_labels: ["Confirmation Party"]
aliases: ["Confirmation Party"]
domains: ["securities"]
message_ids: []
flow_ids: []
limitations: ["Table16 account-role headers differ from functional labels in table14. Preserve the source mapping without reversing or repairing it."]
---

# Confirmation Party

## Definition and context

An infrastructure that issues trade confirmations, receives trade affirmations, matches allocations to confirmations and confirmations to instructions, and generates standing or special instructions to create settlement instructions.

**Evidence:** src-000196 §3.1 Business Roles table15, row8. Original: [src-000196](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx>).

## Responsibilities and relationships

The source role overview and mapping table are linked from [the participant index](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/participants.md>). Assignment to a flow requires that flow’s evidence.

## Source labels and identifier schemes

Source labels: `Confirmation Party`. The role definition does not mandate a universal identifier scheme. Consult the exact message component for its permitted identification choices.

## Limitations

Table16 account-role headers differ from functional labels in table14. Preserve the source mapping without reversing or repairing it.

[Message-set participants](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/participants.md>) · [sese.023.001.13 context](<../../../domains/securities/reference/messages/sese.023.001.13/business.md>)
