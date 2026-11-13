---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.1 PartyIdentification315", "66.1.30.1.1 Identification <Id>", "66.1.30.1.1.4 DigitalLedgerIdentification <DgtlLdgrId>"]
file_pages: [4908]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.1.1.4 DigitalLedgerIdentification <DgtlLdgrId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4908 to 4908.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4908

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.30.1.1.4  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of settlement expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
66.1.30.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 5395
66.1.30.1.3  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification7"
on page 5044 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 5044
   Country <Ctry> [1..1] CodeSet C12 5044
   AlternateIdentification <AltrnId> [1..1] Text 5045
66.1.30.1.4  ProcessingDate <PrcgDt>
Presence: [0..1]
Definition: Date/time at which the instruction was processed by the specified party.
ProcessingDate <PrcgDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
66.1.30.1.5  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4908 May 2026
```

