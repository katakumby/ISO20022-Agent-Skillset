---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.1 MessageDefinition Functionality"]
file_pages: [23, 24, 25]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.1 MessageDefinition Functionality

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 23 to 25.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 23

```text
3 seev.031.001.16
CorporateActionNotificationV16
3.1 MessageDefinition Functionality
Scope
The CorporateActionNotification message is sent by an account servicer to an account owner or its
designated agent to notify details of a corporate action event and optionally account information and
preliminary information about eligible balance and entitlements.
It may also include possible elections or choices available to the account owner. The account servicer
can initially send the CorporateActionNotification message as a preliminary advice, subsequently
replaced by another CorporateActionNotification message with complete or confirmed information.
It may also be sent to an account owner or its designated agent, to remind of event details and/or of
missing or incomplete instructions for a corporate action event.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionNotificationV16 MessageDefinition is composed of 25 MessageBuildingBlocks:
A. Pagination
Page number of the message and continuation indicator to indicate that the multi-part notification is
to continue or that the message is the last page of the multi-part notification.
B. NotificationGeneralInformation
General information about the event notification type, status and contents.
C. PreviousNotificationIdentification
Identification of the previously sent notification document.
D. InstructionIdentification
Identification of a related instruction document.
E. OtherDocumentIdentification
Identification of other documents as well as the document number.
F. EventsLinkage
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 23 February 2026
```

## File page 24

```text
Identification of another corporate action event that needs to be closely linked to the processing of
the event notified in this document.
G. CorporateActionGeneralInformation
General information about the corporate action event.
H. AccountDetails
General information about the safekeeping account, owner and account balance.
I. IntermediateSecurity
Details on rights credited to the account as for example trading period, expiry date, renounceability.
J. CorporateActionDetails
Information about the corporate action event.
K. CorporateActionOptionDetails
Information about the corporate action option.
L. AdditionalInformation
Additional information on the event.
M. IssuerAgent
Party appointed to administer the event on behalf of the issuer company/offeror. The party may be
contacted for more information about the event.
N. PayingAgent
Agent (principal or fiscal paying agent) appointed to execute the payment for the corporate action
event on behalf of the issuer company/offeror.
O. SubPayingAgent
Sub-agent appointed to execute the payment for the corporate action event on behalf of the issuer
company/offeror.
P. Registrar
Party/agent responsible for maintaining the register of the security.
Q. ResellingAgent
Broker-dealer responsible for reselling to new investors securities (usually bonds) that have been
tendered for purchase by their owner.
R. PhysicalSecuritiesAgent
Trust company, bank or similar financial institution assigned by an issuer to accept presentations of
instruments, usually bonds, for transfer and or exchange.
S. DropAgent
Trust company, bank or similar financial institution that acts on behalf of an out-of-town agent or
event agent where securities can be delivered in person.
T. SolicitationAgent
Trust company, bank or similar financial institution assigned by an issuer to maintain records of
investors and account balances and transactions for the consent of a material change.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 24 February 2026
```

## File page 25

```text
U. InformationAgent
Trust company, bank or similar financial institution assigned by an Issuer to provide information
and copies of the offering documentation.
V. Issuer
Issuer of the financial instrument.
W. Offeror
Party making the offer and which is different from the issuing company.
X. TransferAgent
Trust company, bank or similar financial institution appointed by a fund management company to
maintain records of investors and account balances. The transfer agent records transactions,
including subscriptions, redemptions, switches, transfers, and re-registrations.
Y. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 25 February 2026
```

