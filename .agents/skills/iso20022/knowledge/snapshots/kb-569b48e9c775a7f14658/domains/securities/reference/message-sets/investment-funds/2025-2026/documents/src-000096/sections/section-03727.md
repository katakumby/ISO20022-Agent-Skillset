---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.26 DataBaseCheck1"]
file_pages: [5013]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.26 DataBaseCheck1

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5013 to 5013.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5013

```text
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
66.1.30.26  DataBaseCheck1
Definition: Information about a database.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DatabaseCheck <DBChck> [1..1] Indicator 5013
   Identification <Id> [1..1] Text 5013
66.1.30.26.1  DatabaseCheck <DBChck>
Presence: [1..1]
Definition: Indicates whether the individual or organisation is listed in an on-line global Know Your
Customer (KYC) database.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.30.26.2  Identification <Id>
Presence: [1..1]
Definition: Identification of the database.
Datatype: "Max35Text" on page 5403
66.1.30.27  PartyIdentification140
Definition: Identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5013
   LEI <LEI> [0..1] IdentifierSet 5014
66.1.30.27.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5013 May 2026
```

