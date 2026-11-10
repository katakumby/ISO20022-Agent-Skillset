---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["4 seev.032.001.09 CorporateActionEventProcessingStatusAdviceV09"]
file_pages: [266]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.032.001.09"]
---

# 4 seev.032.001.09 CorporateActionEventProcessingStatusAdviceV09

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 266 to 266.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 266

```text
4 seev.032.001.09
CorporateActionEventProcessingStatusAdvic
eV09
4.1 MessageDefinition Functionality
Scope
An account servicer sends the CorporateActionEventProcessingStatusAdvice message to an account
owner or its designated agent to report processing status of a corporate action event.
The account servicer uses this message to provide a reason as to why a corporate action event has not
been completed by the announced payment dates.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate),
using the relevant elements in the business application header (BAH).
Outline
The CorporateActionEventProcessingStatusAdviceV09 MessageDefinition is composed of 6
MessageBuildingBlocks:
A. NotificationIdentification
Identification of a previously sent notification document.
B. OtherDocumentIdentification
Identification of other documents as well as the document number.
C. CorporateActionGeneralInformation
General information about the corporate action event.
D. EventProcessingStatus
Information about the status of the corporate action.
E. AdditionalInformation
Provides additional information.
F. SupplementaryData
Approved by the Securities SEG on 27 January 2026 seev.032.001.09
CorporateActionEventProcessingStatusAdviceV09
Corporate Actions - Maintenance 2025 - 2026 266 February 2026
```

