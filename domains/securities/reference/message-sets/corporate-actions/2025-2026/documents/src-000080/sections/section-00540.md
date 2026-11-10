---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["11 seev.039.001.13 CorporateActionCancellationAdviceV13", "11.4 Message Building Blocks", "11.4.1 CancellationAdviceGeneralInformation <CxlAdvcGnlInf>", "11.4.1.1 CancellationReasonCode <CxlRsnCd>"]
file_pages: [706]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.039.001.13"]
---

# 11.4.1.1 CancellationReasonCode <CxlRsnCd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 706 to 706.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 706

```text
CancellationAdviceGeneralInformation <CxlAdvcGnlInf> contains the following
CorporateActionCancellation3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CancellationReasonCode <CxlRsnCd> [1..1] CodeSet 706
   CancellationReason <CxlRsn> [0..1] Text 706
   ProcessingStatus <PrcgSts> [1..1]  706
     EventCompletenessStatus <EvtCmpltnsSts> [1..1] CodeSet 706
     EventConfirmationStatus <EvtConfSts> [1..1] CodeSet 707
11.4.1.1  CancellationReasonCode <CxlRsnCd>
Presence: [1..1]
Definition: Specifies reasons for cancellation of a corporate action event.
Datatype: "CorporateActionCancellationReason1Code" on page 1167
CodeName Name Definition
WITH Withrawal Cancellation due to the corporate action
event being cancelled by the issuer.
PROC Processing Cancellation due to a processing error.
11.4.1.2  CancellationReason <CxlRsn>
Presence: [0..1]
Definition: Additional information about cancellation of a corporate action event.
Datatype: "Max140Text" on page 1249
11.4.1.3  ProcessingStatus <PrcgSts>
Presence: [1..1]
Definition: Specifies the status of the details of the event.
ProcessingStatus <PrcgSts> contains the following CorporateActionEventStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EventCompletenessStatus <EvtCmpltnsSts> [1..1] CodeSet 706
   EventConfirmationStatus <EvtConfSts> [1..1] CodeSet 707
11.4.1.3.1  EventCompletenessStatus <EvtCmpltnsSts>
Presence: [1..1]
Definition: Indicates whether the details provided about an event are complete or incomplete.
Datatype: "EventCompletenessStatus1Code" on page 1208
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 706 February 2026
```

