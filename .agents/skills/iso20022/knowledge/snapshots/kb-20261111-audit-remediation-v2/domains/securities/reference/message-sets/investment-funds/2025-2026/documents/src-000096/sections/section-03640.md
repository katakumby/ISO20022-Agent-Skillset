---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification", "66.1.29.2 Organisation40", "66.1.29.2.3 Identification <Id>", "66.1.29.2.3.1 AnyBIC <AnyBIC>"]
file_pages: [4890]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29.2.3.1 AnyBIC <AnyBIC>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4890 to 4890.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4890

```text
Definition: Unique and unambiguous identifier for the organisation.
Identification <Id> contains one of the following PartyIdentification177Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4890
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 4890
66.1.29.2.3.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C4 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 5389
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
66.1.29.2.3.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification1" on
page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.29.2.4  LegalEntityIdentifier <LglNttyIdr>
Presence: [0..1]
Definition: Identification of the organisation with a Legal Entity Identifier. This is a code allocated to a
party as described in ISO 17442 "Financial Services - Legal Entity Identifier (LEI)".
Datatype: "LEIIdentifier" on page 5395
66.1.29.2.5  Purpose <Purp>
Presence: [0..1]
Definition: Purpose of the organisation, for example, charity.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4890 May 2026
```

