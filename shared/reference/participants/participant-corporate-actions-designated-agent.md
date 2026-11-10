---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "securities"
participant_id: "participant-corporate-actions-designated-agent"
title: "Designated agent of the corporate-action account owner"
source_labels: ["its designated agent"]
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
source_locations: [{"source_id": "src-000080", "locator": "file page665, §9.1 Scope"}, {"source_id": "src-000080", "locator": "file page813, §15.1 Scope"}, {"source_id": "src-000080", "locator": "file page692, section10.1 MessageDefinition Functionality / Scope", "message_id": "seev.038.001.09", "evidence_id": "src-000080-seev.038.001.09-p692-c001"}]
role_type: "functional agent acting for the account owner; receiver for seev.037/044 and bidirectional participant for bilaterally agreed seev.038"
aliases: []
flows: ["flow-src-000079-p153-movement-reversal"]
message_ids: ["seev.037.001.17", "seev.038.001.09", "seev.044.001.13"]
message_families: ["seev.037", "seev.038", "seev.044"]
limitations: ["The cited functionality names this role but does not provide a separate definition, appointment procedure or identifier scheme.", "The cited movement-reversal sequence drawings show direct delivery to Account Owner and omit this alternative receiver. Their two-actor scope does not limit the separately documented bidirectional CorporateActionNarrative usage."]
---



# Designated agent of the corporate-action account owner

The movement-reversal and preliminary-advice-cancellation functionality permits delivery to the account owner or its designated agent. For those messages the designated agent is an alternative functional receiver. CorporateActionNarrative separately permits a bidirectional exchange between the account servicer and the account owner or its designated agent, only when bilaterally agreed. The agent is a relationship-specific function; these scopes do not separately define the agent or its identifier scheme.

## Responsibilities and relationships

| Message | Sender | Receiver relationship | Evidence |
| --- | --- | --- | --- |
| seev.037.001.17 | Account Servicer | Account Owner or its designated agent | src-000080 file p665 §9.1 |
| seev.044.001.13 | Account Servicer | Account Owner or its designated agent | src-000080 file p813 §15.1 |

The role is linked to [the Corporate Actions account owner](participant-src-000079-account-owner.md) and participates in [the movement-reversal flow](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p153-movement-reversal.md). The cited movement-reversal sequence drawings show only the direct owner/servicer exchange; their two-actor boundary does not remove the narrative-supported alternative receiver for that flow.

Original evidence: [src-000080 MDR Part2](../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf).

## Bidirectional CorporateActionNarrative scope

Source src-000080, file and printed page692, section10.1 MessageDefinition Functionality / Scope (seev.038.001.09):

> The CorporateActionNarrative message is sent between an account servicer and an account owner or its designated agent to cater for such processes that cannot be handled using messages such as the CorporateActionNotification.

The same scope explicitly states that the message is bidirectional and should be used only when bilaterally agreed. It excludes event narrative, which belongs in CorporateActionNotification; tax reclaims, restrictions and documentation requirements are examples of permitted contexts. The designated agent remains an alternative to the account owner, and no fixed initiating party is supplied. These conditions do not change the receiving directions of seev.037.001.17 or seev.044.001.13 above.

See [the exact CorporateActionNarrative role evidence](../../../domains/securities/reference/messages/seev.038.001.09/roles.md).
