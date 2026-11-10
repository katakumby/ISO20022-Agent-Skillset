---
template: false
document_kind: "participant"
review_status: "reviewed"
manual_curated: true
domain: "shared"
domains: ["payments"]
participant_id: "participant-src-000173-head-office"
title: "Head Office"
source_labels: ["Head Office"]
role_type: "Narrative institutional example"
aliases: []
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
source_locations: [{"source_id": "src-000173", "locator": "P194; P197; figures17–18"}]
flow_ids: ["flow-src-000173-p192-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play", "flow-src-000173-p195-one-actor-plays-roles-of-initiating-party-and-ultimate-debtor-second-a"]
message_ids: []
limitations: ["These are separate source scenarios: do not collapse their debtor/ultimate-debtor roles.", "No participant identifier scheme is specified in the cited evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative and original figure evidence inspected."}
---









# Head Office

[src-000173](../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx)

## Definition, context and responsibilities

In one relay example it is debtor and initiating party for subsidiary ultimate debtors. In another it is initiating party and ultimate debtor while a foreign subsidiary supplies the debtor account. (P194; P197; figures17–18)

Role classification: Narrative institutional example.

## Relationships

- [subsidiary](participant-src-000173-subsidiary.md)
- [initiating party](participant-src-000173-initiating-party.md)
- [debtor](participant-src-000173-debtor.md)
- [ultimate debtor](participant-src-000173-ultimate-debtor.md)

## Identifier schemes and limitations

These are separate source scenarios: do not collapse their debtor/ultimate-debtor roles.

No participant identifier scheme is specified in this bounded evidence. Functional roles describe relationships, not permanent institutional identities. Message and flow links are maintained below.

<!-- INITIATION-FLOW-192 -->
[One actor plays roles of Initiating Party and Debtor, Second Actor plays role of Ultimate Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p192-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play.md)
<!-- /INITIATION-FLOW-192 -->

<!-- INITIATION-FLOW-195 -->
[One actor plays roles of Initiating Party and Ultimate Debtor, Second Actor plays role of Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p195-one-actor-plays-roles-of-initiating-party-and-ultimate-debtor-second-a.md)
<!-- /INITIATION-FLOW-195 -->
