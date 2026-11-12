---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.16 CustomerConductClassification1Choice", "66.1.24.16.2 Proprietary <Prtry>"]
file_pages: [4664, 4665]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.16.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4664 to 4665.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4664

```text
CodeName Name Definition
RCLT Reluctant Reluctant.
STAN Standard Standard.
66.1.24.16.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Conduct type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.25 InvestmentFundCashForecast
66.1.25.1  Fund2
Definition: Information about an investment fund.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4664 May 2026
```

## File page 4665

```text
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
Following Must be True
    /Identification Must be present
 Or    /LegalEntityIdentifier Must be absent
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4665 May 2026
```

