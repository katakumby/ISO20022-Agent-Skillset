---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04", "9.2 Structure"]
file_pages: [117]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.042.001.04"]
---

# 9.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 117 to 117.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 117

```text
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. MessagePagination
Pagination of the message.
F. FundOrSubFundDetails
Information about the fund/sub fund when the report either specifies cash flow for the fund/sub fund
or for a share class of the fund/sub fund.
G. EstimatedFundCashForecastDetails
Information related to the estimated cash-in and cash-out flows for a specific trade date as a result
of transactions in shares in an investment fund, for example, subscriptions, redemptions or
switches. The information provided is sorted by pre-defined criteria such as country, institution,
currency or user defined criteria.
H. ConsolidatedNetCashForecast
Estimated net cash as a result of the cash-in and cash-out flows specified in the fund cash forecast
details.
I. Extension
Additional information that can not be captured in the structured fields and/or any other specific
block.
9.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FndDtldEstmtdCshFcstRpt> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 119
   PoolReference <PoolRef> [0..1] ± 120
   PreviousReference <PrvsRef> [0..*] ± 120
   RelatedReference <RltdRef> [0..*] ± 120
   MessagePagination <MsgPgntn> [1..1] ± 121
   FundOrSubFundDetails <FndOrSubFndDtls> [0..1] ± C14,
C15,
C16
121
   EstimatedFundCashForecastDetails <EstmtdFndCshFcstDtls> [1..*] ± C11 123
   ConsolidatedNetCashForecast <CnsltdNetCshFcst> [0..1] ± 124
   Extension <Xtnsn> [0..*] ± C12 124
Approved by the Securities SEG on 27 January 2026 camt.042.001.04
FundDetailedEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 117 May 2026
```

