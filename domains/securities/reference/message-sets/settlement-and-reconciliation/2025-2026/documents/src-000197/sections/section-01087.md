---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.15 Market", "35.1.15.5 PlaceOfTradeIdentification1"]
file_pages: [1527]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.15.5 PlaceOfTradeIdentification1

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1527 to 1527.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1527

```text
Definition: Description of the market when no Market Identifier Code is available.
Datatype: "Max35Text" on page 2192
35.1.15.5  PlaceOfTradeIdentification1
Definition: Identification of market in which a trade transaction has been executed.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketTypeAndIdentification <MktTpAndId> [0..1] ± C27 1527
   LEI <LEI> [0..1] IdentifierSet 1527
35.1.15.5.1  MarketTypeAndIdentification <MktTpAndId>
Presence: [0..1]
Definition: Identification and type of the place of trade.
Impacted by: C27 "MarketTypeAndIdentificationRule"
MarketTypeAndIdentification <MktTpAndId> contains the following elements (see
"MarketIdentification84" on page 1527 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 1528
   Type <Tp> [1..1] ± 1528
Constraints
• MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
35.1.15.5.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a place of trade.
Datatype: "LEIIdentifier" on page 2187
35.1.15.6  MarketIdentification84
Definition: Context, or geographic environment, in which trading parties may meet in order to negotiate
and execute trades among themselves.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 1528
   Type <Tp> [1..1] ± 1528
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1527 March 2026
```

