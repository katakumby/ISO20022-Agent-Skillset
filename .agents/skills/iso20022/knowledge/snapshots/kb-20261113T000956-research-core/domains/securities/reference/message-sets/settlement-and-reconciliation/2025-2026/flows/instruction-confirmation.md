---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Instruction and confirmation"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
flow_id: "flow-settlement-reconciliation-instruction-confirmation"
participant_ids: ["participant-settlement-reconciliation-instructing-party", "participant-settlement-reconciliation-executing-servicing-party"]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13"]
limitations: ["Unreviewed source reconstructions and full source coverage remain visible in the coverage inventory."]
diagram_ids: ["fig-0001", "fig-0019"]
---

# Instruction and confirmation

## Purpose and boundaries

Instruct settlement, booking or movement of securities and report processing and settlement.

**Trigger:** External process such as exchange/OTC trade, realignment, repo trade or portfolio transfer.

**Preconditions:** The high-level Instruction definition states None.

**Outcome/postconditions:** Acknowledgement of acceptance at the Instruction-process boundary. The full exchange ends with settlement confirmation.

**Evidence:** [src-000196](../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md), §4 Instruction table17; §5.1 table28; §6.1 paragraphs324–327.

## Participants

- [instructing party](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- [executing servicing party](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)

## Activities, decisions and alternatives

The instructing party sends sese.023. The executing/servicing party may return processing and/or settlement status using sese.024. When settlement takes place it sends sese.025. Successful validation can also lead to a status update even though that path is omitted from the activity diagram.

- [Complete source table 17](../documents/src-000196/tables/tbl-0017.md) — §4 Instruction table17; §5.1 table28; §6.1 paragraphs324–327.
- [Complete source table 28](../documents/src-000196/tables/tbl-0028.md) — §4 Instruction table17; §5.1 table28; §6.1 paragraphs324–327.

## Messages and navigation

- [sese.023.001.13](../../../../messages/sese.023.001.13/index.md)
- [sese.024.001.14](../../../../messages/sese.024.001.14/index.md)
- [sese.025.001.13](../../../../messages/sese.025.001.13/index.md)

[Reconstructed source sequence](../diagrams/pilot/01-typical-sequence.md)

[Participant index](../participants.md) · [Flow index](index.md)






<!-- SOURCE-ACTIVITY-0019-START -->
[Settlement instruction status processes — source activity/communication diagram](../diagrams/settlement-activities/fig-0019.md)
<!-- SOURCE-ACTIVITY-0019-END -->

<!-- SOURCE-ACTIVITY-0001-START -->
[Settlement communication scope and account relationships — source activity/communication diagram](../diagrams/settlement-activities/fig-0001.md)
<!-- SOURCE-ACTIVITY-0001-END -->
