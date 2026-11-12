---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.18 PlanCharacteristics <PlanChrtcs>"]
file_pages: [329]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.18 PlanCharacteristics <PlanChrtcs>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 329 to 329.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 329

```text
SwitchProcessingCharacteristics <SwtchPrcgChrtcs> contains the following elements (see
"ProcessingCharacteristics9" on page 4734 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DealingCurrencyAccepted <DealgCcyAccptd> [0..*] CodeSet C1 4735
   SwitchAuthorisation <SwtchAuthstn> [0..1]  4736
     ApplicationForm <ApplForm> [1..1] Indicator 4736
     SignatureType <SgntrTp> [1..1] CodeSet 4736
   AmountIndicator <AmtInd> [0..1] Indicator 4737
   UnitsIndicator <UnitsInd> [0..1] Indicator 4737
   Rounding <Rndg> [0..1] CodeSet 4737
   MainFundOrderDeskLocation <MainFndOrdrDskLctn> [0..1] ± 4737
   DealingFrequency <DealgFrqcy> [0..1] CodeSet 4737
   DealingFrequencyDescription <DealgFrqcyDesc> [0..1] Text 4738
   DealingCutOffTime <DealgCutOffTm> [0..1] Time 4738
   DealingCutOffTimeFrame <DealgCutOffTmFrame> [0..1] ± C23,
C33
4738
   DealConfirmationTime <DealConfTm> [0..1] Time 4739
   DealConfirmationTimeFrame <DealConfTmFrame> [0..1] ± C26,
C36
4739
   LimitedPeriod <LtdPrd> [0..1] Text 4740
   SettlementCycle <SttlmCycl> [0..1]  4740
{Or     TradePlus <TPlus> [1..1] Quantity 4740
Or}     RenunciationPlus <RPlus> [1..1] Quantity 4740
   AdditionalInformation <AddtlInf> [0..*] ± 4740
Constraints
• DealingCutOffTimeFrameRule
If DealingCutOffTimeFrame is present, then DealingCutOffTimeFrame/OtherTimeFrameDescription
or DealingCutOffTimeFrame/ReferToOrderDesk or DealingCutOffTimeFrame/TradeMinus must be
present.
On Condition
    /DealingCutOffTimeFrame is present
Following Must be True
    /DealingCutOffTimeFrame/OtherTimeFrameDescription Must be present
 Or    /DealingCutOffTimeFrame/TradeMinus Must be present
 Or    /DealingCutOffTimeFrame/ReferToOrderDesk Must be present
15.4.5.18  PlanCharacteristics <PlanChrtcs>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 329 May 2026
```

