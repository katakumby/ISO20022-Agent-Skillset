---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: []
file_pages: [53, 54, 55, 56, 57, 58, 59]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# Continuation at file page 53

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 53 to 59.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 53

```text
Following Must be True
    /CorporateActionDetails/PriceDetails/LastBidIncrementPrice Must be absent
This constraint is defined at the MessageDefinition level.
C68 LastBidIncrementPriceEventType1Rule
If LastBidIncrementPrice is present in CorporateActionDetails/PriceDetails, then
CorporateActionGeneralInformation/EventType/Code value must be equal to either BIDS
(Repurchase Offer) or DTCH (Dutch Auction) or TEND (Tender).
(MT 564 NVR C30)
On Condition
    /CorporateActionDetails/PriceDetails/LastBidIncrementPrice is present
Following Must be True
    /CorporateActionGeneralInformation/EventType/Code Must be equal to value 
'RepurchaseOffer'
 Or    /CorporateActionGeneralInformation/EventType/Code Must be equal to 
value 'DutchAuction'
 Or    /CorporateActionGeneralInformation/EventType/Code Must be equal to 
value 'Tender'
This constraint is defined at the MessageDefinition level.
C69 LastBidIncrementPriceEventType2Rule
If LastBidIncrementPrice is present in any occurrence of CorporateActionOptionDetails/
PriceDetails, then CorporateActionGeneralInformation/EventType/Code value must be equal to
either BIDS (Repurchase Offer) or DTCH (Dutch Auction) or TEND (Tender).
(MT 564 NVR C30)
On Condition
    /CorporateActionOptionDetails[*]/PriceDetails/LastBidIncrementPrice is 
present
Following Must be True
    /CorporateActionGeneralInformation/EventType/Code Must be equal to value 
'RepurchaseOffer'
 Or    /CorporateActionGeneralInformation/EventType/Code Must be equal to 
value 'DutchAuction'
 Or    /CorporateActionGeneralInformation/EventType/Code Must be equal to 
value 'Tender'
This constraint is defined at the MessageDefinition level.
C70 MaturityDateRule
Maturity date may only provide generic information about the final maturity of the underlying
instrument.
C71 MaturityDateRule
Maturity date may only provide generic information about the final maturity of the underlying
instrument.
C72 MaximumAndMinimumQuantitySoughtUsageRule
When MaximumQuantity is present, MinimumQuantitySought must be present too. When
MinimumQuantitySought is present, MaximumQuantity must be present too.
When MinimumQuantitySought/Code is AnyAndAll, then MaximumQuantity/Code must not be
AnyAndAll.
When MaximumQuantity/Code is AnyAndAll, MinimumQuantitySought/code must not be used
with the value AnyAndAll.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 53 February 2026
```

## File page 54

```text
C73 MaximumPrice1Rule
If MaximumPrice is present in CorporateActionDetails/PriceDetails, then MaximumPrice is not
allowed in any occurences of CorporateActionOptionDetails/PriceDetails.
(MT 564 NVR C24)
On Condition
    /CorporateActionDetails/PriceDetails/MaximumPrice is present
Following Must be True
    /CorporateActionOptionDetails[*]/PriceDetails/MaximumPrice Must be absent
This constraint is defined at the MessageDefinition level.
C74 MaximumPrice2Rule
If MaximumPrice is present in any occurrences of CorporateActionOptionDetails/PriceDetails,
then MaximumPrice is not allowed in CorporateActionDetails/PriceDetails.
(MT 564 NVR C24)
On Condition
    /CorporateActionOptionDetails[*]/PriceDetails/MaximumPrice is present
Following Must be True
    /CorporateActionDetails/PriceDetails/MaximumPrice Must be absent
This constraint is defined at the MessageDefinition level.
C75 MinimumPrice1Rule
If MinimumPrice is present in CorporateActionDetails/PriceDetails, then MinimumPrice is not
allowed in any occurences of CorporateActionOptionDetails/PriceDetails.
(MT 564 NVR C24)
On Condition
    /CorporateActionDetails/PriceDetails/MinimumPrice is present
Following Must be True
    /CorporateActionOptionDetails[*]/PriceDetails/MinimumPrice Must be absent
This constraint is defined at the MessageDefinition level.
C76 MinimumPrice2Rule
If MinimumPrice is present in any occurrences of CorporateActionOptionDetails/PriceDetails,
then MinimumPrice is not allowed in CorporateActionDetails/PriceDetails.
(MT 564 NVR C24)
On Condition
    /CorporateActionOptionDetails[*]/PriceDetails/MinimumPrice is present
Following Must be True
    /CorporateActionDetails/PriceDetails/MinimumPrice Must be absent
This constraint is defined at the MessageDefinition level.
C77 NameChangeRule
If CorporateActionDetails/AdditionalInformation/NewCompanyName/AdditionalInformation is
present, then CorporateActionGeneralInformation/EventType/Code value CHAN (Change) must
be present and CorporateActionDetails/ChangeType/Code value NAME (Name) must be
present in at least one occurrence of CorporateActionDetails/ChangeType.
(MT 564 NVR C10).
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 54 February 2026
```

