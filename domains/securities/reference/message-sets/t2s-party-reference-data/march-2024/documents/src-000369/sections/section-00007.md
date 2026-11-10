---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 reda.014.001.02 PartyCreationRequestV02", "2.4 Message Building Blocks", "2.4.2 Party <Pty>", "2.4.2.1 PartyIdentification <PtyId>"]
file_pages: [10]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.014.001.02"]
---

# 2.4.2.1 PartyIdentification <PtyId>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 10 to 10.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 10

```text
2.4.2.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Unique identification of the party within the system.
PartyIdentification <PtyId> contains the following SystemPartyIdentification9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 10
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 10
   ValidFrom <VldFr> [0..1] Date 10
2.4.2.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification of the party.
Identification <Id> contains the following elements (see "PartyIdentification136" on page 168 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 168
   LEI <LEI> [0..1] IdentifierSet 168
2.4.2.1.2  ResponsiblePartyIdentification <RspnsblPtyId>
Presence: [0..1]
Definition: Unique identification of the responsible party.
ResponsiblePartyIdentification <RspnsblPtyId> contains the following elements (see
"PartyIdentification136" on page 168 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 168
   LEI <LEI> [0..1] IdentifierSet 168
2.4.2.1.3  ValidFrom <VldFr>
Presence: [0..1]
Definition: Starting date from which the identification is valid.
Datatype: "ISODate" on page 184
2.4.2.2  Address <Adr>
Presence: [0..*]
Definition: Information that locates and identifies a specific address.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.014.001.02 PartyCreationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
10 March 2024
```

