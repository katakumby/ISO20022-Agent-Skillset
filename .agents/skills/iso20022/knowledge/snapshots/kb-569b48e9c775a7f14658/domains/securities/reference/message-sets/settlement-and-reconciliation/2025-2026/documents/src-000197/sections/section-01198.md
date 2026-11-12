---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.96 SafekeepingPlaceFormat41Choice", "35.1.16.96.1 Identification <Id>"]
file_pages: [1649]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.96.1 Identification <Id>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1649 to 1649.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1649

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  1649
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1649
     Identification <Id> [0..1] Text 1649
Or   Country <Ctry> [1..1] CodeSet C7 1649
Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1650
Or   TypeAndIdentification <TpAndId> [1..1]  1650
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1650
     Identification <Id> [1..1] IdentifierSet C5 1650
Or}   Proprietary <Prtry> [1..1] ± 1651
35.1.16.96.1  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping expressed as a code and a narrative description.
Identification <Id> contains the following SafekeepingPlaceTypeAndText8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1649
   Identification <Id> [0..1] Text 1649
35.1.16.96.1.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Definition: Place of safekeeping as a code.
Datatype: "SafekeepingPlace3Code" on page 2137
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
35.1.16.96.1.2  Identification <Id>
Presence: [0..1]
Definition: Additional information about the place of safekeeping.
Datatype: "Max35Text" on page 2192
35.1.16.96.2  Country <Ctry>
Presence: [1..1]
Definition: Place of safekeeping expressed with a country code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1649 March 2026
```

