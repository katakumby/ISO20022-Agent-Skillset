---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02", "admi.006.001.01", "admi.007.001.01", "camt.064.001.01", "camt.065.001.01", "camt.066.001.02", "camt.067.001.02", "camt.068.001.02", "camt.072.001.02", "camt.073.001.02", "camt.074.001.02", "camt.075.001.02", "camt.076.001.01", "camt.077.001.01", "camt.078.001.02", "camt.079.001.02", "camt.080.001.02", "camt.081.001.02", "camt.082.001.02", "camt.083.001.02", "camt.084.001.02", "camt.085.001.02", "colr.001.001.02", "colr.002.001.02", "head.002.001.01", "reda.006.001.01", "reda.007.001.01", "reda.008.001.01", "reda.009.001.01", "reda.010.001.01", "reda.012.001.01", "reda.013.001.01", "reda.014.001.02", "reda.015.001.01", "reda.016.001.01", "reda.017.001.02"]
---

# 1 Message Set Overview

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 13 to 22.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 13

```text
1 Message Set Overview
Introduction
This document describes the Target2-Securities message set. It includes all of the MessageDefinitions
that have been developed in the scope of the Target2-Securities Business Justification and approved
by the Securities and Payments SEGs, under the lead of the Securities SEG and by the Cross-SEG
Harmonisation (CSH) group for the Business File Header (see BJ #42).
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
admi.005.001.02
ReportQueryRequestV02
The ReportQueryRequest message is exchanged
between system member and system transaction
administrator.
It aims at querying the latest available report data of a
specific report type. A report is stored and available for
query until the event occurs again report is replaced.
admi.006.001.01
ResendRequestV01
A system member or any parties authorised by them
send a ResendRequest message to the Central
System (such as the T2S platform). The purpose of
this request is, that the requesting party wants to
receive the "original" message once again. This might
be caused through technical problems on the receiving
side (message could not be received or processed or
is missing in the message sequencing) or for archiving
purposes.
admi.007.001.01
ReceiptAcknowledgementV01
The ReceiptAcknowledgement message is sent by the
transaction administrator to a member of the system
and vice versa. It is sent to acknowledge the receipt of
one or multiple messages sent previously. The
Acknowledgement message is 1) an application receipt
acknowledgement and 2) conveys information about
the processing of the original message(s). In case of 2)
the ReceiptAcknowledgement can be used as a
Generic error message, which provides information
about the status (e.g. rejection, acceptance) of an
instruction.
camt.064.001.01
LimitUtilisationJournalQueryV01
The LimitUtilisationJournalQuery message is
exchanged between a central securities depository or a
directly connected system participant (the central
securities depository participant granted direct access,
like a bank or a central counter party) and the central
system. Its purpose is to query information regarding
the journal of transaction impacting the utilisation of
limits that have been defined by the system participant.
camt.065.001.01
LimitUtilisationJournalReportV01
The LimitUtilisationJournalReport message is
exchanged between the central system and a central
securities depository or a directly connected system
party (the central securities depository participant
granted direct access, like a bank or central counter
party) and is used to return information about the limit.
Its purpose is to report information regarding the
journal of transactions impacting the utilisation of limits
that have been defined by the system participant.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 13 August 2026
```

## File page 14

```text
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 14 August 2026
```

## File page 15

```text
MessageDefinition Definition
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 15 August 2026
```

## File page 16

```text
MessageDefinition Definition
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function
of the message is "Duplicate")
- provide a third party with a copy of a message for
information (the sub-function of the message is "Copy")
- re-send to a third party a copy of a message for
information (the sub-function of the message is
"CopyDuplicate").
camt.076.001.01
BillingReportRequestV01
The BillingReportRequest message is sent by the
system member to the system transaction
administrator to request cumulative or itemised billing
data. The billing data may be cumulative information or
aggregated information on the level of a single
securities or a dedicated cash account within a given
period for each service item.
camt.077.001.01
BillingReportV01
The BillingReport message is exchanged between the
system transaction administrator and a system
member. It aims at providing the invoice or invoice
cancellation and informing about data providing
cumulative or itemised details backing an invoice.
BillingReport is used for the following usages:
- Invoice
The Cumulative Invoice will consist of the following:
- Sum of the total number of units per service item for
each CSD or CB;
- Sum of the amounts based on the total number of
units per service item for each CSD or CB;
- Cancellation status of the invoice data.
- Invoice Cancellation
- Cumulative Billing Data Query Response:
The BillingReport message is also used to inform the
system member about details backing an invoice. This
can be sent via cumulative billing data or itemised
billing data as response to an invoice query message.
Itemised Billing Data Query Response: The
BillingReport message is also used to inform the
system member about details backing an invoice. This
can be via cumulative billing data or itemised billing
data as response to an invoice query message.
camt.078.001.02
IntraBalanceMovementQueryV02
The IntraBalanceMovementQuery message is sent
from an account owner/requestor to a settlement
infrastructure to query intra-balance movement
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 16 August 2026
```

