---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.12 Market", "12.1.12.2 MarketIdentification1Choice"]
file_pages: [435]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.12.2 MarketIdentification1Choice

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 435 to 435.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 435

```text
Proprietary <Prtry> contains the following elements (see GenericIdentification30 on page 400 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 400
   Issuer <Issr> [1..1] Text 401
   SchemeName <SchmeNm> [0..1] Text 401
12.1.12.2  MarketIdentification1Choice
Definition: Choice of market identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 435
Or}   Description <Desc> [1..1] Text 435
12.1.12.2.1  MarketIdentifierCode <MktIdrCd>
Presence: [1..1]
Definition: ISO 10383 Market Identification Code.
Datatype: MICIdentifier on page 490
12.1.12.2.2  Description <Desc>
Presence: [1..1]
Definition: Description of the market when no Market Identifier Code is available.
Datatype: Max35Text on page 493
12.1.12.3  MarketIdentification20
Definition: Context, or geographic environment, in which trading parties may meet in order to negotiate
and execute trades among themselves.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 435
   Type <Tp> [1..1] ± 436
Constraints
• MarketTypeAndIdentificationRule
(Rule)
If MarketType is OverTheCounter (OTCO), then Identification/Description must specify a system. If
MarketType is Exchange (EXCH), then Identification/MarketIdentificationCode must be present.
12.1.12.3.1  Identification <Id>
Presence: [0..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 435
```

