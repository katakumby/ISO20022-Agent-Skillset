---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["6 reda.022.001.02 PartyModificationRequestV02", "6.4 Message Building Blocks", "6.4.3 Modification <Mod>", "6.4.3.2 RequestedModification <ReqdMod>", "6.4.3.2.1 SystemPartyDate <SysPtyDt>", "6.4.3.2.1.1 OpeningDate <OpngDt>"]
file_pages: [68]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 6.4.3.2.1.1 OpeningDate <OpngDt>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 68 to 68.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 68

```text
SystemPartyDate <SysPtyDt> contains the following SystemParty2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OpeningDate <OpngDt> [0..1] Date 68
   ClosingDate <ClsgDt> [0..1] Date 68
6.4.3.2.1.1  OpeningDate <OpngDt>
Presence: [0..1]
Definition: Specifies the opening date of the party.
Datatype: "ISODate" on page 184
6.4.3.2.1.2  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Specifies the closing date of the party.
Datatype: "ISODate" on page 184
6.4.3.2.2  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Unique identification to unambiguously identify the party within the system.
PartyIdentification <PtyId> contains the following SystemPartyIdentification10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 68
   Identification <Id> [0..1] ± 68
6.4.3.2.2.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Starting date from which the identification is valid.
Datatype: "ISODate" on page 184
6.4.3.2.2.2  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous way to identify a system party.
Identification <Id> contains the following elements (see "PartyIdentification136" on page 168 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 168
   LEI <LEI> [0..1] IdentifierSet 168
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.022.001.02 PartyModificationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
68 March 2024
```

