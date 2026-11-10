---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.22 Price", "7.1.22.5 PriceInformation28", "7.1.22.5.4 SourceOfPrice <SrcOfPric>"]
file_pages: [515]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.22.5.4 SourceOfPrice <SrcOfPric>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 515 to 515.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 515

```text
DateTimeRange <DtTmRg> contains the following elements (see "DateTimePeriod1" on page 268 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 268
   ToDateTime <ToDtTm> [1..1] DateTime 268
7.1.22.5.4  SourceOfPrice <SrcOfPric>
Presence: [0..1]
Definition: Place from which the price was obtained.
Impacted by: C16 "IdentificationPresenceRule", C23 "MarketTypeAndIdentificationRule", C33
"PlaceOfTradeRule"
SourceOfPrice <SrcOfPric> contains the following elements (see "MarketIdentification93" on
page 282 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 282
   Type <Tp> [0..1] ± 282
Constraints
• IdentificationPresenceRule
If Type/Code is not Various (VARI) OR Over The Counter (OTCO) then Identification must be
present. 
• MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
• PlaceOfTradeRule
If the trade was executed on multiple places of trade and the place of trade field is used, code VARI
must be used.
7.1.23 Rate
7.1.23.1  RateName1
Definition: Rate name specifies the reference rate or basis rate on which a variable rate is based (ex:
EONIA, EURIBOR, LIBOR, FEFUND, EURREPO).
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 515 February 2025
```

