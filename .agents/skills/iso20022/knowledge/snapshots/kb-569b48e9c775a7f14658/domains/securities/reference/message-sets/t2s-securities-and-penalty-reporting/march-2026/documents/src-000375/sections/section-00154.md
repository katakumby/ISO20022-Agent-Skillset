---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.8 CalculationData <ClctnData>", "6.4.6.11.4.8.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "6.4.6.11.4.8.3.1 Identification <Id>"]
file_pages: [219]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.8.3.1 Identification <Id>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 219 to 219.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 219

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following
PenaltyFinancialInstrumentIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± C6, C7,
C10,
C11,
C13
219
   SubjectToPenalties <SbjtToPnlties> [0..1] Indicator 220
   ClassificationType <ClssfctnTp> [0..1] ± 221
   Liquidity <Lqdty> [0..1] Indicator 221
   PriceData <PricData> [0..1]  221
     Value <Val> [1..1]  221
{Or       Rate <Rate> [1..1] Rate 222
Or}       Amount <Amt> [1..1] Amount C1, C5 222
     SourceOfPrice <SrcOfPric> [0..1] ± 222
     QuotationDate <QtnDt> [0..1] ± 223
   ForeignExchangeData <FXData> [0..*]  223
     ExchangeRate <XchgRate> [1..1] Rate 223
     UnitCurrency <UnitCcy> [0..1] CodeSet C1 223
     QuotedCurrency <QtdCcy> [0..1] CodeSet C1 224
     QuotationDate <QtnDt> [0..1] ± 224
   SecuritiesPenaltyRateData <SctiesPnltyRateData> [0..1]  224
     MarketIdentification <MktId> [0..1] ± 224
     SMEGrowthMarket <SMEGrwthMkt> [0..1] Indicator 225
     Rate <Rate> [1..1] Rate 225
6.4.6.11.4.8.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the financial instrument.
Impacted by: C6 "DescriptionPresenceRule", C7 "DescriptionUsageRule", C10 "ISINGuideline", C11
"ISINPresenceRule", C13 "OtherIdentificationPresenceRule"
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 219 March 2026
```

