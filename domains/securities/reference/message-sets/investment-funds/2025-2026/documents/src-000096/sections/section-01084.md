---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.3 Constraints"]
file_pages: [1505, 1506, 1507, 1508, 1509]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.3 Constraints

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1505 to 1509.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1505

```text
40.3 Constraints
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
C6 AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
C7 AssetQuantity1Guideline
If Instrument/Security is present, then Quantity/Unit or Quantity/FaceAmount or Quantity/
AmortisedValue must be present.
C8 AssetQuantity2Guideline
If Instrument/CashAsset is present, then Quantity/CashAmount must be present.
C9 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C10 BlockTransferRetirementAgeProtectionRule
If BlockTransfer is "false" or "0" (No), then RetirementAgeProtection is not allowed.
If BlockTransfer is "true" or "1" (Yes), then RetirementAgeProtection may be present.
C11 BlockTransferTaxFreeCashProtectionRule
If BlockTransfer is "false" or "0" (No), then TaxFreeCashProtection is not allowed.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1505 May 2026
```

## File page 1506

```text
If BlockTransfer is "true" or "1" (Yes), then TaxFreeCashProtection may be present.
C12 BookTransferGuideline
In the case of an own account internal transfer, the account of (delivering) Party2 at (delivering)
Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
C13 Conversion1Rule
If TransferType/Code/CONV (Conversion) is present, then Conversion must be present.
C14 Conversion2Rule
If TransferType/Code/CONV (Conversion) is not present, then Conversion is not allowed.
C15 Corporate1Rule
If PrimaryCorporateInvestor is not present, then SecondaryCorporateInvestor is not allowed.
If PrimaryCorporateInvestor is present, then SecondaryCorporateInvestor may be present.
On Condition
    /PrimaryCorporateInvestor is absent
Following Must be True
    /SecondaryCorporateInvestor Must be absent
This constraint is defined at the MessageDefinition level.
C16 Corporate2Rule
If PrimaryCorporateInvestor is not present, then OtherCorporateInvestor is not allowed.
If PrimaryCorporateInvestor is present, then OtherCorporateInvestor may be present.
On Condition
    /PrimaryCorporateInvestor is absent
Following Must be True
    /OtherCorporateInvestor[*] Must be absent
This constraint is defined at the MessageDefinition level.
C17 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C18 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C19 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C20 DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1506 May 2026
```

## File page 1507

```text
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
C21 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C22 DescriptionUsageRule
Description must be used alone as the last resort.
C23 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C24 DiscountElementRule
Amount Or Rate Or Basis must be present.
C25 EffectiveDatesGuideline
When the portfolio transfer confirmation is used to confirm the intent to transfer, effective
transfer date and effective settlement date are not applicable.
C26 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C27 HoldingTransferCurrencyGuideline
When cash is transferred in a currency other than that of the cash, the currency should be
specified in TransferCurrency.
C28 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C29 IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C30 IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C31 Investor1Rule
If PrimaryIndividualInvestor is not present, then SecondaryIndividualInvestor is not allowed.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1507 May 2026
```

## File page 1508

```text
If PrimaryIndividualInvestor is present, then SecondaryIndividualInvestor may be present.
On Condition
    /PrimaryIndividualInvestor is absent
Following Must be True
    /SecondaryIndividualInvestor Must be absent
This constraint is defined at the MessageDefinition level.
C32 Investor2Rule
If PrimaryIndividualInvestor is not present, then OtherIndividualInvestor is not allowed.
If PrimaryIndividualInvestor is present, then OtherIndividualInvestor may be present.
On Condition
    /PrimaryIndividualInvestor is absent
Following Must be True
    /OtherIndividualInvestor[*] Must be absent
This constraint is defined at the MessageDefinition level.
C33 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C34 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C35 NomineeAccountServicerRule
NomineeAccount/Servicer must be present when and only when different from
TransferorAccount/Servicer.
This constraint is defined at the MessageDefinition level.
C36 NonStandardSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
C37 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C38 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C39 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C40 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C41 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C42 PensionOrderTypeGuideline
A pension policy, plan or scheme cannot have both an earmark and a sharing order.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1508 May 2026
```

## File page 1509

```text
If PensionOrder/Type/Code/SHAR is present, then PensionOrder/Type/Code/EARM is not
allowed.
If PensionOrder/Type/Code/EARM is present, then PensionOrder/Type/Code/SHAR is not
allowed.
C43 RetirementAgeRule
If RetirementAgeProtection is "false" or "0" (No), then RetirementAge is not allowed.
If RetirementAgeProtection is "true" or "1" (Yes), then RetirementAge may be present.
C44 RingFencedDrawdownAssets1Rule
If DrawdownStatus/Code/NONE (None) is present, then RingFencedDrawdownAssets is not
allowed.
C45 RingFencedDrawdownAssets2Rule
If DrawdownStatus/Code/PART (Partial) or FULL (Full) is present, then
RingFencedDrawdownAssets must be present.
C46 SECUGuideline
The code SECU (Asset) is used when a financial instrument such as units of a fund are to be
transferred.
The code SECU is also used when assets such as equities or bonds are to be transferred. The
code SECU is also used for assets such as property, moveable property and other similar types
of other asset.
C47 SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.
C48 SocialSecurityNumberGuideline
The UK Insurance Number must be indicated without spaces.
C49 SpecificPreviousYearsGuideline
SpecificPreviousYears must not contain the current year.
C50 TaxFreeCashAmountRule
If TaxFreeCashProtection is "false" or "0" (No), then TaxFreeCashAmount is not allowed.
If TaxFreeCashProtection is "true" or "1" (Yes), then TaxFreeCashAmount may be present.
C51 TaxFreeCashAndValueRule
If TaxFreeCashProtection is "true" or "1" (Yes), then TaxFreeCashAmount and
ValueOfPensionPolicyOrPlanOrScheme must be present.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1509 May 2026
```

