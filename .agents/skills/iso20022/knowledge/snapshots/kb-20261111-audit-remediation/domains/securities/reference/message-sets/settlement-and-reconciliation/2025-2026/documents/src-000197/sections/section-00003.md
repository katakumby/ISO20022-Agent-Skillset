---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12", "semt.003.001.12", "semt.013.001.07", "semt.014.001.09", "semt.015.001.10", "semt.016.001.10", "semt.017.001.14", "semt.018.001.15", "semt.019.001.12", "semt.020.001.07", "semt.021.001.09", "semt.022.001.07", "sese.020.001.09", "sese.021.001.08", "sese.022.001.08", "sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.026.001.12", "sese.027.001.09", "sese.028.001.12", "sese.029.001.08", "sese.030.001.10", "sese.031.001.11", "sese.032.001.13", "sese.033.001.13", "sese.034.001.11", "sese.035.001.13", "sese.036.001.10"]
---

# 1 Message Set Overview

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 7 to 16.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 7

```text
1 Message Set Overview
Introduction
This document describes the Settlement And Reconciliation message set. It includes the new version of
the MessageDefinitions that have been added as part of the maintenance cycle 2025-2026 (See MCR
#XXX) and approved by the Securities Standards Evaluation Group on 27 January 2026.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
semt.002.001.12
SecuritiesBalanceCustodyReportV12
An account servicer sends a
SecuritiesBalanceCustodyReport to an account owner
to provide, at a moment in time, the quantity and
identification of the financial instruments that the
account servicer holds for the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of their
participants, or
- an agent (sub-custodian) acting on behalf of their
global custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer, or
- a transfer agent acting on behalf of a fund manager
or an account owner's designated agent.
semt.003.001.12
SecuritiesBalanceAccountingReportV12
An account servicer sends a
SecuritiesBalanceAccountingReport to an account
owner to provide, at a moment in time, valuations of
the portfolio together with details of each financial
instrument holding.
The account servicer/owner relationship may be:
- an accounting agent acting on behalf of an account
owner, or
- a transfer agent acting on behalf of a fund manager
or an account owner's designated agent.
semt.013.001.07
IntraPositionMovementInstructionV07
An account owner sends a
IntraPositionMovementInstruction to an account
servicer to instruct the movement of securities within its
holding from one sub-balance to another, for example,
blocking of securities.
The account owner/servicer relationship may be:
- a global custodian which has an account with its local
agent (sub-custodian), or
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Settlement And Reconciliation - Maintenance 2025 - 2026 7 March 2026
```

## File page 8

```text
MessageDefinition Definition
- an investment management institution which manage
a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository participant which has
an account with a central securities depository, or
- a central securities depository which has an account
with a custodian, another central securities depository
or another settlement market infrastructure.
semt.014.001.09
IntraPositionMovementStatusAdviceV09
An account servicer sends a
IntraPositionMovementStatusAdvice to an account
owner to advise the status of an intra-position
movement instruction previously sent by the account
owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their
global custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
semt.015.001.10
IntraPositionMovementConfirmationV10
The IntraPositionMovementConfirmation is sent by an
account servicer to an account owner to confirm the
movement of securities within its holding from one sub-
balance to another, for example, blocking of securities.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of its participant
- an agent (sub-custodian) acting on behalf of its global
custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
semt.016.001.10
IntraPositionMovementPostingReportV10
The IntraPositionMovementPostingReport is sent by an
account servicer to an account owner to provide the
details of increases and decreases in securities with a
given status within a holding, that is, intra-position
transfers, which occurred during a specified period, for
all or selected securities in a specified safekeeping
account which the account servicer holds for the
account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of its participant
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Settlement And Reconciliation - Maintenance 2025 - 2026 8 March 2026
```

## File page 9

```text
MessageDefinition Definition
- an agent (sub-custodian) acting on behalf of its global
custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
semt.017.001.14
SecuritiesTransactionPostingReportV14
SecuritiesTransactionPostingReport is sent by an
account servicer to an account owner to provide the
details of increases and decreases of holdings which
occurred during a specified period, for all or selected
securities in the specified safekeeping account or sub-
safekeeping account which the account servicer holds
for the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of its participants
- an agent (sub-custodian) acting on behalf of its global
custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
semt.018.001.15
SecuritiesTransactionPendingReportV15
SecuritiesTransactionPendingReport is sent by an
account servicer to an account owner to provide, as at
a specified time, the details of pending increases and
decreases of holdings, for all or selected securities in a
specified safekeeping account, for all or selected
reasons why the transaction is pending.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of its participants
- an agent (sub-custodian) acting on behalf of its global
custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
semt.019.001.12
SecuritiesSettlementTransactionAllegementRep
ortV12
An account servicer sends a
SecuritiesSettlementTransactionAllegementReport to
an account owner to provide, at a specified time, the
status and details of pending settlement allegements,
for all or selected securities in a specified safekeeping
account.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their
global custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Settlement And Reconciliation - Maintenance 2025 - 2026 9 March 2026
```

