---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["10 seev.038.001.09 CorporateActionNarrativeV09"]
file_pages: [692]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.038.001.09"]
---

# 10 seev.038.001.09 CorporateActionNarrativeV09

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 692 to 692.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 692

```text
10 seev.038.001.09
CorporateActionNarrativeV09
10.1 MessageDefinition Functionality
Scope
The CorporateActionNarrative message is sent between an account servicer and an account owner or
its designated agent to cater for such processes that cannot be handled using messages such as the
CorporateActionNotification. It is not to be used for event narrative as that should be included in the
CorporateActionNotification. Examples of when the CorporateActionNarrative message may be used
include tax reclaims, restrictions, documentation requirements. This message should only be used
when bilaterally agreed. This message is bi-directional.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionNarrativeV09 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. AccountDetails
General information about the safekeeping account and the account owner.
B. UnderlyingSecurity
Provides information about the securitised right for entitlement.
C. CorporateActionGeneralInformation
General information about the corporate action event.
D. AdditionalInformation
Provides additional information.
E. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.038.001.09 CorporateActionNarrativeV09
Corporate Actions - Maintenance 2025 - 2026 692 February 2026
```

