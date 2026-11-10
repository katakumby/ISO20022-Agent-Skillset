---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000365-issuer-csd"
title: "Issuer CSD"
source_labels: ["Issuer CSD"]
role_type: "source-scoped functional participant"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
source_locations: [{"source_id": "src-000365", "locator": "P58; P233-P235"}]
message_sets: ["t2s-link-reference-data"]
message_ids: ["reda.045.001.01", "reda.047.001.01", "reda.049.001.01", "reda.051.001.01"]
flows: ["flow-src-000365-p120-link-creation-process"]
aliases: []
limitations: ["No identifier scheme or general institution equivalence is stated in this passage."]
---



# Issuer CSD

A CSD identified as the issuer-side endpoint of a Security CSD Link. P58 lists its identification among link-creation data; example P233-P235 links ISIN XXABCDEFGHI1 to issuer CSD CSDAXXYYAAA. The source does not say this endpoint necessarily sends the request.

Source [src-000365](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`; P58; P233-P235.

Link-reference source context: [Link creation activity with validation and retry](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/diagrams/curated/fig-0007.md). [flow Link Creation Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p120-link-creation-process.md).
