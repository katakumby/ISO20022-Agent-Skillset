---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.13 Market"]
file_pages: [227]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.13 Market

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 227 to 227.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 227

```text
9.1.13 Market
9.1.13.1  MarketIdentification3Choice
Definition: Choice of market identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 227
Or}   Description <Desc> [1..1] Text 227
9.1.13.1.1  MarketIdentifierCode <MktIdrCd>
Presence: [1..1]
Definition: Market Identifier Code. Identification of a financial market, as stipulated in the norm ISO
10383 "Codes for exchanges and market identifications".
Datatype: "MICIdentifier" on page 342
9.1.13.1.2  Description <Desc>
Presence: [1..1]
Definition: Description of the market when no Market Identifier Code is available.
Datatype: "Max35Text" on page 345
9.1.14 Miscellaneous
9.1.14.1  LinkageType3Choice
Definition: Choice of format for the linkage type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 227
Or}   Proprietary <Prtry> [1..1] ± 228
9.1.14.1.1  Code <Cd>
Presence: [1..1]
Definition: Linkage type expressed as an ISO 20022 code.
Datatype: "LinkageType1Code" on page 330
CodeName Name Definition
LINK Link Request is to link the referenced
transactions.
UNLK Unlink Request is to unlink the referenced
transactions.
SOFT Soft Request is to soft link the referenced
transactions.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 227 September 2025
```

