---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.19 Tax"]
file_pages: [1221]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.19 Tax

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1221 to 1221.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1221

```text
Datatype: "Max35Text" on page 1246
10.1.19 Tax
10.1.19.1  TaxParty2
Definition: Details about the entity involved in the tax paid or to be paid.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxIdentification <TaxId> [0..1] Text 1221
   RegistrationIdentification <RegnId> [0..1] Text 1221
   TaxType <TaxTp> [0..1] Text 1221
   Authorisation <Authstn> [0..1]  1221
     Title <Titl> [0..1] Text 1222
     Name <Nm> [0..1] Text 1222
10.1.19.1.1  TaxIdentification <TaxId>
Presence: [0..1]
Definition: Tax identification number of the debtor.
Datatype: "Max35Text" on page 1246
10.1.19.1.2  RegistrationIdentification <RegnId>
Presence: [0..1]
Definition: Unique identification, as assigned by an organisation, to unambiguously identify a party.
Datatype: "Max35Text" on page 1246
10.1.19.1.3  TaxType <TaxTp>
Presence: [0..1]
Definition: Type of tax payer.
Datatype: "Max35Text" on page 1246
10.1.19.1.4  Authorisation <Authstn>
Presence: [0..1]
Definition: Details of the authorised tax paying party.
Authorisation <Authstn> contains the following TaxAuthorisation1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Title <Titl> [0..1] Text 1222
   Name <Nm> [0..1] Text 1222
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1221 March 2026
```

