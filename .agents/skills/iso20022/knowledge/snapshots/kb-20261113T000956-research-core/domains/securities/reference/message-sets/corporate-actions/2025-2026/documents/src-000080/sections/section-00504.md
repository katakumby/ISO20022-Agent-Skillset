---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17"]
file_pages: [665, 666]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9 seev.037.001.17 CorporateActionMovementReversalAdviceV17

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 665 to 666.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 665

```text
9 seev.037.001.17
CorporateActionMovementReversalAdviceV1
7
9.1 MessageDefinition Functionality
Scope
The CorporateActionMovementReversalAdvice message is sent by an account servicer to an account
owner or its designated agent to reverse a previously confirmed posting of securities or cash.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionMovementReversalAdviceV17 MessageDefinition is composed of 14
MessageBuildingBlocks:
A. MovementConfirmationIdentification
Identification of a previously sent movement confirmation document.
B. OtherDocumentIdentification
Identification of other documents as well as the document number.
C. EventsLinkage
Identification of another corporate action event that needs to be closely linked to the processing of
the event notified in this document.
D. ReversalReason
Reason for the reversal.
E. TransactionIdentification
Transaction type and identification information.
F. CorporateActionGeneralInformation
General information about the corporate action event.
G. AccountDetails
General information about the safekeeping account, owner and account balance.
H. CorporateActionDetails
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 665 February 2026
```

## File page 666

```text
Information about the corporate action event.
I. CorporateActionConfirmationDetails
Information about the corporate action option.
J. AdditionalInformation
Provides additional information.
K. IssuerAgent
Party appointed to administer the event on behalf of the issuer company/offeror. The party may be
contacted for more information about the event.
L. PayingAgent
Agent (principal or fiscal paying agent) appointed to execute the payment for the corporate action
event on behalf of the issuer company/offeror.
M. SubPayingAgent
Sub-agent appointed to execute the payment for the corporate action event on behalf of the issuer
company/offeror.
N. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 666 February 2026
```

