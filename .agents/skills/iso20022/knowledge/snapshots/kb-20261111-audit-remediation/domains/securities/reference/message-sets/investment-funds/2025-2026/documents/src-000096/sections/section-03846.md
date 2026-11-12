---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.38 Safekeeping Place", "66.1.38.2 SafekeepingPlaceFormatChoice", "66.1.38.2.2 IdentificationAsDSS <IdAsDSS>"]
file_pages: [5135]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.38.2.2 IdentificationAsDSS <IdAsDSS>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5135 to 5135.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5135

```text
Party <Pty> contains the following elements (see "PartyIdentification3" on page 4895 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICOrBEI <BICOrBEI> [1..1] IdentifierSet C5 4895
66.1.38.2.2  IdentificationAsDSS <IdAsDSS>
Presence: [1..1]
Definition: Place of safekeeping expressed with a propriety identification scheme.
IdentificationAsDSS <IdAsDSS> contains the following elements (see "GenericIdentification5" on
page 4549 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [1..1] Text 4549
   Information <Inf> [1..1] Text 4549
   Narrative <Nrrtv> [0..1] Text 4549
66.1.38.2.3  IdentificationAsCountry <IdAsCtry>
Presence: [1..1]
Definition: Place of safekeeping expressed with a country code.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.38.3  SafekeepingPlaceFormat28Choice
Definition: Choice of formats for a place of safekeeping.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  5136
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 5136
     Identification <Id> [0..1] Text 5136
Or   Country <Ctry> [1..1] CodeSet C12 5136
Or   TypeAndIdentification <TpAndId> [1..1]  5136
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 5137
     Identification <Id> [1..1] IdentifierSet C4 5137
Or}   Proprietary <Prtry> [1..1] ± 5137
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5135 May 2026
```