## File page 55

```text
C78 NetDistributionRate1Rule
If NetDistributionRate is repeated, then RateTypeAndAmountAndRateStatus/RateType/Code
values must all be different in each occurrence of NetDistributionRate. (MT 564 NVR C8).
C79 NetDistributionRate1Rule
If NetDistributionRate is repeated, then:
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of NetDistributionRate. (MT 564 NVR C8).
C80 NetDistributionRate2Rule
Only a single occurrence of either NetDistributionRate/Amount or NetDistributionRate/
AmountAndRateStatus or NetDistributionRate/NotSpecifiedRate may be present, and only one
of these elements may be present. (MT 564 NVR C7).
C81 NetDistributionRate2Rule
Only a single occurrence of either NetDistributionRate/Amount or NetDistributionRate/
AmountAndRateStatus or NetDistributionRate/NotSpecifiedRate may be present, and only one
of these elements may be present.
(MT 564 NVR C7).
C82 NewMaturityDateRule
If CorporateActionDetails/DateDetails/NewMaturityDate is present, then
CorporateActionGeneralInformation/EventType/Code must be EXTM (Maturity Extension).
This constraint is defined at the MessageDefinition level.
C83 NotificationIdentification1Rule
If NotificationGeneralInformation/NotificationType is REPL (Replacement) and Pagination/
PageNumber is equal to value 1, then PreviousNotificationIdentification must be present.
(MT 564 NVR C9).
On Condition
    /NotificationGeneralInformation/NotificationType is equal to value 
'Replacement'
 And    /Pagination/PageNumber is equal to value '1'
Following Must be True
    /PreviousNotificationIdentification Must be present
This constraint is defined at the MessageDefinition level.
C84 NotificationIdentification2Rule
If NotificationGeneralInformation/NotificationType is RMDR (Reminder) and Pagination/
PageNumber is equal to value 1, then PreviousNotificationIdentification must be present.
(MT 564 NVR C9).
On Condition
    /NotificationGeneralInformation/NotificationType is equal to value 
'Reminder'
 And    /Pagination/PageNumber is equal to value '1'
Following Must be True
    /PreviousNotificationIdentification Must be present
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 55 February 2026
```

## File page 56

```text
C85 NotificationTypeGuideline
NotificationType REPL is used to replace a previously sent CorporateActionNotification
message that was reported with EventCompletenessStatus being incomplete or complete.
C86 NumberRule
If Number is negative, then Sign must be present.
C87 OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the structure and usage of the Official Corporate Action Event Reference
(COAF). These recommendations are
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
C88 OptionNumberGuideline
For differentiation between options, it is recommended to use the OptionNumber rather than the
OptionType, for example, in the case where two or more offers can be described by the same
corporate action option code.
C89 OptionTypeUnknownProceedsUsageRule
When used, the corporate action option code PRUN (Unknown Proceeds) should be
maintained throughout the full lifecycle of the event.
C90 OtherEventRule
If CorporateActionGeneralInformation/EventType/Code is OTHR (Other) then at least one
occurrence of AdditionalInformation/AdditionalText/AdditionalInformation must be present.
(MT564 NVR C4).
On Condition
    /CorporateActionGeneralInformation/EventType/Code is present
 And    /CorporateActionGeneralInformation/EventType/Code is equal to value 
'OtherEvent'
Following Must be True
    /AdditionalInformation Must be present
 And    /AdditionalInformation/AdditionalText[*] Must be present
 And    /AdditionalInformation/AdditionalText[*]/AdditionalInformation[*] 
Must be present
This constraint is defined at the MessageDefinition level.
C91 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C92 PaginationRule
If pagination is present, then NotificationGeneralInformation/NotificationIdentification must be
present.
On Condition
    /Pagination is present
Following Must be True
    /NotificationGeneralInformation/NotificationIdentification Must be present
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 56 February 2026
```

