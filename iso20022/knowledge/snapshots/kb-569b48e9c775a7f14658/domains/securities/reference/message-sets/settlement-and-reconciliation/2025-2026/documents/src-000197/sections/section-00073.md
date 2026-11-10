---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.8 BalanceForAccount <BalForAcct>", "3.4.8.19 SupplementaryData <SplmtryData>"]
file_pages: [109, 110, 111]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.8.19 SupplementaryData <SplmtryData>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 109 to 111.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 109

```text
Datatype: "Max350Text" on page 2192
3.4.8.19  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C40 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1565
   Envelope <Envlp> [1..1] (External Schema) 1565
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
3.4.9 SubAccountDetails <SubAcctDtls>
Presence: [0..*]
Definition: Sub-account of the safekeeping or investment account.
Impacted by: C3 "ActivityAndBalanceForSubAccount1Rule", C4
"ActivityAndBalanceForSubAccount2Rule", C28 "SafekeepingAccountOrBlockChainAddress1Rule",
C30 "SafekeepingAccountOrBlockChainAddress2Rule", C32
"SafekeepingAccountOrBlockChainAddress3Rule", C39 "SubSafekeepingReportingRule"
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 109 March 2026
```

## File page 110

```text
SubAccountDetails <SubAcctDtls> contains the following SubAccountIdentification72 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 110 March 2026
```

## File page 111

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ForeignExchangeDetails <FXDtls> [0..*] ± 128
       DaysAccrued <DaysAcrd> [0..1] Quantity 128
       AccountBaseCurrencyAmounts
<AcctBaseCcyAmts>
[1..1] ± 128
       InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± 129
       AlternateReportingCurrencyAmounts
<AltrnRptgCcyAmts>
[0..1] ± 129
       QuantityBreakdown <QtyBrkdwn> [0..*] ± 129
       ExposureType <XpsrTp> [0..1] ± 130
       BalanceBreakdown <BalBrkdwn> [0..*] ± C8, C37 130
       AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C17,
C38
131
       HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 131
     HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 131
     SupplementaryData <SplmtryData> [0..*] ± C40 132
Constraints
• ActivityAndBalanceForSubAccount1Rule
If the ActivityIndicator is TRUE (Yes), then at least one occurrence of BalanceForSubAccount must
be present.
On Condition
    /ActivityIndicator is equal to value 'true'
Following Must be True
    /BalanceForSubAccount[1] Must be present
• ActivityAndBalanceForSubAccount2Rule
If the ActivityIndicator is FALSE (No), then BalanceForSubAccount must not be present.
On Condition
    /ActivityIndicator is equal to value 'false'
Following Must be True
    /BalanceForSubAccount[*] Must be absent
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 111 March 2026
```

