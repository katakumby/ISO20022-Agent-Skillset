---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.10 PartyIdentificationAndAccount170", "82.1.20.10.4 ProcessingIdentification <PrcgId>"]
file_pages: [3078]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.10.4 ProcessingIdentification <PrcgId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3078 to 3078.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3078

```text
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
82.1.20.10.4  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 3328
82.1.20.11  SystemPartyIdentification8
Definition: Unique and unambiguous identification of a party within a system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
82.1.20.11.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification to unambiguously identify the party within the system.
Identification <Id> contains the following elements (see "PartyIdentification136" on page 3060 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
82.1.20.11.2  ResponsiblePartyIdentification <RspnsblPtyId>
Presence: [0..1]
Definition: Unique identification of the party responsible for the maintenance of the party reference data.
ResponsiblePartyIdentification <RspnsblPtyId> contains the following elements (see
"PartyIdentification136" on page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3078 August 2026
```

