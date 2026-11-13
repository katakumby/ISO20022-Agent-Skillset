---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.14 Market", "16.1.14.1 CorporateActionOption30Choice", "16.1.14.1.2 Proprietary <Prtry>"]
file_pages: [883]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.14.1.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 883 to 883.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 883

```text
CodeName Name Definition
OVER Oversubscribe Subscribe to more equities than
underlying securities position allows.
QINV QualifiedInvestor Account owner is a qualified investor.
SECU Security Distribution of securities to holders.
SLLE SellEntitlement Sell the intermediate securities.
PRUN UnknownProceeds Proceeds not known during election
period. The option can result in cash
and/or securities.
16.1.14.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of corporate action options.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.14.2  MarketIdentification1Choice
Definition: Choice of market identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 883
Or}   Description <Desc> [1..1] Text 883
16.1.14.2.1  MarketIdentifierCode <MktIdrCd>
Presence: [1..1]
Definition: ISO 10383 Market Identification Code.
Datatype: "MICIdentifier" on page 1246
16.1.14.2.2  Description <Desc>
Presence: [1..1]
Definition: Description of the market when no Market Identifier Code is available.
Datatype: "Max35Text" on page 1251
16.1.14.3  MarketIdentification3Choice
Definition: Choice of market identification.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 883 February 2026
```

