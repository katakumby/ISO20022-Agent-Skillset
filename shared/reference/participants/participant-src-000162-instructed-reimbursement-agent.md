---
template: false
document_kind: "participant"
manual_curated: true
review_status: "reviewed"
domain: "shared"
domains: ["payments"]
participant_id: "participant-src-000162-instructed-reimbursement-agent"
title: "Instructed Reimbursement Agent"
source_labels: ["Instructed Reimbursement Agent"]
aliases: []
role_type: "Source-named cover-payment role"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
source_locations: [{"source_id": "src-000162", "locator": "P278–289; figure20"}]
flow_ids: ["flow-src-000162-p277-debtor-agent-and-creditor-agent-are-not-correspondents-2"]
message_ids: []
limitations: ["No independent role definition or identifier scheme is supplied in this bounded Part1 evidence.", "No identifier scheme is specified in cited bounded role evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Source narrative and original/Word-rendered figures read."}
---





# Instructed Reimbursement Agent

[src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Definition, context and responsibilities

P278 names the middle actor instructed reimbursement agent in the post-settlement customer-transfer return scenario; P280–289 describe the common-agent cover and return-funding exchanges. (P278–289; figure20)

Classification: Source-named cover-payment role.

## Relationships

- [reimbursement agent](participant-src-000162-reimbursement-agent.md)
- [debtor agent](participant-src-000162-debtor-agent.md)
- [creditor agent](participant-src-000162-creditor-agent.md)

## Limits and identifier schemes

No independent role definition or identifier scheme is supplied in this bounded Part1 evidence.

No identifier scheme is specified in the cited role evidence. Message and flow relationships are maintained below.

<!-- CLEARING-FLOW-277 -->
[Debtor Agent and Creditor Agent are not Correspondents - 2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p277-debtor-agent-and-creditor-agent-are-not-correspondents-2.md)
<!-- /CLEARING-FLOW-277 -->
