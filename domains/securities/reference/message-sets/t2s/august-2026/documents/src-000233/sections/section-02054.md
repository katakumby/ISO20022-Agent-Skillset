---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.8 CalculationData <ClctnData>", "81.4.6.11.4.8.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "81.4.6.11.4.8.3.3 ClassificationType <ClssfctnTp>"]
file_pages: [2803]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.8.3.3 ClassificationType <ClssfctnTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2803 to 2803.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2803

```text
Usage: If not provided it means that the security is subject to penalties on this business day.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
81.4.6.11.4.8.3.3  ClassificationType <ClssfctnTp>
Presence: [0..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.
ClassificationType <ClssfctnTp> contains one of the following elements (see
"ClassificationType1Choice" on page 2985 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 2986
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 2986
81.4.6.11.4.8.3.4  Liquidity <Lqdty>
Presence: [0..1]
Definition: Specifies whether the security is liquid or illiquid.
Usage: When indicator in not provided, the liquidity is not relevant.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
81.4.6.11.4.8.3.5  PriceData <PricData>
Presence: [0..1]
Definition: Further details on the price of the financial instrument.
PriceData <PricData> contains the following PriceInformation25 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1]  2803
{Or     Rate <Rate> [1..1] Rate 2804
Or}     Amount <Amt> [1..1] Amount C1, C5 2804
   SourceOfPrice <SrcOfPric> [0..1] ± 2804
   QuotationDate <QtnDt> [0..1] ± 2805
81.4.6.11.4.8.3.5.1  Value <Val>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2803 August 2026
```

