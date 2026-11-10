---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["8 camt.041.001.04 FundConfirmedCashForecastReportV04", "8.4 Message Building Blocks"]
file_pages: [109]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.041.001.04"]
---

# 8.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 109 to 109.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 109

```text
C15 FundIdentification3Rule
If Legal Entity Identifier is not present, then Identification or Name must be present.
Identification, Name and Legal Entity Identifier may all be present.
C16 FundOrSubFundAndShareClassGuideline
When using the message to provide cash in and cash out amounts for more than one fund/sub
fund, and more than one share classes, (two or more FundOrSubFundDetails sequences and
two or more FundCashForecastDetails sequences and used), in this usage there is no way to
determine which share class belongs to which fund/sub fund from the message content itself,
which may not be desirable and this type of usage should be bilaterally agreed.
This constraint is defined at the MessageDefinition level.
C17 PreviousTradeDateRule
If any occurrence of FundCashForecastDetails is present, then any occurrence of
FundOrSubFundDetails/PreviousTradeDateTime is not allowed.
On Condition
    /FundCashForecastDetails[*] is present
Following Must be True
    /FundOrSubFundDetails[*]/PreviousTradeDateTime Must be absent
This constraint is defined at the MessageDefinition level.
C18 TradeDate1Rule
If any occurrence of FundCashForecastDetails is present, then any occurrence of
FundOrSubFundDetails/TradeDateTime is not allowed.
On Condition
    /FundCashForecastDetails[*] is present
Following Must be True
    /FundOrSubFundDetails[*]/TradeDateTime Must be absent
This constraint is defined at the MessageDefinition level.
C19 TradeDate2Rule
If FundCashForecastDetails is not present, then at least one occurrence of
FundOrSubFundDetails/TradeDateTime must be present.
On Condition
    /FundCashForecastDetails[*] is absent
Following Must be True
    /FundOrSubFundDetails[*]/TradeDateTime Must be present
This constraint is defined at the MessageDefinition level.
8.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
8.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Identifies the message.
Approved by the Securities SEG on 27 January 2026 camt.041.001.04
FundConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 109 May 2026
```

