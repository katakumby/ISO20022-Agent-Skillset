---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Transaction generation notification"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
flow_id: "flow-settlement-reconciliation-transaction-generation"
participant_ids: ["participant-settlement-reconciliation-instructing-party", "participant-settlement-reconciliation-executing-servicing-party"]
message_ids: ["sese.032.001.13"]
limitations: ["Unreviewed source reconstructions and full source coverage remain visible in the coverage inventory."]
diagram_ids: ["fig-0001"]
---

# Transaction generation notification

## Purpose and boundaries

Advise an instructing party that a servicing party generated a settlement transaction for it.

**Trigger:** Examples: automatic transformation of pending instructions after a corporate event, or account-owner transaction-database recovery initiated by servicing party.

**Preconditions:** No formal precondition list is provided.

**Outcome/postconditions:** Instructing party is informed of generated transaction.

**Evidence:** [src-000196](<../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx>), §5.16 paragraphs314–315; §6.16 paragraphs633–634.

## Participants

- [instructing party](<../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md>)
- [executing servicing party](<../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md>)

## Activities, decisions and alternatives

Executing/servicing party sends SecuritiesSettlementTransactionGenerationNotification to instructing party. Cited paragraphs do not prescribe a response, failure branch or further activity sequence.


## Messages and navigation

- [sese.032.001.13](<../../../../messages/sese.032.001.13/index.md>)

[Participant index](<../participants.md>) · [Flow index](<index.md>)

<!-- SOURCE-ACTIVITY-0001-START -->
[Settlement communication scope and account relationships — source activity/communication diagram](../diagrams/settlement-activities/fig-0001.md)
<!-- SOURCE-ACTIVITY-0001-END -->
