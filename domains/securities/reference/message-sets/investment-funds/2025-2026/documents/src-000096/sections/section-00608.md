---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.3 Constraints"]
file_pages: [826, 827, 828]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.3 Constraints

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 826 to 828.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 826

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       AdditionalInformation <AddtlInf> [0..*] ± 937
     OtherDrawdownInformation <OthrDrwdwnInf> [0..1]  937
       EmploymentDetails <MplymntDtls> [0..1]  937
         TaxCode <TaxCd> [0..1] ± 938
         OtherTaxCodeIndicator <OthrTaxCdInd> [0..1] Indicator 938
         CumulativeTaxIndicator <CmltvTaxInd> [0..1] Indicator 938
         PreviousPay <PrvsPay> [0..1] Amount C1, C10 939
         PreviousTax <PrvsTax> [0..1] Amount C1, C10 939
         StartDate <StartDt> [0..1] ± 939
         EndDate <EndDt> [0..1] ± 940
         AdditionalInformation <AddtlInf> [0..*] ± 940
       AdditionalInformation <AddtlInf> [0..*] ± 940
     QueryResponse <QryRspn> [0..*] Text 940
     StatusInitiator <StsInitr> [0..1] ± 940
     StatusIssuer <StsIssr> [0..1] ± 941
     StatusRecipient <StsRcpt> [0..1] ± 941
     AdditionalInformation <AddtlInf> [0..*] ± 941
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 941
   Extension <Xtnsn> [0..*] ± C15 0
34.3 Constraints
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
C3 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 826 May 2026
```

## File page 827

```text
C4 AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
C5 BeneficiaryDetailsRule
If RecipientOfDrawdownIndicator is "false" or "0" (No), then BeneficiaryDetails is not allowed.
If RecipientOfDrawdownIndicator is "true" or "1" (Yes), then BeneficiaryDetails may be present.
C6 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C7 ConversionRule
If at least one occurence of TransferEventType is ConversionStatus (CONV) then Conversion
must be present.
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C12 DescriptionUsageRule
Description must be used alone as the last resort.
C13 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C14 DiscountElementRule
Amount Or Rate Or Basis must be present.
C15 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C16 HoldingTransferCurrencyGuideline
When cash is transferred in a currency other than that of the cash, the currency should be
specified in TransferCurrency.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 827 May 2026
```

## File page 828

```text
C17 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C18 IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C19 IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C20 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C21 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C22 NonStandardSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
C23 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C24 OtherReferenceRule
Reference/OtherReference should be used to reference a transfer instruction or a transfer
cancellation request 'message' sent in a proprietary way or used for a system reference. If
Reference/OtherReference is present, Reference/OtherReference/MessageName must contain
'fax' or 'phone' or 'email', etc.
This constraint is defined at the MessageDefinition level.
C25 OtherRule
If Reason/Code/OTHR (Other) is present, then AdditionReasonInformation must be present
and the reason for the rejection status must be provided.
C26 RelatedReferenceRule
If Reference/RelatedReference/MessageName is present, it must start with sese.001,
sese.002, sese.005, sese.006, sese.009, sese.012 or sese.014.
This constraint is defined at the MessageDefinition level.
C27 TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
C28 TransferStatusEventType1Rule
If at least one occurence of TransferEventType is Information (INFO) then TransferStatus/
Status/Status must be equal to Received (RECE).
C29 TransferStatusEventType2Rule
If at least one occurence of TransferEventType is ConversionStatus (CONV) then
TransferStatus/Status/Status must be equal to Received (RECE).
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 828 May 2026
```

