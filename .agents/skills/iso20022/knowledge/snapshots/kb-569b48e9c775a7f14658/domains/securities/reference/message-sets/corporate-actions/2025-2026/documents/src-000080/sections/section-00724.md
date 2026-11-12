---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.17 CorporateActionProcessingStatus5Choice", "16.1.15.17.1 Code <Cd>"]
file_pages: [917]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.17.1 Code <Cd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 917 to 917.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 917

```text
16.1.15.17.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the status of the details of the corporate action event.
Code <Cd> contains the following CorporateActionEventStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EventCompletenessStatus <EvtCmpltnsSts> [1..1] CodeSet 917
   EventConfirmationStatus <EvtConfSts> [1..1] CodeSet 917
16.1.15.17.1.1  EventCompletenessStatus <EvtCmpltnsSts>
Presence: [1..1]
Definition: Indicates whether the details provided about an event are complete or incomplete.
Datatype: "EventCompletenessStatus1Code" on page 1208
CodeName Name Definition
COMP Complete Event details are complete.
INCO Incomplete Event details are not complete.
16.1.15.17.1.2  EventConfirmationStatus <EvtConfSts>
Presence: [1..1]
Definition: Indicates the status of the occurrence of an event.
Datatype: "EventConfirmationStatus1Code" on page 1208
CodeName Name Definition
CONF Confirmed Occurrence of the event has been
confirmed.
UCON Unconfirmed Occurrence of the event has not been
confirmed.
16.1.15.17.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Information related to an identification, for example, party identification or account
identification.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 917 February 2026
```

