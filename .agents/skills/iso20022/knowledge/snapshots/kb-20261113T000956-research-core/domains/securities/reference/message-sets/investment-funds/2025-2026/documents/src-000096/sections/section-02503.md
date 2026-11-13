---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.3 Constraints"]
file_pages: [3509, 3510, 3511, 3512]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
topic_continuations: [{"constraint_ids": ["C37", "C38"], "until_heading": "53.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 3513, "topic": "53.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02504.md"}]
---

# 53.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3509 to 3512.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 53.3 Constraints topic continues in [Constraints continuation C37–C38 (file p3513)](section-02504.md#file-page-3513). Read the text before **53.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 3509

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 3787
Or                 BICFI <BICFI> [1..1] IdentifierSet C5 3788
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 3788
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 3789
               LEI <LEI> [0..1] IdentifierSet 3789
             DrawerIdentification <DrwrId> [0..1] ± 3790
Or           CashAccountDetails <CshAcctDtls> [1..1]  C1 3790
             AccountIdentification <AcctId> [0..1] Text 3790
             Type <Tp> [0..1] ± 3790
Or}           BlockChainCashWallet <BlckChainCshWllt> [1..1]  3791
             Identification <Id> [1..1] Text 3791
             Type <Tp> [0..1] ± 3791
             Name <Nm> [0..1] Text 3791
             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3792
     ForeignExchangeDetails <FXDtls> [0..1]  3792
       UnitCurrency <UnitCcy> [1..1] CodeSet C2 3792
       QuotedCurrency <QtdCcy> [1..1] CodeSet C2 3793
       ExchangeRate <XchgRate> [1..1] Rate 3793
       QuotationDate <QtnDt> [0..1] DateTime 3793
       QuotingInstitution <QtgInstn> [0..1] ± 3794
     FinancialAdvice <FinAdvc> [0..1] CodeSet 3794
     NegotiatedTrade <NgtdTrad> [0..1] CodeSet 3794
     CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 3794
     TransactionChannelType <TxChanlTp> [0..1] ± 3795
     SignatureType <SgntrTp> [0..1] ± 3795
     OrderWaiverDetails <OrdrWvrDtls> [0..1] ± C38 3795
   CopyDetails <CpyDtls> [0..1] ± 3796
   Extension <Xtnsn> [0..*] ± C15 0
53.3 Constraints
C1 AccountElementRule
Either AccountIdentification or Type must be present. Both may be present.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3509 May 2026
```

## File page 3510

```text
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
C4 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C5 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C6 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C7 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C8 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C9 DeliverersCustodianRule
If DeliverersIntermediary1Details is present, then DeliverersCustodianDetails must be present.
If DeliverersIntermediary1Details is not present then DeliverersCustodianDetails is optional.
C10 DeliverersIntermediary1DetailsRule
If DeliverersIntermediary2Details is present, then DeliverersIntermediary1Details must be
present. If DeliverersIntermediary2Details is not present then DeliverersIntermediary1Details is
optional.
C11 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C12 DescriptionUsageRule
Description must be used alone as the last resort.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3510 May 2026
```

## File page 3511

```text
C13 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C14 DiscountElementRule
Amount Or Rate Or Basis must be present.
C15 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C16 FeeElementRule
One of the elements (Basis, StandardAmount, StandardRate, DiscountDetails,
RequestedAmount, RequestedRate, NonStandardSLAReference, RecipientIdentification) must
be present.
C17 FeeTaxElementRule
One of the elements (CommercialAgreementReference, IndividualFee, IndividualTax,
DigitalNetworkFee) must be present.
C18 FinancialInstrumentQuantity1Rule
If SubscriptionLegDetails/FinancialInstrumentQuantityChoice is not present, then
RedemptionLegDetails/FinancialInstrumentQuantityChoice is mandatory in each occurrence of
RedemptionLegDetails.
If SubscriptionLegDetails/FinancialInstrumentQuantityChoice is present, then it must be present
in each occurrence of SubscriptionLegDetails.
C19 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C20 IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C21 InvestmentAccountDetailsRule
Either InvestmentAccountDetails or all occurrences of SubscriptionLegDetails/
InvestmentAccountDetails and RedemptionLegDetails/InvestmentAccountDetails must be
present, but not both.
Either InvestmentAccountDetails or all occurrences of SubscriptionLegDetails/
InvestmentAccountDetails and RedemptionLegDetails/InvestmentAccountDetails must be
present, but not both.
C22 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C23 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3511 May 2026
```

## File page 3512

```text
C24 MultipleSwitchOrderRule
If SwitchOrderDetails is present more than once, then SwitchOrderDetails/
RedemptionLegDetails and SwitchOrderDetails/SubscriptionLegDetails must only be present
once.
This constraint is defined at the MessageDefinition level.
C25 OrderOriginatorEligibility1Rule
OrderOriginatorEligibility may only be present if Role is either UCL1 (UnderlyingClient1) or
UCL2 (UnderlyingClient2).
C26 OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
C27 OrderOriginatorEligibility3Rule
Either InvestmentAccountDetails/OrderOriginatorEligibility or a single occurrence of
RedemptionLegDetails/InvestmentAccountDetails/OrderOriginatorEligibility or a single
occurrence of SubscriptionLegDetails/InvestmentAccountDetails/OrderOriginatorEligibility
should be only present.
C28 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C29 PhysicalDeliveryDetails1Rule
If PhysicalDeliveryIndicator is "false" or "0" (No), then PhysicalDeliveryDetails is not allowed.
C30 PhysicalDeliveryDetails1Rule
If PhysicalDeliveryIndicator is "false" or "0" (No), then PhysicalDeliveryDetails is not allowed.
C31 PhysicalDeliveryDetails2Rule
If PhysicalDeliveryIndicator is "true" or "1" (Yes), then PhysicalDeliveryDetails must be present.
C32 PhysicalDeliveryDetails2Rule
If PhysicalDeliveryIndicator is "true" or "1" (Yes), then PhysicalDeliveryDetails must be present.
C33 ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present.
If ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
C34 ReceiversIntermediary1DetailsRule
If ReceiversIntermediary2Details is present, then ReceiversIntermediary1Details must be
present. If ReceiversIntermediary2Details is not present, then ReceiversIntermediary1Details is
optional.
C35 SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
C36 StandardFeeAmountCalculation
If StandardAmount, RequestedAmount and DiscountDetails/Amount are all present, then
StandardAmount minus DiscountDetails/Amount must equal RequestedAmount.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3512 May 2026
```

