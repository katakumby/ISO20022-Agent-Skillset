---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.3 Constraints"]
file_pages: [4117, 4118]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.3 Constraints

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4117 to 4118.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4117

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or             Sicovam <SCVM> [1..1] IdentifierSet 4199
Or             Belgian <Belgn> [1..1] IdentifierSet 4199
Or             Common <Cmon> [1..1] IdentifierSet 4199
Or             DTI <DTI> [1..1] IdentifierSet 4199
Or}             OtherProprietaryIdentification <OthrPrtryId> [1..1]  4199
               Identification <Id> [1..1] Text 4200
               IdentificationSource <IdSrc> [1..1] ± 4200
           Name <Nm> [0..1] Text 4200
           ShortName <ShrtNm> [0..1] Text 4200
           SupplementaryIdentification <SplmtryId> [0..1] Text 4200
           ClassType <ClssTp> [0..1] Text 4200
           SecuritiesForm <SctiesForm> [0..1] CodeSet 4201
           DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4201
           ProductGroup <PdctGrp> [0..1] Text 4201
           SeriesIdentification <SrsId> [0..1]  C19 4201
             SeriesDate <SrsDt> [0..1] ± 4202
             SeriesName <SrsNm> [0..1] Text 4202
       StatusInitiator <StsInitr> [0..1] ± 4202
       OrderData <OrdrData> [0..1] ± C20 4202
       NewDetails <NewDtls> [0..1]  4203
         ExpectedTradeDateTime <XpctdTradDtTm> [0..1] ± 4203
         ExpectedCashSettlementDate <XpctdCshSttlmDt> [0..1] Date 4203
   Extension <Xtnsn> [0..*] ± C11 4204
56.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4117 May 2026
```

## File page 4118

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AdditionaInformationRule
The AdditionalInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
C4 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C5 CancelledElementRule
Either Reason or AdditionalInformation must be present. Both may be present.
C6 CommercialAgreementRule
If CommercialAgreementReference is present, then
NewCommercialAgreementReferenceIndicator must be present too.
C7 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C8 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 DateElementRule
Either ExpectedTradeDateTime or ExpectedCashSettlementDate must be present. Both may
be present.
C11 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C12 FeeElementRule
One of the elements (Type, RepairedStandardAmount, RepairedStandardRate,
RepairedDiscountAmount, RepairedDiscountRate, RepairedRequestedAmount,
RepairedRequestedRate, CommercialAgreementReference,
NewCommercialAgreementReferenceIndicator) must be present.
C13 IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4118 May 2026
```

