---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.3 Constraints"]
file_pages: [375, 376, 377, 378, 379, 380, 381, 382, 383, 384]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.3 Constraints

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 375 to 384.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 375

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     PartyContactNarrative <PtyCtctNrrtv> [0..1]  533
       AdditionalInformation <AddtlInf> [1..*] Text 533
     RegistrationDetails <RegnDtls> [0..1]  533
       AdditionalInformation <AddtlInf> [1..*] Text 533
     BasketOrIndexInformation <BsktOrIndxInf> [0..1]  533
       AdditionalInformation <AddtlInf> [1..*] Text 534
     CertificationBreakdown <CertfctnBrkdwn> [0..1]  534
       AdditionalInformation <AddtlInf> [1..*] Text 534
     ProcessingTextForNextIntermediary <PrcgTxtForNxtIntrmy> [0..1]  534
       AdditionalInformation <AddtlInf> [1..*] Text 534
   IssuerAgent <IssrAgt> [0..*] ± 535
   PayingAgent <PngAgt> [0..*] ± 535
   SubPayingAgent <SubPngAgt> [0..*] ± 535
   Registrar <Regar> [0..1] ± 536
   ResellingAgent <RsellngAgt> [0..*] ± 536
   PhysicalSecuritiesAgent <PhysSctiesAgt> [0..1] ± 536
   DropAgent <DrpAgt> [0..1] ± 536
   SolicitationAgent <SlctnAgt> [0..*] ± 537
   InformationAgent <InfAgt> [0..1] ± 537
   Issuer <Issr> [0..1] ± 537
   Offeror <Offerr> [0..*] ± 538
   TransferAgent <TrfAgt> [0..1] ± 538
   SupplementaryData <SplmtryData> [0..*] ± C79 538
7.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 375 February 2026
```

## File page 376

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AdditionalInformationRule
The AdditionalInformation field in all elements must not contain information that can be
provided in a structured field unless bilaterally agreed or advised differently in the element
definition as in NarrativeVersion.
C4 AdditionalInformationRule
The AdditionalInformation field in all elements must not contain information that can be
provided in a structured field unless bilaterally agreed or advised differently in the element
definition as in NarrativeVersion.
C5 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C6 AdditionalTextRule
If OptionType/Code is OTHR (Other), then AdditionalInformation/AdditionalText/
AdditionalInformation must be present.
(MT564 NVR C5).
C7 AffectedAndUnaffectedBalanceRule
UnaffectedBalance and AffectedBalance should only be mentioned as a result of the process
that was run through the event. For instance lottery results, Dutch auction results or tender offer
results.
C8 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C9 AppliedOptionRule
If CorporateActionMovementDetails/AppliedOptionIndicator value is 'true' or '1' (Yes) in one or
more occurrences of CorporateActionMovementDetails, then
CorporateActionGeneralInformation/MandatoryVoluntaryEventType/Code value must be CHOS
(MandatoryWithOptions) and at least one of the CorporateActionDetails/
AdditionalBusinessProcessIndicator/Code values must be REAC (RequiredAction).
This constraint is defined at the MessageDefinition level.
C10 AppliedOptionRule
If DefaultProcessingOrStandingInstruction/DefaultOptionIndicator is present and its value is '1'
or 'true' (Yes), then AppliedOptionIndicator value must not be '1' or 'true' (Yes).
C11 BeneficialOwnerBreakdownRequestRule
If in at least one occurrence of CorporateActionMovementDetails, OptionType/Code value is
BOBD (BeneficialOwnerBreakdownRequest), then CorporateActionGeneralInformation/
EventType/Code value must be WTRC (Withholding Tax Relief Certification).
(MT 564 NVR C23).
On Condition
    /CorporateActionMovementDetails[*]/OptionType/Code is equal to value 
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 376 February 2026
```

## File page 377

