---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["11 seev.039.001.13 CorporateActionCancellationAdviceV13"]
file_pages: [701, 702]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.039.001.13"]
---

# 11 seev.039.001.13 CorporateActionCancellationAdviceV13

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 701 to 702.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 701

```text
11 seev.039.001.13
CorporateActionCancellationAdviceV13
11.1 MessageDefinition Functionality
Scope
The CorporateActionCancellationAdvice message is sent by an account servicer to an account owner
or its designated agent to cancel a previously announced corporate action event in case of error from
the account servicer or in case of withdrawal by the issuer.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionCancellationAdviceV13 MessageDefinition is composed of 15
MessageBuildingBlocks:
A. CancellationAdviceGeneralInformation
General information about the event cancellation status and cancellation reason.
B. CorporateActionGeneralInformation
General information about the corporate action event.
C. AccountsDetails
General information about the safekeeping account and the account owner.
D. CorporateActionDetails
Information about the corporate action event.
E. AdditionalText
Provides additional information or specifies in more detail the content of a message. This field may
only be used when the information to be transmitted, cannot be coded.
F. IssuerAgent
Party appointed to administer the event on behalf of the issuer company/offeror. The party may be
contacted for more information about the event.
G. PayingAgent
Agent (principal or fiscal paying agent) appointed to execute the payment for the corporate action
event on behalf of the issuer company/offeror.
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 701 February 2026
```

## File page 702

```text
H. SubPayingAgent
Sub-agent appointed to execute the payment for the corporate action event on behalf of the issuer
company/offeror.
I. Registrar
Party/agent responsible for maintaining the register of a security.
J. ResellingAgent
Broker-dealer responsible for reselling to new investors securities (usually bonds) that have been
tendered for purchase by their owner.
K. PhysicalSecuritiesAgent
Trust company, bank or similar financial institution assigned by an issuer to accept presentations of
instruments, usually bonds, for transfer and or exchange.
L. DropAgent
Trust company, bank or similar financial institution that acts on behalf of an out-of-town agent or
event agent where securities can be delivered in person.
M. SolicitationAgent
Trust company, bank or similar financial institution assigned by an issuer to maintain records of
investors and account balances and transactions for the consent of a material change.
N. InformationAgent
Trust company, bank or similar financial institution assigned by an Issuer to provide information
and copies of the offering documentation.
O. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 702 February 2026
```

