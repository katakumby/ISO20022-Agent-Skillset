---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.39 Securities Identification", "66.1.39.2 SecurityIdentification3Choice", "66.1.39.2.10 Dutch <Dtch>"]
file_pages: [5141]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.39.2.10 Dutch <Dtch>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5141 to 5141.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5141

```text
66.1.39.2.10  Dutch <Dtch>
Presence: [1..1]
Definition: Identifier for Dutch securities.
Datatype: "DutchIdentifier" on page 5392
66.1.39.2.11  Valoren <Vlrn>
Presence: [1..1]
Definition: Identifier for Swiss securities assigned by Telekurs Financial, the Swiss numbering agency.
Datatype: "ValorenIdentifier" on page 5399
66.1.39.2.12  Sicovam <SCVM>
Presence: [1..1]
Definition: Identifier for French securities assigned by the Societe Interprofessionnelle Pour La
Compensation des Valeurs Mobilieres in France. The Sicovam is composed of 5-digits.
Datatype: "SicovamIdentifier" on page 5397
66.1.39.2.13  Belgian <Belgn>
Presence: [1..1]
Definition: Identifier for Belgian securities.
Datatype: "BelgianIdentifier" on page 5390
66.1.39.2.14  Common <Cmon>
Presence: [1..1]
Definition: Identifier of securities issued in Luxembourg. The common code is a 9-digit code that
replaces the CEDEL (Clearstream) and Euroclear codes.
Datatype: "EuroclearClearstreamIdentifier" on page 5393
66.1.39.2.15  OtherProprietaryIdentification <OthrPrtryId>
Presence: [1..1]
Definition: Proprietary identification of a security assigned by an institution or organisation.
OtherProprietaryIdentification <OthrPrtryId> contains the following elements (see
"AlternateSecurityIdentification1" on page 5138 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 5138
{Or   DomesticIdentificationSource <DmstIdSrc> [1..1] CodeSet C12 5138
Or}   ProprietaryIdentificationSource <PrtryIdSrc> [1..1] Text 5138
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5141 May 2026
```

