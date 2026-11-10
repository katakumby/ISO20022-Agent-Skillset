---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification", "66.1.29.6 PartyIdentification220", "66.1.29.6.2 LegalEntityIdentifier <LglNttyIdr>"]
file_pages: [4904]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29.6.2 LegalEntityIdentifier <LglNttyIdr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4904 to 4904.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4904

```text
Datatype: "Max35Text" on page 5403
66.1.29.6.2  LegalEntityIdentifier <LglNttyIdr>
Presence: [0..1]
Definition: Identification of the organisation with a Legal Entity Identifier. This is a code allocated to a
party as described in ISO 17442 "Financial Services - Legal Entity Identifier (LEI)".
Datatype: "LEIIdentifier" on page 5395
66.1.29.7  Organisation36
Definition: Organised structure that is set up for a particular purpose, for example, a business,
government body, department, charity, or financial institution.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4904
   Identification <Id> [0..1] ± 4904
   Purpose <Purp> [0..1] Text 4904
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C12 4905
   RegistrationCountry <RegnCtry> [0..1] CodeSet C12 4905
   RegistrationDate <RegnDt> [0..1] Date 4905
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 4905
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 4905
   CorporateInvestorAddress <CorpInvstrAdr> [1..1] ± 4905
66.1.29.7.1  Name <Nm>
Presence: [1..1]
Definition: Name by which the party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 5402
66.1.29.7.2  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the organisation.
Identification <Id> contains the following elements (see "PartyIdentification140" on page 5013 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5013
   LEI <LEI> [0..1] IdentifierSet 5014
66.1.29.7.3  Purpose <Purp>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4904 May 2026
```

