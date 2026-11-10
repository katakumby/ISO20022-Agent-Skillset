---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.7 Financial Institution Identification", "6.1.7.3 BranchAndFinancialInstitutionIdentification8", "6.1.7.3.2 BranchIdentification <BrnchId>"]
file_pages: [543]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.7.3.2 BranchIdentification <BrnchId>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 543 to 543.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 543

```text
Other <Othr> contains the following elements (see "GenericFinancialIdentification1" on page 538 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 538
   SchemeName <SchmeNm> [0..1]  539
{Or     Code <Cd> [1..1] CodeSet 539
Or}     Proprietary <Prtry> [1..1] Text 539
   Issuer <Issr> [0..1] Text 539
6.1.7.3.2  BranchIdentification <BrnchId>
Presence: [0..1]
Definition: Identifies a specific branch of a financial institution.
Usage: This component should be used in case the identification information in the financial institution
component does not provide identification up to branch level.
BranchIdentification <BrnchId> contains the following BranchData5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 543
   LEI <LEI> [0..1] IdentifierSet 543
   Name <Nm> [0..1] Text 543
   PostalAddress <PstlAdr> [0..1] ± 543
6.1.7.3.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a branch of a financial institution.
Datatype: "Max35Text" on page 609
6.1.7.3.2.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification for the branch of the financial institution.
Datatype: "LEIIdentifier" on page 604
6.1.7.3.2.3  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 608
6.1.7.3.2.4  PostalAddress <PstlAdr>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 543 March 2026
```

