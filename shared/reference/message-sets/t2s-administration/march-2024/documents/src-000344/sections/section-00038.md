---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 Message Items Types", "5.1 MessageComponents", "5.1.5 Financial Institution Identification", "5.1.5.2 BranchAndFinancialInstitutionIdentification8", "5.1.5.2.2 BranchIdentification <BrnchId>"]
file_pages: [45]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 5.1.5.2.2 BranchIdentification <BrnchId>

Source: [src-000344](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 45 to 45.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 45

```text
Other <Othr> contains the following elements (see "GenericFinancialIdentification1" on page 46 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 47
   SchemeName <SchmeNm> [0..1]  47
{Or     Code <Cd> [1..1] CodeSet 47
Or}     Proprietary <Prtry> [1..1] Text 47
   Issuer <Issr> [0..1] Text 47
5.1.5.2.2  BranchIdentification <BrnchId>
Presence: [0..1]
Definition: Identifies a specific branch of a financial institution.
Usage: This component should be used in case the identification information in the financial institution
component does not provide identification up to branch level.
BranchIdentification <BrnchId> contains the following BranchData5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 45
   LEI <LEI> [0..1] IdentifierSet 45
   Name <Nm> [0..1] Text 45
   PostalAddress <PstlAdr> [0..1] ± 45
5.1.5.2.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a branch of a financial institution.
Datatype: "Max35Text" on page 69
5.1.5.2.2.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification for the branch of the financial institution.
Datatype: "LEIIdentifier" on page 67
5.1.5.2.2.3  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 68
5.1.5.2.2.4  PostalAddress <PstlAdr>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Administration - Maintenance 2023 -
2024
45 March 2024
```

