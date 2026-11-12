---
template: false
document_kind: "participant"
review_status: "needs-review"
title: "Global Settlement Agent"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
participant_id: "participant-settlement-reconciliation-global-settlement-agent"
role_kind: "business role"
source_labels: ["Global Settlement Agent"]
aliases: ["Global Settlement Agent"]
domains: ["securities"]
message_ids: []
flow_ids: []
limitations: ["Table16 account-role headers differ from functional labels in table14. Preserve the source mapping without reversing or repairing it."]
---

# Global Settlement Agent

## Definition and context

Party that holds another party's inventory of financial instruments, and effects or receives deliveries versus payment, or free of payment. Deliveries, receipts, and payments may be affected within the facilities of the global settlement agent, or within the facilities of a local settlement agent, and directed by the global settlement agent. A global settlement agent may be a custodian and/or a clearing broker.

**Evidence:** src-000196 §3.1 Business Roles table15, row2. Original: [src-000196](../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md).

## Responsibilities and relationships

The source role overview and mapping table are linked from [the participant index](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/participants.md). Assignment to a flow requires that flow’s evidence.

## Source labels and identifier schemes

Source labels: `Global Settlement Agent`. The role definition does not mandate a universal identifier scheme. Consult the exact message component for its permitted identification choices.

## Limitations

Table16 account-role headers differ from functional labels in table14. Preserve the source mapping without reversing or repairing it.

[Message-set participants](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/participants.md) · [sese.023.001.13 context](../../../domains/securities/reference/messages/sese.023.001.13/business.md)
