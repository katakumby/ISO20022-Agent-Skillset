---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.33 ProcessingCharacteristics10", "66.1.26.33.1 DealingCurrencyAccepted <DealgCcyAccptd>"]
file_pages: [4801]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.33.1 DealingCurrencyAccepted <DealgCcyAccptd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4801 to 4801.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4801

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DealingCurrencyAccepted <DealgCcyAccptd> [0..*] CodeSet C1 4801
   RedemptionAuthorisation <RedAuthstn> [0..1]  4802
     ApplicationForm <ApplForm> [1..1] Indicator 4802
     SignatureType <SgntrTp> [1..1] CodeSet 4802
   AmountIndicator <AmtInd> [0..1] Indicator 4803
   UnitsIndicator <UnitsInd> [0..1] Indicator 4803
   Rounding <Rndg> [0..1] CodeSet 4803
   PercentageIndicator <PctgInd> [0..1] Indicator 4803
   MainFundOrderDeskLocation <MainFndOrdrDskLctn> [0..1] ± 4803
   DealingFrequency <DealgFrqcy> [0..1] CodeSet 4804
   DealingFrequencyDescription <DealgFrqcyDesc> [0..1] Text 4804
   DealingCutOffTime <DealgCutOffTm> [0..1] Time 4804
   DealingCutOffTimeFrame <DealgCutOffTmFrame> [0..1] ± C23,
C33
4805
   DealConfirmationTime <DealConfTm> [0..1] Time 4805
   DealConfirmationTimeFrame <DealConfTmFrame> [0..1] ± C26,
C36
4805
   LimitedPeriod <LtdPrd> [0..1] Text 4806
   SettlementCycle <SttlmCycl> [0..1]  4806
{Or     TradePlus <TPlus> [1..1] Quantity 4806
Or}     RenunciationPlus <RPlus> [1..1] Quantity 4807
   AdditionalInformation <AddtlInf> [0..*] ± 4807
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
66.1.26.33.1  DealingCurrencyAccepted <DealgCcyAccptd>
Presence: [0..*]
Definition: Currency in which a redemption is accepted.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4801 May 2026
```