## File page 57

```text
C93 PaymentDateRule
If at least one occurrence of CorporateActionOptionDetails/SecuritiesMovementDetails or at
least one occurrence of CorporateActionOptionDetails/CashMovementDetails is present, then
CorporateActionDetails/DateDetails/PaymentDate must be absent. (MT 564 NVR C16).
On Condition
    /CorporateActionOptionDetails[*]/CashMovementDetails[*] is present
 Or    /CorporateActionOptionDetails[*]/SecuritiesMovementDetails[*] is 
present
Following Must be True
    /CorporateActionDetails/DateDetails/PaymentDate Must be absent
This constraint is defined at the MessageDefinition level.
C94 PreviousNextFactorRule
In case of partial redemption by pool factor, PreviousFactor provides the factor applicable
before redemption and NextFactor provides the factor applicable after redemption.
C95 PreviousNextFactorRule
In case of partial redemption by pool factor, PreviousFactor provides the factor applicable
before redemption and NextFactor provides the factor applicable after redemption.
C96 RateAndCorporateActionEventRule
If CorporateActionOptionDetails/RateAndAmountDetails/GrossDistributionRate/
NotSpecifiedRate Code value or CorporateActionOptionDetails/RateAndAmountDetails/
GrossInterestRateUsedForPayment/NotSpecifiedRate Code value is NILP (Nil Payment), then
CorporateActionGeneralInformation/EventType/Code must be either DVCA (CashDividend) or
INTR (InterestPayment).
If CorporateActionOptionDetails/CashMovementDetails/RateAndAmountDetails/
GrossDistributionRate/NotSpecifiedRate Code value or CorporateActionOptionDetails/
CashMovementDetails/RateAndAmountDetails/GrossInterestRateUsedForPayment/
NotSpecifiedRate Code value is NILP (Nil Payment), then CorporateActionGeneralInformation/
EventType/Code must be either DVCA (CashDividend) or INTR (InterestPayment).
This constraint is defined at the MessageDefinition level.
C97 RateStatusGuideline
The code value ACTU is the default value for a rate status.
C98 RevocabilityPeriodRule
If WithdrawalAllowedIndicator or ChangeAllowedIndicator is present and is 'true' or '1' (Yes),
then PeriodDetails/RevocabilityPeriod must be present to indicate the period during which the
change or withdrawal of instruction is allowed.
C99 SafekeepingAccount1Rule
If AccountDetails/ForAllAccounts/IdentificationCode value is GENR (General) then any element
in the list (MinimumNominalQuantity,
MinimumExercisableQuantity,MinimumExercisableMultipleQuantity, ContractSize) must not be
present in any occurrences of CorporateActionOptionDetails/SecuritiesMovementDetails/
SecurityDetails;
(MT564 Rule C2 - part 1).
On Condition
    /AccountDetails/ForAllAccounts is present
 And    /AccountDetails/ForAllAccounts/IdentificationCode is equal to value 
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 57 February 2026
```

## File page 58

