---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.38 Safekeeping Place", "66.1.38.1 SafekeepingPlaceFormat42Choice", "66.1.38.1.4 TypeAndIdentification <TpAndId>", "66.1.38.1.4.2 Identification <Id>"]
file_pages: [5133]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.38.1.4.2 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5133 to 5133.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5133

```text
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
66.1.38.1.4.2  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping.
Impacted by: C4 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 5389
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
66.1.38.1.5  Proprietary <Prtry>
Presence: [1..1]
Definition: Place of safekeeping expressed with a propriety identification scheme.
Proprietary <Prtry> contains the following elements (see "GenericIdentification78" on page 4554 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 4554
   Identification <Id> [0..1] Text 4554
66.1.38.2  SafekeepingPlaceFormatChoice
Definition: Choice of formats for the place of safekeeping.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  C13 5133
     PlaceSafekeeping <PlcSfkpg> [1..1] CodeSet 5134
     Narrative <Nrrtv> [0..1] Text 5134
     Party <Pty> [0..1] ± 5134
Or   IdentificationAsDSS <IdAsDSS> [1..1] ± 5135
Or}   IdentificationAsCountry <IdAsCtry> [1..1] CodeSet C12 5135
66.1.38.2.1  Identification <Id>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5133 May 2026
```

