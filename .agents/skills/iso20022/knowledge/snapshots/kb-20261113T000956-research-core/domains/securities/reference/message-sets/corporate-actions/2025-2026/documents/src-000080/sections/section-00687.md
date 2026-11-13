---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.13 Identification Information", "16.1.13.4 IdentificationType42Choice", "16.1.13.4.2 Proprietary <Prtry>"]
file_pages: [878]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.13.4.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 878 to 878.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 878

```text
Datatype: "TypeOfIdentification1Code" on page 1242
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
16.1.13.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of identification is defined using a data source scheme.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.13.5  GenericIdentification36
Definition: Identification using a proprietary scheme.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 878
   Issuer <Issr> [1..1] Text 878
   SchemeName <SchmeNm> [0..1] Text 879
16.1.13.5.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Max35Text" on page 1251
16.1.13.5.2  Issuer <Issr>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 878 February 2026
```

