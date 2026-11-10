---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.5 IndividualPerson32", "66.1.32.5.4 OtherIdentification <OthrId>", "66.1.32.5.4.2 IdentificationType <IdTp>", "66.1.32.5.4.2.2 Proprietary <Prtry>"]
file_pages: [5078]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.5.4.2.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5078 to 5078.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5078

```text
CodeName Name Definition
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
AREG AlienRegistrationNumber Number assigned by a government
agency to identify foreign nationals.
DRLC DriversLicenseNumber Number assigned by a license authority
to a driver's license.
EMID EmployerIdentificationNumber Number assigned to an employer by a
registration authority.
NINV NonResidentInvestor Number that identifies the type of
investor registered at a securities and
exchange commission.
INCL IndustryClassification Number, typically assigned by a
government to describe ownership,
administrative and authoritative relations.
GIIN GlobalIntermediaryIdentificationNumber Global intermediary tax identification
number.
66.1.32.5.4.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of identification expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.32.5.4.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identifier.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5078 May 2026
```

