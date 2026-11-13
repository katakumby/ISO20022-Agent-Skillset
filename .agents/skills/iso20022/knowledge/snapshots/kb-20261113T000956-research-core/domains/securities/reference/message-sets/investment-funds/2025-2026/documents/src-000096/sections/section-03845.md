---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.38 Safekeeping Place", "66.1.38.2 SafekeepingPlaceFormatChoice", "66.1.38.2.1 Identification <Id>", "66.1.38.2.1.1 PlaceSafekeeping <PlcSfkpg>"]
file_pages: [5134]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.38.2.1.1 PlaceSafekeeping <PlcSfkpg>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5134 to 5134.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5134

```text
Definition: Place of safekeeping expressed as a code and BIC.
Impacted by: C13 "Party1Rule"
Identification <Id> contains the following SafekeepingPlaceAsCodeAndPartyIdentification
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceSafekeeping <PlcSfkpg> [1..1] CodeSet 5134
   Narrative <Nrrtv> [0..1] Text 5134
   Party <Pty> [0..1] ± 5134
Constraints
• Party1Rule
If PlaceSafekeeping is not SHHE, then Party is mandatory. If PlaceSafekeeping is SHHE, then Party
is optional.
66.1.38.2.1.1  PlaceSafekeeping <PlcSfkpg>
Presence: [1..1]
Definition: Place of safekeeping as a code.
Datatype: "SafekeepingPlace1Code" on page 5358
CodeName Name Definition
CUST SharesHeldAtLocalCustodian Financial instruments held at a local
custodian.
ICSD SharesHeldAtICSD Financial instruments held at an
International Central Securities
Depository.
NCSD SharesHeldAtNCSD Financial instruments held at a National
Central Securities Depository.
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
66.1.38.2.1.2  Narrative <Nrrtv>
Presence: [0..1]
Definition: Additional information about the place of safekeeping.
Datatype: "Max35Text" on page 5403
66.1.38.2.1.3  Party <Pty>
Presence: [0..1]
Definition: Place of safekeeping.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5134 May 2026
```