## File page 10

```text
MessageDefinition Definition
semt.020.001.07
SecuritiesMessageCancellationAdviceV07
An account servicer sends a
SecuritiesMessageCancellationAdvice to an account
owner to inform of the cancellation of a securities
message previously sent by an account servicer.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their
global custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
semt.021.001.09
SecuritiesStatementQueryV09
An account owner sends a SecuritiesStatementQuery
to an account servicer to request any existing
securities statement.
The account owner/servicer relationship may be:
- a global custodian which has an account with a local
custodian, or
- an investment management institution which manage
a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository participant which has
an account with a central securities depository, or
- a central securities depository which has an account
with a custodian, another central securities depository
or another settlement market infrastructure, or
- a central counterparty or a stock exchange or a trade
matching utility which need to instruct to a central
securities depository or another settlement market
infrastructure.
semt.022.001.07
SecuritiesSettlementTransactionAuditTrailRepor
tV07
This message is sent by the Market Infrastructure to
the CSD to advise of the history of all the statuses,
modifications, replacement and cancellation of a
specific transaction during its whole life cycle when the
instructing party is a direct participant to the Settlement
Infrastructure.
sese.020.001.09
SecuritiesTransactionCancellationRequestV09
An account owner sends a
SecuritiesTransactionCancellationRequest to an
account servicer to request the cancellation of a
securities transaction.
The account owner/servicer relationship may be:
- a global custodian which has an account with a local
custodian, or
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Settlement And Reconciliation - Maintenance 2025 - 2026 10 March 2026
```

## File page 11

```text
MessageDefinition Definition
- an investment management institution which manage
a fund account opened at a custodian, or - a broker
which has an account with a custodian, or
- a central securities depository participant which has
an account with a central securities depository, or
- a central securities depository which has an account
with a custodian, another central securities depository
or another settlement market infrastructure, or
- a central counterparty or a stock exchange or a trade
matching utility which need to instruct to a central
securities depository or another settlement market
infrastructure.
sese.021.001.08
SecuritiesTransactionStatusQueryV08
An account owner sends a
SecuritiesTransactionStatusQuery to an account
servicer to request a status on a securities transaction.
The account owner/servicer relationship may be:
- a global custodian which has an account with a local
custodian, or
- an investment management institution which manage
a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository participant which has
an account with a central securities depository, or
- a central securities depository which has an account
with a custodian, another central securities depository
or another settlement market infrastructure, or
- a central counterparty or a stock exchange or a trade
matching utility which need to instruct to a central
securities depository or another settlement market
infrastructure.
sese.022.001.08
SecuritiesStatusOrStatementQueryStatusAdvic
eV08
An account servicer sends a
SecuritiesStatusOrStatementQueryStatusAdvice to an
account owner to advise the status of a status query or
statement query previously sent by the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their
global custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
An account owner sends a
SecuritiesSettlementTransactionInstruction to an
account servicer to instruct the receipt or delivery of
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Settlement And Reconciliation - Maintenance 2025 - 2026 11 March 2026
```

## File page 12

```text
MessageDefinition Definition
financial instruments with or without payment,
physically or by book-entry.
The account owner/servicer relationship may be:
- a global custodian which has an account with a local
custodian, or
- an investment management institution which
manages a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository participant which has
an account with a central securities depository, or
- a central securities depository which has an account
with a custodian, another central securities depository
or another settlement market infrastructure, or
- a central counterparty or a stock exchange or a trade
matching utility which need to instruct the settlement of
transactions to a central securities depository or
another settlement market infrastructure.
sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV
14
An account servicer sends a
SecuritiesSettlementTransactionStatusAdvice to an
account owner to advise the status of a securities
settlement transaction instruction previously sent by
the account owner or the status of a settlement
transaction existing in the books of the servicer for the
account of the owner. The status may be a processing,
pending processing, internal matching, matching
and/or settlement status.
The status advice may be sent as a response to the
request of the account owner or not.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their
global custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
sese.025.001.13
SecuritiesSettlementTransactionConfirmationV1
3
An account servicer sends a
SecuritiesSettlementTransactionConfirmation to an
account owner to confirm the partial or full delivery or
receipt of financial instruments, free or against of
payment, physically or by book-entry.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of their
participants
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Settlement And Reconciliation - Maintenance 2025 - 2026 12 March 2026
```

## File page 13

```text
MessageDefinition Definition
- an agent (sub-custodian) acting on behalf of their
global custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
sese.026.001.12
SecuritiesSettlementTransactionReversalAdvice
V12
An account servicer sends a
SecuritiesSettlementTransactionReversalAdvice to an
account owner to reverse the confirmation of a partial
or full delivery or receipt of financial instruments, free
or against of payment, physically or by book-entry.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their
global custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
sese.027.001.09
SecuritiesTransactionCancellationRequestStatu
sAdviceV09
An account servicer sends an
SecuritiesTransactionCancellationRequestStatusAdvic
e to an account owner to advise the status of a
securities transaction cancellation request previously
sent by the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their
global custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
sese.028.001.12
SecuritiesSettlementTransactionAllegementNoti
ficationV12
An account servicer sends a
SecuritiesSettlementTransactionAllegementNotification
to an account owner to advise the account owner that
a counterparty has alleged an instruction against the
account owner's account at the account servicer and
that the account servicer could not find the
corresponding instruction of the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their
global custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Settlement And Reconciliation - Maintenance 2025 - 2026 13 March 2026
```

