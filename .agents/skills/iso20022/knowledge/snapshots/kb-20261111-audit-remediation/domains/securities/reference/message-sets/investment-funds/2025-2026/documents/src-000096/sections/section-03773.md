---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.1 IndividualPerson31", "66.1.32.1.5 OtherIdentification <OthrId>", "66.1.32.1.5.1 Identification <Id>"]
file_pages: [5060]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.1.5.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5060 to 5060.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5060

```text
66.1.32.1.5.1  Identification <Id>
Presence: [1..1]
Definition: Name or number assigned by an entity to enable recognition of that entity, for example,
account identifier.
Datatype: "Max35Text" on page 5403
66.1.32.1.5.2  IdentificationType <IdTp>
Presence: [1..1]
Definition: Specifies the nature of the identifier.
IdentificationType <IdTp> contains one of the following OtherIdentification3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5060
Or}   Proprietary <Prtry> [1..1] ± 5061
66.1.32.1.5.2.1  Code <Cd>
Presence: [1..1]
Definition: Type of identification expressed as a code.
Datatype: "PartyIdentificationType7Code" on page 5336
CodeName Name Definition
ATIN AdoptionTaxpayerIdentificationNumber Temporary tax processing number (used
in the domestic adoption of a child).
IDCD IdentityCardNumber Number assigned by a national authority
to an identity card.
NRIN NationalRegistrationIdentificationNumber National registration identification
number. In Singapore this is known as
the NRIC.
OTHR Other Another type of identification type.
PASS PassportNumber Number assigned by a passport
authority to a passport.
POCD PostOfficeCardNumber Post office card number as assigned by
a national post office.
SOCS SocialSecurityNumber Number assigned by a social security
agency.
SRSA SRSAccountNumber Supplementary retirement scheme
account number.
GUNL GunLicenseNumber Gun license number as assigned by a
gun licensing authority.
GTIN GenericTaxIdentificationNumber Generic tax identification number.
ITIN IndividualTaxpayerIdentificationNumber Tax processing number.
CPFA CPFAccountNumber Account issued by the Central Provident
Fund Board (Singapore).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5060 May 2026
```

