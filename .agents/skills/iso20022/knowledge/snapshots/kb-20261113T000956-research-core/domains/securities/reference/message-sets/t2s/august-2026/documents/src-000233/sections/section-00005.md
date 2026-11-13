---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: []
file_pages: [23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.018.001.01", "reda.019.001.01", "reda.020.001.01", "reda.021.001.01", "reda.022.001.02", "reda.023.001.01", "reda.024.001.01", "reda.025.001.01", "reda.026.001.01", "reda.027.001.01", "reda.028.001.01", "reda.029.001.01", "reda.030.001.01", "reda.031.001.01", "reda.032.001.01", "reda.033.001.01", "reda.034.001.01", "reda.035.001.01", "reda.036.001.01", "reda.037.001.01", "reda.041.001.02", "reda.042.001.01", "reda.043.001.02", "reda.044.001.01", "reda.045.001.01", "reda.046.001.01", "reda.047.001.01", "reda.049.001.01", "reda.050.001.01", "reda.051.001.01", "reda.075.001.01", "reda.077.001.01", "semt.025.001.01", "semt.026.001.01", "semt.027.001.01", "semt.028.001.01", "semt.029.001.01", "semt.030.001.01", "semt.031.001.01", "semt.032.001.01", "semt.033.001.01", "semt.034.001.01", "semt.040.001.01"]
---

# Continuation at file page 23

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 23 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 23

```text
MessageDefinition Definition
a central counter party, a payment bank, a trading
party or a stock exchange to provide detailed
information on the requested party reference data of
the party defined in the system.
reda.018.001.01
SecuritiesAccountCreationRequestV01
The SecuritiesAccountCreationRequest message
message is sent by an instructing party to the
executing party to instruct the creation of a new
securities account with the required account attributes
details.
Usage:
Processing and confirmation of the securities account
creation request message are provided via a
SecuritiesAccountStatusAdvice message.
reda.019.001.01
SecuritiesAccountQueryV01
The SecuritiesAccountQuery message sent by an
instructing party to the executing party to request the
details related to the securities account.
reda.020.001.01
SecuritiesAccountStatusAdviceV01
The SecuritiesAccountStatusAdvice message is send
by the the executing party to an instructing party to
provide the status of the execution of an creation,
modification or deletion of securities account reference
data.
Usage:
When processing information is negative - a failure
occurred in applying the changes the message
accordingly also delivers information about the reason
why the creation or update could not be processed.
When the processing is succesfully performed, the
message includes the related securities account
identification.
reda.021.001.01
SecuritiesAccountReportV01
The SecuritiesAccountReport message sent by the
executing party to an instructing party to provide the
details of the securities account details as requested in
the query.
reda.022.001.02
PartyModificationRequestV02
Scope:
The PartyModificationRequest message is sent by the
instructing party to the executing party to request for an
update of the party reference data of a party defined in
the executing system.
Usage:
It aims at instructing the update of an existing party by
amending its existing details or by providing additional
details.
Processing and confirmation of the party modification
request message are provided via a party status
advice.
reda.023.001.01
SecuritiesAccountModificationRequestV01
The SecuritiesAccountModificationRequest message is
sent by an instructing party to the executing party to
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 23 August 2026
```

## File page 24

```text
MessageDefinition Definition
instruct the update of an existing securities account by
amending its existing attributes or by providing
additional attibutes details.
Usage:
Processing and confirmation of the securities account
creation request message are provided via a
SecuritiesAccountStatusAdvice message.
reda.024.001.01
CollateralValueCreationRequestV01
The CollateralValueCreationRequest message is sent
by the instructing party to the executing party to
request for the creation of a collateral value in the
executing system collateral management reference
data.
Usage:
It aims at instructing the creation of a new collateral
value with corresponding details.
Processing and confirmation of the collateral value
creation request message are provided via a collateral
management status advice.
reda.025.001.01
EligibleSecuritiesCreationRequestV01
The EligibleSecuritiesCreationRequest message is
exchanged between an instructing party and the
executing party to request for the creation of an eligible
securities in the executing system collateral
management reference data.
Usage:
It aims at instructing the creation of a new eligible
securities with corresponding details.
Processing and confirmation of the eligible securities
creation request message are provided via a collateral
management status advice.
reda.026.001.01
EligibleCounterpartCSDCreationRequestV01
The EligibleCounterpartCSDCreationRequest message
is sent by an instructing party to the executing party to
request for the creation of an eligible counterpart CSD
in the executing system collateral management
reference data.
Usage:
It aims at instructing the creation of a new eligible
counterpart CSD with corresponding details.
Processing and confirmation of the eligible counterpart
CSD creation request message are provided via a
collateral management status advice.
reda.027.001.01
CloseLinkCreationRequestV01
The CloseLinkCreationRequest message is sent by an
instructing party to the executing party to request for
the creation of a close link in the executing system
collateral management reference data.
Usage:
It aims at instructing the creation of a new close link
with corresponding details.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 24 August 2026
```

## File page 25

```text
MessageDefinition Definition
Processing and confirmation of the close link creation
request message are provided via a collateral
management status advice.
reda.028.001.01
CollateralDataStatusAdviceV01
The CollateralDataStatusAdvice message is sent by
the executing party to an instructing party (the
requestor) to provide information of a request on
collateral management reference data.
Usage:
It aims at informing about the status of the request.
reda.029.001.01
SecurityMaintenanceStatusAdviceV01
An executing/servicing party sends a
SecurityMaintenanceStatusAdvice message to an
instructing party to report the status of a
SecurityMaintencanceRequest message previously
sent by the instructing party.
The SecurityMaintenanceStatusAdvice message may
be sent as a response to the request of the instructing
party or not.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.030.001.01
SecurityDeletionStatusAdviceV01
An executing/servicing party sends a
SecurityDeletionStatusAdvice message to an
instructing party to report the status of a
SecurityDeletionRequest message previously sent by
the instructing party.
The SecurityDeletionStatusAdvice message is sent as
a response to the request of the instructing party.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 25 August 2026
```

## File page 26

```text
MessageDefinition Definition
reda.031.001.01
PartyDeletionRequestV01
Scope:
The PartyDeletionRequest message is sent by the
instructing party to the executing party to request a
deletion of a party defined in the executing system.
Usage:
It aims at instructing the deletion of an existing party by
providing its identification.
Processing of the party deletion request message is
provided via a party status advice.
reda.032.001.01
SecuritiesAccountDeletionRequestV01
The SecuritiesAccountDeletionRequest message is
sent by an instructing party to the executing party to
request for the deletion of a securities account from the
securities account reference data defined in the system
of the executing party.
Usage:
It aims at instructing the deletion of an existing
securities account providing securities account
identification.
The result of the deletion is provided through a
SecuritiesAccountStatusAdvice message.
reda.033.001.01
SecuritiesAuditTrailQueryV01
The SecuritiesAuditTrailQuery message is sent by an
instructing party to the executing party to query for the
securities audit trail recorded in the system.
reda.034.001.01
SecuritiesAuditTrailReportV01
The SecuritiesAuditTrailReport message is sent by the
executing party to an instructing party to provide
detailed information on the requested securities audit
trail recorded in the system.
reda.035.001.01
SecuritiesAccountActivityAdviceV01
The SecuritieAccountActivityReport message is sent
by the executing party to an instructing party containing
information about changes on securities account
reference data.
Scope and usage:
It aims at informing about the changes occurred during
a business date for securities account reference data.
reda.036.001.01
SecuritiesAccountAuditTrailQueryV01
The SecuritiesAccountAuditTrailQuery message is sent
by an instructing party to the executing party to query
for the securities account audit trail recorded in the
system.
reda.037.001.01
SecuritiesAccountAuditTrailReportV01
The SecuritiesAccountAuditTrailReport message is
sent by the executing party to an instructing party to
provide detailed information on the requested
securities account audit trail recorded in the system.
reda.041.001.02
PartyActivityAdviceV02
The PartyActivityReport message is sent by the
executing party to an instructing party containing
information about changes on party reference data.
Scope and usage:
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 26 August 2026
```

## File page 27

```text
MessageDefinition Definition
It aims at informing about the changes occurred during
a business date for party reference data.
reda.042.001.01
PartyAuditTrailQueryV01
The PartyAuditTrailQuery message is sent by an
instructing party to the executing party to query for the
party audit trail recorded in the system.
reda.043.001.02
PartyAuditTrailReportV02
The PartyAuditTrailReport message is sent by the
executing party to an instructing party to provide
detailed information on the requested party audit trail
recorded in the system.
reda.044.001.01
EligibleCounterpartCSDStatusAdviceV01
The EligibleCounterpartCSDStatusAdvice message is
sent by the executing party to an instructing party (the
requestor) to provide information for a request on
eligible counterpart CSD reference data.
Usage:
It aims at informing about the status of the request.
reda.045.001.01
SecurityCSDLinkCreationRequestV01
An instructing party sends a
SecurityCSDLinkCreationRequest message to an
executing/servicing party to request the creation of the
link between a financial instrument and a CSD in their
system.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
An instructing party sends a
SecurityCSDLinkMaintenanceRequest message to an
executing/servicing party to request the maintenance
of the link between a financial instrument and a CSD in
their system.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 27 August 2026
```

## File page 28

```text
MessageDefinition Definition
reda.047.001.01
SecurityCSDLinkStatusAdviceV01
An executing/servicing party sends a
SecurityCSDLinkStatusAdvice message to an
instructing party to report the status of a
SecurityCSDLink Request message previously sent by
the instructing party.
The SecurityCSDLinkStatusAdvice message may be
sent as a response to the request of the instructing
party or not.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.049.001.01
AccountLinkCreationRequestV01
reda.050.001.01
AccountLinkMaintenanceRequestV01
SCOPE:
The AccountLinkMaintenanceRequest message is sent
by the instructing party to the executing/servicing party
to request for the maintenance of an account link in
their system.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish account link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE:
The request is sent when the instructing party identified
a gap in the account link coverage of the executing/
servicing party. The instructing party needs this
account link to be maintained at the executing /
servicing party to perform its activities.
Initiator: instructing party.
reda.051.001.01
AccountLinkStatusAdviceV01
SCOPE:
The AccountLinkStatusAdvice message is sent by the
executing/servicing party to the instructing party to
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 28 August 2026
```

## File page 29

```text
MessageDefinition Definition
provide details about the processing of a request on
account link reference data (create or update).
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish account link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE:
Initiator: executing/servicing party
When processing information is negative - a failure
occurred in applying the changes the message
accordingly also delivers information about the reason
why the creation or update could not be processed.
When the processing is successfully performed, the
message includes the related account link
identification.
reda.075.001.01
EligibleSecuritiesDeletionRequestV01
The EligibleSecuritiesDeletionRequest message is
exchanged between an instructing party and the
executing party to request for the deletion of an eligible
securities in the executing system collateral
management reference data.
Usage:
It aims at instructing the deletion of a existing eligible
securities with corresponding details.
Processing and confirmation of the eligible securities
deletion request message are provided via a collateral
management status advice.
reda.077.001.01
CloseLinkDeletionRequestV01
The CloseLinkDeletionRequest message is sent by an
instructing party to the executing party to request for
the deletion of a close link in the executing system
collateral management reference data.
Usage:
It aims at instructing the deletion of an existing close
link with corresponding details.
Processing and confirmation of the close link creation
request message are provided via a collateral
management status advice.
semt.025.001.01 The SecuritiesAccountPositionQuery message is sent
by an account owner to an account servicer or
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 29 August 2026
```

## File page 30

```text
MessageDefinition Definition
SecuritiesAccountPositionQueryV01 servicing party to request an account view on the
position at a particular point in time period, or during a
particular time period, where all positions are
summarised in the account structure that is compatible
with the query.
Usage:
The message may also be used to:
-re-send a message previously sent (the sub-function
of the message is Duplicate),
- provide a third party with a copy of a message for
information (the sub-function of the message is Copy),
-re-send to a third party a copy of a message for
information (the sub-function of the message is
CopyDuplicate).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
The SecuritiesSettlementInstructionQuery message is
sent from an account owner/requestor to a settlement
infrastructure.
The message is used to query information on the
securities settlement instructions, that satisfy the
defined selection criteria.
semt.027.001.01
SecuritiesSettlementTransactionQueryRespons
eV01
The SecuritiesSettlementResponse message is sent
from a settlement infrastructure to an account owner/
requestor to provide the details of the securities
settlement instructions, as selected in the search
criteria defined in the request.
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 30 August 2026
```

## File page 31

```text
MessageDefinition Definition
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 31 August 2026
```

## File page 32

```text
MessageDefinition Definition
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
semt.040.001.01
SecuritiesAccountPositionResponseV01
The SecuritiesAccountPositionResponse message is
sent by a market infrastructure to an instructing party to
report the securities positions for the given date period
as requested in the query, for all securities across all
accounts satisfying the query criteria.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Set Overview
Target2-Securities 32 August 2026
```

