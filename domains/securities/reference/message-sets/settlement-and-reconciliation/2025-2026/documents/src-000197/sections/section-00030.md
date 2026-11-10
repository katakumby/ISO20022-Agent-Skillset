---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.9 SubAccountDetails <SubAcctDtls>", "2.4.9.4 ActivityIndicator <ActvtyInd>"]
file_pages: [56, 57]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.9.4 ActivityIndicator <ActvtyInd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 56 to 57.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 56

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet2" on page 1633 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1633
   Type <Tp> [0..1] ± 1633
   Name <Nm> [0..1] Text 1634
2.4.9.4  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
2.4.9.5  BalanceForSubAccount <BalForSubAcct>
Presence: [0..*]
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities subaccount.
Impacted by: C10 "BalanceAtSafekeepingPlaceRule", C20 "FinancialInstrumentAttributesRule", C21
"HoldingAdditionalDetailsRule", C6 "AggregateBalanceGuideline"
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 56 March 2026
```

## File page 57

```text
BalanceForSubAccount <BalForSubAcct> contains the following AggregateBalanceInformation46
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C15,
C16,
C23,
C24,
C25
58
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
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 57 March 2026
```

