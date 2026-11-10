---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.15 Party Identification", "9.1.15.4 PartyIdentification148", "9.1.15.4.2 LEI <LEI>"]
file_pages: [256]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.15.4.2 LEI <LEI>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 256 to 256.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 256

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
9.1.15.4.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 342
9.1.15.4.3  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 345
9.1.15.5  PartyIdentificationAndAccount170
Definition: Party and account details.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 256
   LEI <LEI> [0..1] IdentifierSet 256
   SafekeepingAccount <SfkpgAcct> [0..1] ± 257
   ProcessingIdentification <PrcgId> [0..1] Text 257
9.1.15.5.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 252 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C6 252
Or   ProprietaryIdentification <PrtryId> [1..1] ± 252
Or}   NameAndAddress <NmAndAdr> [1..1] ± 252
9.1.15.5.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 342
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 256 September 2025
```