```text
'General'
Following Must be True
    /CorporateActionOptionDetails[*]/SecuritiesMovementDetails[*]/
SecurityDetails/MinimumNominalQuantity Must be absent
 And    /CorporateActionOptionDetails[*]/SecuritiesMovementDetails[*]/
SecurityDetails/MinimumQuantityToInstruct Must be absent
 And    /CorporateActionOptionDetails[*]/SecuritiesMovementDetails[*]/
SecurityDetails/MinimumMultipleQuantityToInstruct Must be absent
 And    /CorporateActionOptionDetails[*]/SecuritiesMovementDetails[*]/
SecurityDetails/ContractSize Must be absent
This constraint is defined at the MessageDefinition level.
C100 SafekeepingAccount2Rule
If AccountDetails/ForAllAccounts/IdentificationCode value is GENR (General) then
AmountDetails must not be present in any occurrences of CorporateActionOptionDetails/
CashMovementDetails.
(MT564 Rule C2 - part 2).
On Condition
    /AccountDetails/ForAllAccounts is present
 And    /AccountDetails/ForAllAccounts/IdentificationCode is equal to value 
'General'
Following Must be True
    /CorporateActionOptionDetails[*]/CashMovementDetails[*]/AmountDetails 
Must be absent
This constraint is defined at the MessageDefinition level.
C101 SafekeepingAccountOrBlockChainAddress1Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C102 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present then SafekeepingAccount must be absent.
C103 SafekeepingAccountOrBlockChainAddress3Rule
If SafekeepingAccount is present, then BlockChainAddressOrWallet must be absent.
C104 SafekeepingPlaceRule
The SafekeepingPlace is only to be used by global custodians that allow their clients to specify
where the securities are to be held, for example, in an ICSD account versus an account at the
local CSD.
C105 SecondLevelTax1Rule
If SecondLevelTax is repeated, then SecondLevelTax/RateTypeAndRate/RateType/Code
values must all be different in each occurrence of SecondLevelTax.
(MT 564 NVR C8).
C106 SecondLevelTax1Rule
If SecondLevelTax is repeated, then SecondLevelTax/RateTypeAndRate/RateType/Code
values must all be different in each occurrence of SecondLevelTax.
(MT 564 NVR C8).
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 58 February 2026
```

## File page 59

```text
C107 SecondLevelTax2Rule
Only a single occurrence of either SecondLevelTax/Amount or SecondLevelTax/Rate or
SecondLevelTax/NotSpecifiedRate may be present, only one of these elements may be
present.
(MT 564 NVR C7).
C108 SecondLevelTax2Rule
Only a single occurrence of either SecondLevelTax/Amount or SecondLevelTax/Rate or
SecondLevelTax/NotSpecifiedRate may be present, only one of these elements may be
present.
(MT 564 NVR C7).
C109 SecondLevelTax3Rule
If at least one occurrence of SecondLevelTax is present, then at least one occurrence of
WithholdingTaxRate must be present. (MT 564 NVR C19).
C110 SecondLevelTax3Rule
If at least one occurrence of SecondLevelTax is present, then at least one occurrence of
WithholdingTaxRate must be present. (MT 564 NVR C19).
C111 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C112 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C113 TotalEligibleBalanceRule
If NotificationGeneralInformation/EligibleBalanceIndicator is 'true' or '1' (Yes), then at least one
occurrence of AccountDetails/AccountsListAndBalanceDetails must be present and
TotalEligibleBalance must be present in all occurrences of AccountDetails/
AccountsListAndBalanceDetails/Balance.
If NotificationGeneralInformation/EligibleBalanceIndicator is 'false' or '0' (No) or is not present,
then TotalEligibleBalance may or may not be present in all occurrences of AccountDetails/
AccountsListAndBalanceDetails/Balance but it will not necessarily be the final eligible balance
quantity.
This constraint is defined at the MessageDefinition level.
C114 WithholdingTaxRate1Rule
If WithholdingTaxRate is repeated, then WithholdingTaxRate/RateTypeAndRate/RateType/
Code values must all be different in each occurrence of WithholdingTaxRate.
(MT 564 NVR C8).
C115 WithholdingTaxRate1Rule
If WithholdingTaxRate is repeated, then WithholdingTaxRate/RateTypeAndRate/RateType/
Code values must all be different in each occurrence of WithholdingTaxRate.
(MT 564 NVR C8).
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 59 February 2026
```