## File page 14

```text
MessageDefinition Definition
sese.029.001.08
SecuritiesSettlementAllegementRemovalAdvice
V08
An account servicer sends a
SecuritiesSettlementAllegementRemovalAdvice to an
account owner to acknowledge that a previously sent
allegement is no longer outstanding, because the
alleged party sent its instruction.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their
global custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
sese.030.001.10
SecuritiesSettlementConditionsModificationReq
uestV10
An account owner sends a
SecuritiesSettlementConditionsModificationRequest to
an account servicer to request the modification of a
processing indicator or another non-matching
information.
The account owner/servicer relationship may be:
- a central securities depository participant which has
an account with a central securities depository.
It could also be, if agreed in a service level agreement:
- a global custodian which has an account with its local
agent (sub-custodian), or
- an investment management institution which manage
a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository which has an account
with a custodian, another central securities depository
or another settlement market infrastructure.
sese.031.001.11
SecuritiesSettlementConditionModificationStatu
sAdviceV11
An account servicer sends a
SecuritiesSettlementConditionsModificationStatusAdvi
ce to an account owner to advise the status of a
modification request previously instructed by the
account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their
global custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Settlement And Reconciliation - Maintenance 2025 - 2026 14 March 2026
```

## File page 15

```text
MessageDefinition Definition
sese.032.001.13
SecuritiesSettlementTransactionGenerationNoti
ficationV13
An account servicer sends a
SecuritiesSettlementTransactionGenerationNotification
to an account owner to advise the account owner of a
securities settlement transaction that has been
generated/created by the account servicer for the
account owner. The reason for creation can range from
the automatic transformation of pending settlement
instructions following a corporate event to the recovery
of an account owner transactions' database initiated by
its account servicer.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their
global custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer
sese.033.001.13
SecuritiesFinancingInstructionV13
An account owner sends a
SecuritiesFinancingInstruction to a securities financing
transaction account servicer to notify the securities
financing transaction account servicer of the details of
a repurchase agreement, reverse repurchase
agreement, securities lending or securities borrowing
transaction to allow the account servicer to manage the
settlement and follow-up of the opening and closing leg
of the transaction.
The account owner/servicer relationship may be:
- a global custodian which has an account with a local
custodian, or
- an investment management institution which manage
a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository participant which has
an account with a central securities depository, or
- a central securities depository which has an account
with a custodian, another central securities depository
or another settlement market infrastructure, or
- a central counterparty or a stock exchange or a trade
matching utility which need to instruct the settlement of
securities financing transactions to a central securities
depository or another settlement market infrastructure.
sese.034.001.11
SecuritiesFinancingStatusAdviceV11
An securities financing transaction account servicer
sends a SecuritiesFinancingStatusAdvice to an
account owner to advise the status of a securities
financing transaction previously instructed by the
account owner.
The status advice may be sent as a response to the
request of the account owner or not.
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Settlement And Reconciliation - Maintenance 2025 - 2026 15 March 2026
```

## File page 16

```text
MessageDefinition Definition
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure managing securities financing
transactions on behalf of their participants
- an agent (sub-custodian) managing securities
financing transactions on behalf of their global
custodian customer, or
- a custodian managing securities financing
transactions on behalf of an investment management
institution or a broker/dealer.
sese.035.001.13
SecuritiesFinancingConfirmationV13
A securities financing transaction account servicer
sends a SecuritiesFinancingConfirmation to an account
owner to confirm or advise of the partial or full
settlement of the opening or closing leg of a securities
financing transaction.
The account servicer/owner relationship may be:
- a central securities depository or another settlement
market infrastructure managing securities financing
transactions on behalf of their participants
- an agent (sub-custodian) managing securities
financing transactions on behalf of their global
custodian customer, or
- a custodian managing securities financing
transactions on behalf of an investment management
institution or a broker/dealer.
sese.036.001.10
SecuritiesFinancingModificationInstructionV10
An account owner sends a
SecuritiesFinancingModificationInstruction to a
securities financing transaction account servicer to
notify the securities financing transaction account
servicer of an update in the details of a repurchase
agreement, reverse repurchase agreement, securities
lending or securities borrowing transaction that does
not impact the original transaction securities quantity.
Such a change may be:
- the providing of closing details not available at the
time of the sending of the Securities Financing
Instruction, for example, termination date for an open
repo,
- the providing of a new rate, for example, a repo rate,
- the rollover of a position extending the closing or
maturity date.
The account owner/servicer relationship may be:
- a global custodian which has an account with a local
custodian, or
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Settlement And Reconciliation - Maintenance 2025 - 2026 16 March 2026
```

