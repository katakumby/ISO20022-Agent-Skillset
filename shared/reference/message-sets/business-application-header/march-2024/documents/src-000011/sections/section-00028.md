---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.1 MessageComponents", "3.1.1 Financial Institution Identification", "3.1.1.2 BranchAndFinancialInstitutionIdentification8", "3.1.1.2.2 BranchIdentification <BrnchId>"]
file_pages: [30]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.1.1.2.2 BranchIdentification <BrnchId>

Source: [src-000011](../../../../../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf). Locator: one-based file pages 30 to 30.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 30

```text
Other <Othr> contains the following elements (see "GenericFinancialIdentification1" on page 31 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 32
   SchemeName <SchmeNm> [0..1]  32
{Or     Code <Cd> [1..1] CodeSet 32
Or}     Proprietary <Prtry> [1..1] Text 32
   Issuer <Issr> [0..1] Text 32
3.1.1.2.2  BranchIdentification <BrnchId>
Presence: [0..1]
Definition: Identifies a specific branch of a financial institution.
Usage: This component should be used in case the identification information in the financial institution
component does not provide identification up to branch level.
BranchIdentification <BrnchId> contains the following BranchData5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 30
   LEI <LEI> [0..1] IdentifierSet 30
   Name <Nm> [0..1] Text 30
   PostalAddress <PstlAdr> [0..1] ± 30
3.1.1.2.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a branch of a financial institution.
Datatype: "Max35Text" on page 57
3.1.1.2.2.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification for the branch of the financial institution.
Datatype: "LEIIdentifier" on page 55
3.1.1.2.2.3  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 56
3.1.1.2.2.4  PostalAddress <PstlAdr>
Presence: [0..1]
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 30 March 2024
```

