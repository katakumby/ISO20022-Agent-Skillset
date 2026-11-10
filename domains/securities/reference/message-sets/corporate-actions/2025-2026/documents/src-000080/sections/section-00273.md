---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"]
file_pages: [360, 361, 362]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 360 to 362.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 360

```text
7 seev.035.001.17
CorporateActionMovementPreliminaryAdvice
V17
7.1 MessageDefinition Functionality
Scope
The CorporateActionMovementPreliminaryAdvice message is sent by an account servicer to an
account owner or its designated agent:
- to advise about the eligible balance and entitlements and,
- to pre-advise an upcoming posting or reversal of securities and/or cash postings.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionMovementPreliminaryAdviceV17 MessageDefinition is composed of 27
MessageBuildingBlocks:
A. Pagination
Page number of the message and continuation indicator to indicate that the multi-part preliminary
advice is to continue or that the message is the last page of the multi-part preliminary advice.
B. MovementPreliminaryAdviceGeneralInformation
General information about the movement preliminary advice document.
C. PreviousMovementPreliminaryAdviceIdentification
Identification of the previously sent movement preliminary advice document.
D. NotificationIdentification
Identification of a previously sent notification document.
E. MovementConfirmationIdentification
Identification of a previously sent movement confirmation document.
F. InstructionIdentification
Identification of a related instruction document.
G. OtherDocumentIdentification
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 360 February 2026
```

## File page 361

```text
Identification of other documents as well as the document number.
H. EventsLinkage
Identification of another corporate action event that needs to be closely linked to the processing of
the event notified in this document.
I. ReversalReason
Reason for the reversal.
J. CorporateActionGeneralInformation
General information about the corporate action event.
K. AccountDetails
General information about the safekeeping account, owner and account balance.
L. CorporateActionDetails
Information about the corporate action event.
M. CorporateActionMovementDetails
Information about the corporate action option.
N. AdditionalInformation
Provides additional information.
O. IssuerAgent
Party appointed to administer the event on behalf of the issuer company/offeror. The party may be
contacted for more information about the event.
P. PayingAgent
Agent (principal or fiscal paying agent) appointed to execute the payment for the corporate action
event on behalf of the issuer company/offeror.
Q. SubPayingAgent
Sub-agent appointed to execute the payment for the corporate action event on behalf of the issuer
company/offeror.
R. Registrar
Party/agent responsible for maintaining the register of a security.
S. ResellingAgent
Broker-dealer responsible for reselling to new investors securities (usually bonds) that have been
tendered for purchase by their owner.
T. PhysicalSecuritiesAgent
Trust company, bank or similar financial institution assigned by an issuer to accept presentations of
instruments, usually bonds, for transfer and or exchange.
U. DropAgent
Trust company, bank or similar financial institution that acts on behalf of an out-of-town agent or
event agent where securities can be delivered in person.
V. SolicitationAgent
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 361 February 2026
```

## File page 362

```text
Trust company, bank or similar financial institution assigned by an issuer to maintain records of
investors and account balances and transactions for the consent of a material change.
W. InformationAgent
Trust company, bank or similar financial institution assigned by an Issuer to provide information
and copies of the offering documentation.
X. Issuer
Issuer of the financial instrument.
Y. Offeror
Party making the offer and which is different from the issuing company.
Z. TransferAgent
Trust company, bank or similar financial institution appointed by a fund management company to
maintain records of investors and account balances. The transfer agent records transactions,
including subscriptions, redemptions, switches, transfers, and re-registrations.
A
A.
SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 362 February 2026
```

