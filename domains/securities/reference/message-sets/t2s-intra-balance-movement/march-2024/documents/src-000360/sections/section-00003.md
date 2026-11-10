---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [5, 6, 7, 8, 9]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.066.001.02", "camt.067.001.02", "camt.068.001.02", "camt.072.001.02", "camt.073.001.02", "camt.074.001.02", "camt.075.001.02", "camt.078.001.02", "camt.079.001.02", "camt.080.001.02", "camt.081.001.02", "camt.082.001.02", "camt.083.001.02", "camt.084.001.02", "camt.085.001.02"]
---

# 1 Message Set Overview

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 5 to 9.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5

```text
1 Message Set Overview
Introduction
This document describes the Target2-Securities - Intra-balance Movement message set. It includes the
new version of the MessageDefinitions that have been added as part of the maintenance cycle
2023-2024 (See MCR #234) and approved by the Securities and the Payments Standards Evaluation
Groups under the leadership of the Securities SEG on 15 February 2024.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
camt.066.001.02
IntraBalanceMovementInstructionV02
The IntraBalanceMovementInstruction message is sent
from an account owner/requestor to a settlement
infrastructure to instruct the movement of an amount of
money within its holdings from one sub-balance to
another.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function
of the message is "Duplicate")
- provide a third party with a copy of a message for
information (the sub-function of the message is "Copy")
- re-send to a third party a copy of a message for
information (the sub-function of the message is
"CopyDuplicate").
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
The IntraBalanceMovementStatusAdvice message is
sent from a settlement infrastructure to an account
owner/requestor to advise the status of an intra-
balance movement instruction previously sent by the
account owner/requestor.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function
of the message is "Duplicate")
- provide a third party with a copy of a message for
information (the sub-function of the message is "Copy")
- re-send to a third party a copy of a message for
information (the sub-function of the message is
"CopyDuplicate").
camt.068.001.02
IntraBalanceMovementConfirmationV02
The IntraBalanceMovementConfirmation message is
sent from a settlement infrastructure to an account
owner/requestor to confirm the movement of an
amount of money within its holdings from one sub-
balance to another.
Usage:
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Set Overview
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
5 March 2024
```

## File page 6

```text
MessageDefinition Definition
The message may be used to:
- re-send a message previously sent (the sub-function
of the message is "Duplicate")
- provide a third party with a copy of a message for
information (the sub-function of the message is "Copy")
- re-send to a third party a copy of a message for
information (the sub-function of the message is
"CopyDuplicate").
camt.072.001.02
IntraBalanceMovementModificationRequestV02
The IntraBalanceMovementModificationRequest
message is sent from an account owner/requestor to a
settlement infrastructure to request the modification of
a processing indicator on a previously sent
IntraBalanceMovementInstruction message.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function
of the message is "Duplicate")
- provide a third party with a copy of a message for
information (the sub-function of the message is "Copy")
- re-send to a third party a copy of a message for
information (the sub-function of the message is
"CopyDuplicate").
camt.073.001.02
IntraBalanceMovementModificationRequestStat
usAdviceV02
The
IntraBalanceMovementModificationRequestStatusAdvi
ce message is sent from a settlement infrastructure to
an account owner/requestor to advise the status of an
intra-balance movement modification request
previously sent by the account owner/requestor.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function
of the message is "Duplicate")
- provide a third party with a copy of a message for
information (the sub-function of the message is "Copy")
- re-send to a third party a copy of a message for
information (the sub-function of the message is
"CopyDuplicate").
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
The IntraBalanceMovementCancellationRequest
message is sent from an account owner/requestor to a
settlement infrastructure to request the cancellation of
a previously sent IntraBalanceMovementInstruction
message.
Usage:
The message may be used to:
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Set Overview
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
6 March 2024
```

## File page 7

