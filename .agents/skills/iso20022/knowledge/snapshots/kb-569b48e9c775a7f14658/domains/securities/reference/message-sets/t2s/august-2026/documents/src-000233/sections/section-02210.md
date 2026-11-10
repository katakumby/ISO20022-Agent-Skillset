---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.18 Market", "82.1.18.5 PlaceOfTradeIdentification1", "82.1.18.5.2 LEI <LEI>"]
file_pages: [2973]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.18.5.2 LEI <LEI>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2973 to 2973.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2973

```text
Constraints
• MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
82.1.18.5.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a place of trade.
Datatype: "LEIIdentifier" on page 3322
82.1.18.6  MarketIdentification84
Definition: Context, or geographic environment, in which trading parties may meet in order to negotiate
and execute trades among themselves.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 2973
   Type <Tp> [1..1] ± 2973
Constraints
• MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
82.1.18.6.1  Identification <Id>
Presence: [0..1]
Definition: Code allocated to places of trade, that is, stock exchanges, regulated markets, for example,
Electronic Trading Platforms (ECN), and unregulated markets, for example, Automated Trading
Systems (ATS), as sources of prices and related information, in order to facilitate automated
processing.
Identification <Id> contains one of the following elements (see "MarketIdentification1Choice" on
page 2971 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 2971
Or}   Description <Desc> [1..1] Text 2971
82.1.18.6.2  Type <Tp>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2973 August 2026
```

