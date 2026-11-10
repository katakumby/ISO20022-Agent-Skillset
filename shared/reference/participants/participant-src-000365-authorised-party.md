---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000365-authorised-party"
title: "Authorised Party"
source_labels: ["Authorised Party"]
role_type: "source-scoped functional participant"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
source_locations: [{"source_id": "src-000365", "locator": "P58/P60/P76/P83; T8/T9"}]
message_sets: ["t2s-link-reference-data"]
message_ids: ["reda.045.001.01", "reda.046.001.01", "reda.047.001.01", "reda.049.001.01", "reda.050.001.01", "reda.051.001.01"]
flows: ["flow-src-000365-p120-link-creation-process", "flow-src-000365-p122-link-modification-process"]
aliases: []
limitations: ["No identifier scheme or general institution equivalence is stated in this passage."]
---







# Authorised Party

The narrative party permitted to request link creation or maintenance. The executing system must know the instructing party and grant appropriate privileges (T8/T9); source P58/P60/P76/P83 supplies this authorization context.

Source [src-000365](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`; P58/P60/P76/P83; T8/T9.

Link-reference source context: [Link creation and modification overview](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/diagrams/curated/fig-0002.md). [flow Link Creation Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p120-link-creation-process.md), [flow Link Modification Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p122-link-modification-process.md).

Link-reference source context: [Link creation activity with validation and retry](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/diagrams/curated/fig-0007.md). [flow Link Creation Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p120-link-creation-process.md).

Link-reference source context: [Link modification activity with validation and retry](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/diagrams/curated/fig-0007.md). [flow Link Modification Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p122-link-modification-process.md).
