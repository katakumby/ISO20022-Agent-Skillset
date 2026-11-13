---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.7 Financial Institution Identification", "10.1.7.3 BranchAndFinancialInstitutionIdentification8", "10.1.7.3.2 BranchIdentification <BrnchId>"]
file_pages: [1177]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.7.3.2 BranchIdentification <BrnchId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1177 to 1177.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1177

```text
Other <Othr> contains the following elements (see "GenericFinancialIdentification1" on page 1172 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1172
   SchemeName <SchmeNm> [0..1]  1173
{Or     Code <Cd> [1..1] CodeSet 1173
Or}     Proprietary <Prtry> [1..1] Text 1173
   Issuer <Issr> [0..1] Text 1173
10.1.7.3.2  BranchIdentification <BrnchId>
Presence: [0..1]
Definition: Identifies a specific branch of a financial institution.
Usage: This component should be used in case the identification information in the financial institution
component does not provide identification up to branch level.
BranchIdentification <BrnchId> contains the following BranchData5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 1177
   LEI <LEI> [0..1] IdentifierSet 1177
   Name <Nm> [0..1] Text 1177
   PostalAddress <PstlAdr> [0..1] ± 1177
10.1.7.3.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a branch of a financial institution.
Datatype: "Max35Text" on page 1246
10.1.7.3.2.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification for the branch of the financial institution.
Datatype: "LEIIdentifier" on page 1241
10.1.7.3.2.3  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 1244
10.1.7.3.2.4  PostalAddress <PstlAdr>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1177 March 2026
```

