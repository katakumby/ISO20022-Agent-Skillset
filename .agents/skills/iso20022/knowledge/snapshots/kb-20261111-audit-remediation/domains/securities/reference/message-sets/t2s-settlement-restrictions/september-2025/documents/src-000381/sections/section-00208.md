---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.15 Party Identification", "9.1.15.3 PartyIdentification136"]
file_pages: [254]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.15.3 PartyIdentification136

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 254 to 254.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 254

```text
9.1.15.3  PartyIdentification136
Definition: Identification of the party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 254
   LEI <LEI> [0..1] IdentifierSet 254
9.1.15.3.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 252 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C6 252
Or   ProprietaryIdentification <PrtryId> [1..1] ± 252
Or}   NameAndAddress <NmAndAdr> [1..1] ± 252
9.1.15.3.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 342
9.1.15.4  PartyIdentification148
Definition: Identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  254
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C6 255
Or     NameAndAddress <NmAndAdr> [1..1] ± 255
Or}     Country <Ctry> [1..1] CodeSet C7 255
   LEI <LEI> [0..1] IdentifierSet 256
   ProcessingIdentification <PrcgId> [0..1] Text 256
9.1.15.4.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 254 September 2025
```

