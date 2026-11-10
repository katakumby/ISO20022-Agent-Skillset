---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [7, 8, 9, 10, 11, 12]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08", "camt.004.001.10", "camt.005.001.11", "camt.006.001.11", "camt.007.001.10", "camt.008.001.11", "camt.009.001.08", "camt.010.001.09", "camt.011.001.08", "camt.012.001.08", "camt.013.001.04", "camt.014.001.05", "camt.015.001.04", "camt.016.001.04", "camt.017.001.05", "camt.018.001.05", "camt.019.001.07", "camt.020.001.04", "camt.021.001.06", "camt.023.001.07", "camt.024.001.08", "camt.025.001.09", "camt.046.001.08", "camt.047.001.08", "camt.048.001.07", "camt.049.001.07", "camt.050.001.07", "camt.051.001.07", "camt.069.001.05", "camt.070.001.06", "camt.071.001.05", "camt.101.001.02", "camt.102.001.03", "camt.103.001.03", "camt.104.001.01"]
---

# 1 Message Set Overview

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 7 to 12.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 7

```text
1 Message Set Overview
Introduction
This document describes the Cash Management message set. It includes the new version of the
MessageDefinitions that have been added as part of the maintenance cycle 2024-2025 (See MCR
#252) and approved by the Payments Standards Evaluation Group on 04 February 2025.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
camt.003.001.08
GetAccountV08
The GetAccount message is sent by a member to the
transaction administrator.
It is used to request information on the details of one or
more accounts held at the transaction administrator,
including information on the balances.
camt.004.001.10
ReturnAccountV10
The ReturnAccount message is sent by the transaction
administrator to a member.
It is used to provide information on the details of one or
more accounts held at the transaction administrator,
including information on the balances.
The Return Account message can be sent as a
response to a related GetAccount message (pull
mode) or initiated by the transaction administrator
(push mode). The push of information can take place
either at prearranged times or as a warning or alarm
when a problem has occurred.
camt.005.001.11
GetTransactionV11
The GetTransaction message is sent by a member to
the transaction administrator.
It is used to request information about payment
instructions held at the transaction administrator.
Payment instructions are either sent by the member,
debiting or crediting its account at the transaction
administrator or received by the transaction
administrator, crediting or debiting the member's
account.
camt.006.001.11
ReturnTransactionV11
The ReturnTransaction message is sent by the
transaction administrator to a member of the system.
It is used to provide information on transactions and
booked entries held at the transaction administrator.
The Return Transaction message can be sent as a
response to a related GetTransaction message (pull
mode) or initiated by the transaction administrator
(push mode). The push of information can take place
either at prearranged times or as a warning or alarm
when a problem has occurred.
camt.007.001.10
ModifyTransactionV10
The ModifyTransaction message is sent by a member
to the transaction administrator.
It is used to request one modification in one payment
instruction held at the transaction administrator and
Approved by the Payments SEG on 04 February 2025 Message Set Overview
Cash Management - Maintenance 2024 - 2025 7 February 2025
```

## File page 8

