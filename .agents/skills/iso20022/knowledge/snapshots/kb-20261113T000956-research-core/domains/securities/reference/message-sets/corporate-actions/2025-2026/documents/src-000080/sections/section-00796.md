---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.66 SafekeepingPlaceFormat41Choice", "16.1.15.66.1 Identification <Id>"]
file_pages: [996]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.66.1 Identification <Id>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 996 to 996.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 996

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  996
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 996
     Identification <Id> [0..1] Text 996
Or   Country <Ctry> [1..1] CodeSet C3 996
Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 997
Or   TypeAndIdentification <TpAndId> [1..1]  997
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 997
     Identification <Id> [1..1] IdentifierSet C1 997
Or}   Proprietary <Prtry> [1..1] ± 998
16.1.15.66.1  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping expressed as a code and a narrative description.
Identification <Id> contains the following SafekeepingPlaceTypeAndText8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 996
   Identification <Id> [0..1] Text 996
16.1.15.66.1.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Definition: Place of safekeeping as a code.
Datatype: "SafekeepingPlace3Code" on page 1242
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
16.1.15.66.1.2  Identification <Id>
Presence: [0..1]
Definition: Additional information about the place of safekeeping.
Datatype: "Max35Text" on page 1251
16.1.15.66.2  Country <Ctry>
Presence: [1..1]
Definition: Place of safekeeping expressed with a country code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 996 February 2026
```

