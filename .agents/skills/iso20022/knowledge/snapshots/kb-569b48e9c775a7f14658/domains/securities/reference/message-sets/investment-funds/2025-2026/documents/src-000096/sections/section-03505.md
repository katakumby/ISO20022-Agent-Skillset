---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.14 MoneyPurchaseAnnualAllowance1", "66.1.26.14.2 TriggeredDate <TrggrdDt>"]
file_pages: [4755]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.14.2 TriggeredDate <TrggrdDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4755 to 4755.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4755

```text
66.1.26.14.2  TriggeredDate <TrggrdDt>
Presence: [0..1]
Definition: Date the annual allowance is taken.
Datatype: "ISODate" on page 5388
66.1.26.15  ProcessingCharacteristics11
Definition: Processing characteristics linked to a subscription to an investment fund or alternative/hedge
fund.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4755 May 2026
```

