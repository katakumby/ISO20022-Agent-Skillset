---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000053-global-clearing-member-buyer"
title: "global clearing member of the buyer — CCP Clearing Functionality"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
source_labels: ["global clearing member of the buyer"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["ccp-clearing"]
message_ids: ["secl.001.001.05"]
message_families: ["secl.001"]
source_locations: [{"source_id": "src-000053", "heading": "2 MX secl.001.001.05 TradeLegNotificationV05", "file_pages": [6], "evidence_id": "src-000053-secl.001.001.05-p6-c003"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# global clearing member of the buyer — CCP Clearing Functionality

[src-000053](../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf)

## Definition and business context

Buyer-side global clearing member to which the CCP sends the other TradeLegNotification. Its distinct buyer-side relationship is retained, and global is not silently replaced by general.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000053-secl.001.001.05-p6-c003

src-000053, file page 6; 2 MX secl.001.001.05 TradeLegNotificationV05.

> The CCP sends a message to the global clearing member of the seller and a message to the global clearing member of the buyer.

## Applicable exact messages


- [secl.001.001.05](../../../domains/securities/reference/messages/secl.001.001.05/roles.md)

## Identity and unresolved scope

Source labels: global clearing member of the buyer. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
