---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.3 Constraints"]
file_pages: [24, 25, 26, 27]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
topic_continuations: [{"constraint_ids": ["C39", "C40", "C41", "C42", "C43", "C44"], "until_heading": "2.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 28, "topic": "2.3 Constraints", "reference_path": "domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00008.md"}]
---

# 2.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 24 to 27.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 2.3 Constraints topic continues in [Constraints continuation C39–C44 (file p28)](section-00008.md#file-page-28). Read the text before **2.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 24

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         ExposureType <XpsrTp> [0..1] ± 73
         BalanceBreakdown <BalBrkdwn> [0..*] ± C9, C39 73
         AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C19,
C40
74
         HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 75
       HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 75
       SupplementaryData <SplmtryData> [0..*] ± C42 75
   AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts> [0..1]  C43 75
     TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] ± 76
     TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] ± 76
     TotalBookValueOfStatement <TtlBookValOfStmt> [0..1] ± 76
     TotalEligibleCollateralValue <TtlElgblCollVal> [0..1] ± 77
2.3 Constraints
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
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 24 March 2026
```

## File page 25

```text
C7 AggregateBalanceGuideline
If AvailableQuantity and NotAvailableQuantity are both present, then the AggregateQuantity
should be the sum of AvailableQuantity and NotAvailableQuantity.
C8 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C9 AvailableWithNoStatusRule
If Subbalance type is AvailableWithNoStatus, then QuantityAndAvailability cannot be used.
C10 BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
C11 BalanceForAccountOrSubAccountDetailsRule
If StatementGeneralDetails/ActivityIndicator is TRUE (Yes), then either BalanceForAccount or
SubAccountDetails must be present. If StatementGeneralDetails/ActivityIndicator is FALSE
(No), then BalanceForAccount and SubAccountDetails must be absent.
On Condition
    /StatementGeneralDetails/ActivityIndicator is equal to value 'false'
Following Must be True
    /SubAccountDetails[*] Must be absent
 And    /BalanceForAccount[*] Must be absent
This constraint is defined at the MessageDefinition level.
C12 BalanceForAccountReportingRule
If StatementGeneralDetails/ActivityIndicator is TRUE (Yes) and SubAccountIndicator is FALSE
(NO), then BalanceForAccount must be present and Sub Account Details must be absent.
On Condition
    /StatementGeneralDetails/SubAccountIndicator is equal to value 'false'
 And    /StatementGeneralDetails/ActivityIndicator is equal to value 'true'
Following Must be True
    /SubAccountDetails[*] Must be absent
 And    /BalanceForAccount[*] Must be present
This constraint is defined at the MessageDefinition level.
C13 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C14 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C15 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C16 DescriptionUsageRule
Description must be used alone as the last resort.
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 25 March 2026
```

## File page 26

```text
C17 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C18 EligibleCollateralValueRule
EligibleCollateralValue is only to be used in (I)CSD-participant communication or if bilaterally
agreed between the sender and receiver.
C19 EligibleForCollateralPurposesRule
If Subbalance type is EligibleForCollateralPurposes, then QuantityAndAvailability cannot be
used.
C20 FinancialInstrumentAttributesRule
If InvestmentFundsFinancialInstrumentAttributes is present, then FinancialInstrumentAttributes
is not allowed.
C21 HoldingAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
present, then it must not contain information that can be provided in a structured field.
C22 HoldingAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if HoldingAdditionnalDetails is
present, then it must not contain information that can be provided in a structured field.
C23 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C24 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C25 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C26 PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO
10383 Market Identifier Code (MIC) must be used.
C27 PledgeeTypeAndIdentificationOrLEIRule
PledgeeTypeAndIdentification must be present or LEI must be present.
C28 ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports
(UpdateType: DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different ReportNumbers. For example, a daily report
sent on day 1 would have ReportNumber 001, on day 2, 002, etc.
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 26 March 2026
```

## File page 27

```text
C29 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
This constraint is defined at the MessageDefinition level.
C30 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C31 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
This constraint is defined at the MessageDefinition level.
C32 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C33 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
This constraint is defined at the MessageDefinition level.
C34 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C35 SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
C36 SecuritiesMarketPracticeGroupGuideline
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the use of this message.
These market practices are available on www.smpg.info.
This constraint is defined at the MessageDefinition level.
C37 SmartContractAutomatedPricingRule
When Type/Code does not equal SmartContractAutomatedPricingSystem (SCAS) then
Identification/Description length must be maximum 35 characters.
C38 SubAccountDetailsBalanceForAccountPresenceRule
If StatementGeneralDetails/ActivityIndicator is TRUE (Yes) and SubAccountIndicator is TRUE
(YES), then SubAccountDetails must be present and BalanceForAccount must be absent.
On Condition
    /StatementGeneralDetails/ActivityIndicator is equal to value 'true'
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 27 March 2026
```

