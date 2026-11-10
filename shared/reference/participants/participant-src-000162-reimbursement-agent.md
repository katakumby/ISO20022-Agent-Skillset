---
template: false
document_kind: "participant"
manual_curated: true
review_status: "reviewed"
domain: "shared"
domains: ["payments"]
participant_id: "participant-src-000162-reimbursement-agent"
title: "Reimbursement Agent"
source_labels: ["Reimbursement Agent"]
aliases: []
role_type: "Cover-payment functional participant"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
source_locations: [{"source_id": "src-000162", "locator": "P173; P199–205; P239–246; P280–289; figures14/17/20"}]
flow_ids: ["flow-src-000162-p198-debtor-agent-and-creditor-agent-are-not-correspondents-2", "flow-src-000162-p236-debtor-agent-and-creditor-agent-are-not-correspondents-2"]
message_ids: []
limitations: ["The narrative supplies a generic cover role, not a general taxonomy equating every reimbursement agent and intermediary.", "No identifier scheme is specified in cited bounded role evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Source narrative and original/Word-rendered figures read."}
---









# Reimbursement Agent

[src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Definition, context and responsibilities

In the depicted common-agent cover scenario, receives FinancialInstitutionCreditTransfer from debtor agent and supplies status; creditor agent later uses a separate FI transfer for returned cover funds. (P173; P199–205; P239–246; P280–289; figures14/17/20)

Classification: Cover-payment functional participant.

## Relationships

- [instructed reimbursement agent](participant-src-000162-instructed-reimbursement-agent.md)
- [instructing reimbursement agent](participant-src-000162-instructing-reimbursement-agent.md)
- [debtor agent](participant-src-000162-debtor-agent.md)
- [creditor agent](participant-src-000162-creditor-agent.md)

## Limits and identifier schemes

The narrative supplies a generic cover role, not a general taxonomy equating every reimbursement agent and intermediary.

No identifier scheme is specified in the cited role evidence. Message and flow relationships are maintained below.

<!-- CLEARING-FLOW-198 -->
[Debtor Agent and Creditor Agent are not Correspondents - 2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p198-debtor-agent-and-creditor-agent-are-not-correspondents-2.md)
<!-- /CLEARING-FLOW-198 -->

<!-- CLEARING-FLOW-236 -->
[Debtor Agent and Creditor Agent are not Correspondents - 2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p236-debtor-agent-and-creditor-agent-are-not-correspondents-2.md)
<!-- /CLEARING-FLOW-236 -->
