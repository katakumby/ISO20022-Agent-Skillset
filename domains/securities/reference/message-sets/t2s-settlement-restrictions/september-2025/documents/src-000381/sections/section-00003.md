---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [4, 5, 6]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01", "semt.029.001.01", "semt.030.001.01", "semt.031.001.01", "semt.032.001.01", "semt.033.001.01", "semt.034.001.01"]
---

# 1 Message Set Overview

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 4 to 6.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4

```text
1 Message Set Overview
Introduction
This document describes the Target2-Securities - Settlement Restrictions message set. It includes the
query report messages related to securities settlement conditions modifications, securities transaction
cancellation and intraposition query report messages that have been developed in the scope of the
Target2-Securities Business Justification (See BJ#042).
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
semt.028.001.01
IntraPositionMovementQueryV01
The IntraPositionMovementQuery message is sent
from an account owner/requestor to a settlement
infrastructure to query intra-position movement
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
semt.029.001.01
IntraPositionMovementQueryResponseV01
The IntraPositionMovementQueryResponse message
is sent from a settlement infrastructure to an account
owner/requestor to provide all intra-position movement
instructions satisfying the selection criteria, as defined
within the query, returning current attributes and latest
status.
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
semt.030.001.01
SecuritiesSettlementConditionsModificationReq
uestQueryV01
The
SecuritiesSettlementConditionsModificationRequestQu
ery message is sent from an account owner/requestor
to a settlement infrastructure to query for the status of
settlement or intra-position movement modification
instruction(s) based on a set of search criteria or
business attributes.
Approved by the Securities SEG on 21 August 2025 Message Set Overview
Target2-Securities - Settlement Restrictions 4 September 2025
```

## File page 5

```text
MessageDefinition Definition
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
semt.031.001.01
SecuritiesSettlementConditionsModificationReq
uestReportV01
The
SecuritiesSettlementConditionsModificationRequestRe
port message is sent from a settlement infrastructure to
an account owner/requestor to provide full details or
current status values of the settlement or intra-position
movement modification request(s), as defined within
the query.
The message may also be used to:
- re-send a message previously sent (the sub-function
of the message is "Duplicate")
- provide a third party with a copy of a message for
information (the sub-function of the message is "Copy")
- re-send to a third party a copy of a message for
information (the sub-function of the message is "Copy
Duplicate").
semt.032.001.01
SecuritiesTransactionCancellationRequestQuer
yV01
The SecuritiesTransactionCancellationRequestQuery
message is sent from an account owner/requestor to a
settlement infrastructure to query for the status of
settlement or intra-position movement cancellation
instruction(s) based on a set of search criteria or
business attributes.
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
semt.033.001.01
SecuritiesTransactionCancellationRequestRepo
rtV01
The SecuritiesTransactionCancellationRequestReport
message is sent from a settlement infrastructure to an
account owner/requestor to provide full details or
current status values of settlement or the intra-position
movement cancellation request(s), as defined within
the query.
The message may also be used to:
Approved by the Securities SEG on 21 August 2025 Message Set Overview
Target2-Securities - Settlement Restrictions 5 September 2025
```

## File page 6

```text
MessageDefinition Definition
- re-send a message previously sent (the sub-function
of the message is "Duplicate")
- provide a third party with a copy of a message for
information (the sub-function of the message is "Copy")
- re-send to a third party a copy of a message for
information (the sub-function of the message is "Copy
Duplicate").
semt.034.001.01
IntraPositionMovementPendingReportV01
This IntraPositionMovementPendingReport message is
sent from a settlement infrastructure to an account
owner/request to report the intra-position movement
instructions, previously sent by the account owner, that
have a pending status.
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
Approved by the Securities SEG on 21 August 2025 Message Set Overview
Target2-Securities - Settlement Restrictions 6 September 2025
```

