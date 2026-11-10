---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Partial settlement confirmation"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
flow_id: "flow-settlement-reconciliation-partial-settlement"
participant_ids: ["participant-settlement-reconciliation-instructing-party", "participant-settlement-reconciliation-executing-servicing-party"]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13"]
limitations: ["Unreviewed source reconstructions and full source coverage remain visible in the coverage inventory."]
diagram_ids: ["fig-0012"]
---

# Partial settlement confirmation

## Purpose and boundaries

Report a single instruction settling in multiple phases while retaining the original instruction.

**Trigger:** Transaction settles only in part.

**Preconditions:** No separate formal precondition list is provided in §6.3; its exchange starts with an instruction.

**Outcome/postconditions:** Confirmation of the remaining quantity completes the exchange described in §6.3.

**Evidence:** [src-000196](../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md), §6.3 paragraphs336–342.

## Participants

- [instructing party](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- [executing servicing party](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)

## Activities, decisions and alternatives

Instructing party sends sese.023; optional processing/settlement statuses use sese.024. Servicer confirms only the partially settled quantity with sese.025, may report the still-pending quantity’s status, then confirms the remaining quantity when settled. This is not instruction splitting: the original instruction is retained.


## Messages and navigation

- [sese.023.001.13](../../../../messages/sese.023.001.13/index.md)
- [sese.024.001.14](../../../../messages/sese.024.001.14/index.md)
- [sese.025.001.13](../../../../messages/sese.025.001.13/index.md)

[Reconstructed source sequence](../diagrams/pilot/02-partial-sequence.md)

[Participant index](../participants.md) · [Flow index](index.md)









<!-- SOURCE-ACTIVITY-0012-START -->
[Partial settlement activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0012.md)
<!-- SOURCE-ACTIVITY-0012-END -->
