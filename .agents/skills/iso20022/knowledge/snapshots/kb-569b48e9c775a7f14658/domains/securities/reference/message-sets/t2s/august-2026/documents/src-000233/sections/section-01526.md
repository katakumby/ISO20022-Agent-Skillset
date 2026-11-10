---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["42 reda.022.001.02 PartyModificationRequestV02", "42.4 Message Building Blocks", "42.4.3 Modification <Mod>", "42.4.3.2 RequestedModification <ReqdMod>", "42.4.3.2.1 SystemPartyDate <SysPtyDt>", "42.4.3.2.1.1 OpeningDate <OpngDt>"]
file_pages: [2147]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 42.4.3.2.1.1 OpeningDate <OpngDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2147 to 2147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2147

```text
SystemPartyDate <SysPtyDt> contains the following SystemParty2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OpeningDate <OpngDt> [0..1] Date 2147
   ClosingDate <ClsgDt> [0..1] Date 2147
42.4.3.2.1.1  OpeningDate <OpngDt>
Presence: [0..1]
Definition: Specifies the opening date of the party.
Datatype: "ISODate" on page 3319
42.4.3.2.1.2  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Specifies the closing date of the party.
Datatype: "ISODate" on page 3319
42.4.3.2.2  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Unique identification to unambiguously identify the party within the system.
PartyIdentification <PtyId> contains the following SystemPartyIdentification10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 2147
   Identification <Id> [0..1] ± 2147
42.4.3.2.2.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Starting date from which the identification is valid.
Datatype: "ISODate" on page 3319
42.4.3.2.2.2  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous way to identify a system party.
Identification <Id> contains the following elements (see "PartyIdentification136" on page 3060 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.022.001.02 PartyModificationRequestV02
Target2-Securities 2147 August 2026
```

