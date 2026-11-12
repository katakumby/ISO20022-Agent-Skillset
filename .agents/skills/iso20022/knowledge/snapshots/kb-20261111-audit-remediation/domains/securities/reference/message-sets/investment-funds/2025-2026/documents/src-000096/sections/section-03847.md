---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.38 Safekeeping Place", "66.1.38.3 SafekeepingPlaceFormat28Choice", "66.1.38.3.1 Identification <Id>"]
file_pages: [5136]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.38.3.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5136 to 5136.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5136

```text
66.1.38.3.1  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping expressed as a code and a narrative description.
Identification <Id> contains the following SafekeepingPlaceTypeAndText6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 5136
   Identification <Id> [0..1] Text 5136
66.1.38.3.1.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Definition: Place of safekeeping as a code.
Datatype: "SafekeepingPlace2Code" on page 5359
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
ALLP AllPlaces All places of safekeeping where the
financial instrument is held.
66.1.38.3.1.2  Identification <Id>
Presence: [0..1]
Definition: Additional information about the place of safekeeping.
Datatype: "Max35Text" on page 5403
66.1.38.3.2  Country <Ctry>
Presence: [1..1]
Definition: Place of safekeeping expressed with a country code.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.38.3.3  TypeAndIdentification <TpAndId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a type and identification.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5136 May 2026
```

