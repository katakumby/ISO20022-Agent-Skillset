---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.16 RedemptionProcessingCharacteristics <RedPrcgChrtcs>"]
file_pages: [327]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.16 RedemptionProcessingCharacteristics <RedPrcgChrtcs>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 327 to 327.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 327

```text
 Or    /DealingCutOffTimeFrame/TradeMinus Must be present
 Or    /DealingCutOffTimeFrame/ReferToOrderDesk Must be present
15.4.5.16  RedemptionProcessingCharacteristics <RedPrcgChrtcs>
Presence: [0..1]
Definition: Processing characteristics linked to a redemption from the investment fund or alternative/
hedge fund.
Impacted by: C9 "DealingCutOffTimeFrameRule"
RedemptionProcessingCharacteristics <RedPrcgChrtcs> contains the following elements (see
"ProcessingCharacteristics12" on page 4784 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DealingCurrencyAccepted <DealgCcyAccptd> [0..*] CodeSet C1 4785
   RedemptionAuthorisation <RedAuthstn> [0..1]  4786
     ApplicationForm <ApplForm> [1..1] Indicator 4786
     SignatureType <SgntrTp> [1..1] CodeSet 4786
   AmountIndicator <AmtInd> [0..1] Indicator 4787
   UnitsIndicator <UnitsInd> [0..1] Indicator 4787
   Rounding <Rndg> [0..1] CodeSet 4787
   PercentageIndicator <PctgInd> [0..1] Indicator 4787
   MainFundOrderDeskLocation <MainFndOrdrDskLctn> [0..1] ± 4787
   DealingFrequency <DealgFrqcy> [0..1] CodeSet 4788
   DealingFrequencyDescription <DealgFrqcyDesc> [0..1] Text 4788
   DealingCutOffTime <DealgCutOffTm> [0..1] Time 4788
   DealingCutOffTimeFrame <DealgCutOffTmFrame> [0..1] ± C23,
C33
4789
   DealConfirmationTime <DealConfTm> [0..1] Time 4789
   DealConfirmationTimeFrame <DealConfTmFrame> [0..1] ± C25,
C35
4789
   LimitedPeriod <LtdPrd> [0..1] Text 4790
   SettlementCycle <SttlmCycl> [0..1]  4790
{Or     TradePlus <TPlus> [1..1] Quantity 4790
Or}     RenunciationPlus <RPlus> [1..1] Quantity 4791
   AdditionalInformation <AddtlInf> [0..*] ± 4791
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 327 May 2026
```

