---
template: false
document_kind: "business-rules"
manual_curated: true
review_status: "reviewed"
title: "Link creation, maintenance and lifecycle rules"
domain: "securities"
source_ids: ["src-000365"]
message_sets: ["t2s-link-reference-data"]
message_ids: ["reda.045.001.01", "reda.046.001.01", "reda.047.001.01", "reda.049.001.01", "reda.050.001.01", "reda.051.001.01"]
source_locations: [{"source_id": "src-000365", "locator": "P57–P96; T8/T9/T11/T12; P145–P227"}]
limitations: ["Part1 business statements are not a substitute for exact schema cardinalities."]
review_date: "2026-11-09"
source_editions: ["december-2024"]
---

# Link creation, maintenance and lifecycle rules

[src-000365](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`; P57–P96.

Security CSD Link creation links a financial instrument to an issuer or investor CSD. P58 lists financial-instrument, CSD, technical-issuer and issuance-account identifications, maintenance responsibility, and validity dates. Account Link creation links securities and dedicated cash accounts; P76–P80 lists default use for settlement, auto-collateralisation and cash legs, plus validity dates. Maintenance updates an existing corresponding link. These are source business descriptions; the exact XSD determines field/group cardinalities.

For either link, REJECTED may have multiple reasons: missing/incorrect mandatory data, a request not being a new occurrence, inadequate creation rights, or a request already received and being processed (P64–P69/P87–P92). Modification can additionally fail because data cannot be updated (P216–P227). QUEUED means processing has been delayed; a valid request blocked by timing is submitted again to validation after a specific event (T11/T12). COMPLETED means successful processing. A request may be rejected after revalidation with new data.

Creation requires a known, privileged Instructing Party that identified a coverage gap and needs the link for its activities (T8). Modification requires the known, privileged party and a changed link attribute (T9). Both source postconditions are acknowledgment of processing. No cancellation or reversal messages are supplied for these flows.

| Flow | Source |
| --- | --- |
| [Creation](flows/flow-src-000365-p120-link-creation-process.md) | T8/T11 |
| [Modification](flows/flow-src-000365-p122-link-modification-process.md) | T9/T12 |



Source business descriptions and complete Word7–9/12–22 compared. Supplied examples remain separately qualified under [issue-000053](example-consistency.md).

| Supplied example | Exact definition |
| --- | --- |
| [Security CSD Link Creation Request](examples/security-csd-creation.md) | reda.045.001.01 |
| [Security CSD Link Modification Request](examples/security-csd-maintenance.md) | reda.046.001.01 |
| [Security CSD Link Status Advice — completed](examples/security-csd-status-completed.md) | reda.047.001.01 |
| [Security CSD Link Status Advice — queued](examples/security-csd-status-queued.md) | reda.047.001.01 |
| [Security CSD Link Status Advice — rejected](examples/security-csd-status-rejected.md) | reda.047.001.01 |
| [Account Link Creation Request](examples/account-link-creation.md) | reda.049.001.01 |
| [Account Link Maintenance Request](examples/account-link-maintenance.md) | reda.050.001.01 |
| [Account Link Status Advice — completed](examples/account-link-status-completed.md) | reda.051.001.01 |
| [Account Link Status Advice — queued](examples/account-link-status-queued.md) | reda.051.001.01 |
| [Account Link Status Advice — rejected](examples/account-link-status-rejected.md) | reda.051.001.01 |

