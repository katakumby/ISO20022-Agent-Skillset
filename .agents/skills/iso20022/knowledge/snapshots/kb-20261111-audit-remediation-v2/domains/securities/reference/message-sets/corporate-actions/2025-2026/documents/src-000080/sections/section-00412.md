---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.3 Constraints"]
file_pages: [550, 551, 552, 553, 554, 555, 556, 557]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
topic_continuations: [{"constraint_ids": ["C75", "C76", "C77"], "until_heading": "8.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 558, "topic": "8.3 Constraints", "reference_path": "domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00413.md"}]
---

# 8.3 Constraints

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 550 to 557.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 8.3 Constraints topic continues in [Constraints continuation C75–C77 (file p558)](section-00413.md#file-page-558). Read the text before **8.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 550

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 660
         GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 660
         CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 661
   AdditionalInformation <AddtlInf> [0..1]  661
     AdditionalText <AddtlTxt> [0..*] Text 662
     NarrativeVersion <NrrtvVrsn> [0..*] Text 662
     PartyContactNarrative <PtyCtctNrrtv> [0..*] Text 662
     TaxationConditions <TaxtnConds> [0..*] Text 662
   IssuerAgent <IssrAgt> [0..*] ± 662
   PayingAgent <PngAgt> [0..*] ± 663
   SubPayingAgent <SubPngAgt> [0..*] ± 663
   SupplementaryData <SplmtryData> [0..*] ± C70 663
8.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 AdditionalInformationRule
All elements in the AdditionalInformation sequence must not contain information that can be
provided in a structured field unless bilaterally agreed or advised differently in the element
definition as in AdditionalInformation/NarrativeVersion.
This constraint is defined at the MessageDefinition level.
C3 AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be
provided in a structured field unless bilaterally agreed or advised differently in the element
definition as in NarrativeVersion.
C4 AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be
provided in a structured field unless bilaterally agreed or advised differently in the element
definition as in NarrativeVersion.
C5 AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be
provided in a structured field unless bilaterally agreed or advised differently in the element
definition as in NarrativeVersion.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 550 February 2026
```

## File page 551

```text
C6 AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be
provided in a structured field unless bilaterally agreed or advised differently in the element
definition as in NarrativeVersion.
C7 AffectedAndUnaffectedBalanceRule
Unaffected balance and Affected balances should only be mentioned as a result of the process
that was run through the event. For instance lottery results, Dutch auction results or tender offer
results.
C8 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C9 BeneficialOwnerReferencePresenceRule
If BeneficialOwnerReference is present then TaxReclaimDocumentationReference must be
absent.
C10 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C11 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C12 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C13 DeemedRate1Rule
If DeemedRate is repeated, then DeemedRate/RateTypeAndAmountAndRateStatus/RateType/
Code values and DeemedRate/RateTypeAndRate/RateType/Code values must all be different
in each occurrence of DeemedRate.
(MT 566 NVR C4).
C14 DeemedRate2Rule
Only a single occurrence of either DeemedRate/Amount or DeemedRate/Rate may be present,
only one of those elements may be present.
(MT 566 NVR C3).
C15 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C16 DescriptionUsageRule
Description must be used alone as the last resort.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 551 February 2026
```

## File page 552

```text
C17 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C18 EventTypeRule
If Code is present, the code OTHR (Other) must only be used in case no other corporate action
event code is appropriate.
If Code is present, the code CHAN (Change) must only be used in case no other corporate
action event code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM (Final Maturity) must only be used when the redemption is
decided by the issuer and not by the securities holders.
C19 ExemptionTypeUsageRule
The lists of exemption type codes to be used in ExemptionType are provided in the document
"ETYP-ITYP Exemption & Income Type Codes" available on the SMPG website at
www.smpg.info.
C20 ExemptionTypeUsageRule
The lists of exemption type codes to be used in ExemptionType are provided in the document
"ETYP-ITYP Exemption & Income Type Codes" available on the SMPG website at
www.smpg.info.
C21 GenericCashPricePerProductGuideline
GenericCashPriceReceivedPerProduct and GenericCashPricePaidPerProduct are prices
received or paid in the course of an event. The specific meaning (redemption price, subscription
price, reinvestment price, etc.) is derived from the event type.
C22 GenericCashPricePerProductGuideline
GenericCashPriceReceivedPerProduct and GenericCashPricePaidPerProduct are prices
received or paid in the course of an event. The specific meaning (redemption price, subscription
price, reinvestment price, ETC.) is derived from the event type.
C23 GenericCashPriceReceivedPerProductGuideline
GenericCashPriceReceivedPerProduct is the price received in the course of an event. The
specific meaning (redemption price, subscription price, reinvestment price, ETC.) is derived
from the event type.
C24 GrossDistributionRate2Rule
If GrossDistributionRate is repeated, then:
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of GrossDistributionRate. (MT 566 NVR C4 ).
C25 GrossDistributionRate2Rule
If GrossDistributionRate is repeated, then:
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of GrossDistributionRate. (MT 566 NVR C4 ).
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 552 February 2026
```

## File page 553

```text
C26 GrossDistributionRate3Rule
Only a single occurrence of either GrossDistributionRate/Amount or GrossDistributionRate/
AmountAndRateStatus may be present. Both elements may not be present together. (MT 566
NVR C3).
C27 GrossDistributionRate3Rule
Only a single occurrence of either GrossDistributionRate/Amount or GrossDistributionRate/
AmountAndRateStatus may be present. Both elements may not be present together. (MT 566
NVR C3).
C28 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C29 IncentivePremiumEventType1Rule
If Code value is equal to INCP (IncentivePremiumPayment) in CorporateActionDetails/
AdditionalBusinessProcessIndicator, then CorporateActionGeneralInformation/EventType/Code
value must be equal to CONS (Consent).
(MT 566 NVR C9)
On Condition
    /CorporateActionDetails/AdditionalBusinessProcessIndicator[*]/Code is 
equal to value 'IncentivePremiumPayment'
Following Must be True
    /CorporateActionGeneralInformation/EventType/Code Must be equal to value 
'Consent'
This constraint is defined at the MessageDefinition level.
C30 IncentivePremiumEventTypeUG1Rule
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
C31 IncomeType1Rule
If at least one occurrence of OtherIncomeType is present, then IncomeType must be present.
C32 IncomeType2Rule
If at least one occurrence of OtherIncomeType is present, then IncomeType must be present.
C33 IncomeTypeUsageRule
The lists of income type codes to be used in IncomeType are provided in the document "ETYP-
ITYP Exemption & Income Type Codes" available on the SMPG website at www.smpg.info.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 553 February 2026
```

## File page 554

```text
C34 IncomeTypeUsageRule
The lists of income type codes to be used in IncomeType are provided in the document "ETYP-
ITYP Exemption & Income Type Codes" available on the SMPG website at www.smpg.info.
C35 IntermediateSecuritiesDistribution1Rule
If CorporateActionGeneralInformation/EventType/Code is RHDI
(IntermediateSecuritiesDistribution), then CorporateActionDetails/
IntermediateSecuritiesDistributionType must be present.
(MT 566 NVR C5).
On Condition
    /CorporateActionGeneralInformation/EventType/Code is equal to value 
'IntermediateSecuritiesDistribution'
Following Must be True
    /CorporateActionDetails Must be present
 And    /CorporateActionDetails/FollowingEventTypeIndicator Must be present
This constraint is defined at the MessageDefinition level.
C36 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C37 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C38 IssuerAgentGuideline
IssuerAgent must be used only in the communication between a CSD and local custodians.
This constraint is defined at the MessageDefinition level.
C39 IssuerOfferorTaxabilityIndicatorUsageRule
The IssuerOfferorTaxabilityIndicator may only be used when no tax rate is provided in the
message and it must not be used in events such as dividend or interest.
The list of proprietary IssuerOfferorTaxabilityIndicator codes that may be used are provided in
the document " TXAP Taxability Codes" available on the SMPG website at www.smpg.info.
C40 IssuerOfferorTaxabilityIndicatorUsageRule
The IssuerOfferorTaxabilityIndicator may only be used when no tax rate is provided in the
message and it must not be used in events such as dividend or interest.
The list of proprietary IssuerOfferorTaxabilityIndicator codes that may be used are provided in
the document " TXAP Taxability Codes" available on the SMPG website at www.smpg.info.
C41 MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 554 February 2026
```

## File page 555

```text
C42 NetDistributionRate1Rule
If NetDistributionRate is repeated, then RateTypeAndAmountAndRateStatus/RateType/Code
values must all be different in each occurrence of NetDistributionRate. (MT 566 NVR C4 ).
C43 NetDistributionRate1Rule
If NetDistributionRate is repeated, then:
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of NetDistributionRate. (MT 566 NVR C4 ).
C44 NetDistributionRate2Rule
Only a single occurrence of either NetDistributionRate/Amount may be present. Both elements
may not be present together. (MT 566 NVR C3).
C45 NetDistributionRate2Rule
Only a single occurrence of either NetDistributionRate/Amount may be present. Both elements
may not be present together. (MT 566 NVR C3).
C46 OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the structure and usage of the Official Corporate Action Event Reference
(COAF). Those recommendations are
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
C47 OptionNumberRule
The CorporateActionConfirmationDetails/OptionNumber value provided must be the same as
the one provided in the related CorporateActionOptionDetails/OptionNumber element of the
CorporateActionNotification or CorporateActionMovementPreliminaryAdvice messages
previously sent.
This constraint is defined at the MessageDefinition level.
C48 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C49 PaginationRule
If pagination is present, then MovementConfirmationIdentification must be present.
On Condition
    /Pagination is present
Following Must be True
    /MovementConfirmationIdentification Must be present
This constraint is defined at the MessageDefinition level.
C50 Party2PresenceRule
If Party 2 is present, then Party 1 must be present.
C51 Party3PresenceRule
If Party 3 is present, then Party 2 must be present.
C52 RateStatusGuideline
The code value ACTU is the default value for a rate status.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 555 February 2026
```

## File page 556

```text
C53 SafekeepingAccountOrBlockChainAddress1Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C54 SafekeepingAccountOrBlockChainAddress1Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C55 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present then SafekeepingAccount must be absent.
C56 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present then SafekeepingAccount must be absent.
C57 SafekeepingAccountOrBlockChainAddress3Rule
If SafekeepingAccount is present, then BlockChainAddressOrWallet must be absent.
C58 SafekeepingAccountOrBlockChainAddress3Rule
If SafekeepingAccount is present, then BlockChainAddressOrWallet must be absent.
C59 SafekeepingPlaceRule
The SafekeepingPlace is only to be used by global custodians that allow their clients to specify
where the securities are to be held, for example, in an ICSD account versus an account at the
local CSD.
C60 ScripOrDividendReinvestment1Rule
If CorporateActionConfirmationDetails/CashMovementDetails/AmountDetails/
CashAmountCarriedForward or CorporateActionConfirmationDetails/CashMovementDetails/
AmountDetails/CashAmountBroughtForward is present, then
CorporateActionGeneralInformation/EventType/Code value must be either DVSC
(ScripDividend) or DRIP (DividendReinvestment).
This constraint is defined at the MessageDefinition level.
C61 ScripOrDividendReinvestment2Rule
If CorporateActionConfirmationDetails/CashMovementDetails/AmountDetails/
NotionalDividendPayableAmount or CorporateActionConfirmationDetails/
CashMovementDetails/AmountDetails/NotionalTaxAmount is present, then
CorporateActionGeneralInformation/EventType/Code value must be DVSC (ScripDividend).
This constraint is defined at the MessageDefinition level.
C62 ScripOrDividendReinvestment3Rule
If CorporateActionConfirmationDetails/CashMovementDetails/TaxVoucherDetails/BargainDate
or CorporateActionConfirmationDetails/CashMovementDetails/TaxVoucherDetails/
BargainSettlementDate is present, then CorporateActionGeneralInformation/EventType/Code
value must be DRIP (DividendReinvestment).
This constraint is defined at the MessageDefinition level.
C63 SecondLevelTax1Rule
If SecondLevelTax is repeated, then SecondLevelTax/RateTypeAndRate/RateType/Code
values must all be different in each occurrence of SecondLevelTax.
(MT 564 NVR C8).
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 556 February 2026
```

## File page 557

```text
C64 SecondLevelTax1Rule
If SecondLevelTax is repeated, then SecondLevelTax/RateTypeAndRate/RateType/Code
values must all be different in each occurrence of SecondLevelTax.
(MT 566 NVR C4).
C65 SecondLevelTax2Rule
Only a single occurrence of either SecondLevelTax/Amount or SecondLevelTax/Rate or
SecondLevelTax/NotSpecifiedRate may be present, only one of these elements may be
present.
(MT 564 NVR C7).
C66 SecondLevelTax2Rule
Only a single occurrence of either SecondLevelTax/Amount or SecondLevelTax/Rate or
SecondLevelTax/NotSpecifiedRate may be present, only one of these elements may be
present.
(MT 566 NVR C3).
C67 SecondLevelTax3Rule
If at least one occurrence of SecondLevelTax is present, then at least one occurrence of
WithholdingTaxRate must be present. (MT 566 NVR C8).
C68 SecondLevelTax3Rule
If at least one occurrence of SecondLevelTax is present, then at least one occurrence of
WithholdingTaxRate must be present. (MT 566 NVR C8).
C69 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C70 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C71 TaxReclaimDocumentationReferencePresenceRule
If TaxReclaimDocumentationReference is present then BeneficialOwnerReference must be
absent.
C72 TaxVoucherPresenceRule
At least one of TaxVoucherReference Or TaxReclaimDocumentationReference Or
BeneficialOwnerReference must be present.
C73 WithholdingTaxRate1Rule
If WithholdingTaxRate is repeated, then WithholdingTaxRate/RateTypeAndRate/RateType/
Code values must all be different in each occurrence of WithholdingTaxRate.
(MT 564 NVR C8).
C74 WithholdingTaxRate1Rule
If WithholdingTaxRate is repeated, then WithholdingTaxRate/RateTypeAndRate/RateType/
Code values must all be different in each occurrence of WithholdingTaxRate.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 557 February 2026
```

