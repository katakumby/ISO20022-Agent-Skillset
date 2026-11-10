---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Settlement reversal advice"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
flow_id: "flow-settlement-reconciliation-reversal-advice"
participant_ids: ["participant-settlement-reconciliation-instructing-party", "participant-settlement-reconciliation-executing-servicing-party"]
message_ids: ["sese.025.001.13", "sese.026.001.12"]
limitations: ["Unreviewed source reconstructions and full source coverage remain visible in the coverage inventory."]
diagram_ids: ["fig-0035"]
---

# Settlement reversal advice

## Purpose and boundaries

Reverse a confirmed transaction and return it to open status.

**Trigger:** Transaction should not have been confirmed, or receiving party returned shares.

**Preconditions:** Transaction has been confirmed and reversal is possible.

**Outcome/postconditions:** Underlying instruction remains in settlement processing; account owner receives statuses and confirmations.

**Evidence:** [src-000196](<../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx>), §4 Reversal table22; §5.14 table47; §6.14 paragraphs624–625.

## Participants

- [instructing party](<../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md>)
- [executing servicing party](<../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md>)

## Activities, decisions and alternatives

After settlement confirmation, executing party sends sese.026 to instructing party to reverse confirmation of partial/full delivery or receipt, free/against payment, physically/by book-entry. This differs from an account owner requesting cancellation of an open transaction.

- [Complete source table 22](<../documents/src-000196/tables/tbl-0022.md>) — §4 Reversal table22; §5.14 table47; §6.14 paragraphs624–625.
- [Complete source table 47](<../documents/src-000196/tables/tbl-0047.md>) — §4 Reversal table22; §5.14 table47; §6.14 paragraphs624–625.

## Messages and navigation

- [sese.025.001.13](<../../../../messages/sese.025.001.13/index.md>)
- [sese.026.001.12](<../../../../messages/sese.026.001.12/index.md>)

[Reconstructed source sequence](<../diagrams/pilot/05-reversal-sequence.md>)

[Participant index](<../participants.md>) · [Flow index](<index.md>)









<!-- SOURCE-ACTIVITY-0035-START -->
[Settlement reversal-advice activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0035.md)
<!-- SOURCE-ACTIVITY-0035-END -->
