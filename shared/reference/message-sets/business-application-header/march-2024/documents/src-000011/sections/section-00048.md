---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.1 MessageComponents", "3.1.6 System Identification", "3.1.6.1 ClearingSystemIdentification2Choice", "3.1.6.1.1 Code <Cd>"]
file_pages: [50]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.1.6.1.1 Code <Cd>

Source: [src-000011](../../../../../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf). Locator: one-based file pages 50 to 50.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 50

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 50
Or}   Proprietary <Prtry> [1..1] Text 50
3.1.6.1.1  Code <Cd>
Presence: [1..1]
Definition: Identification of a clearing system, in a coded form as published in an external list.
Datatype: "ExternalClearingSystemIdentification1Code" on page 51
3.1.6.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Identification code for a clearing system, that has not yet been identified in the list of clearing
systems.
Datatype: "Max35Text" on page 57
3.2 Message Datatypes
3.2.1 CodeSet
3.2.1.1  AddressType2Code
Definition: Specifies the type of address.
Type: CodeSet
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
3.2.1.2  BusinessMessagePriorityCode
Definition: Specifies the priority levels for the BusinessMessage.
The different priorities are typically user / service / implementation dependent. The semantics of the
different values for a Mesage (Set) need to be defined by the relevant user community (SEG.).
Type: CodeSet
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 50 March 2024
```

