---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.7 IntermediaryInformation <IntrmyInf>"]
file_pages: [90, 91]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.7 IntermediaryInformation <IntrmyInf>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 90 to 91.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 90

```text
3.4.7 IntermediaryInformation <IntrmyInf>
Presence: [0..10]
Definition: Information about the party that provides services relating to financial products to investors,
for example, advice on products and placement of orders for the investment fund.
IntermediaryInformation <IntrmyInf> contains the following elements (see "Intermediary44" on
page 1682 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1683
   Role <Role> [0..1] ± 1683
   Account <Acct> [0..1] ± 1683
3.4.8 BalanceForAccount <BalForAcct>
Presence: [0..*]
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
Impacted by: C9 "BalanceAtSafekeepingPlaceRule", C18 "FinancialInstrumentAttributesRule", C19
"HoldingAdditionalDetailsRule"
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 90 March 2026
```

## File page 91

```text
BalanceForAccount <BalForAcct> contains the following AggregateBalanceInformation45
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
   AlternateReportingCurrencyAmounts
<AltrnRptgCcyAmts>
[0..1] ± 99
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 99
   BalanceBreakdown <BalBrkdwn> [0..*] ± C8, C37 100
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
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 91 March 2026
```

