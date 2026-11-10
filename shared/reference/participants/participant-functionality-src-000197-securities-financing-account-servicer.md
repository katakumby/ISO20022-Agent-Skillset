---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000197-securities-financing-account-servicer"
title: "securities financing transaction account servicer — Settlement and Reconciliation Functionality"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
source_labels: ["securities financing transaction account servicer"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["settlement-and-reconciliation"]
message_ids: ["sese.033.001.13", "sese.034.001.11", "sese.035.001.13", "sese.036.001.10"]
message_families: ["sese.033", "sese.034", "sese.035", "sese.036"]
source_locations: [{"source_id": "src-000197", "heading": "27 sese.033.001.13 SecuritiesFinancingInstructionV13", "file_pages": [879], "evidence_id": "src-000197-sese.033.001.13-p879-c001"}, {"source_id": "src-000197", "heading": "28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "file_pages": [951], "evidence_id": "src-000197-sese.034.001.11-p951-c001"}, {"source_id": "src-000197", "heading": "29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "file_pages": [994], "evidence_id": "src-000197-sese.035.001.13-p994-c001"}, {"source_id": "src-000197", "heading": "30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10", "file_pages": [1059], "evidence_id": "src-000197-sese.036.001.10-p1059-c001"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# securities financing transaction account servicer — Settlement and Reconciliation Functionality

[src-000197](../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf)

## Definition and business context

Account-servicer function specifically scoped by the source to securities-financing transactions. The named responsibilities and relationships remain those of the quoted message clauses.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000197-sese.033.001.13-p879-c001

src-000197, file page 879; 27 sese.033.001.13 SecuritiesFinancingInstructionV13.

> An account owner sends a SecuritiesFinancingInstruction to a securities financing transaction account servicer to notify the securities financing transaction account servicer of the details of a repurchase agreement, reverse repurchase agreement, securities lending or securities borrowing transaction to allow the account servicer to manage the settlement and follow-up of the opening and closing leg of the transaction.

### src-000197-sese.034.001.11-p951-c001

src-000197, file page 951; 28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11.

> An securities financing transaction account servicer sends a SecuritiesFinancingStatusAdvice to an account owner to advise the status of a securities financing transaction previously instructed by the account owner.

### src-000197-sese.035.001.13-p994-c001

src-000197, file page 994; 29 sese.035.001.13 SecuritiesFinancingConfirmationV13.

> A securities financing transaction account servicer sends a SecuritiesFinancingConfirmation to an account owner to confirm or advise of the partial or full settlement of the opening or closing leg of a securities financing transaction.

### src-000197-sese.036.001.10-p1059-c001

src-000197, file page 1059; 30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10.

> An account owner sends a SecuritiesFinancingModificationInstruction to a securities financing transaction account servicer to notify the securities financing transaction account servicer of an update in the details of a repurchase agreement, reverse repurchase agreement, securities lending or securities borrowing transaction that does not impact the original transaction securities quantity.

## Applicable exact messages


- [sese.033.001.13](../../../domains/securities/reference/messages/sese.033.001.13/roles.md)
- [sese.034.001.11](../../../domains/securities/reference/messages/sese.034.001.11/roles.md)
- [sese.035.001.13](../../../domains/securities/reference/messages/sese.035.001.13/roles.md)
- [sese.036.001.10](../../../domains/securities/reference/messages/sese.036.001.10/roles.md)

## Identity and unresolved scope

Source labels: securities financing transaction account servicer. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
