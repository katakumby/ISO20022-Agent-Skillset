---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.15 Market", "35.1.15.3 MarketIdentification1Choice"]
file_pages: [1526]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.15.3 MarketIdentification1Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1526 to 1526.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1526

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.15.3  MarketIdentification1Choice
Definition: Choice of market identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 1526
Or}   Description <Desc> [1..1] Text 1526
35.1.15.3.1  MarketIdentifierCode <MktIdrCd>
Presence: [1..1]
Definition: ISO 10383 Market Identification Code.
Datatype: "MICIdentifier" on page 2187
35.1.15.3.2  Description <Desc>
Presence: [1..1]
Definition: Description of the market when no Market Identifier Code is available.
Datatype: "Max35Text" on page 2192
35.1.15.4  MarketIdentification3Choice
Definition: Choice of market identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 1526
Or}   Description <Desc> [1..1] Text 1526
35.1.15.4.1  MarketIdentifierCode <MktIdrCd>
Presence: [1..1]
Definition: Market Identifier Code. Identification of a financial market, as stipulated in the norm ISO
10383 "Codes for exchanges and market identifications".
Datatype: "MICIdentifier" on page 2187
35.1.15.4.2  Description <Desc>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1526 March 2026
```