```text
'BeneficialOwnerBreakdownRequest'
Following Must be True
    /CorporateActionGeneralInformation/EventType/Code Must be equal to value 
'WithholdingTaxReliefCertification'
This constraint is defined at the MessageDefinition level.
C12 BeneficialOwnerBreakdownRequestUGRule
If in at least one occurrence of CorporateActionOptionDetails, OptionType/Code value is BOBD
(BeneficialOwnerBreakdownRequest), then CorporateActionGeneralInformation/EventType/
Code value must be WTRC (Withholding Tax Relief Certification).
(MT 564 NVR C23).
if 
    at least one occurrence of [CorporateActionMovementDetails/OptionType/
Code] has value included in the following list 'BOBD' 
, then 
    every occurrence of [CorporateActionGeneralInformation/EventType/Code] 
must have value included in the following list 'WTRC' 
Expression Language: UGRule
This constraint is defined at the MessageDefinition level.
C13 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C14 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C15 DeemedRate1Rule
If DeemedRate is repeated, then DeemedRate/RateTypeAndAmountAndRateStatus/RateType/
Code values and DeemedRate/RateTypeAndRate/RateType/Code values must all be different
in each occurrence of DeemedRate.
(MT 564 NVR C8).
C16 DeemedRate2Rule
Only a single occurrence of either DeemedRate/Amount or DeemedRate/Rate or DeemedRate/
NotSpecifiedRate may be present, only one of these elements may be present.
(MT 564 NVR C7).
C17 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C18 DescriptionUsageRule
Description must be used alone as the last resort.
C19 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 377 February 2026
```

## File page 378

```text
C20 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C21 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C22 DissenterRights1Rule
If OfferType/Code value is equal to DISS (DissenterRights), then OfferType/Code value equal
to NDIS (DissenterRightsNotApplicable) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
C23 DissenterRights1UGRule
If OfferType/Code value is equal to DISS (DissenterRights), then OfferType/Code value equal
to NDIS (DissenterRightsNotApplicable) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
Expression Language: UGRule
C24 DissenterRights2Rule
If OfferType/Code value is equal to NDISS (DissenterRightsNotApplicable), then OfferType/
Code value equal to DISS (DissenterRights) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
C25 DissenterRights2UGRule
If OfferType/Code value is equal to NDIS (DissenterRightsNotApplicable), then OfferType/Code
value equal to DISS (DissenterRights) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
Expression Language: UGRule
C26 EventTypeRule
If Code is present, the code OTHR (Other) must only be used in case no other corporate action
event code is appropriate.
If Code is present, the code CHAN (Change) must only be used in case no other corporate
action event code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM (Final Maturity) must only be used when the redemption is
decided by the issuer and not by the securities holders.
C27 ExemptionTypeUsageRule
The lists of exemption type codes to be used in ExemptionType are provided in the document
"ETYP-ITYP Exemption & Income Type Codes" available on the SMPG website at
www.smpg.info.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 378 February 2026
```

## File page 379

```text
C28 ExemptionTypeUsageRule
The lists of exemption type codes to be used in ExemptionType are provided in the document
"ETYP-ITYP Exemption & Income Type Codes" available on the SMPG website at
www.smpg.info.
C29 GenericCashPricePerProductGuideline
GenericCashPriceReceivedPerProduct and GenericCashPricePaidPerProduct are prices
received or paid in the course of an event. The specific meaning (redemption price, subscription
price, reinvestment price, etc.) is derived from the event type.
C30 GenericCashPricePerProductGuideline
GenericCashPriceReceivedPerProduct and GenericCashPricePaidPerProduct are prices
received or paid in the course of an event. The specific meaning (redemption price, subscription
price, reinvestment price, ETC.) is derived from the event type.
C31 GrossDistributionRate2Rule
If GrossDistributionRate is repeated, then:
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of GrossDistributionRate.
(MT 564 NVR C8).
C32 GrossDistributionRate2Rule
If GrossDDistributionRate is repeated, then:
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of GrossDistributionRate. (MT 564 NVR C8).
C33 GrossDistributionRate3Rule
Only a single occurrence of either GrossDistributionRate/Amount or GrossDistributionRate/
AmountAndRateStatus or GrossDistributionRate/NotSpecifiedRate may be present, only one of
these elements may be present. (MT 564 NVR C7).
C34 GrossDistributionRate3Rule
Only a single occurrence of either GrossDistributionRate/Amount or
GrossGrossDistributionRate/AmountAndRateStatus or GrossGrossDistributionRate/
NotSpecifiedRate may be present, and only one of these elements may be present.
(MT 564 NVR C7).
C35 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C36 IncentivePremiumEventType1Rule
If Code value is equal to INCP (IncentivePremiumPayment) in CorporateActionDetails/
AdditionalBusinessProcessIndicator, then CorporateActionGeneralInformation/EventType/Code
value must be equal to CONS (Consent).
(MT 564 NVR C26)
On Condition
    /CorporateActionDetails/AdditionalBusinessProcessIndicator[*]/Code is 
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 379 February 2026
```

