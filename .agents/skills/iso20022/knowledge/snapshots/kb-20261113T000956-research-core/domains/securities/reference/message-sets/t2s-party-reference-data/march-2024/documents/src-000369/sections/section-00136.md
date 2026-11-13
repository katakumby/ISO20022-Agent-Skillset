---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["11 Message Items Types", "11.1 MessageComponents", "11.1.5 Party Identification", "11.1.5.3 SystemPartyIdentification8"]
file_pages: [170]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.1.5.3 SystemPartyIdentification8

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 170 to 170.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 170

```text
11.1.5.3  SystemPartyIdentification8
Definition: Unique and unambiguous identification of a party within a system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 170
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 170
11.1.5.3.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification to unambiguously identify the party within the system.
Identification <Id> contains the following elements (see "PartyIdentification136" on page 168 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 168
   LEI <LEI> [0..1] IdentifierSet 168
11.1.5.3.2  ResponsiblePartyIdentification <RspnsblPtyId>
Presence: [0..1]
Definition: Unique identification of the party responsible for the maintenance of the party reference data.
ResponsiblePartyIdentification <RspnsblPtyId> contains the following elements (see
"PartyIdentification136" on page 168 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 168
   LEI <LEI> [0..1] IdentifierSet 168
11.1.6 Person Identification
11.1.6.1  Contact14
Definition: Specifies the details of the contact person.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
170 March 2024
```

