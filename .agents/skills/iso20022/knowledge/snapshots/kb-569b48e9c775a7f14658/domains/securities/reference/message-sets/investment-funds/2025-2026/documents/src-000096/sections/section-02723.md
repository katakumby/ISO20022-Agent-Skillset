---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.3 Constraints"]
file_pages: [3824, 3825, 3826]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3824 to 3826.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3824

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     OrderWaiverDetails <OrdrWvrDtls> [0..1] ± C37 4107
   CopyDetails <CpyDtls> [0..1] ± 0
   Extension <Xtnsn> [0..*] ± C16 0
55.3 Constraints
C1 AccountElementRule
Either AccountIdentification or Type must be present. Both may be present.
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
C5 AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
C6 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C7 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C8 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3824 May 2026
```

## File page 3825

```text
C10 DeliverersCustodianRule
If DeliverersIntermediary1Details is present, then DeliverersCustodianDetails must be present.
If DeliverersIntermediary1Details is not present then DeliverersCustodianDetails is optional.
C11 DeliverersIntermediary1DetailsRule
If DeliverersIntermediary2Details is present, then DeliverersIntermediary1Details must be
present. If DeliverersIntermediary2Details is not present then DeliverersIntermediary1Details is
optional.
C12 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C13 DescriptionUsageRule
Description must be used alone as the last resort.
C14 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C15 DiscountElementRule
Amount Or Rate Or Basis must be present.
C16 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C17 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C18 IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C19 InvestmentAccountDetailsRule
Either InvestmentAccountDetails or all occurrences of SubscriptionLegDetails/
InvestmentAccountDetails and RedemptionLegDetails/InvestmentAccountDetails must be
present, but not both.
C20 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C21 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C22 MultipleSwitchExecutionRule
If SwitchExecutionDetails is present more than once, then SwitchExecutionDetails/
RedemptionLegDetails and SwitchExecutionDetails/SubscriptionLegDetails must only be
present once.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3825 May 2026
```

## File page 3826

```text
This constraint is defined at the MessageDefinition level.
C23 NonStandardSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
C24 OrderOriginatorEligibility1Rule
OrderOriginatorEligibility may only be present if Role is either UCL1 (UnderlyingClient1) or
UCL2 (UnderlyingClient2).
C25 OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
C26 OrderOriginatorEligibility3Rule
Either InvestmentAccountDetails/OrderOriginatorEligibility or a single occurrence of
RedemptionLegDetails/InvestmentAccountDetails/OrderOriginatorEligibility or a single
occurrence of SubscriptionLegDetails/InvestmentAccountDetails/OrderOriginatorEligibility
should be only present.
C27 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C28 PhysicalDeliveryDetails1Rule
If PhysicalDeliveryIndicator is "false" or "0" (No), then PhysicalDeliveryDetails is not allowed.
C29 PhysicalDeliveryDetails1Rule
If PhysicalDeliveryIndicator is "false" or "0" (No), then PhysicalDeliveryDetails is not allowed.
C30 PhysicalDeliveryDetails2Rule
If PhysicalDeliveryIndicator is "true" or "1" (Yes), then PhysicalDeliveryDetails must be present.
C31 PhysicalDeliveryDetails2Rule
If PhysicalDeliveryIndicator is "true" or "1" (Yes), then PhysicalDeliveryDetails must be present.
C32 ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present.
If ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
C33 ReceiversIntermediary1DetailsRule
If ReceiversIntermediary2Details is present, then ReceiversIntermediary1Details must be
present. If ReceiversIntermediary2Details is not present, then ReceiversIntermediary1Details is
optional.
C34 SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
C35 TaxElementRule
One of the elements (TaxableIncomePerDividend, EUCapitalGain, EUDividendStatus,
PercentageOfDebtClaim, IndividualTax) must be present.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3826 May 2026
```