## File page 380

```text
equal to value 'IncentivePremiumPayment'
Following Must be True
    /CorporateActionGeneralInformation/EventType/Code Must be equal to value 
'Consent'
This constraint is defined at the MessageDefinition level.
C37 IncentivePremiumEventTypeUG1Rule
If Code value is equal to INCP (IncentivePremiumPayment) in any occurrence of
CorporateActionDetails/AdditionalBusinessProcessIndicator, then
CorporateActionGeneralInformation/EventType/Code value must be equal to CONS (Consent).
(MT 564 NVR C26)
if 
    at least one occurrence of [CorporateActionDetails/
AdditionalBusinessProcessIndicator/Code] has value included in the following 
list 'INCP' 
, then 
    every occurrence of [CorporateActionGeneralInformation/EventType/Code] 
must have value included in the following list 'CONS' 
Expression Language: UGRule
This constraint is defined at the MessageDefinition level.
C38 IncomeType1Rule
If at least one occurrence of OtherIncomeType is present, then IncomeType must be present.
C39 IncomeType2Rule
If at least one occurrence of OtherIncomeType is present, then IncomeType must be present.
C40 IncomeTypeUsageRule
The lists of income type codes to be used in IncomeType are provided in the document "ETYP-
ITYP Exemption & Income Type Codes" available on the SMPG website at www.smpg.info.
C41 IncomeTypeUsageRule
The lists of income type codes to be used in IncomeType are provided in the document "ETYP-
ITYP Exemption & Income Type Codes" available on the SMPG website at www.smpg.info.
C42 InstructCashAmountRule
If OptionFeatures/Code QCAS (InstructCashAmount) is not present, then any message
elements in the list (PriceDetails/MaximumCashToInstruct, PriceDetails/
MinimumCashToInstruct, PriceDetails/MinimumMutipleCashToInstruct) must not be present.
(MT564 NVR C20).
C43 IntermediateSecuritiesDistributionRule
If CorporateActionGeneralInformation/EventType/Code is RHDI
(IntermediateSecuritiesDistribution), then CorporateActionDetails/
IntermediateSecuritiesDistributionType must be present.
(MT 564 NVR C11).
On Condition
    /CorporateActionGeneralInformation/EventType/Code is equal to value 
'IntermediateSecuritiesDistribution'
Following Must be True
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 380 February 2026
```

## File page 381

```text
    /CorporateActionDetails Must be present
 And    /CorporateActionDetails/FollowingEventTypeIndicator Must be present
This constraint is defined at the MessageDefinition level.
C44 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C45 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C46 IssuerOfferorTaxabilityIndicatorUsageRule
The IssuerOfferorTaxabilityIndicator may only be used when no tax rate is provided in the
message and it must not be used in events such as dividend or interest.
The list of proprietary IssuerOfferorTaxabilityIndicator codes that may be used are provided in
the document " TXAP Taxability Codes" available on the SMPG website at www.smpg.info.
C47 IssuerOfferorTaxabilityIndicatorUsageRule
The IssuerOfferorTaxabilityIndicator may only be used when no tax rate is provided in the
message and it must not be used in events such as dividend or interest.
The list of proprietary IssuerOfferorTaxabilityIndicator codes that may be used are provided in
the document " TXAP Taxability Codes" available on the SMPG website at www.smpg.info.
C48 MaturityDateRule
Maturity date may only provide generic information about the final maturity of the underlying
instrument.
C49 MaturityDateRule
Maturity date may only provide generic information about the final maturity of the underlying
instrument.
C50 NetDistributionRate1Rule
If NetDistributionRate is repeated, then RateTypeAndAmountAndRateStatus/RateType/Code
values must all be different in each occurrence of NetDistributionRate. (MT 564 NVR C8).
C51 NetDistributionRate1Rule
If NetDistributionRate is repeated, then:
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of NetDistributionRate. (MT 564 NVR C8).
C52 NetDistributionRate2Rule
Only a single occurrence of either NetDistributionRate/Amount or NetDistributionRate/
AmountAndRateStatus or NetDistributionRate/NotSpecifiedRate may be present, and only one
of these elements may be present. (MT 564 NVR C7).
C53 NetDistributionRate2Rule
Only a single occurrence of either NetDistributionRate/Amount or NetDistributionRate/
AmountAndRateStatus or NetDistributionRate/NotSpecifiedRate may be present, and only one
of these elements may be present.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 381 February 2026
```

