---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17"]
file_pages: [540, 541]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8 seev.036.001.17 CorporateActionMovementConfirmationV17

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 540 to 541.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 540

```text
8 seev.036.001.17
CorporateActionMovementConfirmationV17
8.1 MessageDefinition Functionality
Scope
The CorporateActionMovementConfirmation message is sent by an account servicer to an account
owner or its designated agent to confirm the posting of securities or cash as a result of a corporate
action event.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionMovementConfirmationV17 MessageDefinition is composed of 17
MessageBuildingBlocks:
A. Pagination
Page number of the message and continuation indicator to indicate that the multi-part notification is
to continue or that the message is the last page of the multi-part notification.
B. MovementConfirmationIdentification
Unique Identification of the group of corporate action movement confirmation messages when the
movement confirmation is split in multiple (paginated) messages.
C. NotificationIdentification
Identification of a previously sent notification document.
D. MovementPreliminaryAdviceIdentification
Identification of a previously sent movement preliminary advice document.
E. InstructionIdentification
Identification of a related instruction document.
F. OtherDocumentIdentification
Identification of other documents as well as the document number.
G. EventsLinkage
Identification of another corporate action event that needs to be closely linked to the processing of
the event notified in this document.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 540 February 2026
```

## File page 541

```text
H. TransactionIdentification
Transaction type and identification information.
I. CorporateActionGeneralInformation
General information about the corporate action event.
J. AccountDetails
General information about the safekeeping account, owner and account balance.
K. CorporateActionDetails
Information about the corporate action event.
L. CorporateActionConfirmationDetails
Information about the corporate action option.
M. AdditionalInformation
Provides additional information.
N. IssuerAgent
Party appointed to administer the event on behalf of the issuer company/offeror. The party may be
contacted for more information about the event.
O. PayingAgent
Agent (principal or fiscal paying agent) appointed to execute the payment for the corporate action
event on behalf of the issuer company/offeror.
P. SubPayingAgent
Sub-agent appointed to execute the payment for the corporate action event on behalf of the issuer
company/offeror.
Q. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 541 February 2026
```

