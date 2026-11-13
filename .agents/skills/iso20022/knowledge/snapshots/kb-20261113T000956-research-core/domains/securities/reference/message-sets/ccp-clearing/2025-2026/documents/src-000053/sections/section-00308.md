---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.9 Identification Information", "12.1.9.1 GenericIdentification29", "12.1.9.1.2 Issuer <Issr>"]
file_pages: [397]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.9.1.2 Issuer <Issr>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 397 to 397.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 397

```text
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: Max35Text on page 493
12.1.9.1.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: Max35Text on page 493
12.1.9.1.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: Max35Text on page 493
12.1.9.2  IdentificationType6Choice
Definition: Choice between a code and a data source scheme to specify the type of alternate
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 397
Or}   Proprietary <Prtry> [1..1] ± 397
12.1.9.2.1  Code <Cd>
Presence: [1..1]
Definition: Type of identification is defined using an ISO 20022 code.
Datatype: TypeOfIdentification1Code on page 486
CodeName Name Definition
ARNU AlienRegistrationNumber Number assigned by a government
agency to identify foreign nationals.
CCPT PassportNumber Number assigned by a passport
authority.
CHTY TaxExemptIdentificationNumber Number assigned to a tax exempt entity.
CORP CorporateIdentification Number assigned to a corporate entity.
DRLC DriverLicenseNumber Number assigned to a driver's license.
FIIN ForeignInvestmentIdentityNumber Number assigned to a foreign investor
(other than the alien number).
TXID TaxIdentificationNumber Number assigned by a tax authority to
an entity.
12.1.9.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of identification is defined using a proprietary code.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 397
```