## File page 382

```text
(MT 564 NVR C7).
C54 OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the structure and usage of the Official Corporate Action Event Reference
(COAF). Those recommendations are
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
C55 OptionNumberGuideline
For differentiation between options, it is recommended to use the OptionNumber rather than the
OptionType, for example, in the case where two or more offers can be described by the same
corporate action option code.
C56 OtherEventRule
If CorporateActionGeneralInformation/EventType/Code is OTHR (Other), then at least one
occurrence of AdditionalInformation/AdditionalText/AdditionalInformation must be present.
(MT564 NVR C4).
On Condition
    /CorporateActionGeneralInformation/EventType/Code is present
 And    /CorporateActionGeneralInformation/EventType/Code is equal to value 
'OtherEvent'
Following Must be True
    /AdditionalInformation Must be present
 And    /AdditionalInformation/AdditionalText Must be present
 And    /AdditionalInformation/AdditionalText/AdditionalInformation[1] Must 
be present
This constraint is defined at the MessageDefinition level.
C57 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C58 PaginationRule
If pagination is present, then MovementPreliminaryAdviceGeneralInformation/
MovementPreliminaryAdviceIdentification must be present.
On Condition
    /Pagination is present
Following Must be True
    /MovementPreliminaryAdviceGeneralInformation/
MovementPreliminaryAdviceIdentification Must be present
This constraint is defined at the MessageDefinition level.
C59 PreviousMovementPreliminaryAdviceIdentification1Rule
If MovementPreliminaryAdiceGeneralInformation/Type is REPL (Replace) and Pagination/
PageNumber is equal to value 1, then PreviousMovementPreliminaryAdviceIdentification must
be present.
(MT 564 NVR C9).
On Condition
    /MovementPreliminaryAdviceGeneralInformation/Type is equal to value 
'Replacement'
 And    /Pagination/PageNumber is equal to value '1'
Following Must be True
    /PreviousMovementPreliminaryAdviceIdentification Must be present
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 382 February 2026
```

## File page 383

