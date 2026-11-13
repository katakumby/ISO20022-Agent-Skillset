---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.19 Tax", "10.1.19.1 TaxParty2", "10.1.19.1.4 Authorisation <Authstn>", "10.1.19.1.4.1 Title <Titl>"]
file_pages: [1222]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.19.1.4.1 Title <Titl>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1222 to 1222.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1222

```text
10.1.19.1.4.1  Title <Titl>
Presence: [0..1]
Definition: Title or position of debtor or the debtor's authorised representative.
Datatype: "Max35Text" on page 1246
10.1.19.1.4.2  Name <Nm>
Presence: [0..1]
Definition: Name of the debtor or the debtor's authorised representative.
Datatype: "Max140Text" on page 1244
10.1.19.2  TaxParty1
Definition: Details about the entity involved in the tax paid or to be paid.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxIdentification <TaxId> [0..1] Text 1222
   RegistrationIdentification <RegnId> [0..1] Text 1222
   TaxType <TaxTp> [0..1] Text 1222
10.1.19.2.1  TaxIdentification <TaxId>
Presence: [0..1]
Definition: Tax identification number of the creditor.
Datatype: "Max35Text" on page 1246
10.1.19.2.2  RegistrationIdentification <RegnId>
Presence: [0..1]
Definition: Unique identification, as assigned by an organisation, to unambiguously identify a party.
Datatype: "Max35Text" on page 1246
10.1.19.2.3  TaxType <TaxTp>
Presence: [0..1]
Definition: Type of tax payer.
Datatype: "Max35Text" on page 1246
10.2 Message Datatypes
10.2.1 Amount
10.2.1.1  ActiveCurrencyAndAmount
Definition: A number of monetary units specified in an active currency where the unit of currency is
explicit and compliant with ISO 4217.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1222 March 2026
```

