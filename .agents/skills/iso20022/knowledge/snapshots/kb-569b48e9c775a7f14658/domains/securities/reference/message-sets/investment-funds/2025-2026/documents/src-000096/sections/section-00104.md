---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["11 camt.044.001.03 FundConfirmedCashForecastReportCancellationV03", "11.4 Message Building Blocks", "11.4.4 RelatedReference <RltdRef>"]
file_pages: [150, 151, 152]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.044.001.03"]
---

# 11.4.4 RelatedReference <RltdRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 150 to 152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 150

```text
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference3" on
page 4537 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4537
   ReferenceIssuer <RefIssr> [0..1] ± 4537
   MessageName <MsgNm> [0..1] Text 4537
11.4.4 RelatedReference <RltdRef>
Presence: [0..*]
Definition: Reference to a linked message that was previously received.
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference3" on
page 4537 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4537
   ReferenceIssuer <RefIssr> [0..1] ± 4537
   MessageName <MsgNm> [0..1] Text 4537
11.4.5 MessagePagination <MsgPgntn>
Presence: [1..1]
Definition: Pagination of the message.
MessagePagination <MsgPgntn> contains the following elements (see "Pagination" on page 4833 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 4833
   LastPageIndicator <LastPgInd> [1..1] Indicator 4833
11.4.6 CashForecastReportToBeCancelled
<CshFcstRptToBeCanc>
Presence: [0..1]
Definition: The FundDetailedConfirmedCashForecastReport to be cancelled.
Impacted by: C7 "ConsolidatedNetCashRule", C16 "FundOrSubFundAndShareClassGuideline", C17
"PreviousTradeDate1Rule", C18 "TradeDate1Rule", C19 "TradeDate2Rule"
Approved by the Securities SEG on 27 January 2026 camt.044.001.03
FundConfirmedCashForecastReportCancellationV0
3
Investment Funds - Maintenance 2025 - 2026 150 May 2026
```

## File page 151

```text
CashForecastReportToBeCancelled <CshFcstRptToBeCanc> contains the following elements (see
"FundConfirmedCashForecastReport3" on page 4429 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FundOrSubFundDetails <FndOrSubFndDtls> [0..*] ± C13,
C14,
C15
4430
   FundCashForecastDetails <FndCshFcstDtls> [0..*] ± C10 4432
   ConsolidatedNetCashForecast <CnsltdNetCshFcst> [0..1] ± 4433
   Extension <Xtnsn> [0..*] ± C16 4434
Constraints
• ConsolidatedNetCashRule
If ConsolidatedNetCashForecast is present, then at least one occurrence of either
FundOrSubFundDetails or FundCashForecastDetails must be present. Both FundOrSubFundDetails
and FundCashForecastDetails may be present.
On Condition
    /ConsolidatedNetCashForecast is present
Following Must be True
    /FundOrSubFundDetails[*] Must be present
 Or    /FundCashForecastDetails[*] Must be present
• FundOrSubFundAndShareClassGuideline
When using the message to provide cash in and cash out amounts for more than one fund/sub fund,
and more than one share classes, (two or more FundOrSubFundDetails sequences and two or more
FundCashForecastDetails sequences and used), in this usage there is no way to determine which
share class belongs to which fund/sub fund from the message content itself, which may not be
desirable and this type of usage should be bilaterally agreed.
• PreviousTradeDate1Rule
If any occurrence of FundCashForecastDetails is present, then any occurrence of
FundOrSubFundDetails/PreviousTradeDateTime is not allowed.
On Condition
    /FundCashForecastDetails[*] is present
Following Must be True
    /FundOrSubFundDetails[*]/PreviousTradeDateTime Must be absent
• TradeDate1Rule
If any occurrence of FundCashForecastDetails is present, then any occurrence of
FundOrSubFundDetails/TradeDateTime is not allowed.
On Condition
    /FundCashForecastDetails[*] is present
Following Must be True
    /FundOrSubFundDetails[*]/TradeDateTime Must be absent
• TradeDate2Rule
If FundCashForecastDetails is not present, then at least one occurrence of FundOrSubFundDetails/
TradeDateTime must be present.
On Condition
    /FundCashForecastDetails[*] is absent
Approved by the Securities SEG on 27 January 2026 camt.044.001.03
FundConfirmedCashForecastReportCancellationV0
3
Investment Funds - Maintenance 2025 - 2026 151 May 2026
```

## File page 152

```text
Following Must be True
    /FundOrSubFundDetails[*]/TradeDateTime Must be present
Approved by the Securities SEG on 27 January 2026 camt.044.001.03
FundConfirmedCashForecastReportCancellationV0
3
Investment Funds - Maintenance 2025 - 2026 152 May 2026
```

