---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.8 Party Identification", "4.1.8.3 SystemPartyIdentification8"]
file_pages: [64]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.8.3 SystemPartyIdentification8

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 64 to 64.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 64

```text
4.1.8.3  SystemPartyIdentification8
Definition: Unique and unambiguous identification of a party within a system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 64
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 64
4.1.8.3.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification to unambiguously identify the party within the system.
Identification <Id> contains the following elements (see "PartyIdentification136" on page 62 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 62
   LEI <LEI> [0..1] IdentifierSet 62
4.1.8.3.2  ResponsiblePartyIdentification <RspnsblPtyId>
Presence: [0..1]
Definition: Unique identification of the party responsible for the maintenance of the party reference data.
ResponsiblePartyIdentification <RspnsblPtyId> contains the following elements (see
"PartyIdentification136" on page 62 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 62
   LEI <LEI> [0..1] IdentifierSet 62
4.1.9 Postal Address
4.1.9.1  NameAndAddress5
Definition: Information that locates and identifies a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 64
   Address <Adr> [0..1] ± 65
4.1.9.1.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 83
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
64 March 2024
```