## File page 17

```text
MessageDefinition Definition
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 17 August 2026
```

## File page 18

```text
MessageDefinition Definition
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 18 August 2026
```

## File page 19

```text
MessageDefinition Definition
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
colr.001.001.02
CollateralValueQueryV02
The CollateralValueQuery message is sent by a
system member (such as a directly connected party) to
the system transaction administrator to query the
current available value of securities for auto
collateralisation for one specific or several cash
accounts.
colr.002.001.02
CollateralValueReportV02
The CollateralValueReport message is sent by the
system transaction administrator to a system member
(such as a directly connected party) to provide further
information the current available value of securities for
auto collateralisation for one specific or several cash
accounts.
head.002.001.01
BusinessFileHeaderV01
The Business File Header contains information about
the parties involved in the file exchange, as well as
information about the content and its structure.
The Business File headers has four major functions:
- Provides information about the sender of the file.
- Identifies the file exchanged: each file must have a
unique File Identifier.
- Describes the type of message(s) exchanged: by
default, the type of messages contained in a file will be
ISO 20022 message definitions.
- Provides processing information to the receiving
party: that would be, for instance, the total number of
messages included in the file.
Usage: The Business File Header (head.002) is to be
used exclusively in existing implementations, such as
the Eurosystem, and will be replaced for general use
by the upcoming next version defined as the Business
File Envelope (nvlp.002). The Business File Header
(head.002) will therefore not be maintained in the
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 19 August 2026
```

## File page 20

```text
MessageDefinition Definition
future and any new implementation must use the
Business File Envelope (nvlp.002).
reda.006.001.01
SecurityCreationRequestV01
An instructing party sends a SecurityCreationRequest
message to an executing/servicing party to request the
creation of financial instrument static details in their
system.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.007.001.01
SecurityMaintenanceRequestV01
An instructing party sends a
SecurityMaintenanceRequest message to an
executing/servicing party to request the maintenance
of financial instrument details in their system.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.008.001.01
SecurityCreationStatusAdviceV01
An executing/servicing party sends a
SecurityCreationStatusAdvice message to an
instructing party to report the status of a
SecurityCreationRequest message previously sent by
the instructing party.
The SecurityCreationStatusAdvice message may be
sent as a response to the request of the instructing
party or not.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 20 August 2026
```

## File page 21

```text
MessageDefinition Definition
- a Market Infrastructure, or
- a Market Data Provider.
reda.009.001.01
SecurityActivityAdviceV01
The SecurityActivityReport message is sent by the
executing party to an instructing party containing
information about changes on securities reference
data.
Scope and usage:
It aims at informing about the changes occurred during
a business date for securities reference data.
reda.010.001.01
SecurityQueryV01
An instructing party sends a SecurityQuery message to
an executing/servicing party to request a report of
financial instrument details in their system.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.012.001.01
SecurityReportV01
An executing/servicing party sends a SecurityReport
message to an instructing party to advise the last
known image of securities data's.
The report may be sent upon request (for example a
query) of the instructing party or push by the executing/
servicing party.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
Initiator: executing/servicing party.
reda.013.001.01
SecurityDeletionRequestV01
An instructing party sends a SecurityDeletionRequest
message to an executing/servicing party to advice the
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 21 August 2026
```

## File page 22

```text
MessageDefinition Definition
complete removal of a financial instrument entry from
their system.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.014.001.02
PartyCreationRequestV02
Scope:
The PartyCreationRequest message is sent by an
instructing party to the executing party to request for
the creation of party reference data for a new party in
the executing system.
Usage:
It aims at instructing the creation of a new party with
corresponding details.
Processing and confirmation of the party creation
request are provided via a party status advice.
reda.015.001.01
PartyQueryV01
Scope:
The PartyQuery message is sent by a central
securities depository, a national central bank, a central
securities depository participant, a central counter
party, a payment bank, a trading party or a stock
exchange to the executing party to query for the party
reference data of a party defined in the system.
reda.016.001.01
PartyStatusAdviceV01
Scope:
The PartyStatusAdvice message is sent by the
executing party to the instructing party to provide
details about the processing of a request on party
reference data (create or update).
Usage:
When processing information is negative - a failure
occurred in applying the changes the message
accordingly also delivers information about the reason
why the creation or update could not be processed.
When processing is successfully performed, the
message includes the related party identification.
reda.017.001.02
PartyReportV02
Scope:
The PartyReport message is sent by the executing
party to a central securities depository, a national
central bank, a central securities depository participant,
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 22 August 2026
```

