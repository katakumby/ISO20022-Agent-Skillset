---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.2 Structure"]
file_pages: [21, 22, 23]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 21 to 23.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 21

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesBalCtdyRpt> [1..1]  C11,
C12,
C29,
C31,
C33,
C38,
C36
   Pagination <Pgntn> [1..1] ± 28
   StatementGeneralDetails <StmtGnlDtls> [1..1] ± C28 28
   AccountOwner <AcctOwnr> [0..1] ± 29
   AccountServicer <AcctSvcr> [0..1] ± 29
   SafekeepingAccount <SfkpgAcct> [0..1] ± 30
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 30
   IntermediaryInformation <IntrmyInf> [0..10] ± 30
   BalanceForAccount <BalForAcct> [0..*]  C10,
C20,
C21, C6
31
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C15,
C16,
C23,
C24,
C25
33
     FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C5, C26 34
     InvestmentFundsFinancialInstrumentAttributes
<InvstmtFndsFinInstrmAttrbts>
[0..1] ± 37
     ValuationHaircutDetails <ValtnHrcutDtls> [0..1] ± 38
     AggregateBalance <AggtBal> [1..1] ± 38
     AvailableBalance <AvlblBal> [0..1] ± 38
     NotAvailableBalance <NotAvlblBal> [0..1] ± 39
     SafekeepingPlace <SfkpgPlc> [0..1] ± C35 39
     CorporateActionOptionType <CorpActnOptnTp> [0..1] CodeSet 39
     PriceDetails <PricDtls> [0..*] ± C44 40
     ForeignExchangeDetails <FXDtls> [0..*] ± 40
     DaysAccrued <DaysAcrd> [0..1] Quantity 40
     AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± C18 41
     InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± C18 41
     QuantityBreakdown <QtyBrkdwn> [0..*] ± 42
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 21 March 2026
```

## File page 22

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     BalanceBreakdown <BalBrkdwn> [0..*] ± C9, C39 42
     AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C19,
C40
43
     BalanceAtSafekeepingPlace <BalAtSfkpgPlc> [0..*]  C22, C7 43
       SafekeepingPlace <SfkpgPlc> [1..1] ± C35 44
       PlaceOfListing <PlcOfListg> [0..1] ± 45
       Pledgee <Pldgee> [0..1] ± C27 45
       AggregateBalance <AggtBal> [1..1] ± 46
       AvailableBalance <AvlblBal> [0..1] ± 46
       NotAvailableBalance <NotAvlblBal> [0..1] ± 47
       PriceDetails <PricDtls> [0..*] ± C44 47
       ForeignExchangeDetails <FXDtls> [0..*] ± 47
       DaysAccrued <DaysAcrd> [0..1] Quantity 48
       AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± C18 48
       InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± C18 48
       QuantityBreakdown <QtyBrkdwn> [0..*] ± 49
       ExposureType <XpsrTp> [0..1] ± 49
       BalanceBreakdown <BalBrkdwn> [0..*] ± C9, C39 50
       AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C19,
C40
50
       HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 51
     HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 51
     SupplementaryData <SplmtryData> [0..*] ± C42 51
   SubAccountDetails <SubAcctDtls> [0..*]  C3, C4,
C30,
C32,
C34,
C41
51
     AccountOwner <AcctOwnr> [0..1] ± 55
     SafekeepingAccount <SfkpgAcct> [0..1] ± 55
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 55
     ActivityIndicator <ActvtyInd> [1..1] Indicator 56
     BalanceForSubAccount <BalForSubAcct> [0..*]  C10,
C20,
C21, C6
56
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C15,
C16,
58
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 22 March 2026
```

## File page 23

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
C23,
C24,
C25
       FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C5, C26 59
       InvestmentFundsFinancialInstrumentAttributes
<InvstmtFndsFinInstrmAttrbts>
[0..1] ± 61
       ValuationHaircutDetails <ValtnHrcutDtls> [0..1] ± 62
       AggregateBalance <AggtBal> [1..1] ± 62
       AvailableBalance <AvlblBal> [0..1] ± 62
       NotAvailableBalance <NotAvlblBal> [0..1] ± 63
       SafekeepingPlace <SfkpgPlc> [0..1] ± C35 63
       CorporateActionOptionType <CorpActnOptnTp> [0..1] CodeSet 63
       PriceDetails <PricDtls> [0..*] ± C44 64
       ForeignExchangeDetails <FXDtls> [0..*] ± 64
       DaysAccrued <DaysAcrd> [0..1] Quantity 64
       AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± C18 65
       InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± C18 65
       QuantityBreakdown <QtyBrkdwn> [0..*] ± 66
       BalanceBreakdown <BalBrkdwn> [0..*] ± C9, C39 66
       AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C19,
C40
67
       BalanceAtSafekeepingPlace <BalAtSfkpgPlc> [0..*]  C22, C7 67
         SafekeepingPlace <SfkpgPlc> [1..1] ± C35 68
         PlaceOfListing <PlcOfListg> [0..1] ± 69
         Pledgee <Pldgee> [0..1] ± C27 69
         AggregateBalance <AggtBal> [1..1] ± 70
         AvailableBalance <AvlblBal> [0..1] ± 70
         NotAvailableBalance <NotAvlblBal> [0..1] ± 71
         PriceDetails <PricDtls> [0..*] ± C44 71
         ForeignExchangeDetails <FXDtls> [0..*] ± 71
         DaysAccrued <DaysAcrd> [0..1] Quantity 72
         AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± C18 72
         InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± C18 72
         QuantityBreakdown <QtyBrkdwn> [0..*] ± 73
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 23 March 2026
```