```text
This constraint is defined at the MessageDefinition level.
C60 PreviousNextFactorRule
In case of partial redemption by pool factor, PreviousFactor provides the factor applicable
before redemption and NextFactor provides the factor applicable after redemption.
C61 PreviousNextFactorRule
In case of partial redemption by pool factor, PreviousFactor provides the factor applicable
before redemption and NextFactor provides the factor applicable after redemption.
C62 RateAndCorporateActionEventRule
If CorporateActionMovementDetails/RateAndAmountDetails/GrossDistributionRate/
NotSpecifiedRate Code value or CorporateActionMovementDetails/RateAndAmountDetails/
GrossInterestRateUsedForPayment/NotSpecifiedRate Code value is NILP (Nil Payment), then
CorporateActionGeneralInformation/EventType/Code must be either DVCA (CashDividend) or
INTR (InterestPayment).
If CorporateActionMovementDetails/CashMovementDetails/RateAndAmountDetails/
GrossDistributionRate/NotSpecifiedRate Code value or CorporateActionMovementDetails/
CashMovementDetails/RateAndAmountDetails/GrossInterestRateUsedForPayment/
NotSpecifiedRate Code value is NILP (Nil Payment), then CorporateActionGeneralInformation/
EventType/Code must be either DVCA (CashDividend) or INTR (InterestPayment).
This constraint is defined at the MessageDefinition level.
C63 RateStatusGuideline
The code value ACTU is the default value for a rate status.
C64 ReversalReasonRule
If CorporateActionDetails/AdditionalBusinessProcessIndicator/Code value is equal to REVR
(ReversalReason), then
ReversalReason must be present and MovementPreliminaryAdviceGeneralInformation/
Function code value is equal to CAPA (PreadviceOfMovement).
if 
    at least one occurrence of [CorporateActionDetails/
AdditionalBusinessProcessIndicator/Code] has value included in the following 
list 'REVR' 
, then 
    at least one occurrence of the following element(s) [ReversalReason] must 
be present 
    and at least one occurrence of 
[MovementPreliminaryAdviceGeneralInformation/Function] must have value 
included in the following list 'CAPA' 
Expression Language: UGRule
This constraint is defined at the MessageDefinition level.
C65 RevocabilityPeriodRule
If WithdrawalAllowedIndicator or ChangeAllowedIndicator is present and is 'true' or '1' (Yes),
then PeriodDetails/RevocabilityPeriod must be present to indicate the period during which the
change or withdrawal of instruction is allowed.
C66 SafekeepingAccount1Rule
If AccountDetails/ForAllAccounts/IdentificationCode value is GENR (General), then any
element in the list (MinimumNominalQuantity,
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 383 February 2026
```

## File page 384

```text
MinimumExercisableQuantity,MinimumExercisableMultipleQuantity, ContractSize) must not be
present in any occurrences of CorporateActionMovementDetails/SecuritiesMovementDetails/
SecurityDetails;
(MT564 Rule C2 - part 1).
On Condition
    /AccountDetails/ForAllAccounts is present
 And    /AccountDetails/ForAllAccounts/IdentificationCode is equal to value 
'General'
Following Must be True
    /CorporateActionMovementDetails[*]/SecuritiesMovementDetails[*]/
SecurityDetails/MinimumNominalQuantity Must be absent
 And    /CorporateActionMovementDetails[*]/SecuritiesMovementDetails[*]/
SecurityDetails/MinimumQuantityToInstruct Must be absent
 And    /CorporateActionMovementDetails[*]/SecuritiesMovementDetails[*]/
SecurityDetails/MinimumMultipleQuantityToInstruct Must be absent
 And    /CorporateActionMovementDetails[*]/SecuritiesMovementDetails[*]/
SecurityDetails/ContractSize Must be absent
This constraint is defined at the MessageDefinition level.
C67 SafekeepingAccount2Rule
If AccountDetails/ForAllAccounts/IdentificationCode value is GENR (General), then
AmountDetails must not be present in any occurrences of CorporateActionMovementDetails/
CashMovementDetails.
(MT564 Rule C2 - part 2).
On Condition
    /AccountDetails/ForAllAccounts is present
 And    /AccountDetails/ForAllAccounts/IdentificationCode is equal to value 
'General'
Following Must be True
    /CorporateActionMovementDetails[*]/CashMovementDetails[*]/AmountDetails 
Must be absent
This constraint is defined at the MessageDefinition level.
C68 SafekeepingAccountOrBlockChainAddress1Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C69 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present then SafekeepingAccount must be absent.
C70 SafekeepingAccountOrBlockChainAddress3Rule
If SafekeepingAccount is present, then BlockChainAddressOrWallet must be absent.
C71 SafekeepingPlaceRule
The SafekeepingPlace is only to be used by global custodians that allow their clients to specify
where the securities are to be held, for example, in an ICSD account versus an account at the
local CSD.
C72 SecondLevelTax1Rule
If SecondLevelTax is repeated, then SecondLevelTax/RateTypeAndRate/RateType/Code
values must all be different in each occurrence of SecondLevelTax.
(MT 564 NVR C8).
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 384 February 2026
```

