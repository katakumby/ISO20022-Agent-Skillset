---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["80 semt.040.001.01 SecuritiesAccountPositionResponseV01", "80.2 Structure"]
file_pages: [2750, 2751, 2752]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.040.001.01"]
---

# 80.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2750 to 2752.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2750

```text
80.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctPosRspn> [1..1]  C13,
C14,
C34
   Pagination <Pgntn> [1..1] ± 2754
   ReportGeneralDetails <RptGnlDtls> [1..1] ± C30 2754
   AccountOwner <AcctOwnr> [0..1] ± 2754
   AccountServicer <AcctSvcr> [0..1] ± 2755
   Balances <Bals> [0..*] ± C12 2755
   PartyBaseCurrencyTotalAmounts <PtyBaseCcyTtlAmts> [0..1]  C40 2758
     TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] ± 2758
     TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] ± 2758
     TotalBookValueOfStatement <TtlBookValOfStmt> [0..1] ± 2759
     TotalEligibleCollateralValue <TtlElgblCollVal> [0..1] ± 2759
   OtherBusinessParties <OthrBizPties> [0..1]  2759
     Investor <Invstr> [0..*] ± C24,
C31,
C32
2759
80.3 Constraints
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
If the ActivityIndicator is "true" (Yes), then at least one occurrence of BalanceForSubAccount
must be present.
C4 ActivityAndBalanceForSubAccount2Rule
If the ActivityIndicator is "false" (No), then BalanceForSubAccount must be absent.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities 2750 August 2026
```

## File page 2751

```text
C5 AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information
that can be provided in a structured field.
C6 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C7 AggregateBalanceGuideline
If AvailableBalance and NotAvailableBalance are both present, then the AggregateBalance
should be the sum of AvailableBalance and NotAvailableBalance.
C8 AggregateBalanceGuideline
If AvailableQuantity and NotAvailableQuantity are both present, then the AggregateQuantity
should be the sum of AvailableQuantity and NotAvailableQuantity.
C9 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C10 AvailableWithNoStatusRule
If Subbalance type is AvailableWithNoStatus, then QuantityAndAvailability cannot be used.
C11 BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
C12 BalanceForAccountOrSubAccountRule
BalanceForAccount must be present or SubAccountDetails must be present, both may be
present.
C13 BalanceForAccountReportingRule
If ReportGeneralDetails/ActivityIndicator is TRUE (Yes) and ReportGeneralDetails/
SubAccountIndicator is FALSE (NO), then Balances/BalanceForAccount must be present and
Balances/SubAccountDetails must be absent.
This constraint is defined at the MessageDefinition level.
C14 BalancePresenceRule
If ReportGeneralDetails/ActivityIndicator is TRUE (Yes), then Balances must be present. If
ReportGeneralDetails/ActivityIndicator is FALSE (No), then Balances must be absent.
This constraint is defined at the MessageDefinition level.
C15 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C16 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities 2751 August 2026
```

## File page 2752

```text
Note: The decimal separator is a dot.
C17 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C18 DescriptionUsageRule
Description must be used alone as the last resort.
C19 EligibleCollateralValueRule
EligibleCollateralValue is only to be used in (I)CSD-participant communication or if bilaterally
agreed between the sender and receiver.
C20 EligibleForCollateralPurposesRule
If Subbalance type is EligibleForCollateralPurposes, then QuantityAndAvailability cannot be
used.
C21 EligibleForCollateralPurposesRule
If Subbalance type is EligibleForCollateralPurposes, then QuantityAndAvailability cannot be
used.
C22 FinancialInstrumentAttributesRule
If InvestmentFundsFinancialInstrumentAttributes is present, then FinancialInstrumentAttributes
is not allowed.
C23 HoldingAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if HoldingAdditionnalDetails is
present, then it must not contain information that can be provided in a structured field.
C24 IdentificationNationalityOfInvestorRule
Identification and/or Nationality must be present.
C25 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C26 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C27 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C28 PlaceOfListingRule
If PlaceOfListing is used and a ISO 10383 MIC exists for the market to be identified, the ISO
10383 Market Identifier Code (MIC) must be used.
C29 PledgeeTypeAndIdentificationOrLEIRule
PledgeeTypeAndIdentification must be present or LEI must be present.
C30 ReportNumberRule
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities 2752 August 2026
```

