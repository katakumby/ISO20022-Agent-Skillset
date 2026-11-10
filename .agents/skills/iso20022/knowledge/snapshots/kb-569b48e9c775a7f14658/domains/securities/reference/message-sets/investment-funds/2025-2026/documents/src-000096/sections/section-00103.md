---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["11 camt.044.001.03 FundConfirmedCashForecastReportCancellationV03", "11.4 Message Building Blocks"]
file_pages: [149]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.044.001.03"]
---

# 11.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 149 to 149.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 149

```text
C17 PreviousTradeDate1Rule
If any occurrence of FundCashForecastDetails is present, then any occurrence of
FundOrSubFundDetails/PreviousTradeDateTime is not allowed.
C18 TradeDate1Rule
If any occurrence of FundCashForecastDetails is present, then any occurrence of
FundOrSubFundDetails/TradeDateTime is not allowed.
C19 TradeDate2Rule
If FundCashForecastDetails is not present, then at least one occurrence of
FundOrSubFundDetails/TradeDateTime must be present.
11.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
11.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Identifies the message.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
11.4.2 PoolReference <PoolRef>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
PoolReference <PoolRef> contains the following elements (see "AdditionalReference3" on page 4537
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4537
   ReferenceIssuer <RefIssr> [0..1] ± 4537
   MessageName <MsgNm> [0..1] Text 4537
11.4.3 PreviousReference <PrvsRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously sent.
Approved by the Securities SEG on 27 January 2026 camt.044.001.03
FundConfirmedCashForecastReportCancellationV0
3
Investment Funds - Maintenance 2025 - 2026 149 May 2026
```

