---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.16 Identification Information", "7.1.16.3 IdentificationType42Choice", "7.1.16.3.2 Proprietary <Prtry>"]
file_pages: [350]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.16.3.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 350 to 350.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 350

```text
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
7.1.16.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of identification is defined using a data source scheme.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.16.4  GenericIdentification36
Definition: Identification using a proprietary scheme.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 350
   Issuer <Issr> [1..1] Text 350
   SchemeName <SchmeNm> [0..1] Text 351
7.1.16.4.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Max35Text" on page 557
7.1.16.4.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 350 March 2026
```

