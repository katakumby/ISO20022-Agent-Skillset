---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.7 Cash", "66.1.7.5 FundDetailedConfirmedCashForecastReport3", "66.1.7.5.2 FundCashForecastDetails <FndCshFcstDtls>"]
file_pages: [4417, 4418]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.7.5.2 FundCashForecastDetails <FndCshFcstDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4417 to 4418.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4417

```text
FundOrSubFundDetails <FndOrSubFndDtls> contains the following elements (see "Fund4" on
page 4707 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 4708
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4708
   Identification <Id> [0..1]  4708
     Identification <Id> [1..1] Text 4708
     Type <Tp> [1..1] ± 4708
   Currency <Ccy> [0..1] CodeSet C2 4709
   TotalNAV <TtlNAV> [0..1] Amount C2, C10 4709
   PreviousTotalNAV <PrvsTtlNAV> [0..1] Amount C2, C10 4709
   TotalUnitsNumber <TtlUnitsNb> [0..1] ± 4710
   PreviousTotalUnitsNumber <PrvsTtlUnitsNb> [0..1] ± 4710
   PercentageOfFundTotalNAV <PctgOfFndTtlNAV> [0..1] Rate 4710
Constraints
• FundIdentification1Rule
If Identification is not present, then Name or LegalEntityIdentifier must be present. Identification,
Name and Legal Entity Identifier may all be present.
On Condition
    /Identification is absent
Following Must be True
    /Name Must be present
 Or    /LegalEntityIdentifier Must be present
• FundIdentification2Rule
If Name is not present, then Identification or Legal Entity Identifier must be present. Identification,
Name and Legal Entity Identifier may all be present.
On Condition
    /Name is absent
Following Must be True
    /Identification Must be present
 Or    /LegalEntityIdentifier Must be absent
• FundIdentification3Rule
If Legal Entity Identifier is not present, then Identification or Name must be present. Identification,
Name and Legal Entity Identifier may all be present.
On Condition
    /LegalEntityIdentifier is absent
Following Must be True
    /Identification Must be present
 Or    /Name Must be present
66.1.7.5.2  FundCashForecastDetails <FndCshFcstDtls>
Presence: [1..*]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4417 May 2026
```

## File page 4418

```text
Definition: Information related to the cash-in and cash-out flows for a specific trade date as a result of
transactions in shares in an investment fund, for example, subscriptions, redemptions or switches. The
information provided is sorted by pre-defined criteria such as country, institution, currency or user
defined criteria.
Impacted by: C11 "ExceptionalCashFlowIndicatorRule"
FundCashForecastDetails <FndCshFcstDtls> contains the following FundCashForecast6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Constraints
• ExceptionalCashFlowIndicatorRule
If ExceptionalNetCashFlowIndicator is "true" or "1" (Yes), then at least one or more of the following
must be present:
BreakdownByParty/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByParty/CashOutForecast/ExceptionalCashFlowIndicator, or
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4418 May 2026
```

