---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "12.4 Message Building Blocks", "12.4.4 RelatedReference <RltdRef>"]
file_pages: [157, 158]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.045.001.03"]
---

# 12.4.4 RelatedReference <RltdRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 157 to 158.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 157

```text
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference3" on
page 4537 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4537
   ReferenceIssuer <RefIssr> [0..1] ± 4537
   MessageName <MsgNm> [0..1] Text 4537
12.4.4 RelatedReference <RltdRef>
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
12.4.5 MessagePagination <MsgPgntn>
Presence: [1..1]
Definition: Pagination of the message.
MessagePagination <MsgPgntn> contains the following elements (see "Pagination" on page 4833 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 4833
   LastPageIndicator <LastPgInd> [1..1] Indicator 4833
12.4.6 CashForecastReportToBeCancelled
<CshFcstRptToBeCanc>
Presence: [0..1]
Definition: The FundDetailedConfirmedCashForecastReport to be cancelled.
Approved by the Securities SEG on 27 January 2026 camt.045.001.03
FundDetailedConfirmedCashForecastReportCancell
ationV03
Investment Funds - Maintenance 2025 - 2026 157 May 2026
```

## File page 158

```text
CashForecastReportToBeCancelled <CshFcstRptToBeCanc> contains the following elements (see
"FundDetailedConfirmedCashForecastReport3" on page 4415 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FundOrSubFundDetails <FndOrSubFndDtls> [0..1] ± C14,
C15,
C16
4416
   FundCashForecastDetails <FndCshFcstDtls> [1..*]  C11 4417
     Identification <Id> [1..1] Text 4419
     TradeDateTime <TradDtTm> [1..1] ± 4419
     PreviousTradeDateTime <PrvsTradDtTm> [0..1] ± 4419
     FinancialInstrumentDetails <FinInstrmDtls> [1..1] ± C12 4419
     TotalNAV <TtlNAV> [0..*] Amount C2, C10 4420
     PreviousTotalNAV <PrvsTtlNAV> [0..*] Amount C2, C10 4420
     TotalUnitsNumber <TtlUnitsNb> [0..1] ± 4421
     PreviousTotalUnitsNumber <PrvsTtlUnitsNb> [0..1] ± 4421
     TotalNAVChangeRate <TtlNAVChngRate> [0..1] Rate 4421
     InvestmentCurrency <InvstmtCcy> [0..*] CodeSet C2 4421
     CurrencyStatus <CcySts> [0..1] ± 4422
     ExceptionalNetCashFlowIndicator
<XcptnlNetCshFlowInd>
[1..1] Indicator 4422
     Price <Pric> [0..1] ± 4422
     ForeignExchangeRate <FXRate> [0..1] ± 4422
     PercentageOfShareClassTotalNAV
<PctgOfShrClssTtlNAV>
[0..1] Rate 4423
     BreakdownByParty <BrkdwnByPty> [0..*] ± 4423
     BreakdownByCountry <BrkdwnByCtry> [0..*] ± 4424
     BreakdownByCurrency <BrkdwnByCcy> [0..*] ± 4425
     BreakdownByUserDefinedParameter
<BrkdwnByUsrDfndParam>
[0..*] ± C17 4426
     NetCashForecastDetails <NetCshFcstDtls> [0..*] ± C5 4427
   ConsolidatedNetCashForecast <CnsltdNetCshFcst> [0..1] ± 4428
   Extension <Xtnsn> [0..*] ± C16 4428
Approved by the Securities SEG on 27 January 2026 camt.045.001.03
FundDetailedConfirmedCashForecastReportCancell
ationV03
Investment Funds - Maintenance 2025 - 2026 158 May 2026
```

