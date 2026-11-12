---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13"]
file_pages: [813, 814]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.044.001.13"]
---

# 15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 813 to 814.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 813

```text
15 seev.044.001.13
CorporateActionMovementPreliminaryAdvice
CancellationAdviceV13
15.1 MessageDefinition Functionality
Scope
The CorporateActionMovementPreliminaryAdviceCancellationAdvice message is sent by an account
servicer to an account owner or its designated agent to cancel a previously announced
CorporateActionMovementPreliminaryAdvice.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 MessageDefinition is
composed of 14 MessageBuildingBlocks:
A. MovementPreliminaryAdviceIdentification
Identification of a previously sent movement preliminary advice document.
B. CorporateActionGeneralInformation
General information about the corporate action event.
C. AccountDetails
General information about the safekeeping account and the account owner.
D. CorporateActionDetails
Information about the corporate action event.
E. IssuerAgent
Party appointed to administer the event on behalf of the issuer company/offeror. The party may be
contacted for more information about the event.
F. PayingAgent
Agent (principal or fiscal paying agent) appointed to execute the payment for the corporate action
event on behalf of the issuer company/offeror.
G. SubPayingAgent
Approved by the Securities SEG on 27 January 2026 seev.044.001.13
CorporateActionMovementPreliminaryAdviceCancel
lationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 813 February 2026
```

## File page 814

```text
Sub-agent appointed to execute the payment for the corporate action event on behalf of the issuer
company/offeror.
H. Registrar
Party/agent responsible for maintaining the register of a security.
I. ResellingAgent
Broker-dealer responsible for reselling to new investors securities (usually bonds) that have been
tendered for purchase by their owner.
J. PhysicalSecuritiesAgent
Trust company, bank or similar financial institution assigned by an issuer to accept presentations of
instruments, usually bonds, for transfer and or exchange.
K. DropAgent
Trust company, bank or similar financial institution that acts on behalf of an out-of-town agent or
event agent where securities can be delivered in person.
L. SolicitationAgent
Trust company, bank or similar financial institution assigned by an issuer to maintain records of
investors and account balances and transactions for the consent of a material change.
M. InformationAgent
Trust company, bank or similar financial institution assigned by an Issuer to provide information
and copies of the offering documentation.
N. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.044.001.13
CorporateActionMovementPreliminaryAdviceCancel
lationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 814 February 2026
```

