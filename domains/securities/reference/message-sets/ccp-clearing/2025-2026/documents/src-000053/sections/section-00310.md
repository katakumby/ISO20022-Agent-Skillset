---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.9 Identification Information", "12.1.9.4 GenericIdentification20"]
file_pages: [399]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.9.4 GenericIdentification20

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 399 to 399.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 399

```text
12.1.9.4  GenericIdentification20
Definition: Information related to an identification, for example, party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 399
   Issuer <Issr> [1..1] Text 399
   SchemeName <SchmeNm> [0..1] Text 399
Constraints
• CoexistenceIssuerSchemeNameRule
(Rule)
During ISO 15022-20022 coexistence, Issuer length must be 4 characters and SchemeName length
must be 4 characters or less. Issuer and Scheme Name must be an ISO registered Issuer and
SchemeName.
12.1.9.4.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: Exact4AlphaNumericText on page 492
12.1.9.4.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: Max35Text on page 493
12.1.9.4.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: Max35Text on page 493
12.1.9.5  GenericIdentification36
Definition: Identification using a proprietary scheme.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 399
   Issuer <Issr> [1..1] Text 400
   SchemeName <SchmeNm> [0..1] Text 400
12.1.9.5.1  Identification <Id>
Presence: [1..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 399
```

