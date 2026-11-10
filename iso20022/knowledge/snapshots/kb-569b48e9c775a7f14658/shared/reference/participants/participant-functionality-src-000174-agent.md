---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["payments"]
participant_id: "participant-functionality-src-000174-agent"
title: "agent — Payments Initiation Functionality"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
source_labels: ["agent"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["payments-initiation"]
message_ids: ["pain.001.001.13", "pain.002.001.15", "pain.007.001.13", "pain.008.001.12"]
message_families: ["pain.001", "pain.002", "pain.007", "pain.008"]
source_locations: [{"source_id": "src-000174", "heading": "2 pain.001.001.13 CustomerCreditTransferInitiationV13", "file_pages": [4], "evidence_id": "src-000174-pain.001.001.13-p4-c001"}, {"source_id": "src-000174", "heading": "2 pain.001.001.13 CustomerCreditTransferInitiationV13", "file_pages": [4], "evidence_id": "src-000174-pain.001.001.13-p4-c004"}, {"source_id": "src-000174", "heading": "2 pain.001.001.13 CustomerCreditTransferInitiationV13", "file_pages": [4], "evidence_id": "src-000174-pain.001.001.13-p4-c006"}, {"source_id": "src-000174", "heading": "2 pain.001.001.13 CustomerCreditTransferInitiationV13", "file_pages": [4], "evidence_id": "src-000174-pain.001.001.13-p4-c007"}, {"source_id": "src-000174", "heading": "2 pain.001.001.13 CustomerCreditTransferInitiationV13", "file_pages": [4], "evidence_id": "src-000174-pain.001.001.13-p4-c008"}, {"source_id": "src-000174", "heading": "2 pain.001.001.13 CustomerCreditTransferInitiationV13", "file_pages": [4], "evidence_id": "src-000174-pain.001.001.13-p4-c009"}, {"source_id": "src-000174", "heading": "2 pain.001.001.13 CustomerCreditTransferInitiationV13", "file_pages": [4], "evidence_id": "src-000174-pain.001.001.13-p4-c010"}, {"source_id": "src-000174", "heading": "2 pain.001.001.13 CustomerCreditTransferInitiationV13", "file_pages": [4], "evidence_id": "src-000174-pain.001.001.13-p4-c013"}, {"source_id": "src-000174", "heading": "3 pain.002.001.15 CustomerPaymentStatusReportV15", "file_pages": [130], "evidence_id": "src-000174-pain.002.001.15-p130-c001"}, {"source_id": "src-000174", "heading": "3 pain.002.001.15 CustomerPaymentStatusReportV15", "file_pages": [130], "evidence_id": "src-000174-pain.002.001.15-p130-c004"}, {"source_id": "src-000174", "heading": "3 pain.002.001.15 CustomerPaymentStatusReportV15", "file_pages": [130], "evidence_id": "src-000174-pain.002.001.15-p130-c005"}, {"source_id": "src-000174", "heading": "4 pain.007.001.13 CustomerPaymentReversalV13", "file_pages": [272], "evidence_id": "src-000174-pain.007.001.13-p272-c002"}, {"source_id": "src-000174", "heading": "5 pain.008.001.12 CustomerDirectDebitInitiationV12", "file_pages": [403], "evidence_id": "src-000174-pain.008.001.12-p403-c001"}, {"source_id": "src-000174", "heading": "5 pain.008.001.12 CustomerDirectDebitInitiationV12", "file_pages": [403], "evidence_id": "src-000174-pain.008.001.12-p403-c004"}, {"source_id": "src-000174", "heading": "5 pain.008.001.12 CustomerDirectDebitInitiationV12", "file_pages": [403], "evidence_id": "src-000174-pain.008.001.12-p403-c005"}, {"source_id": "src-000174", "heading": "5 pain.008.001.12 CustomerDirectDebitInitiationV12", "file_pages": [403], "evidence_id": "src-000174-pain.008.001.12-p403-c006"}, {"source_id": "src-000174", "heading": "5 pain.008.001.12 CustomerDirectDebitInitiationV12", "file_pages": [403], "evidence_id": "src-000174-pain.008.001.12-p403-c007"}, {"source_id": "src-000174", "heading": "5 pain.008.001.12 CustomerDirectDebitInitiationV12", "file_pages": [403], "evidence_id": "src-000174-pain.008.001.12-p403-c008"}, {"source_id": "src-000174", "heading": "5 pain.008.001.12 CustomerDirectDebitInitiationV12", "file_pages": [403], "evidence_id": "src-000174-pain.008.001.12-p403-c011"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# agent — Payments Initiation Functionality

[src-000174](../../../evidence/omitted/577241d5215d98d6ed689f57.md)

## Definition and business context

Generic agent function explicitly named in this publication’s quoted message Functionality. Its precise capacity and counterparties are retained per clause rather than being inferred from the generic label.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000174-pain.001.001.13-p4-c001

src-000174, file page 4; 2 pain.001.001.13 CustomerCreditTransferInitiationV13.

> The CustomerCreditTransferInitiation message is sent by the initiating party to the forwarding agent or debtor agent.

### src-000174-pain.001.001.13-p4-c004

src-000174, file page 4; 2 pain.001.001.13 CustomerCreditTransferInitiationV13.

> Payment transactions that result in book transfers at the debtor agent or payments to another financial institution;

### src-000174-pain.001.001.13-p4-c006

src-000174, file page 4; 2 pain.001.001.13 CustomerCreditTransferInitiationV13.

> In a direct scenario, the message is sent directly to the debtor agent.

### src-000174-pain.001.001.13-p4-c007

src-000174, file page 4; 2 pain.001.001.13 CustomerCreditTransferInitiationV13.

> The debtor agent is the account servicer of the debtor.

### src-000174-pain.001.001.13-p4-c008

src-000174, file page 4; 2 pain.001.001.13 CustomerCreditTransferInitiationV13.

> In a relay scenario, the message is sent to a forwarding agent.

### src-000174-pain.001.001.13-p4-c009

src-000174, file page 4; 2 pain.001.001.13 CustomerCreditTransferInitiationV13.

> The forwarding agent acts as a concentrating financial institution.

### src-000174-pain.001.001.13-p4-c010

src-000174, file page 4; 2 pain.001.001.13 CustomerCreditTransferInitiationV13.

> It will forward the CustomerCreditTransferInitiation message to the debtor agent.

### src-000174-pain.001.001.13-p4-c013

src-000174, file page 4; 2 pain.001.001.13 CustomerCreditTransferInitiationV13.

> The CustomerCreditTransferInitiation message must not be used by the debtor agent to execute the credit transfer instruction(s).

### src-000174-pain.002.001.15-p130-c001

src-000174, file page 130; 3 pain.002.001.15 CustomerPaymentStatusReportV15.

> The CustomerPaymentStatusReport message is sent by an instructed agent to the previous party in the payment chain.

### src-000174-pain.002.001.15-p130-c004

src-000174, file page 130; 3 pain.002.001.15 CustomerPaymentStatusReportV15.

> The CustomerPaymentStatusReport message is exchanged between an agent and a non-financial institution customer to provide status information on instructions previously sent.

### src-000174-pain.002.001.15-p130-c005

src-000174, file page 130; 3 pain.002.001.15 CustomerPaymentStatusReportV15.

> Its usage may be governed by a bilateral or multilateral agreement between the agent and the non-financial institution customer.

### src-000174-pain.007.001.13-p272-c002

src-000174, file page 272; 4 pain.007.001.13 CustomerPaymentReversalV13.

> The CustomerPaymentReversal message is exchanged between a non-financial institution customer and an agent to reverse a CustomerDirectDebitInitiation message that has been settled.

### src-000174-pain.008.001.12-p403-c001

src-000174, file page 403; 5 pain.008.001.12 CustomerDirectDebitInitiationV12.

> The CustomerDirectDebitInitiation message is sent by the initiating party to the forwarding agent or creditor agent.

### src-000174-pain.008.001.12-p403-c004

src-000174, file page 403; 5 pain.008.001.12 CustomerDirectDebitInitiationV12.

> In a direct scenario, the message is sent directly to the creditor agent.

### src-000174-pain.008.001.12-p403-c005

src-000174, file page 403; 5 pain.008.001.12 CustomerDirectDebitInitiationV12.

> The creditor agent is the account servicer of the creditor.

### src-000174-pain.008.001.12-p403-c006

src-000174, file page 403; 5 pain.008.001.12 CustomerDirectDebitInitiationV12.

> In a relay scenario, the message is sent to a forwarding agent.

### src-000174-pain.008.001.12-p403-c007

src-000174, file page 403; 5 pain.008.001.12 CustomerDirectDebitInitiationV12.

> The forwarding agent acts as a concentrating financial institution.

### src-000174-pain.008.001.12-p403-c008

src-000174, file page 403; 5 pain.008.001.12 CustomerDirectDebitInitiationV12.

> It will forward the CustomerDirectDebitInitiation message to the creditor agent.

### src-000174-pain.008.001.12-p403-c011

src-000174, file page 403; 5 pain.008.001.12 CustomerDirectDebitInitiationV12.

> The CustomerDirectDebitInitiation message must not be used by the creditor agent to execute the direct debit instruction(s).

## Applicable exact messages


- [pain.001.001.13](../../../domains/payments/reference/messages/pain.001.001.13/roles.md)
- [pain.002.001.15](../../../domains/payments/reference/messages/pain.002.001.15/roles.md)
- [pain.007.001.13](../../../domains/payments/reference/messages/pain.007.001.13/roles.md)
- [pain.008.001.12](../../../domains/payments/reference/messages/pain.008.001.12/roles.md)

## Identity and unresolved scope

Source labels: agent. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
