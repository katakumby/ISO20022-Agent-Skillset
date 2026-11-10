---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.8 Financial Institution Identification", "16.1.8.2 BranchData3"]
file_pages: [865]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.8.2 BranchData3

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 865 to 865.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 865

```text
Other <Othr> contains the following elements (see "GenericFinancialIdentification1" on page 866 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 866
   SchemeName <SchmeNm> [0..1]  867
{Or     Code <Cd> [1..1] CodeSet 867
Or}     Proprietary <Prtry> [1..1] Text 867
   Issuer <Issr> [0..1] Text 867
16.1.8.2  BranchData3
Definition: Information that locates and identifies a specific branch of a financial institution.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 865
   LEI <LEI> [0..1] IdentifierSet 865
   Name <Nm> [0..1] Text 865
   PostalAddress <PstlAdr> [0..1] ± 865
16.1.8.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a branch of a financial institution.
Datatype: "Max35Text" on page 1251
16.1.8.2.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification for the branch of the financial institution.
Datatype: "LEIIdentifier" on page 1246
16.1.8.2.3  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 1249
16.1.8.2.4  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 865 February 2026
```

