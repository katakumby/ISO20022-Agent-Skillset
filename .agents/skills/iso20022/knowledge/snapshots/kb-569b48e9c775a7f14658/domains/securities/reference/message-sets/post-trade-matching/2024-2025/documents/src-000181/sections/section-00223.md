---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.17 Identification Information", "7.1.17.3 IdentificationType43Choice"]
file_pages: [277]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.17.3 IdentificationType43Choice

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 277 to 277.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 277

```text
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Max35Text" on page 669
7.1.17.3  IdentificationType43Choice
Definition: Choice between a code and a data source scheme to specify the type of alternate
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 277
Or}   Proprietary <Prtry> [1..1] ± 277
7.1.17.3.1  Code <Cd>
Presence: [1..1]
Definition: Type of identification is defined using a code.
Datatype: "TypeOfIdentification2Code" on page 657
CodeName Name Definition
ARNU AlienRegistrationNumber Number assigned by a government
agency to identify foreign nationals.
CHTY TaxExemptIdentificationNumber Number assigned to a tax exempt entity.
CORP CorporateIdentification Number assigned to a corporate entity.
FIIN ForeignInvestmentIdentityNumber Number assigned to a foreign investor
(other than the alien number).
TXID TaxIdentificationNumber Number assigned by a tax authority to
an entity.
7.1.17.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of identification is defined using a data source scheme.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 279 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 279
   Issuer <Issr> [1..1] Text 279
   SchemeName <SchmeNm> [0..1] Text 279
7.1.17.4  SimpleIdentificationInformation2
Definition: Information related to a party identification or account identification.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 277 February 2025
```

