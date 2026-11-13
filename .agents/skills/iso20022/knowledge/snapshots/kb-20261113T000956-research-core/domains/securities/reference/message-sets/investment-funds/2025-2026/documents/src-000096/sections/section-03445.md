---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.5 EstimatedFundCashForecast6", "66.1.25.5.3 PreviousTradeDateTime <PrvsTradDtTm>"]
file_pages: [4693]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.5.3 PreviousTradeDateTime <PrvsTradDtTm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4693 to 4693.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4693

```text
Definition: Date and, if required, the time, at which the price will be applied.
TradeDateTime <TradDtTm> contains one of the following elements (see "DateAndDateTimeChoice"
on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
66.1.25.5.3  PreviousTradeDateTime <PrvsTradDtTm>
Presence: [0..1]
Definition: Previous date and time at which the price was applied.
PreviousTradeDateTime <PrvsTradDtTm> contains one of the following elements (see
"DateAndDateTimeChoice" on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
66.1.25.5.4  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class to which the cash flow is related.
Impacted by: C12 "FinancialInstrumentIdentificationGuideline"
FinancialInstrumentDetails <FinInstrmDtls> contains the following elements (see
"FinancialInstrument9" on page 4493 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4493
   Name <Nm> [0..1] Text 4494
   SupplementaryIdentification <SplmtryId> [0..1] Text 4494
   RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C2 4494
   ClassType <ClssTp> [0..1] Text 4495
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4495
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4495
   DualFundIndicator <DualFndInd> [1..1] Indicator 4495
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4693 May 2026
```

