---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.1 IndividualPerson31", "66.1.32.1.2 BirthDate <BirthDt>"]
file_pages: [5059]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.1.2 BirthDate <BirthDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5059 to 5059.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5059

```text
66.1.32.1.2  BirthDate <BirthDt>
Presence: [0..1]
Definition: Date on which the person is born.
Datatype: "ISODate" on page 5388
66.1.32.1.3  CountryAndResidentialStatus <CtryAndResdtlSts>
Presence: [0..1]
Definition: Country and residential status of the individual, for example, non-permanent resident.
CountryAndResidentialStatus <CtryAndResdtlSts> contains the following elements (see
"CountryAndResidentialStatusType2" on page 5004 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [1..1] CodeSet C12 5004
   ResidentialStatus <ResdtlSts> [1..1] CodeSet 5004
66.1.32.1.4  BeneficiaryCertificationCompletion <BnfcryCertfctnCmpltn>
Presence: [0..1]
Definition: Beneficial owner or its designated agent certifies that it complies with any holding or
investment restrictions or requirements of the fund.
Datatype: "BeneficiaryCertificationCompletion1Code" on page 5277
CodeName Name Definition
NCER CertificationNotRequired Certification is not required for this fund.
ELEC ElectronicCertification Electronic certification is acceptable.
PHYS PhysicalCertification Electronic certification is not acceptable
and is required in physical form.
66.1.32.1.5  OtherIdentification <OthrId>
Presence: [0..*]
Definition: Alternative identification, for example, national registration identification number, passport
number, or an account number used to further identify the beneficial owner, for example, a Central
Provident Fund (CFP) account as required for Singapore.
OtherIdentification <OthrId> contains the following GenericIdentification164 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 5060
   IdentificationType <IdTp> [1..1]  5060
{Or     Code <Cd> [1..1] CodeSet 5060
Or}     Proprietary <Prtry> [1..1] ± 5061
   Issuer <Issr> [0..1] Text 5061
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5059 May 2026
```

