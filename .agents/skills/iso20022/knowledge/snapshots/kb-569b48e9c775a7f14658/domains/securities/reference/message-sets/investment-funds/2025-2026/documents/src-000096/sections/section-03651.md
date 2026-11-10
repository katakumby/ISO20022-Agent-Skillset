---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification", "66.1.29.6 PartyIdentification220", "66.1.29.6.1 Identification <Id>"]
file_pages: [4901]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29.6.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4901 to 4901.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4901

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1]  4901
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4901
Or     ProprietaryIdentification <PrtryId> [1..1] ± 4902
Or     NameAndAddress <NmAndAdr> [1..1]  4902
       Name <Nm> [1..1] Text 4902
       PostalAddress <PstlAdr> [0..1] ± C23 4902
Or     TaxIdentificationNumber <TaxIdNb> [1..1] Text 4903
Or}     NationalRegistrationNumber <NtlRegnNb> [1..1] Text 4903
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4904
Constraints
• OrganisationIdentificationRule
Either Identification or Legal Entity Identifier must be present. Both Identification and Legal Entity
Identifier may be present.
Following Must be True
    /Identification Must be present
 Or    /LegalEntityIdentifier Must be present
66.1.29.6.1  Identification <Id>
Presence: [0..1]
Definition: Identification of the organisation.
Identification <Id> contains one of the following PartyIdentification182Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4901
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4902
Or   NameAndAddress <NmAndAdr> [1..1]  4902
     Name <Nm> [1..1] Text 4902
     PostalAddress <PstlAdr> [0..1] ± C23 4902
Or   TaxIdentificationNumber <TaxIdNb> [1..1] Text 4903
Or}   NationalRegistrationNumber <NtlRegnNb> [1..1] Text 4903
66.1.29.6.1.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Identification of the party expressed as a BIC.
Impacted by: C4 "AnyBIC"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4901 May 2026
```

