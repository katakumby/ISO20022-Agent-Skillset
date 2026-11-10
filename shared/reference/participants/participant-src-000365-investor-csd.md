---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000365-investor-csd"
title: "Investor CSD"
source_labels: ["Investor CSD"]
role_type: "source-scoped functional participant"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
source_locations: [{"source_id": "src-000365", "locator": "P58; P283-P287"}]
message_sets: ["t2s-link-reference-data"]
message_ids: ["reda.045.001.01", "reda.046.001.01", "reda.047.001.01", "reda.049.001.01", "reda.050.001.01", "reda.051.001.01"]
flows: ["flow-src-000365-p120-link-creation-process", "flow-src-000365-p122-link-modification-process"]
aliases: []
limitations: ["No identifier scheme or general institution equivalence is stated in this passage."]
---





# Investor CSD

A CSD identified as the investor-side endpoint of a Security CSD Link. P58 permits issuer or investor identification; P283-P287 identifies a maintenance target by the ISIN–Investor CSD pair. The source does not equate this endpoint with the sender.

Source [src-000365](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`; P58; P283-P287.

Link-reference source context: [Link creation activity with validation and retry](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/diagrams/curated/fig-0007.md). [flow Link Creation Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p120-link-creation-process.md).

Link-reference source context: [Link modification activity with validation and retry](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/diagrams/curated/fig-0007.md). [flow Link Modification Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p122-link-modification-process.md).
