---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.8 BalanceForAccount <BalForAcct>", "2.4.8.18 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>", "2.4.8.18.16 HoldingAdditionalDetails <HldgAddtlDtls>"]
file_pages: [51, 52, 53, 54]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.8.18.16 HoldingAdditionalDetails <HldgAddtlDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 51 to 54.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 51

```text
Constraints
• EligibleForCollateralPurposesRule
If Subbalance type is EligibleForCollateralPurposes, then QuantityAndAvailability cannot be used.
On Condition
    /SubBalanceType/Code is equal to value 'EligibleForCollateralPurposes'
Following Must be True
    /Quantity/Quantity/QuantityAndAvailability Must be absent
• SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
2.4.8.18.16  HoldingAdditionalDetails <HldgAddtlDtls>
Presence: [0..1]
Definition: Provides additional information on the holding.
Datatype: "Max350Text" on page 2192
2.4.8.19  HoldingAdditionalDetails <HldgAddtlDtls>
Presence: [0..1]
Definition: Provides additional information on the holding.
Datatype: "Max350Text" on page 2192
2.4.8.20  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C42 "SupplementaryDataRule"
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
2.4.9 SubAccountDetails <SubAcctDtls>
Presence: [0..*]
Definition: Sub-account of the safekeeping or investment account.
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 51 March 2026
```

## File page 52

```text
Impacted by: C3 "ActivityAndBalanceForSubAccount1Rule", C4
"ActivityAndBalanceForSubAccount2Rule", C30 "SafekeepingAccountOrBlockChainAddress1Rule",
C32 "SafekeepingAccountOrBlockChainAddress2Rule", C34
"SafekeepingAccountOrBlockChainAddress3Rule", C41 "SubSafekeepingReportingRule"
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 52 March 2026
```

## File page 53

```text
SubAccountDetails <SubAcctDtls> contains the following SubAccountIdentification71 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 53 March 2026
```

## File page 54

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AvailableBalance <AvlblBal> [0..1] ± 70
       NotAvailableBalance <NotAvlblBal> [0..1] ± 71
       PriceDetails <PricDtls> [0..*] ± C44 71
       ForeignExchangeDetails <FXDtls> [0..*] ± 71
       DaysAccrued <DaysAcrd> [0..1] Quantity 72
       AccountBaseCurrencyAmounts
<AcctBaseCcyAmts>
[0..1] ± C18 72
       InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± C18 72
       QuantityBreakdown <QtyBrkdwn> [0..*] ± 73
       ExposureType <XpsrTp> [0..1] ± 73
       BalanceBreakdown <BalBrkdwn> [0..*] ± C9, C39 73
       AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C19,
C40
74
       HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 75
     HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 75
     SupplementaryData <SplmtryData> [0..*] ± C42 75
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
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 54 March 2026
```

