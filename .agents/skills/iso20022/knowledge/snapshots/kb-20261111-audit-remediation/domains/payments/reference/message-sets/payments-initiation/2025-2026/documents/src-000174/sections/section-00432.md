---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.18 System Identification", "6.1.18.1 ClearingSystemIdentification2Choice", "6.1.18.1.1 Code <Cd>"]
file_pages: [583]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.18.1.1 Code <Cd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 583 to 583.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 583

```text
6.1.18.1.1  Code <Cd>
Presence: [1..1]
Definition: Identification of a clearing system, in a coded form as published in an external list.
Datatype: "ExternalClearingSystemIdentification1Code" on page 592
6.1.18.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Identification code for a clearing system, that has not yet been identified in the list of clearing
systems.
Datatype: "Max35Text" on page 609
6.1.19 Tax
6.1.19.1  TaxParty2
Definition: Details about the entity involved in the tax paid or to be paid.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxIdentification <TaxId> [0..1] Text 583
   RegistrationIdentification <RegnId> [0..1] Text 583
   TaxType <TaxTp> [0..1] Text 583
   Authorisation <Authstn> [0..1]  584
     Title <Titl> [0..1] Text 584
     Name <Nm> [0..1] Text 584
6.1.19.1.1  TaxIdentification <TaxId>
Presence: [0..1]
Definition: Tax identification number of the debtor.
Datatype: "Max35Text" on page 609
6.1.19.1.2  RegistrationIdentification <RegnId>
Presence: [0..1]
Definition: Unique identification, as assigned by an organisation, to unambiguously identify a party.
Datatype: "Max35Text" on page 609
6.1.19.1.3  TaxType <TaxTp>
Presence: [0..1]
Definition: Type of tax payer.
Datatype: "Max35Text" on page 609
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 583 March 2026
```

