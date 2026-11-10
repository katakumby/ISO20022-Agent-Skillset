---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.8 CalculationData <ClctnData>", "81.4.6.11.4.8.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "81.4.6.11.4.8.3.1 Identification <Id>"]
file_pages: [2801]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.8.3.1 Identification <Id>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2801 to 2801.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2801

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
2801
   SubjectToPenalties <SbjtToPnlties> [0..1] Indicator 2802
   ClassificationType <ClssfctnTp> [0..1] ± 2803
   Liquidity <Lqdty> [0..1] Indicator 2803
   PriceData <PricData> [0..1]  2803
     Value <Val> [1..1]  2803
{Or       Rate <Rate> [1..1] Rate 2804
Or}       Amount <Amt> [1..1] Amount C1, C5 2804
     SourceOfPrice <SrcOfPric> [0..1] ± 2804
     QuotationDate <QtnDt> [0..1] ± 2805
   ForeignExchangeData <FXData> [0..*]  2805
     ExchangeRate <XchgRate> [1..1] Rate 2805
     UnitCurrency <UnitCcy> [0..1] CodeSet C1 2805
     QuotedCurrency <QtdCcy> [0..1] CodeSet C1 2806
     QuotationDate <QtnDt> [0..1] ± 2806
   SecuritiesPenaltyRateData <SctiesPnltyRateData> [0..1]  2806
     MarketIdentification <MktId> [0..1] ± 2806
     SMEGrowthMarket <SMEGrwthMkt> [0..1] Indicator 2807
     Rate <Rate> [1..1] Rate 2807
81.4.6.11.4.8.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the financial instrument.
Impacted by: C6 "DescriptionPresenceRule", C7 "DescriptionUsageRule", C10 "ISINGuideline", C11
"ISINPresenceRule", C13 "OtherIdentificationPresenceRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2801 August 2026
```

