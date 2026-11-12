---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.66 SafekeepingPlaceFormat41Choice", "16.1.15.66.3 DigitalLedgerIdentification <DgtlLdgrId>"]
file_pages: [997]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.66.3 DigitalLedgerIdentification <DgtlLdgrId>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 997 to 997.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 997

```text
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 1205
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
16.1.15.66.3  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 1245
16.1.15.66.4  TypeAndIdentification <TpAndId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a type and identification.
TypeAndIdentification <TpAndId> contains the following SafekeepingPlaceTypeAndIdentification1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 997
   Identification <Id> [1..1] IdentifierSet C1 997
16.1.15.66.4.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Definition: Place of safekeeping as a code.
Datatype: "SafekeepingPlace1Code" on page 1241
CodeName Name Definition
CUST SharesHeldAtLocalCustodian Financial instruments held at a local
custodian.
ICSD SharesHeldAtICSD Financial instruments held at an
International Central Securities
Depository.
NCSD SharesHeldAtNCSD Financial instruments held at a National
Central Securities Depository.
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
16.1.15.66.4.2  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 997 February 2026
```

