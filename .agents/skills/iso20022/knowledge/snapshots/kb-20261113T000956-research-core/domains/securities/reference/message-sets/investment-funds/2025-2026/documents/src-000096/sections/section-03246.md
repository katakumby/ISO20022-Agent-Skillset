---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.17 Financial Institution Identification", "66.1.17.1 FinancialInstitutionIdentification11Choice", "66.1.17.1.4 ProprietaryIdentification <PrtryId>", "66.1.17.1.4.1 Identification <Id>"]
file_pages: [4482]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.17.1.4.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4482 to 4482.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4482

```text
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following SimpleIdentificationInformation4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4482
66.1.17.1.4.1  Identification <Id>
Presence: [1..1]
Definition: Name or number assigned by an entity to enable recognition of that entity, for example,
account identifier.
Datatype: "Max35Text" on page 5403
66.1.17.2  BranchData4
Definition: Information that locates and identifies a specific branch of a financial institution.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4482
   Name <Nm> [0..1] Text 4482
   PostalAddress <PstlAdr> [0..1] ± 4482
66.1.17.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a branch of a financial institution.
Datatype: "Max35Text" on page 5403
66.1.17.2.2  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max35Text" on page 5403
66.1.17.2.3  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4482 May 2026
```

