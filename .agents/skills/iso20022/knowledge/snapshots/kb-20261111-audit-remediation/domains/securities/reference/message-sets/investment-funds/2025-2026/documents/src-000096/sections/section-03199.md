---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.7 Cash", "66.1.7.6 FundConfirmedCashForecastReport3", "66.1.7.6.1 FundOrSubFundDetails <FndOrSubFndDtls>"]
file_pages: [4430, 4431]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.7.6.1 FundOrSubFundDetails <FndOrSubFndDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4430 to 4431.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4430

```text
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
Following Must be True
    /FundOrSubFundDetails[*]/TradeDateTime Must be present
66.1.7.6.1  FundOrSubFundDetails <FndOrSubFndDtls>
Presence: [0..*]
Definition: Information about the fund/sub fund when the report either specifies cash flow for the
fund/sub fund or for a share class of the fund/sub fund.
Impacted by: C13 "FundIdentification1Rule", C14 "FundIdentification2Rule", C15
"FundIdentification3Rule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4430 May 2026
```

## File page 4431

```text
FundOrSubFundDetails <FndOrSubFndDtls> contains the following elements (see "Fund2" on
page 4664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 4666
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4666
   Identification <Id> [0..1]  4666
     Identification <Id> [1..1] Text 4666
     Type <Tp> [1..1] ± 4666
   Currency <Ccy> [0..1] CodeSet C2 4667
   TradeDateTime <TradDtTm> [0..1] ± 4667
   PreviousTradeDateTime <PrvsTradDtTm> [0..1] ± 4667
   TotalNAV <TtlNAV> [0..1] Amount C2, C10 4668
   PreviousTotalNAV <PrvsTtlNAV> [0..1] Amount C2, C10 4668
   TotalUnitsNumber <TtlUnitsNb> [0..1] ± 4668
   PreviousTotalUnitsNumber <PrvsTtlUnitsNb> [0..1] ± 4669
   PercentageOfFundTotalNAV <PctgOfFndTtlNAV> [0..1] Rate 4669
   CashInForecastDetails <CshInFcstDtls> [0..*] ± 4669
   CashOutForecastDetails <CshOutFcstDtls> [0..*] ± 4669
   NetCashForecastDetails <NetCshFcstDtls> [0..*]  4669
     CashSettlementDate <CshSttlmDt> [0..1] Date 4670
     NetAmount <NetAmt> [0..1] Amount C2, C10 4670
     NetUnitsNumber <NetUnitsNb> [0..1] ± 4670
     FlowDirection <FlowDrctn> [1..1] CodeSet 4670
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4431 May 2026
```