```text
MessageDefinition Definition
- re-send a message previously sent (the sub-function
of the message is "Duplicate")
- provide a third party with a copy of a message for
information (the sub-function of the message is "Copy")
- re-send to a third party a copy of a message for
information (the sub-function of the message is
"CopyDuplicate").
camt.075.001.02
IntraBalanceMovementCancellationRequestStat
usAdviceV02
The
IntraBalanceMovementCancellationRequestStatusAdvi
ce message is sent from a settlement infrastructure to
an account owner/requestor to advise the status of an
intra-balance movement cancellation request
previously sent by the account owner/requestor.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function
of the message is "Duplicate")
- provide a third party with a copy of a message for
information (the sub-function of the message is "Copy")
- re-send to a third party a copy of a message for
information (the sub-function of the message is
"CopyDuplicate").
camt.078.001.02
IntraBalanceMovementQueryV02
The IntraBalanceMovementQuery message is sent
from an account owner/requestor to a settlement
infrastructure to query intra-balance movement
instructions, along with their current status, based on a
set of search criteria.
The message may also be used to:
- re-send a message sent by the account owner to the
account servicer (the sub-function of the message is
"Duplicate")
- provide a third party with a copy of a message being
sent by the account owner for information (the sub-
function of the message is "Copy")
- re-send to a third party a copy of a message being
sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
camt.079.001.02
IntraBalanceMovementQueryResponseV02
The IntraBalanceMovementQueryResponse message
is sent from a settlement infrastructure to an account
owner/requestor to provide all intra-balance movement
instructions satisfying the selection criteria, as defined
within the query, returning current attributes and latest
status.
The message may also be used to:
- re-send a message sent by the account owner to the
account servicer (the sub-function of the message is
"Duplicate")
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Set Overview
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
7 March 2024
```

## File page 8

```text
MessageDefinition Definition
- provide a third party with a copy of a message being
sent by the account owner for information (the sub-
function of the message is "Copy")
- re-send to a third party a copy of a message being
sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
camt.080.001.02
IntraBalanceMovementModificationQueryV02
The IntraBalanceMovementModificationQuery
message is sent from an account owner/requestor to a
settlement infrastructure to query for the status of intra-
balance movement modification instruction(s) based on
a set of search criteria or business attributes.
The message may also be used to:
- re-send a message sent by the account owner to the
account servicer (the sub-function of the message is
"Duplicate")
- provide a third party with a copy of a message being
sent by the account owner for information (the sub-
function of the message is "Copy")
- re-send to a third party a copy of a message being
sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
camt.081.001.02
IntraBalanceMovementModificationReportV02
The IntraBalanceMovementModificationReport
message is sent from a settlement infrastructure to an
account owner/requestor to provide full details or
current status values of the intra-balance movement
modification request(s), as defined within the query.
The message may also be used to:
- re-send a message previously sent (the sub-function
of the message is "Duplicate")
- provide a third party with a copy of a message for
information (the sub-function of the message is "Copy")
- re-send to a third party a copy of a message for
information (the sub-function of the message is "Copy
Duplicate").
camt.082.001.02
IntraBalanceMovementCancellationQueryV02
The IntraBalanceMovementCancellationQuery
message is sent from an account owner/requestor to a
settlement infrastructure to query for the status of intra-
balance movement cancellation instruction(s) based on
a set of search criteria or business attributes.
The message may also be used to:
- re-send a message sent by the account owner to the
account servicer (the sub-function of the message is
"Duplicate")
- provide a third party with a copy of a message being
sent by the account owner for information (the sub-
function of the message is "Copy")
- re-send to a third party a copy of a message being
sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Set Overview
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
8 March 2024
```

## File page 9

```text
MessageDefinition Definition
camt.083.001.02
IntraBalanceMovementCancellationReportV02
The IntraBalanceMovementCancellationReport
message is sent from a settlement infrastructure to an
account owner/requestor to provide full details or
current status values of the intra-balance movement
cancellation request(s), as defined within the query.
The message may also be used to:
- re-send a message previously sent (the sub-function
of the message is "Duplicate")
- provide a third party with a copy of a message for
information (the sub-function of the message is "Copy")
- re-send to a third party a copy of a message for
information (the sub-function of the message is "Copy
Duplicate").
camt.084.001.02
IntraBalanceMovementPostingReportV02
This IntraBalanceMovementPostingReport message is
sent from a settlement infrastructure to an account
owner/requestor to report the intra-balance movement
instructions, previously sent by the account owner, that
have a settled status.
The message may also be used to:
- - re-send a message sent by the account owner to
the account servicer (the sub-function of the message
is "Duplicate")
- - provide a third party with a copy of a message being
sent by the account owner for information (the sub-
function of the message is "Copy")
- - re-send to a third party a copy of a message being
sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
camt.085.001.02
IntraBalanceMovementPendingReportV02
This IntraBalanceMovementPendingReport message is
sent from a settlement infrastructure to an account
owner/request to report the intra-balance movement
instructions, previously sent by the account owner, that
have a pending status.
The message may also be used to:
- re-send a message sent by the account owner to the
account servicer (the sub-function of the message is
"Duplicate")
- provide a third party with a copy of a message being
sent by the account owner for information (the sub-
function of the message is "Copy")
- - re-send to a third party a copy of a message being
sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Set Overview
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
9 March 2024
```

