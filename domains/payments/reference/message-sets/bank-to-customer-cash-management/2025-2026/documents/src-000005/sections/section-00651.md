---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.26 Tax", "6.1.26.1 TaxParty2", "6.1.26.1.4 Authorisation <Authstn>"]
file_pages: [884]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.26.1.4 Authorisation <Authstn>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 884 to 884.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 884

```text
6.1.26.1.4  Authorisation <Authstn>
Presence: [0..1]
Definition: Details of the authorised tax paying party.
Authorisation <Authstn> contains the following TaxAuthorisation1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Title <Titl> [0..1] Text 884
   Name <Nm> [0..1] Text 884
6.1.26.1.4.1  Title <Titl>
Presence: [0..1]
Definition: Title or position of debtor or the debtor's authorised representative.
Datatype: "Max35Text" on page 916
6.1.26.1.4.2  Name <Nm>
Presence: [0..1]
Definition: Name of the debtor or the debtor's authorised representative.
Datatype: "Max140Text" on page 914
6.1.26.2  TaxParty1
Definition: Details about the entity involved in the tax paid or to be paid.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxIdentification <TaxId> [0..1] Text 884
   RegistrationIdentification <RegnId> [0..1] Text 884
   TaxType <TaxTp> [0..1] Text 884
6.1.26.2.1  TaxIdentification <TaxId>
Presence: [0..1]
Definition: Tax identification number of the creditor.
Datatype: "Max35Text" on page 916
6.1.26.2.2  RegistrationIdentification <RegnId>
Presence: [0..1]
Definition: Unique identification, as assigned by an organisation, to unambiguously identify a party.
Datatype: "Max35Text" on page 916
6.1.26.2.3  TaxType <TaxTp>
Presence: [0..1]
Definition: Type of tax payer.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
884 March 2026
```

