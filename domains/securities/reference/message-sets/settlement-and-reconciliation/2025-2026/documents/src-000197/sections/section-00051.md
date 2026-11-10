---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.2 Structure"]
file_pages: [80, 81, 82]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 80 to 82.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 80

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesBalAcctgRpt> [1..1]  C10,
C11,
C27,
C29,
C31,
C36,
C34
   Pagination <Pgntn> [1..1] ± 87
   StatementGeneralDetails <StmtGnlDtls> [1..1] ± C26 87
   AccountOwner <AcctOwnr> [0..1] ± 88
   AccountServicer <AcctSvcr> [0..1] ± 89
   SafekeepingAccount <SfkpgAcct> [0..1] ± 89
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 89
   IntermediaryInformation <IntrmyInf> [0..10] ± 90
   BalanceForAccount <BalForAcct> [0..*]  C9, C18,
C19
90
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C14,
C15,
C21,
C22,
C23
92
     FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C5, C24 93
     InvestmentFundsFinancialInstrumentAttributes
<InvstmtFndsFinInstrmAttrbts>
[0..1] ± 95
     AdditionalDerivativeAttributes <AddtlDerivAttrbts> [0..1] ± 96
     AggregateBalance <AggtBal> [1..1] ± 96
     SafekeepingPlace <SfkpgPlc> [0..1] ± C33 96
     CorporateActionOptionType <CorpActnOptnTp> [0..1] CodeSet 97
     PriceDetails <PricDtls> [1..*] ± C41 97
     ForeignExchangeDetails <FXDtls> [0..*] ± 98
     DaysAccrued <DaysAcrd> [0..1] Quantity 98
     AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [1..1] ± 98
     InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± 98
     AlternateReportingCurrencyAmounts <AltrnRptgCcyAmts> [0..1] ± 99
     QuantityBreakdown <QtyBrkdwn> [0..*] ± 99
     BalanceBreakdown <BalBrkdwn> [0..*] ± C8, C37 100
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 80 March 2026
```

## File page 81

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C17,
C38
100
     BalanceAtSafekeepingPlace <BalAtSfkpgPlc> [0..*]  C20, C6 101
       SafekeepingPlace <SfkpgPlc> [1..1] ± C33 102
       PlaceOfListing <PlcOfListg> [0..1] ± 103
       Pledgee <Pldgee> [0..1] ± C25 103
       AggregateBalance <AggtBal> [1..1] ± 104
       PriceDetails <PricDtls> [1..*] ± C41 104
       ForeignExchangeDetails <FXDtls> [0..*] ± 105
       DaysAccrued <DaysAcrd> [0..1] Quantity 105
       AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [1..1] ± 105
       InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± 106
       AlternateReportingCurrencyAmounts <AltrnRptgCcyAmts> [0..1] ± 106
       QuantityBreakdown <QtyBrkdwn> [0..*] ± 106
       ExposureType <XpsrTp> [0..1] ± 107
       BalanceBreakdown <BalBrkdwn> [0..*] ± C8, C37 107
       AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C17,
C38
108
       HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 108
     HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 108
     SupplementaryData <SplmtryData> [0..*] ± C40 109
   SubAccountDetails <SubAcctDtls> [0..*]  C3, C4,
C28,
C30,
C32,
C39
109
     AccountOwner <AcctOwnr> [0..1] ± 112
     SafekeepingAccount <SfkpgAcct> [0..1] ± 112
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 112
     ActivityIndicator <ActvtyInd> [1..1] Indicator 113
     BalanceForSubAccount <BalForSubAcct> [0..*]  C9, C18,
C19
113
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C14,
C15,
C21,
C22,
C23
115
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 81 March 2026
```

## File page 82

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C5, C24 116
       InvestmentFundsFinancialInstrumentAttributes
<InvstmtFndsFinInstrmAttrbts>
[0..1] ± 118
       AdditionalDerivativeAttributes <AddtlDerivAttrbts> [0..1] ± 119
       AggregateBalance <AggtBal> [1..1] ± 119
       SafekeepingPlace <SfkpgPlc> [0..1] ± C33 119
       CorporateActionOptionType <CorpActnOptnTp> [0..1] CodeSet 120
       PriceDetails <PricDtls> [1..*] ± C41 120
       ForeignExchangeDetails <FXDtls> [0..*] ± 121
       DaysAccrued <DaysAcrd> [0..1] Quantity 121
       AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [1..1] ± 121
       InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± 121
       AlternateReportingCurrencyAmounts <AltrnRptgCcyAmts> [0..1] ± 122
       QuantityBreakdown <QtyBrkdwn> [0..*] ± 122
       BalanceBreakdown <BalBrkdwn> [0..*] ± C8, C37 123
       AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C17,
C38
123
       BalanceAtSafekeepingPlace <BalAtSfkpgPlc> [0..*]  C20, C6 124
         SafekeepingPlace <SfkpgPlc> [1..1] ± C33 125
         PlaceOfListing <PlcOfListg> [0..1] ± 126
         Pledgee <Pldgee> [0..1] ± C25 126
         AggregateBalance <AggtBal> [1..1] ± 127
         PriceDetails <PricDtls> [1..*] ± C41 127
         ForeignExchangeDetails <FXDtls> [0..*] ± 128
         DaysAccrued <DaysAcrd> [0..1] Quantity 128
         AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [1..1] ± 128
         InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± 129
         AlternateReportingCurrencyAmounts <AltrnRptgCcyAmts> [0..1] ± 129
         QuantityBreakdown <QtyBrkdwn> [0..*] ± 129
         ExposureType <XpsrTp> [0..1] ± 130
         BalanceBreakdown <BalBrkdwn> [0..*] ± C8, C37 130
         AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C17,
C38
131
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 82 March 2026
```

