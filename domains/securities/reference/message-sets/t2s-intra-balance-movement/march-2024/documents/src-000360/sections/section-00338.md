---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.9 Financial Institution Identification", "17.1.9.2 BranchAndFinancialInstitutionIdentification8", "17.1.9.2.2 BranchIdentification <BrnchId>"]
file_pages: [404]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.9.2.2 BranchIdentification <BrnchId>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 404 to 404.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 404

```text
Other <Othr> contains the following elements (see "GenericFinancialIdentification1" on page 405 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 406
   SchemeName <SchmeNm> [0..1]  406
{Or     Code <Cd> [1..1] CodeSet 406
Or}     Proprietary <Prtry> [1..1] Text 406
   Issuer <Issr> [0..1] Text 406
17.1.9.2.2  BranchIdentification <BrnchId>
Presence: [0..1]
Definition: Identifies a specific branch of a financial institution.
Usage: This component should be used in case the identification information in the financial institution
component does not provide identification up to branch level.
BranchIdentification <BrnchId> contains the following BranchData5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 404
   LEI <LEI> [0..1] IdentifierSet 404
   Name <Nm> [0..1] Text 404
   PostalAddress <PstlAdr> [0..1] ± 404
17.1.9.2.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a branch of a financial institution.
Datatype: "Max35Text" on page 497
17.1.9.2.2.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification for the branch of the financial institution.
Datatype: "LEIIdentifier" on page 494
17.1.9.2.2.3  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 496
17.1.9.2.2.4  PostalAddress <PstlAdr>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
404 March 2024
```

