---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.9 SubAccountDetails <SubAcctDtls>", "3.4.9.4 ActivityIndicator <ActvtyInd>"]
file_pages: [113, 114]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.9.4 ActivityIndicator <ActvtyInd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 113 to 114.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 113

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet2" on page 1633 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1633
   Type <Tp> [0..1] ± 1633
   Name <Nm> [0..1] Text 1634
3.4.9.4  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
3.4.9.5  BalanceForSubAccount <BalForSubAcct>
Presence: [0..*]
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities subaccount.
Impacted by: C9 "BalanceAtSafekeepingPlaceRule", C18 "FinancialInstrumentAttributesRule", C19
"HoldingAdditionalDetailsRule"
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 113 March 2026
```

## File page 114

```text
BalanceForSubAccount <BalForSubAcct> contains the following AggregateBalanceInformation45
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C14,
C15,
C21,
C22,
C23
115
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
   AlternateReportingCurrencyAmounts
<AltrnRptgCcyAmts>
[0..1] ± 122
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
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 114 March 2026
```

