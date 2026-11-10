---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.3 Constraints"]
file_pages: [83, 84, 85, 86]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 83 to 86.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 83

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 131
       HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 131
       SupplementaryData <SplmtryData> [0..*] ± C40 132
   AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts> [0..1]  132
     TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] ± 132
     TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] ± 133
     TotalBookValueOfStatement <TtlBookValOfStmt> [0..1] ± 133
   AlternateReportingCurrencyTotalAmounts
<AltrnRptgCcyTtlAmts>
[0..1]  133
     TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] ± 133
     TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] ± 134
     TotalBookValueOfStatement <TtlBookValOfStmt> [0..1] ± 134
3.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 ActivityAndBalanceForSubAccount1Rule
If the ActivityIndicator is TRUE (Yes), then at least one occurrence of BalanceForSubAccount
must be present.
C4 ActivityAndBalanceForSubAccount2Rule
If the ActivityIndicator is FALSE (No), then BalanceForSubAccount must not be present.
C5 AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information
that can be provided in a structured field.
C6 AggregateBalanceGuideline
If AvailableQuantity and NotAvailableQuantity are both present, then the AggregateQuantity
should be the sum of AvailableQuantity and NotAvailableQuantity.
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 83 March 2026
```

## File page 84

```text
C7 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C8 AvailableWithNoStatusRule
If Subbalance type is AvailableWithNoStatus, then QuantityAndAvailability cannot be used.
C9 BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
C10 BalanceForAccountOrSubAccountDetailsRule
If StatementGeneralDetails/ActivityIndicator is TRUE (Yes), then either BalanceForAccount or
SubAccountDetails must be present. If StatementGeneralDetails/ActivityIndicator is FALSE
(No), then BalanceForAccount and SubAccountDetails must be absent.
On Condition
    /StatementGeneralDetails/ActivityIndicator is equal to value 'false'
Following Must be True
    /SubAccountDetails[*] Must be absent
 And    /BalanceForAccount[*] Must be absent
This constraint is defined at the MessageDefinition level.
C11 BalanceForAccountReportingRule
If StatementGeneralDetails/ActivityIndicator is TRUE (Yes) and SubAccountIndicator is FALSE
(NO), then BalanceForAccount must be present and Sub Account Details must be absent.
On Condition
    /StatementGeneralDetails/SubAccountIndicator is equal to value 'false'
 And    /StatementGeneralDetails/ActivityIndicator is equal to value 'true'
Following Must be True
    /SubAccountDetails[*] Must be absent
 And    /BalanceForAccount[*] Must be present
This constraint is defined at the MessageDefinition level.
C12 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C13 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C14 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C15 DescriptionUsageRule
Description must be used alone as the last resort.
C16 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 84 March 2026
```

## File page 85

```text
C17 EligibleForCollateralPurposesRule
If Subbalance type is EligibleForCollateralPurposes, then QuantityAndAvailability cannot be
used.
C18 FinancialInstrumentAttributesRule
If InvestmentFundsFinancialInstrumentAttributes is present, then FinancialInstrumentAttributes
is not allowed.
C19 HoldingAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
present, then it must not contain information that can be provided in a structured field.
C20 HoldingAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
present, then it must not contain information that can be provided in a structured field.
C21 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C22 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C23 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C24 PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO
10383 Market Identifier Code (MIC) must be used.
C25 PledgeeTypeAndIdentificationOrLEIRule
PledgeeTypeAndIdentification must be present or LEI must be present.
C26 ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports
(UpdateType: DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different ReportNumbers. For example, a daily report
sent on day 1 would have ReportNumber 001, on day 2, 002, etc.
C27 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 85 March 2026
```

## File page 86

```text
C28 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C29 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
This constraint is defined at the MessageDefinition level.
C30 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C31 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
This constraint is defined at the MessageDefinition level.
C32 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C33 SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
C34 SecuritiesMarketPracticeGroupGuideline
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the use of this message.
These market practices are available on www.smpg.info.
This constraint is defined at the MessageDefinition level.
C35 SmartContractAutomatedPricingRule
When Type/Code does not equal SmartContractAutomatedPricingSystem (SCAS) then
Identification/Description length must be maximum 35 characters.
C36 SubAccountDetailsBalanceForAccountPresenceRule
If StatementGeneralDetails/ActivityIndicator is TRUE (Yes) and SubAccountIndicator is TRUE
(YES), then SubAccountDetails must be present and BalanceForAccount must be absent.
On Condition
    /StatementGeneralDetails/ActivityIndicator is equal to value 'true'
 And    /StatementGeneralDetails/SubAccountIndicator is equal to value 'true'
Following Must be True
    /SubAccountDetails[*] Must be present
 And    /BalanceForAccount[*] Must be absent
This constraint is defined at the MessageDefinition level.
C37 SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 86 March 2026
```

