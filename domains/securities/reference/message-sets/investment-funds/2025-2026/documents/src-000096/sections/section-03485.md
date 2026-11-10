---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.7 ProcessingCharacteristics9", "66.1.26.7.1 DealingCurrencyAccepted <DealgCcyAccptd>"]
file_pages: [4735]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.7.1 DealingCurrencyAccepted <DealgCcyAccptd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4735 to 4735.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4735

```text
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
66.1.26.7.1  DealingCurrencyAccepted <DealgCcyAccptd>
Presence: [0..*]
Definition: Currency in which a switch is accepted.
Impacted by: C1 "ActiveCurrency"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4735 May 2026
```

