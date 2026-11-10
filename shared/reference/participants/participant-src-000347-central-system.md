---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000347-central-system"
title: "Central System"
source_labels: ["Central System"]
role_type: "source-scoped operational participant"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
source_locations: [{"source_id": "src-000347", "locator": "T8 rows2-4"}]
message_sets: ["t2s-billing"]
message_ids: ["camt.076.001.01", "camt.077.001.01"]
flows: ["flow-src-000347-p110-billing-report"]
aliases: []
limitations: ["No identifier scheme is assigned to this role in the cited passage. Contextual functional-role correspondences do not identify a particular institution."]
---



# Central System

The system named in the formal billing-process definition and trigger. The source does not separately define its identity relative to the activity participant labels.

## Responsibilities and relationships

Sends invoices, cancellation status, consumption data, or query responses; retains invoice data and generates corresponding-period billing events. The record remains distinct from the separately defined Central Database System.

Source [src-000347](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`; T8 rows2-4.

Billing source context: [Billing process overview](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0002.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p110-billing-report.md).
