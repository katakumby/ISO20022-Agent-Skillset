---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.4 AdditionalBusinessProcessFormat17Choice", "16.1.15.4.2 Proprietary <Prtry>"]
file_pages: [891]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.4.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 891 to 891.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 891

```text
16.1.15.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the additional business process linked to a corporate action
event.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.5  OptionAvailabilityStatus3Choice
Definition: Choice between a standard code or proprietary code to specify the option availability status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 891
Or}   Proprietary <Prtry> [1..1] ± 891
16.1.15.5.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the status of the option availability.
Datatype: "OptionAvailabilityStatus1Code" on page 1224
CodeName Name Definition
INTV Inactive Option is not active and can no longer be
responded to. Any responses already
processed against this option will remain
valid, for example, expired option.
CANC Cancelled Option is not valid; it has been cancelled
by the market or service provider, and
cannot be responded to. Any responses
already processed against this option
are considered void and new responses
will be required.
16.1.15.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the status of the option availability.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 891 February 2026
```

