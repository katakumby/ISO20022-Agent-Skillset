---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.19 Tax", "6.1.19.1 TaxParty2", "6.1.19.1.4 Authorisation <Authstn>"]
file_pages: [584]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.19.1.4 Authorisation <Authstn>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 584 to 584.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 584

```text
6.1.19.1.4  Authorisation <Authstn>
Presence: [0..1]
Definition: Details of the authorised tax paying party.
Authorisation <Authstn> contains the following TaxAuthorisation1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Title <Titl> [0..1] Text 584
   Name <Nm> [0..1] Text 584
6.1.19.1.4.1  Title <Titl>
Presence: [0..1]
Definition: Title or position of debtor or the debtor's authorised representative.
Datatype: "Max35Text" on page 609
6.1.19.1.4.2  Name <Nm>
Presence: [0..1]
Definition: Name of the debtor or the debtor's authorised representative.
Datatype: "Max140Text" on page 608
6.1.19.2  TaxParty1
Definition: Details about the entity involved in the tax paid or to be paid.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxIdentification <TaxId> [0..1] Text 584
   RegistrationIdentification <RegnId> [0..1] Text 584
   TaxType <TaxTp> [0..1] Text 584
6.1.19.2.1  TaxIdentification <TaxId>
Presence: [0..1]
Definition: Tax identification number of the creditor.
Datatype: "Max35Text" on page 609
6.1.19.2.2  RegistrationIdentification <RegnId>
Presence: [0..1]
Definition: Unique identification, as assigned by an organisation, to unambiguously identify a party.
Datatype: "Max35Text" on page 609
6.1.19.2.3  TaxType <TaxTp>
Presence: [0..1]
Definition: Type of tax payer.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 584 March 2026
```

