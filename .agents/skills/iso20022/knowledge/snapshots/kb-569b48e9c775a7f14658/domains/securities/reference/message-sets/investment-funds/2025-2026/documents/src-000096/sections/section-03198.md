---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.7 Cash", "66.1.7.6 FundConfirmedCashForecastReport3"]
file_pages: [4429]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.7.6 FundConfirmedCashForecastReport3

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4429 to 4429.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4429

```text
Extension <Xtnsn> contains the following elements (see "Extension1" on page 4835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [1..1] Text 4836
   Text <Txt> [1..1] Text 4836
Constraints
• ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
66.1.7.6  FundConfirmedCashForecastReport3
Definition: Information about a cash forecast report.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4429 May 2026
```

