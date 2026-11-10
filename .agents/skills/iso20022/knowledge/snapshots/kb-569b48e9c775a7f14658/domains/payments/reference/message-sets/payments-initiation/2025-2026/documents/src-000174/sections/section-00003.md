---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [3]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13", "pain.002.001.15", "pain.007.001.13", "pain.008.001.12"]
---

# 1 Message Set Overview

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 3 to 3.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3

```text
1 Message Set Overview
Introduction
This document describes the Payments Initiation message set. It includes the new version of the
MessageDefinitions that have been added as part of the maintenance cycle 2025-2026 (See MCR
#277) and approved by the Payments Standards Evaluation Group on 12 January 2026.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
pain.001.001.13
CustomerCreditTransferInitiationV13
The CustomerCreditTransferInitiation message is sent
by the initiating party to the forwarding agent or debtor
agent. It is used to request movement of funds from
the debtor account to a creditor.
pain.002.001.15
CustomerPaymentStatusReportV15
The CustomerPaymentStatusReport message is sent
by an instructed agent to the previous party in the
payment chain. It is used to inform this party about the
positive or negative status of an instruction (either
single or file). It is also used to report on a pending
instruction.
pain.007.001.13
CustomerPaymentReversalV13
The CustomerPaymentReversal message is sent by
the initiating party to the next party in the payment
chain. It is used to reverse a payment previously
executed.
pain.008.001.12
CustomerDirectDebitInitiationV12
The CustomerDirectDebitInitiation message is sent by
the initiating party to the forwarding agent or creditor
agent. It is used to request single or bulk collection(s)
of funds from one or various debtor's account(s) for a
creditor.
Approved by the Payments SEG on 12 January 2026 Message Set Overview
Payments Initiation - Maintenance 2025 - 2026 3 March 2026
```

