---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.13 ValuationDealingCharacteristics <ValtnDealgChrtcs>"]
file_pages: [324]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.13 ValuationDealingCharacteristics <ValtnDealgChrtcs>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 324 to 324.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 324

```text
15.4.5.13  ValuationDealingCharacteristics <ValtnDealgChrtcs>
Presence: [0..1]
Definition: Processing characteristics linked to the instrument, that is, not to the market.
ValuationDealingCharacteristics <ValtnDealgChrtcs> contains the following elements (see
"ValuationDealingProcessingCharacteristics3" on page 5122 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValuationFrequency <ValtnFrqcy> [0..1] CodeSet 5122
   ValuationFrequencyDescription <ValtnFrqcyDesc> [0..1] Text 5123
   ValuationTime <ValtnTm> [0..1] Time 5123
   DecimalisationUnits <DcmlstnUnits> [0..1] Quantity 5123
   DecimalisationPrice <DcmlstnPric> [0..1] Quantity 5123
   DualFundIndicator <DualFndInd> [0..1] Indicator 5123
   PriceMethod <PricMtd> [0..1] CodeSet 5124
   PriceCurrency <PricCcy> [0..*] CodeSet C1 5124
   AdditionalInformation <AddtlInf> [0..*] ± 5124
15.4.5.14  InvestmentRestrictions <InvstmtRstrctns>
Presence: [0..1]
Definition: Investment restrictions linked to the trading of the investment fund or an alternative/hedge
fund.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 324 May 2026
```

