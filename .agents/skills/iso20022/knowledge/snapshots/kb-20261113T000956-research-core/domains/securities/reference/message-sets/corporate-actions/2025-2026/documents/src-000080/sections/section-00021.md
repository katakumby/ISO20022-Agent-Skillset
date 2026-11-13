---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.3 Constraints"]
file_pages: [43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.3 Constraints

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 43 to 52.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 43

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     ProcessingTextForNextIntermediary <PrcgTxtForNxtIntrmy> [0..*]  C7 260
       Language <Lang> [1..1] CodeSet 260
       AdditionalInformation <AddtlInf> [1..*] Text 261
   IssuerAgent <IssrAgt> [0..*] ± 0
   PayingAgent <PngAgt> [0..*] ± 261
   SubPayingAgent <SubPngAgt> [0..*] ± 0
   Registrar <Regar> [0..1] ± 262
   ResellingAgent <RsellngAgt> [0..*] ± 262
   PhysicalSecuritiesAgent <PhysSctiesAgt> [0..1] ± 262
   DropAgent <DrpAgt> [0..1] ± 0
   SolicitationAgent <SlctnAgt> [0..*] ± 263
   InformationAgent <InfAgt> [0..1] ± 0
   Issuer <Issr> [0..1] ± 0
   Offeror <Offerr> [0..*] ± 0
   TransferAgent <TrfAgt> [0..1] ± 0
   SupplementaryData <SplmtryData> [0..*] ± C112 265
3.3 Constraints
C1 AcceptancePriorityLevelUGRule
If OfferType/Code is equal to AcceptancePriority (ACPR), then AcceptancePriorityLevel must
be present.
Expression Language: UGRule
C2 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C3 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 43 February 2026
```

## File page 44

```text
C4 AdditionalInformationRule
The AdditionalInformation field in all elements must not contain information that can be
provided in a structured field unless bilaterally agreed or advised differently in the element
definition.
C5 AdditionalInformationRule
The AdditionalInformation field in all elements must not contain information that can be
provided in a structured field unless bilaterally agreed or advised differently in the element
definition as in NarrativeVersion.
C6 AdditionalInformationRule
The AdditionalInformation field in all elements must not contain information that can be
provided in a structured field unless bilaterally agreed or advised differently in the element
definition as in NarrativeVersion.
C7 AdditionalInformationRule
The Additionalnformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
C8 AdditionalTextRule
If OptionType/Code is OTHR (Other), then at least one occurrence of AdditionalInformation/
AdditionalText/AdditionalInformation must be present.
(MT564 NVR C5).
C9 AffectedAndUnaffectedBalanceRule
UnaffectedBalance and AffectedBalance should only be mentioned as a result of the process
that was run through the event. For instance lottery results, Dutch auction results or tender offer
results.
C10 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C11 AppliedOptionRule
If CorporateActionOptionDetails/AppliedOptionIndicator value is 'true' or '1' (Yes) in one or more
occurrences of CorporateActionOptionDetails, then CorporateActionGeneralInformation/
MandatoryVoluntaryEventType/Code value must be CHOS (MandatoryWithOptions) and at
least one of the CorporateActionDetails/AdditionalBusinessProcessIndicator/Code values must
be REAC (RequiredAction).
This constraint is defined at the MessageDefinition level.
C12 AppliedOptionRule
If DefaultProcessingOrStandingInstruction/DefaultOptionIndicator is present and its value is '1'
or 'true' (Yes), then AppliedOptionIndicator value must not be '1' or 'true' (Yes).
C13 BeneficialOwnerBreakdownRequestRule
If in at least one occurrence of CorporateActionOptionDetails, OptionType/Code value is BOBD
(BeneficialOwnerBreakdownRequest), then CorporateActionGeneralInformation/EventType/
Code value must be WTRC (Withholding Tax Relief Certification).
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 44 February 2026
```

## File page 45

```text
(MT 564 NVR C23).
On Condition
    /CorporateActionOptionDetails[*]/OptionType/Code is equal to value 
'BeneficialOwnerBreakdownRequest'
Following Must be True
    /CorporateActionGeneralInformation/EventType/Code Must be equal to value 
'WithholdingTaxReliefCertification'
This constraint is defined at the MessageDefinition level.
C14 BeneficialOwnerBreakdownRequestUGRule
If in at least one occurrence of CorporateActionOptionDetails, OptionType/Code value is BOBD
(BeneficialOwnerBreakdownRequest), then CorporateActionGeneralInformation/EventType/
Code value must be WTRC (Withholding Tax Relief Certification).
(MT 564 NVR C23).
if 
    at least one occurrence of [CorporateActionOptionDetails/OptionType/Code] 
has value included in the following list 'BOBD' 
, then 
    every occurrence of [CorporateActionGeneralInformation/EventType/Code] 
must have value included in the following list 'WTRC' 
Expression Language: UGRule
This constraint is defined at the MessageDefinition level.
C15 BidInterval1Rule
If BidInterval is present in CorporateActionDetails/RateAndAmountDetails, then BidInterval is
not allowed in any occurences of CorporateActionOptionDetails/RateAndAmountDetails.
(MT 564 NVR C25)
On Condition
    /CorporateActionDetails/RateAndAmountDetails/BidInterval is present
Following Must be True
    /CorporateActionOptionDetails[*]/RateAndAmountDetails/BidInterval Must be 
absent
This constraint is defined at the MessageDefinition level.
C16 BidInterval2Rule
If BidInterval is present in any occurrences of CorporateActionOptionDetails/
RateAndAmountDetails, then BidInterval is not allowed in CorporateActionDetails/
RateAndAmountDetails.
(MT 564 NVR C25)
On Condition
    /CorporateActionOptionDetails[*]/RateAndAmountDetails/BidInterval is 
present
Following Must be True
    /CorporateActionDetails/RateAndAmountDetails/BidInterval Must be absent
This constraint is defined at the MessageDefinition level.
C17 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 45 February 2026
```

## File page 46

```text
C18 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C19 DeclaredRateRule
If CorporateActionOptionDetails/RateAndAmountDetails/IssuerDeclaredExchangeRate is
present, then CorporateActionDetails/RateAndAmountDetails/DeclaredRate must be present.
On Condition
    /CorporateActionOptionDetails[*] is present
 And    /CorporateActionOptionDetails[*]/RateAndAmountDetails is present
 And    /CorporateActionOptionDetails[*]/RateAndAmountDetails/
IssuerDeclaredExchangeRate is present
Following Must be True
    /CorporateActionDetails/RateAndAmountDetails/DeclaredRate Must be present
This constraint is defined at the MessageDefinition level.
C20 DeclaredRateRule
DeclaredRate may only be used if the dividend or interest declared by the issuer is actually paid
in a different currency than the declared one or if the dividend or the interest event makes it
possible to elect amongst multiple currency options.
C21 DeemedRate1Rule
If DeemedRate is repeated, then DeemedRate/RateTypeAndAmountAndRateStatus/RateType/
Code values and DeemedRate/RateTypeAndRate/RateType/Code values must all be different
in each occurrence of DeemedRate.
(MT 564 NVR C8).
C22 DeemedRate2Rule
Only a single occurrence of either DeemedRate/Amount or DeemedRate/Rate or DeemedRate/
NotSpecifiedRate may be present, only one of these elements may be present.
(MT 564 NVR C7).
C23 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C24 DescriptionUsageRule
Description must be used alone as the last resort.
C25 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C26 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C27 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 46 February 2026
```

## File page 47

```text
C28 DissenterRights1Rule
If OfferType/Code value is equal to DISS (DissenterRights), then OfferType/Code value equal
to NDIS (DissenterRightsNotApplicable) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
C29 DissenterRights1UGRule
If OfferType/Code value is equal to DISS (DissenterRights), then OfferType/Code value equal
to NDIS (DissenterRightsNotApplicable) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
Expression Language: UGRule
C30 DissenterRights2Rule
If OfferType/Code value is equal to NDISS (DissenterRightsNotApplicable), then OfferType/
Code value equal to DISS (DissenterRights) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
C31 DissenterRights2UGRule
If OfferType/Code value is equal to NDIS (DissenterRightsNotApplicable), then OfferType/Code
value equal to DISS (DissenterRights) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
Expression Language: UGRule
C32 EffectiveDateRule
Effective date is to be used in events where there is no concept of entitlement, for example
Name Change (CHAN) or Place of Incorporation (PLAC), and in events where there is a sense
of eligibility but with a legal obligation, for example Merger (MRGR).
C33 EventTypeRule
If Code is present, the code OTHR (Other) must only be used if no other corporate action event
code is appropriate.
If Code is present, the code CHAN (Change) must only be used if no other corporate action
event code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM (Final Maturity) must only be used if the redemption is
decided by the issuer and not by the securities holders.
C34 ExemptionTypeUsageRule
The lists of exemption type codes to be used in ExemptionType are provided in the document
"ETYP-ITYP Exemption & Income Type Codes" available on the SMPG website at
www.smpg.info.
C35 ExemptionTypeUsageRule
The lists of exemption type codes to be used in ExemptionType are provided in the document
"ETYP-ITYP Exemption & Income Type Codes" available on the SMPG website at
www.smpg.info.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 47 February 2026
```

## File page 48

```text
C36 FirstBidIncrementPrice1Rule
If FirstBidIncrementPrice is present in CorporateActionDetails/PriceDetails, then
FirstBidIncrementPrice is not allowed in any occurences of CorporateActionOptionDetails/
PriceDetails.
(MT 564 NVR C24)
On Condition
    /CorporateActionDetails/PriceDetails/FirstBidIncrementPrice is present
Following Must be True
    /CorporateActionOptionDetails[*]/PriceDetails/FirstBidIncrementPrice Must 
be absent
This constraint is defined at the MessageDefinition level.
C37 FirstBidIncrementPrice2Rule
If FirstBidIncrementPrice is present in any occurrences of CorporateActionOptionDetails/
PriceDetails, then FirstBidIncrementPrice is not allowed in CorporateActionDetails/PriceDetails.
(MT 564 NVR C24)
On Condition
    /CorporateActionOptionDetails[*]/PriceDetails/FirstBidIncrementPrice is 
present
Following Must be True
    /CorporateActionDetails/PriceDetails/FirstBidIncrementPrice Must be absent
This constraint is defined at the MessageDefinition level.
C38 FirstBidIncrementPriceEventType1Rule
If FirstBidIncrementPrice is present in CorporateActionDetails/PriceDetails, then
CorporateActionGeneralInformation/EventType/Code value must be equal to either BIDS
(Repurchase Offer) or DTCH (Dutch Auction) or TEND (Tender).
(MT 564 NVR C30)
On Condition
    /CorporateActionDetails/PriceDetails/FirstBidIncrementPrice is present
Following Must be True
    /CorporateActionGeneralInformation/EventType/Code Must be equal to value 
'RepurchaseOffer'
 Or    /CorporateActionGeneralInformation/EventType/Code Must be equal to 
value 'DutchAuction'
 Or    /CorporateActionGeneralInformation/EventType/Code Must be equal to 
value 'Tender'
This constraint is defined at the MessageDefinition level.
C39 FirstBidIncrementPriceEventType2Rule
If FirstBidIncrementPrice is present in any occurrence of CorporateActionOptionDetails/
PriceDetails, then CorporateActionGeneralInformation/EventType/Code value must be equal to
either BIDS (Repurchase Offer) or DTCH (Dutch Auction) or TEND (Tender).
(MT 564 NVR C30)
On Condition
    /CorporateActionOptionDetails[*]/PriceDetails/FirstBidIncrementPrice is 
present
Following Must be True
    /CorporateActionGeneralInformation/EventType/Code Must be equal to value 
'RepurchaseOffer'
 Or    /CorporateActionGeneralInformation/EventType/Code Must be equal to 
value 'DutchAuction'
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 48 February 2026
```

## File page 49

```text
 Or    /CorporateActionGeneralInformation/EventType/Code Must be equal to 
value 'Tender'
This constraint is defined at the MessageDefinition level.
C40 GenericCashPricePerProductGuideline
GenericCashPriceReceivedPerProduct and GenericCashPricePaidPerProduct are prices
received or paid in the course of an event. The specific meaning (redemption price, subscription
price, reinvestment price, etc.) is derived from the event type.
C41 GenericCashPricePerProductGuideline
GenericCashPriceReceivedPerProduct and GenericCashPricePaidPerProduct are prices
received or paid in the course of an event. The specific meaning (redemption price, subscription
price, reinvestment price.) is derived from the event type.
C42 GenericCashPricePerProductGuideline
GenericCashPriceReceivedPerProduct and GenericCashPricePaidPerProduct are prices
received or paid in the course of an event. The specific meaning (redemption price, subscription
price, reinvestment price, ETC.) is derived from the event type.
C43 GrossDistributionRate2Rule
If GrossDistributionRate is repeated, then:
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of GrossDistributionRate. (MT 564 NVR C8).
C44 GrossDistributionRate2Rule
If GrossDistributionRate is repeated, then:
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of GrossDistributionRate. (MT 564 NVR C8).
C45 GrossDistributionRate3Rule
Only a single occurrence of either GrossDistributionRate/Amount or GrossDistributionRate/
AmountAndRateStatus or GrossDistributionRate/NotSpecifiedRate may be present, only one of
these elements may be present. (MT 564 NVR C7).
C46 GrossDistributionRate3Rule
Only a single occurrence of either GrossDistributionRate/Amount or GrossDistributionRate/
AmountAndRateStatus or GrossDistributionRate/NotSpecifiedRate may be present, and only
one of these elements may be present.
(MT 564 NVR C7).
C47 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C48 IncentivePremiumEventType1Rule
If Code value is equal to INCP (IncentivePremiumPayment) in any occurrence of
CorporateActionDetails/AdditionalBusinessProcessIndicator, then
CorporateActionGeneralInformation/EventType/Code value must be equal to CONS (Consent).
(MT 564 NVR C26)
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 49 February 2026
```

## File page 50

```text
On Condition
    /CorporateActionDetails/AdditionalBusinessProcessIndicator[*]/Code is 
equal to value 'IncentivePremiumPayment'
Following Must be True
    /CorporateActionGeneralInformation/EventType/Code Must be equal to value 
'Consent'
This constraint is defined at the MessageDefinition level.
C49 IncentivePremiumEventTypeUG1Rule
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
C50 IncomeType1Rule
If at least one occurrence of OtherIncomeType is present, then IncomeType must be present.
C51 IncomeType2Rule
If at least one occurrence of OtherIncomeType is present, then IncomeType must be present.
C52 IncomeTypeUsageRule
The lists of income type codes to be used in IncomeType are provided in the document "ETYP-
ITYP Exemption & Income Type Codes" available on the SMPG website at www.smpg.info.
C53 IncomeTypeUsageRule
The lists of income type codes to be used in IncomeType are provided in the document "ETYP-
ITYP Exemption & Income Type Codes" available on the SMPG website at www.smpg.info.
C54 InformationEventRule
If CorporateActionGeneralInformation/EventType/Code is INFO (Information), then
IntermediateSecurity must be absent and no occurrences of CorporateActionOptionDetails may
be present.
(MT 564 NVR C6).
On Condition
    /CorporateActionGeneralInformation/EventType/Code is present
 And    /CorporateActionGeneralInformation/EventType/Code is equal to value 
'Information'
Following Must be True
    /IntermediateSecurity Must be absent
 And    /CorporateActionOptionDetails[*] Must be absent
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 50 February 2026
```

## File page 51

```text
C55 InstructCashAmountRule
If OptionFeatures/Code QCAS (InstructCashAmount) is not present, then any message
elements in the list (PriceDetails/MaximumCashToInstruct, PriceDetails/
MinimumCashToInstruct, PriceDetails/MinimumMutipleCashToInstruct) must not be present.
(MT564 NVR C20).
C56 InterestPaymentRule
CorporateActionDetails/RateAndAmountDetails/InterestRate and
CorporateActionOptionsDetails/RateAndAmountDetails/GrossInterestRateUsedforPayment
must not be mixed. InterestRate is used to provide the annual rate of the financial instrument.
InterestRateUsedforPayment is used to provide the applicable rate for the current payment,
after all calculations have been performed, that is, application of period and method of interest
computation.
This constraint is defined at the MessageDefinition level.
C57 InterestPeriodRule
InterestPeriod must be used only if it is different from a normal accrued interest period.
C58 IntermediateSecuritiesDistribution1Rule
If CorporateActionGeneralInformation/EventType/Code is RHDI
(IntermediateSecuritiesDistribution), then CorporateActionDetails/
IntermediateSecuritiesDistributionType must be present.
(MT 564 NVR C11).
On Condition
    /CorporateActionGeneralInformation/EventType/Code is present
 And    /CorporateActionGeneralInformation/EventType/Code is equal to value 
'IntermediateSecuritiesDistribution'
Following Must be True
    /CorporateActionDetails Must be present
 And    /CorporateActionDetails/FollowingEventTypeIndicator Must be present
This constraint is defined at the MessageDefinition level.
C59 IntermediateSecurity1Rule
If CorporateActionGeneralInformation/EventType/Code is RHDI
(IntermediateSecuritiesDistribution), then IntermediateSecurity must be absent.
(MT 564 NVR C6).
On Condition
    /CorporateActionGeneralInformation/EventType/Code is present
 And    /CorporateActionGeneralInformation/EventType/Code is equal to value 
'IntermediateSecuritiesDistribution'
Following Must be True
    /IntermediateSecurity Must be absent
This constraint is defined at the MessageDefinition level.
C60 IntermediateSecurity2Rule
If CorporateActionGeneralInformation/EventType/Code is RHTS (Rights Issue), then
IntermediateSecurity must be present.
(MT 564 NVR C6).
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 51 February 2026
```

## File page 52

```text
On Condition
    /CorporateActionGeneralInformation/EventType/Code is present
 And    /CorporateActionGeneralInformation/EventType/Code is equal to value 
'RightsIssue'
Following Must be True
    /IntermediateSecurity Must be present
This constraint is defined at the MessageDefinition level.
C61 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C62 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C63 IssuerAgentGuideline
IssuerAgent must be used only in the communication between a CSD and local custodians.
This constraint is defined at the MessageDefinition level.
C64 IssuerOfferorTaxabilityIndicatorUsageRule
The IssuerOfferorTaxabilityIndicator may only be used when no tax rate is provided in the
message and it must not be used in events such as dividend or interest.
The list of proprietary IssuerOfferorTaxabilityIndicator codes that may be used are provided in
the document " TXAP Taxability Codes" available on the SMPG website at www.smpg.info.
C65 IssuerOfferorTaxabilityIndicatorUsageRule
The IssuerOfferorTaxabilityIndicator may only be used when no tax rate is provided in the
message and it must not be used in events such as dividend or interest.
The list of proprietary IssuerOfferorTaxabilityIndicator codes that may be used are provided in
the document "TXAP Taxability Codes" available on the SMPG website at www.smpg.info.
C66 LastBidIncrementPrice1Rule
If LastBidIncrementPrice is present in CorporateActionDetails/PriceDetails, then
LastBidIncrementPrice is not allowed in any occurences of CorporateActionOptionDetails/
PriceDetails.
(MT 564 NVR C24)
On Condition
    /CorporateActionDetails/PriceDetails/LastBidIncrementPrice is present
Following Must be True
    /CorporateActionOptionDetails[*]/PriceDetails/LastBidIncrementPrice Must 
be absent
This constraint is defined at the MessageDefinition level.
C67 LastBidIncrementPrice2Rule
If LastBidIncrementPrice is present in any occurrences of CorporateActionOptionDetails/
PriceDetails, then LastBidIncrementPrice is not allowed in CorporateActionDetails/PriceDetails.
(MT 564 NVR C24)
On Condition
    /CorporateActionOptionDetails[*]/PriceDetails/LastBidIncrementPrice is 
present
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 52 February 2026
```

