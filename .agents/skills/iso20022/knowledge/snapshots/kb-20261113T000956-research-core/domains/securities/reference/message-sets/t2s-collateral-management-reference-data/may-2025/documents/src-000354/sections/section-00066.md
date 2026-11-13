---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.4 Party Identification", "10.1.4.1 PartyIdentification120Choice", "10.1.4.1.3 NameAndAddress <NmAndAdr>"]
file_pages: [71]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.4.1.3 NameAndAddress <NmAndAdr>

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 71 to 71.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 71

```text
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification36" on
page 65 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 66
   Issuer <Issr> [1..1] Text 66
   SchemeName <SchmeNm> [0..1] Text 66
10.1.4.1.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of a party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 72 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 72
   Address <Adr> [0..1] ± 73
10.1.4.2  PartyIdentification136
Definition: Identification of the party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 71
   LEI <LEI> [0..1] IdentifierSet 71
10.1.4.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 70 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 70
Or   ProprietaryIdentification <PrtryId> [1..1] ± 70
Or}   NameAndAddress <NmAndAdr> [1..1] ± 71
10.1.4.2.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Approved by the Securities SEG on 17 April 2025. Message Items Types
Target2-Securities - Collateral Management Reference Data 71 May 2025
```

