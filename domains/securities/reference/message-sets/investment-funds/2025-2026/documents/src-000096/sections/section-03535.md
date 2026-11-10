---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.29 ProcessingCharacteristics12", "66.1.26.29.1 DealingCurrencyAccepted <DealgCcyAccptd>"]
file_pages: [4785]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.29.1 DealingCurrencyAccepted <DealgCcyAccptd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4785 to 4785.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4785

```text
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
66.1.26.29.1  DealingCurrencyAccepted <DealgCcyAccptd>
Presence: [0..*]
Definition: Currency in which a redemption is accepted.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4785 May 2026
```

