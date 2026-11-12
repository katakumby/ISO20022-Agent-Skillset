---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["7 camt.040.001.04 FundEstimatedCashForecastReportV04", "7.4 Message Building Blocks", "7.4.5 MessagePagination <MsgPgntn>"]
file_pages: [100, 101]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.040.001.04"]
---

# 7.4.5 MessagePagination <MsgPgntn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 100 to 101.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 100

```text
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference3" on
page 4537 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4537
   ReferenceIssuer <RefIssr> [0..1] ± 4537
   MessageName <MsgNm> [0..1] Text 4537
7.4.5 MessagePagination <MsgPgntn>
Presence: [1..1]
Definition: Pagination of the message.
MessagePagination <MsgPgntn> contains the following elements (see "Pagination" on page 4833 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 4833
   LastPageIndicator <LastPgInd> [1..1] Indicator 4833
7.4.6 FundOrSubFundDetails <FndOrSubFndDtls>
Presence: [0..*]
Definition: Information about the fund/sub fund when the report either specifies cash flow for the
fund/sub fund or for a share class of the fund/sub fund.
Impacted by: C13 "FundIdentification1Rule", C14 "FundIdentification2Rule", C15
"FundIdentification3Rule"
Approved by the Securities SEG on 27 January 2026 camt.040.001.04
FundEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 100 May 2026
```

## File page 101

```text
FundOrSubFundDetails <FndOrSubFndDtls> contains the following elements (see "Fund1" on
page 4681 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 4683
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4683
   Identification <Id> [0..1]  4683
     Identification <Id> [1..1] Text 4683
     Type <Tp> [1..1] ± 4683
   Currency <Ccy> [0..1] CodeSet C2 4684
   TradeDateTime <TradDtTm> [0..1] ± 4684
   PreviousTradeDateTime <PrvsTradDtTm> [0..1] ± 4684
   EstimatedTotalNAV <EstmtdTtlNAV> [0..1] Amount C2, C10 4685
   PreviousTotalNAV <PrvsTtlNAV> [0..1] Amount C2, C10 4685
   EstimatedTotalUnitsNumber <EstmtdTtlUnitsNb> [0..1] ± 4685
   PreviousTotalUnitsNumber <PrvsTtlUnitsNb> [0..1] ± 4686
   EstimatedPercentageOfFundTotalNAV
<EstmtdPctgOfFndTtlNAV>
[0..1] Rate 4686
   EstimatedCashInForecastDetails <EstmtdCshInFcstDtls> [0..*] ± 4686
   EstimatedCashOutForecastDetails
<EstmtdCshOutFcstDtls>
[0..*] ± 4686
   EstimatedNetCashForecastDetails
<EstmtdNetCshFcstDtls>
[0..*]  4686
     CashSettlementDate <CshSttlmDt> [0..1] Date 4687
     NetAmount <NetAmt> [0..1] Amount C2, C10 4687
     NetUnitsNumber <NetUnitsNb> [0..1] ± 4687
     FlowDirection <FlowDrctn> [1..1] CodeSet 4687
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
Approved by the Securities SEG on 27 January 2026 camt.040.001.04
FundEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 101 May 2026
```

