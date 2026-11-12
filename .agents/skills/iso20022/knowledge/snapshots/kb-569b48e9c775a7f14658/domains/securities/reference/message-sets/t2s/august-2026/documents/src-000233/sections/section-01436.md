---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["34 reda.014.001.02 PartyCreationRequestV02", "34.4 Message Building Blocks", "34.4.2 Party <Pty>", "34.4.2.1 PartyIdentification <PtyId>"]
file_pages: [2047]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.014.001.02"]
---

# 34.4.2.1 PartyIdentification <PtyId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2047 to 2047.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2047

```text
34.4.2.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Unique identification of the party within the system.
PartyIdentification <PtyId> contains the following SystemPartyIdentification9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 2047
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 2047
   ValidFrom <VldFr> [0..1] Date 2047
34.4.2.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification of the party.
Identification <Id> contains the following elements (see "PartyIdentification136" on page 3060 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
34.4.2.1.2  ResponsiblePartyIdentification <RspnsblPtyId>
Presence: [0..1]
Definition: Unique identification of the responsible party.
ResponsiblePartyIdentification <RspnsblPtyId> contains the following elements (see
"PartyIdentification136" on page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
34.4.2.1.3  ValidFrom <VldFr>
Presence: [0..1]
Definition: Starting date from which the identification is valid.
Datatype: "ISODate" on page 3319
34.4.2.2  Address <Adr>
Presence: [0..*]
Definition: Information that locates and identifies a specific address.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.014.001.02 PartyCreationRequestV02
Target2-Securities 2047 August 2026
```

