---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.34 ContactAttributes5"]
file_pages: [5021]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.34 ContactAttributes5

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5021 to 5021.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5021

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.30.34  ContactAttributes5
Definition: Communication device number or address used for communication.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5021
   PostalAddress <PstlAdr> [0..1] ± 5021
   PhoneNumber <PhneNb> [0..1] Text 5022
   FaxNumber <FaxNb> [0..1] Text 5022
   EmailAddress <EmailAdr> [0..1] Text 5022
   URLAddress <URLAdr> [0..1] Text 5022
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5022
   LEI <LEI> [0..1] IdentifierSet 5023
66.1.30.34.1  Name <Nm>
Presence: [1..1]
Definition: Name of the party.
Datatype: "Max350Text" on page 5403
66.1.30.34.2  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Address of the party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5021 May 2026
```

