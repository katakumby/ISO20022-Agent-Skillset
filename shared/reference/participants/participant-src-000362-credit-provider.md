---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000362-credit-provider"
title: "Credit Provider"
source_labels: ["Credit Provider"]
role_type: "source-scoped functional participant"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
source_locations: [{"source_id": "src-000362", "locator": "P62/P65/P77/P153"}]
message_sets: ["t2s-limit-utilisation-journal"]
message_ids: ["camt.064.001.01", "camt.065.001.01"]
flows: ["flow-src-000362-p137-pull-mode", "flow-src-000362-p143-push-mode"]
aliases: []
limitations: ["No identifier scheme or general institution equivalence is stated in this passage."]
---









# Credit Provider

Manages the cash limits whose amount, utilisation and transaction journal are queried and reported. P65 expressly describes an NCB acting as parent and credit provider; the role is not equated with the query sender in every case.

Source [src-000362](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`; P62/P65/P77/P153.

Limit-journal source context: [Participant-triggered limit-journal pull activity](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0010.md). [flow Pull mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md).

Limit-journal source context: [Scheduled limit-journal push activity](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0011.md). [flow Push mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p143-push-mode.md).

Limit-journal source context: [Limit-journal business transaction exchange](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0012.md). [flow Pull mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md).

Related contextual roles: [national central bank ncb](participant-src-000362-national-central-bank-ncb.md), [central securities depositories csd](participant-src-000362-central-securities-depositories-csd.md), [payment bank](participant-src-000362-payment-bank.md). The source examples identify parties with AnyBIC/BICFI and dedicated cash account9000000123 (P169-P170/P192/P197/P223/P230/P241); these are example values, not a universal institution assignment.
