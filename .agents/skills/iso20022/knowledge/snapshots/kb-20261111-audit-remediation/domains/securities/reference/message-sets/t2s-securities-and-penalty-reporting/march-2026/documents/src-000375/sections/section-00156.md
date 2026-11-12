---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.8 CalculationData <ClctnData>", "6.4.6.11.4.8.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "6.4.6.11.4.8.3.3 ClassificationType <ClssfctnTp>"]
file_pages: [221]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.8.3.3 ClassificationType <ClssfctnTp>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 221 to 221.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 221

```text
Usage: If not provided it means that the security is subject to penalties on this business day.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 553):
• Meaning When True: True
• Meaning When False: False
6.4.6.11.4.8.3.3  ClassificationType <ClssfctnTp>
Presence: [0..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.
ClassificationType <ClssfctnTp> contains one of the following elements (see
"ClassificationType1Choice" on page 366 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 366
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 366
6.4.6.11.4.8.3.4  Liquidity <Lqdty>
Presence: [0..1]
Definition: Specifies whether the security is liquid or illiquid.
Usage: When indicator in not provided, the liquidity is not relevant.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 553):
• Meaning When True: True
• Meaning When False: False
6.4.6.11.4.8.3.5  PriceData <PricData>
Presence: [0..1]
Definition: Further details on the price of the financial instrument.
PriceData <PricData> contains the following PriceInformation25 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1]  221
{Or     Rate <Rate> [1..1] Rate 222
Or}     Amount <Amt> [1..1] Amount C1, C5 222
   SourceOfPrice <SrcOfPric> [0..1] ± 222
   QuotationDate <QtnDt> [0..1] ± 223
6.4.6.11.4.8.3.5.1  Value <Val>
Presence: [1..1]
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 221 March 2026
```

