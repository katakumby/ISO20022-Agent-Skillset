---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.1 IndividualPerson31", "66.1.32.1.5 OtherIdentification <OthrId>", "66.1.32.1.5.2 IdentificationType <IdTp>", "66.1.32.1.5.2.2 Proprietary <Prtry>"]
file_pages: [5061]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.1.5.2.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5061 to 5061.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5061

```text
CodeName Name Definition
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
66.1.32.1.5.2.2  Proprietary <Prtry>
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
66.1.32.1.5.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identifier.
Datatype: "Max35Text" on page 5403
66.1.32.2  IndividualPerson35
Definition: Human entity, as distinguished from a corporate entity (which is sometimes referred to as an
'artificial person').
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   GivenName <GvnNm> [0..1] Text 5062
   MiddleName <MddlNm> [0..1] Text 5062
   Name <Nm> [1..1] Text 5062
   Gender <Gndr> [0..1] CodeSet 5062
   BirthDate <BirthDt> [0..1] Date 5062
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5061 May 2026
```

