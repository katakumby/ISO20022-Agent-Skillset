---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.8 BalanceForAccount <BalForAcct>"]
file_pages: [31, 32]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.8 BalanceForAccount <BalForAcct>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 31 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 31

```text
IntermediaryInformation <IntrmyInf> contains the following elements (see "Intermediary44" on
page 1682 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1683
   Role <Role> [0..1] ± 1683
   Account <Acct> [0..1] ± 1683
2.4.8 BalanceForAccount <BalForAcct>
Presence: [0..*]
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
Impacted by: C10 "BalanceAtSafekeepingPlaceRule", C20 "FinancialInstrumentAttributesRule", C21
"HoldingAdditionalDetailsRule", C6 "AggregateBalanceGuideline"
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 31 March 2026
```

## File page 32

```text
BalanceForAccount <BalForAcct> contains the following AggregateBalanceInformation46
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 32 March 2026
```

