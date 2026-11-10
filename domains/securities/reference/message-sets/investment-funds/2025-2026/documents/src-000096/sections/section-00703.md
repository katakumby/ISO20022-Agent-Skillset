---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.3 Constraints"]
file_pages: [956, 957, 958, 959, 960]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.3 Constraints

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 956 to 960.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 956

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           Party1 <Pty1> [0..1] ± 1102
           Party2 <Pty2> [0..1] ± 1102
           Party3 <Pty3> [0..1] ± 1102
           Party4 <Pty4> [0..1] ± 1103
           Party5 <Pty5> [0..1] ± 1103
       AssetsHeldInOwnName <AsstsHeldInOwnNm> [0..1] Indicator 1104
       TransferResultsInChangeOfBeneficialOwner
<TrfRsltsInChngOfBnfclOwnr>
[0..1] Indicator 1104
       AdditionalInformation <AddtlInf> [0..*] ± 1104
     AdditionalInformation <AddtlInf> [0..*] ± 1104
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 0
   Extension <Xtnsn> [0..*] ± C24 1105
35.3 Constraints
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
C4 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C5 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 956 May 2026
```

## File page 957

```text
C6 AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
C7 AssetLiquidatedCurrencyGuideline
When a security is to be liquidated and transferred as cash (TransferType is CASH), then the
currency of the resulting cash is specified in TransferCurrency.
C8 AssetQuantity1Guideline
If Instrument/Security is present and Quantity is present, then Quantity/Unit or Quantity/
PercentageRate or Quantity/FaceAmount or Quantity/AmortisedValue must be present.
C9 AssetQuantity2Guideline
If Instrument/CashAsset is present and Quantity is present, then Quantity/CashAmount or
Quantity/Percentage must be present.
C10 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C11 BookTransferGuideline
In the case of an own account internal transfer, the account of (delivering) Party2 at (delivering)
Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
C12 Conversion1Rule
If TransferType/Code/CONV (Conversion) is present, then Conversion must be present.
C13 Conversion2Rule
If TransferType/Code/CONV (Conversion) is not present, then Conversion is not allowed.
C14 Corporate1Rule
If PrimaryCorporateInvestor is not present, then SecondaryCorporateInvestor is not allowed.
If PrimaryCorporateInvestor is present, then SecondaryCorporateInvestor may be present.
On Condition
    /PrimaryCorporateInvestor is absent
Following Must be True
    /SecondaryCorporateInvestor Must be absent
This constraint is defined at the MessageDefinition level.
C15 Corporate2Rule
If PrimaryCorporateInvestor is not present, then OtherCorporateInvestor is not allowed.
If PrimaryCorporateInvestor is present, then OtherCorporateInvestor may be present.
On Condition
    /PrimaryCorporateInvestor is absent
Following Must be True
    /OtherCorporateInvestor[*] Must be absent
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 957 May 2026
```

## File page 958

```text
C16 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C17 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C18 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C19 DepositoryGuideline
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
C20 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C21 DescriptionUsageRule
Description must be used alone as the last resort.
C22 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C23 DiscountElementRule
Amount Or Rate Or Basis must be present.
C24 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 958 May 2026
```

## File page 959

```text
C25 HoldingTransferCurrencyGuideline
When cash is transferred in a currency other than that of the cash, the currency should be
specified in TransferCurrency.
C26 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C27 IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C28 IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C29 Investor1Rule
If PrimaryIndividualInvestor is not present, then SecondaryIndividualInvestor is not allowed.
If PrimaryIndividualInvestor is present, then SecondaryIndividualInvestor may be present.
On Condition
    /PrimaryIndividualInvestor is absent
Following Must be True
    /SecondaryIndividualInvestor Must be absent
This constraint is defined at the MessageDefinition level.
C30 Investor2Rule
If PrimaryIndividualInvestor is not present, then OtherIndividualInvestor is not allowed.
If PrimaryIndividualInvestor is present, then OtherIndividualInvestor may be present.
On Condition
    /PrimaryIndividualInvestor is absent
Following Must be True
    /OtherIndividualInvestor[*] Must be absent
This constraint is defined at the MessageDefinition level.
C31 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C32 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C33 NomineeAccountServicerRule
NomineeAccount/Servicer must be present when and only when different from
TransferorAccount/Servicer.
This constraint is defined at the MessageDefinition level.
C34 NonStandardSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
C35 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 959 May 2026
```

## File page 960

```text
C36 PartialInstructedQuantityRule
If the value of PartialInstructedQuantity is 'true' or '1' (Yes), then Quantity must be present.
If the value of PartialInstructedQuantity is 'false' or '0'(No), then Quantity maybe present.
C37 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C38 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C39 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C40 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C41 SECUGuideline
The code SECU (Asset) is used when a financial instrument such as units of a fund are to be
transferred.
The code SECU is also used when assets such as equities or bonds are to be transferred. The
code SECU is also used for assets such as property, moveable property and other similar types
of other asset.
C42 SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.
C43 SocialSecurityNumberGuideline
The UK Insurance Number must be indicated without spaces.
C44 SpecificPreviousYearsGuideline
SpecificPreviousYears must not contain the current year.
C45 TotalAmountYearToDateRule
TotalAmountYearToDate must be equal to the sum of EquityComponent and CashComponent
if present.
C46 TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 960 May 2026
```

