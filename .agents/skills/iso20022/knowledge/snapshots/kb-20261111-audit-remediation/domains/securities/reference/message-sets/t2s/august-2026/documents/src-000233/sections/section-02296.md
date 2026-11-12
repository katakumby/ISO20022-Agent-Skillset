---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.9 PartyIdentification15", "82.1.20.9.2 Identification <Id>"]
file_pages: [3077]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.9.2 Identification <Id>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3077 to 3077.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3077

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
82.1.20.9.2  Identification <Id>
Presence: [1..1]
Definition: Description of an organisation.
Datatype: "Max35Text" on page 3328
82.1.20.10  PartyIdentificationAndAccount170
Definition: Party and account details.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3077
   LEI <LEI> [0..1] IdentifierSet 3077
   SafekeepingAccount <SfkpgAcct> [0..1] ± 3077
   ProcessingIdentification <PrcgId> [0..1] Text 3078
82.1.20.10.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 3079 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 3079
Or   ProprietaryIdentification <PrtryId> [1..1] ± 3079
Or}   NameAndAddress <NmAndAdr> [1..1] ± 3079
82.1.20.10.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 3322
82.1.20.10.3  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3077 August 2026
```

