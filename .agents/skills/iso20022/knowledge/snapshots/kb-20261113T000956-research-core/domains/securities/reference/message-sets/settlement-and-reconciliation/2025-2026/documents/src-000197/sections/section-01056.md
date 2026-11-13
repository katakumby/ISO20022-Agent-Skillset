---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.10 IdentificationType42Choice", "35.1.14.10.2 Proprietary <Prtry>"]
file_pages: [1495]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.10.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1495 to 1495.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1495

```text
CodeName Name Definition
CORP CorporateIdentification Number assigned to a corporate entity.
DRLC DriverLicenseNumber Number assigned to a driver's license.
FIIN ForeignInvestmentIdentityNumber Number assigned to a foreign investor
(other than the alien number).
TXID TaxIdentificationNumber Number assigned by a tax authority to
an entity.
35.1.14.10.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of identification is defined using a data source scheme.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.14.11  GenericIdentification3
Definition: Information related to an identification, for example, party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1495
   Issuer <Issr> [0..1] Text 1495
35.1.14.11.1  Identification <Id>
Presence: [1..1]
Definition: Name or number assigned by an entity to enable recognition of that entity, for example,
account identifier.
Datatype: "Max35Text" on page 2192
35.1.14.11.2  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 2192
35.1.14.12  References41Choice
Definition: Choice of reference.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1495 March 2026
```

