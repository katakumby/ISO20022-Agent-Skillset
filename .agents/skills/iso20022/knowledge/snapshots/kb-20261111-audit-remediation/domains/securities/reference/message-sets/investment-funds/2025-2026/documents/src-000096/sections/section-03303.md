---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.23 Identification Information", "66.1.23.5 GenericIdentification47", "66.1.23.5.1 Identification <Id>"]
file_pages: [4540]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.23.5.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4540 to 4540.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4540

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.23.5.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Exact4AlphaNumericText" on page 5402
66.1.23.5.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max4AlphaNumericText" on page 5404
66.1.23.5.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max4AlphaNumericText" on page 5404
66.1.23.6  IdentificationSource5Choice
Definition: Choice between source of identification of a financial instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DomesticIdentificationSource <DmstIdSrc> [1..1] CodeSet C12 4540
Or}   ProprietaryIdentificationSource <PrtryIdSrc> [1..1] Text 4540
66.1.23.6.1  DomesticIdentificationSource <DmstIdSrc>
Presence: [1..1]
Definition: Country of the proprietary identification scheme.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.23.6.2  ProprietaryIdentificationSource <PrtryIdSrc>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4540 May 2026
```

