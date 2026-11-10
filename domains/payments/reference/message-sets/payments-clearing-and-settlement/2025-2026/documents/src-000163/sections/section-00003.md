---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [4, 5]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16", "pacs.003.001.12", "pacs.004.001.15", "pacs.007.001.14", "pacs.008.001.14", "pacs.009.001.13", "pacs.010.001.06", "pacs.028.001.07"]
---

# 1 Message Set Overview

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 4 to 5.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4

```text
1 Message Set Overview
Introduction
This document describes the Payments Clearing and Settlement message set. It includes the new
version of the MessageDefinitions that have been added as part of the maintenance cycle 2025-2026
(See MCR #277) and approved by the Payments Standards Evaluation Group on 12 January 2026.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
pacs.002.001.16
FIToFIPaymentStatusReportV16
The FIToFIPaymentStatusReport message is sent by
an instructed agent to the previous party in the
payment chain. It is used to inform this party about the
positive or negative status of an instruction (either
single or file). It is also used to report on a pending
instruction.
pacs.003.001.12
FIToFICustomerDirectDebitV12
The
FinancialInstitutionToFinancialInstitutionCustomerDirec
tDebit message is sent by the creditor agent to the
debtor agent, directly or through other agents and/or a
payment clearing and settlement system.
It is used to collect funds from a debtor account for a
creditor.
pacs.004.001.15
PaymentReturnV15
The PaymentReturn message is sent by an agent to
the previous agent in the payment chain to undo a
payment previously settled.
pacs.007.001.14
FIToFIPaymentReversalV14
The
FinancialInstitutionToFinancialInstitutionPaymentRever
sal message is sent by an agent to the next party in the
payment chain. It is used to reverse a payment
previously executed.
pacs.008.001.14
FIToFICustomerCreditTransferV14
The
FinancialInstitutionToFinancialInstitutionCustomerCredi
tTransfer message is sent by the debtor agent to the
creditor agent, directly or through other agents and/or a
payment clearing and settlement system. It is used to
move funds from a debtor account to a creditor.
pacs.009.001.13
FinancialInstitutionCreditTransferV13
The FinancialInstitutionCreditTransfer message is sent
by a debtor financial institution to a creditor financial
institution, directly or through other agents and/or a
payment clearing and settlement system.
It is used to move funds from a debtor account to a
creditor, where both debtor and creditor are financial
institutions.
pacs.010.001.06
FinancialInstitutionDirectDebitV06
Scope:
The FinancialInstitutionDirectDebit message is sent by
an exchange or clearing house, or a financial
institution, directly or through another agent, to the
DebtorAgent. It is used to instruct the DebtorAgent to
move funds from one or more debtor(s) account(s) to
Approved by the Payments SEG on 12 January 2026 Message Set Overview
Payments Clearing and Settlement - Maintenance 2025 -
2026
4 March 2026
```

## File page 5

```text
MessageDefinition Definition
one or more creditor(s), where both debtor and creditor
are financial institutions.
Usage:
The FinancialInstitutionDirectDebit message is
exchanged between agents and can contain one or
more financial institution direct debit instruction(s) for
one or more creditor(s). The
FinancialInstitutionDirectDebit message can be used in
domestic and cross-border scenarios.
pacs.028.001.07
FIToFIPaymentStatusRequestV07
The
FinancialInstitutionToFinancialInstitutionPaymentStatu
sRequest message is sent by the debtor agent to the
creditor agent, directly or through other agents and/or a
payment clearing and settlement system. It is used to
request a FIToFIPaymentStatusReport message
containing information on the status of a previously
sent instruction.
Approved by the Payments SEG on 12 January 2026 Message Set Overview
Payments Clearing and Settlement - Maintenance 2025 -
2026
5 March 2026
```