```text
MessageDefinition Definition
sent by the member, debiting or crediting its account at
the transaction administrator.
camt.008.001.11
CancelTransactionV11
The CancelTransaction message is sent by a member
to the transaction administrator.
It is used to request the cancellation of one payment
instruction held at the transaction administrator and
sent by the member.
camt.009.001.08
GetLimitV08
The GetLimit message is used to request information
on the details of one or more limits set by the member
(or on behalf of the member) and managed by the
transaction administrator.
camt.010.001.09
ReturnLimitV09
The ReturnLimit message is sent by the transaction
administrator to a member of the system.
It is used to provide information on the details of one or
more limits set by the member (or on behalf of the
member) and managed by the transaction
administrator.
The ReturnLimit message can be sent as a response
to a related GetLimit message (pull mode) or initiated
by the transaction administrator (push mode). The
push of information can take place either at
prearranged times or as a warning or alarm when a
problem has occurred.
camt.011.001.08
ModifyLimitV08
The ModifyLimit message is sent by a member to the
transaction administrator.
It is used to request modifications in the details of one
particular, several or all limits set by the member and
managed by the transaction administrator.
Each ModifyLimit message can alter only one type of
limit (current or default).
camt.012.001.08
DeleteLimitV08
The DeleteLimit message is sent by a member to the
transaction administrator.
It is used to request the deletion of one particular,
several or all limits set by the member and managed
by the transaction administrator.
The DeleteLimit message may delete several types of
current limits (risk or liquidity management limit), based
on a multiple requests.
camt.013.001.04
GetMemberV04
The GetMember message is sent by a member to the
transaction administrator.
It is used to request information on static data
maintained by the transaction administrator and related
to the participants in the system and their membership
status vis-a-vis this system.
camt.014.001.05
ReturnMemberV05
The ReturnMember message is sent by the transaction
administrator to a member of the system.
It is used to provide information on static data
maintained by the transaction administrator and related
to the participants in the system and their membership
status vis-a-vis this system.
Approved by the Payments SEG on 04 February 2025 Message Set Overview
Cash Management - Maintenance 2024 - 2025 8 February 2025
```

## File page 9

```text
MessageDefinition Definition
The ReturnMember message can be sent as a
response to a related GetMember message (pull
mode) or initiated by the transaction administrator
(push mode). The push of information can take place
either at prearranged times or as a warning or alarm
when a problem has occurred.
camt.015.001.04
ModifyMemberV04
The ModifyMember message is sent by a member to
the transaction administrator.
It is used to request modifications to the static data
related to the profile of a member that the transaction
administrator maintains.
camt.016.001.04
GetCurrencyExchangeRateV04
The GetCurrencyExchangeRate message is sent by a
member to the transaction administrator.
It is used to request information on static data
maintained by the transaction administrator and related
to currency exchange details as maintained for the
system operations by the transaction administrator.
camt.017.001.05
ReturnCurrencyExchangeRateV05
The ReturnCurrencyExchangeRate message is sent by
the transaction administrator to a member of the
system.
It is used to provide information on static data and
related to currency exchange details as maintained for
system operations by the transaction administrator.
The ReturnCurrencyExchangeRate message can be
sent as a response to a related
GetCurrencyExchangeRate message (pull mode) or
initiated by the account servicer (push mode). The
push of information can take place either at
prearranged times or as a warning or alarm when a
problem has occurred.
camt.018.001.05
GetBusinessDayInformationV05
The GetBusinessDayInformation message is sent by a
member to the transaction administrator.
It is used to request information on different types of
administrative data linked to the system.
camt.019.001.07
ReturnBusinessDayInformationV07
The ReturnBusinessDayInformation message is sent
by the transaction administrator to a member of the
system.
It is used to provide information on different types of
administrative data linked to the system.
The ReturnBusinessDayInformation message can be
sent as a response to a related GetBusines
DayInformation message (pull mode), or initiated by
the transaction administrator (push mode). The push of
information can take place either at prearranged times
or as a warning or alarm when a problem has
occurred.
camt.020.001.04
GetGeneralBusinessInformationV04
The GetGeneralBusinessInformation message is sent
by a member to the transaction administrator.
It is used to request information on a broadcast-type
message previously sent by the transaction
Approved by the Payments SEG on 04 February 2025 Message Set Overview
Cash Management - Maintenance 2024 - 2025 9 February 2025
```

## File page 10

