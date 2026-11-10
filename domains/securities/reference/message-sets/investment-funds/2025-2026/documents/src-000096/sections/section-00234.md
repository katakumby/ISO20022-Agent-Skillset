---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.21 LocalMarketAnnex <LclMktAnx>", "15.4.5.21.2 LocalOrderDesk <LclOrdrDsk>"]
file_pages: [336, 337]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.21.2 LocalOrderDesk <LclOrdrDsk>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 336 to 337.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 336

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
15.4.5.21.2  LocalOrderDesk <LclOrdrDsk>
Presence: [1..1]
Definition: Local entity appointed by the fund, to which orders should be submitted.
LocalOrderDesk <LclOrdrDsk> contains the following elements (see "OrderDesk1" on page 4959 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderDesk <OrdrDsk> [0..1] ± 4959
   ClosureDates <ClsrDts> [0..*] Date 4959
   AdditionalInformation <AddtlInf> [0..*] ± 4959
15.4.5.21.3  SubscriptionProcessingCharacteristics <SbcptPrcgChrtcs>
Presence: [0..1]
Definition: Processing characteristics linked to a subscription to the investment fund or alternative/
hedge fund.
Impacted by: C8 "DealingCutOffTimeFrameRule"
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 336 May 2026
```

## File page 337

```text
SubscriptionProcessingCharacteristics <SbcptPrcgChrtcs> contains the following elements (see
"ProcessingCharacteristics11" on page 4755 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DealingCurrencyAccepted <DealgCcyAccptd> [0..*] CodeSet C1 4756
   InitialInvestmentApplication <InitlInvstmtAppl> [0..1]  4756
     ApplicationForm <ApplForm> [1..1] Indicator 4756
     SignatureType <SgntrTp> [1..1] CodeSet 4756
   SubsequentInvestmentApplication <SbsqntInvstmtAppl> [0..1]  4757
     ApplicationForm <ApplForm> [1..1] Indicator 4757
     SignatureType <SgntrTp> [1..1] CodeSet 4757
   AmountIndicator <AmtInd> [0..1] Indicator 4758
   UnitsIndicator <UnitsInd> [0..1] Indicator 4758
   Rounding <Rndg> [0..1] CodeSet 4758
   MainFundOrderDeskLocation <MainFndOrdrDskLctn> [0..1] ± 4758
   DealingFrequency <DealgFrqcy> [0..1] CodeSet 4759
   DealingFrequencyDescription <DealgFrqcyDesc> [0..1] Text 4759
   DealingCutOffTime <DealgCutOffTm> [0..1] Time 4759
   DealingCutOffTimeFrame <DealgCutOffTmFrame> [0..1] ± C23,
C33
4760
   DealConfirmationTime <DealConfTm> [0..1] Time 4760
   DealConfirmationTimeFrame <DealConfTmFrame> [0..1] ± C24,
C34
4760
   LimitedPeriod <LtdPrd> [0..1] Text 4761
   SettlementCycle <SttlmCycl> [0..1]  4761
{Or     TradePlus <TPlus> [1..1] Quantity 4761
Or}     Prepayment <Prepmt> [1..1] Indicator 4762
   AdditionalInformation <AddtlInf> [0..*] ± 4762
Constraints
• DealingCutOffTimeFrameRule
If DealingCutOffTimeFrame is present, then DealingCutOffTimeFrame/OtherTimeFrameDescription
or DealingCutOffTimeFrame/ReferToOrderDesk or DealingCutOffTimeFrame/TradeMinus must be
present.
On Condition
    /DealingCutOffTimeFrame is present
Following Must be True
    /DealingCutOffTimeFrame/OtherTimeFrameDescription Must be present
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 337 May 2026
```

