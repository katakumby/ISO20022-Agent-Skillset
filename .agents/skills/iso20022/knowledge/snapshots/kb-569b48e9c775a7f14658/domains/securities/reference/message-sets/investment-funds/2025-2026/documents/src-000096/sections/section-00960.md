---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.3 Constraints"]
file_pages: [1319, 1320, 1321, 1322, 1323]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1319 to 1323.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1319

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           Party4 <Pty4> [0..1] ± 1434
           Party5 <Pty5> [0..1] ± 1435
         DeliveringSideDetails <DlvrgSdDtls> [0..1]  C11,
C17,
C32,
C33,
C34,
C35,
C40
1435
           Depository <Dpstry> [0..1] ± 1437
           Party1 <Pty1> [0..1] ± 1438
           Party2 <Pty2> [0..1] ± 1438
           Party3 <Pty3> [0..1] ± 1438
           Party4 <Pty4> [0..1] ± 1439
           Party5 <Pty5> [0..1] ± 1439
       AssetsHeldInOwnName <AsstsHeldInOwnNm> [0..1] Indicator 1440
       TransferResultsInChangeOfBeneficialOwner
<TrfRsltsInChngOfBnfclOwnr>
[0..1] Indicator 1440
       AdditionalInformation <AddtlInf> [0..*] ± 1440
     AdditionalInformation <AddtlInf> [0..*] ± 1440
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 1441
   Extension <Xtnsn> [0..*] ± C22 0
38.3 Constraints
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
C3 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1319 May 2026
```

## File page 1320

```text
C4 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C5 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C6 AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
C7 AssetQuantity1Guideline
If Instrument/Security is present, then Quantity/Unit or Quantity/FaceAmount or Quantity/
AmortisedValue must be present.
C8 AssetQuantity2Guideline
If Instrument/CashAsset is present, then Quantity/CashAmount must be present.
C9 BlockTransferRetirementAgeProtectionRule
If BlockTransfer is "false" or "0" (No), then RetirementAgeProtection is not allowed.
If BlockTransfer is "true" or "1" (Yes), then RetirementAgeProtection may be present.
C10 BlockTransferTaxFreeCashProtectionRule
If BlockTransfer is "false" or "0" (No), then TaxFreeCashProtection is not allowed.
If BlockTransfer is "true" or "1" (Yes), then TaxFreeCashProtection may be present.
C11 BookTransferGuideline
In the case of an own account internal transfer, the account of (delivering) Party2 at (delivering)
Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
C12 Corporate1Rule
If PrimaryCorporateInvestor is not present, then SecondaryCorporateInvestor is not allowed.
If PrimaryCorporateInvestor is present, then SecondaryCorporateInvestor may be present.
On Condition
    /PrimaryCorporateInvestor is absent
Following Must be True
    /SecondaryCorporateInvestor Must be absent
This constraint is defined at the MessageDefinition level.
C13 Corporate2Rule
If PrimaryCorporateInvestor is not present, then OtherCorporateInvestor is not allowed.
If PrimaryCorporateInvestor is present, then OtherCorporateInvestor may be present.
On Condition
    /PrimaryCorporateInvestor is absent
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1320 May 2026
```

## File page 1321

```text
Following Must be True
    /OtherCorporateInvestor[*] Must be absent
This constraint is defined at the MessageDefinition level.
C14 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C15 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C16 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C17 DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD
exists in a particular market, the stock exchange BIC will be used.
Country code should be used for settlement taking place outside of an institution published in
the PSET's BIC list. This includes physical deliveries and investment funds not settling at a
CSD.
The format and content of the settlement party sequences will comply with the market practices
published for the counterparty depository included in the message.
For more details, see the relevant market practice document on www.smpg.info.
C18 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C19 DescriptionUsageRule
Description must be used alone as the last resort.
C20 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C21 DiscountElementRule
Amount Or Rate Or Basis must be present.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1321 May 2026
```

## File page 1322

```text
C22 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C23 IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C24 IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C25 Investor1Rule
If PrimaryIndividualInvestor is not present, then SecondaryIndividualInvestor is not allowed.
If PrimaryIndividualInvestor is present, then SecondaryIndividualInvestor may be present.
On Condition
    /PrimaryIndividualInvestor is absent
Following Must be True
    /SecondaryIndividualInvestor Must be absent
This constraint is defined at the MessageDefinition level.
C26 Investor2Rule
If PrimaryIndividualInvestor is not present, then OtherIndividualInvestor is not allowed.
If PrimaryIndividualInvestor is present, then OtherIndividualInvestor may be present.
On Condition
    /PrimaryIndividualInvestor is absent
Following Must be True
    /OtherIndividualInvestor[*] Must be absent
This constraint is defined at the MessageDefinition level.
C27 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C28 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C29 NomineeAccountServicerRule
NomineeAccount/Servicer must be present when and only when different from
TransferorAccount/Servicer.
This constraint is defined at the MessageDefinition level.
C30 NonStandardSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
C31 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C32 Party2PresenceRule
If Party2 is present, then Party1 must be present.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1322 May 2026
```

## File page 1323

```text
C33 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C34 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C35 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C36 PensionOrderTypeGuideline
A pension policy, plan or scheme cannot have both an earmark and a sharing order.
If PensionOrder/Type/Code/SHAR is present, then PensionOrder/Type/Code/EARM is not
allowed.
If PensionOrder/Type/Code/EARM is present, then PensionOrder/Type/Code/SHAR is not
allowed.
C37 RetirementAgeRule
If RetirementAgeProtection is "false" or "0" (No), then RetirementAge is not allowed.
If RetirementAgeProtection is "true" or "1" (Yes), then RetirementAge may be present.
C38 RingFencedDrawdownAssets1Rule
If DrawdownStatus/Code/NONE (None) is present, then RingFencedDrawdownAssets is not
allowed.
C39 RingFencedDrawdownAssets2Rule
If DrawdownStatus/Code/PART (Partial) or FULL (Full) is present, then
RingFencedDrawdownAssets must be present.
C40 SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.
C41 SocialSecurityNumberGuideline
The UK Insurance Number must be indicated without spaces.
C42 SpecificPreviousYearsGuideline
SpecificPreviousYears must not contain the current year.
C43 TaxFreeCashAmountRule
If TaxFreeCashProtection is "false" or "0" (No), then TaxFreeCashAmount is not allowed.
If TaxFreeCashProtection is "true" or "1" (Yes), then TaxFreeCashAmount may be present.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1323 May 2026
```