```text
MessageDefinition Definition
administrator to all or some of the members, giving
information related to the processing business.
camt.021.001.06
ReturnGeneralBusinessInformationV06
The ReturnGeneralBusinessInformation message is
sent by the transaction administrator to a member of
the system. It is used to provide some or all of the
members with information related to the processing of
the system.
The Return General Business Information message
can be sent as a response to a related
GetGeneralBusinessInformation message (pull mode)
or initiated by the transaction administrator (push
mode). The push of information can take place either
at prearranged times or as a warning or alarm when a
problem has occurred.
camt.023.001.07
BackupPaymentV07
The BackupPayment message is sent by a member to
the transaction administrator.
It is used to request a liquidity transfer from the
member to another participant in the system when the
user is in recovery mode.
camt.024.001.08
ModifyStandingOrderV08
The ModifyStandingOrder message is sent by a
member to the transaction administrator.
It is used to request a change in the features of a
permanent order for the transfer of funds between two
accounts belonging to the same member and being
held at the transaction administrator.
camt.025.001.09
ReceiptV09
The Receipt message is sent by a message recipient
to the message sender. It is sent to acknowledge the
receipt of one or multiple messages sent previously.
The Receipt message is an application receipt
acknowledgement and conveys information about the
processing of the original message(s).
camt.046.001.08
GetReservationV08
The GetReservation message is sent by a member to
the transaction administrator.
It is used to request information on the details of one or
more reservation facilities set by the member and
managed by the transaction administrator.
camt.047.001.08
ReturnReservationV08
The ReturnReservation message is sent by the
transaction administrator to a member.
It is used to provide information on the details of one or
more reservation facilities set by the member and
managed by the transaction administrator.
The ReturnReservation message can be sent as a
response to a related Get Reservation message (pull
mode) or initiated by the transaction administrator
(push mode). The push of information can take place
either at prearranged times or as a warning or alarm
when a problem has occurred.
camt.048.001.07
ModifyReservationV07
The ModifyReservation message is used to request
modifications in the details of one particular reservation
set by the member and managed by the transaction
administrator.
Approved by the Payments SEG on 04 February 2025 Message Set Overview
Cash Management - Maintenance 2024 - 2025 10 February 2025
```

## File page 11

```text
MessageDefinition Definition
camt.049.001.07
DeleteReservationV07
The DeleteReservation message is used to request the
deletion of one particular reservation by the member
and managed by the transaction administrator.
camt.050.001.07
LiquidityCreditTransferV07
The LiquidityCreditTransfer message is sent by a
member to the transaction administrator.
It is used to request a transfer of funds between two
accounts belonging to the same member or the same
group of accounts, and being held at the transaction
administrator.
camt.051.001.07
LiquidityDebitTransferV07
The LiquidityDebitTransfer message is sent by a
member to the transaction administrator.
It is used to request a transfer of funds between two
accounts belonging to the same member or the same
group of accounts, and being held at the transaction
administrator.
camt.069.001.05
GetStandingOrderV05
The GetStandingOrder message is sent by a member
to the transaction administrator.
It is used to request information on the details of one or
more standing orders, based on specific request
criteria, especially to query the amount of the overall
liquidity available. It will allow to query both reserved
liquidity and liquidity available for normal operations.
camt.070.001.06
ReturnStandingOrderV06
The ReturnStandingOrder message is sent by a
transaction administrator to a member.
It is used to provide information on the details of one or
more standing orders, based on specific request and
return criteria.
in response to a request a on information on standing
and predefined orders.
camt.071.001.05
DeleteStandingOrderV05
The DeleteStandingOrder message is sent by the
system member to delete one or more standing orders
within the static data held by the system transaction
administrator.
camt.101.001.02
CreateLimitV02
The CreateLimit message is sent by a member to the
transaction administrator.
It is used to create one or several limits set by the
member and managed by the transaction
administrator.
camt.102.001.03
CreateStandingOrderV03
The CreateStandingOrder message is sent by a
member to the transaction administrator.
It is used to create a permanent order for the transfer
of funds between two accounts belonging to the same
member and being held at the transaction
administrator.
camt.103.001.03
CreateReservationV03
The CreateReservation message is used to request for
the creation of one particular reservation by the
member and managed by the transaction
administrator.
Approved by the Payments SEG on 04 February 2025 Message Set Overview
Cash Management - Maintenance 2024 - 2025 11 February 2025
```

## File page 12

```text
MessageDefinition Definition
camt.104.001.01
CreateMemberV01
The ModifyMember message is sent by a member to
the transaction administrator.
It is used to create the profile of a member that the
transaction administrator maintains.
Approved by the Payments SEG on 04 February 2025 Message Set Overview
Cash Management - Maintenance 2024 - 2025 12 February 2025
```

