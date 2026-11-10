---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.7 PartyIdentification148", "82.1.20.7.1 Identification <Id>", "82.1.20.7.1.2 NameAndAddress <NmAndAdr>"]
file_pages: [3067]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.7.1.2 NameAndAddress <NmAndAdr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3067 to 3067.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3067

```text
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C2 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 3320
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
82.1.20.7.1.2  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 3098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 3098
   Address <Adr> [0..1] ± 3098
82.1.20.7.1.3  Country <Ctry>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
82.1.20.7.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 3322
82.1.20.7.3  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3067 August 2026
```

