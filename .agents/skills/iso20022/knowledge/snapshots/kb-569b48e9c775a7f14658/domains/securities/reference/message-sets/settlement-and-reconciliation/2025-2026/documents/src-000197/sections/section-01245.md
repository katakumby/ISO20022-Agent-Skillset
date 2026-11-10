---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.25 PartyIdentification315", "35.1.18.25.1 Identification <Id>", "35.1.18.25.1.2 NameAndAddress <NmAndAdr>"]
file_pages: [1702]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.25.1.2 NameAndAddress <NmAndAdr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1702 to 1702.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1702

```text
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
35.1.18.25.1.2  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 1704 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 1704
   Address <Adr> [0..1] ± 1704
35.1.18.25.1.3  Country <Ctry>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C7 "Country"
Datatype: "CountryCode" on page 2057
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
35.1.18.25.1.4  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of settlement expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 2186
35.1.18.25.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 2187
35.1.18.25.3  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1702 March 2026
```

