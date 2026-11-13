---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.3 Constraints"]
file_pages: [2784, 2785, 2786]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
topic_continuations: [{"constraint_ids": ["C38", "C39", "C40"], "until_heading": "49.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 2787, "topic": "49.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01991.md"}]
---

# 49.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2784 to 2786.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 49.3 Constraints topic continues in [Constraints continuation C38–C40 (file p2787)](section-01991.md#file-page-2787). Read the text before **49.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 2784

```text
49.3 Constraints
C1 AccountElementRule
Either AccountIdentification or Type must be present. Both may be present.
C2 AccountIdentificationRule
If this message is linked to an account opening request and the account identification is not yet
known then the value of the AccountIdentification element in BulkExecutionDetails/
IndividualExecutionDetails/InvestmentAccountDetails must be UNKNOWN.
This constraint is defined at the MessageDefinition level.
C3 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C4 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C5 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C6 AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
C7 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C8 BulkCashSettlementDetailsRule
Either IndividualExecutionDetails/CashSettlementDetails or BulkCashSettlementDetails may be
present, but not both.
C9 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2784 May 2026
```

## File page 2785

```text
Note: The decimal separator is a dot.
C12 DeliverersCustodianRule
If DeliverersIntermediary1Details is present, then DeliverersCustodianDetails must be present.
If DeliverersIntermediary1Details is not present then DeliverersCustodianDetails is optional.
C13 DeliverersIntermediary1DetailsRule
If DeliverersIntermediary2Details is present, then DeliverersIntermediary1Details must be
present. If DeliverersIntermediary2Details is not present then DeliverersIntermediary1Details is
optional.
C14 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C15 DescriptionUsageRule
Description must be used alone as the last resort.
C16 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C17 DiscountElementRule
Amount Or Rate Or Basis must be present.
C18 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C19 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C20 IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C21 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C22 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C23 NonStandardsSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
C24 OrderOriginatorEligibility1Rule
OrderOriginatorEligibility may only be present if Role is either UCL1 (UnderlyingClient1) or
UCL2 (UnderlyingClient2).
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2785 May 2026
```

## File page 2786

```text
C25 OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
C26 OrderOriginatorEligibility3Rule
Either InvestmentAccountDetails/OrderOriginatorEligibility or one or more occurrences of
RelatedPartyDetails/OrderOriginatorEligibility may be present, but not both.
C27 OrderReferenceRule
If this message is not solicited by the receiver, then the value of the OrderReference element in
every occurrence of BulkExecutionDetails/IndividualExecutionDetails must be UNSOLICITED.
This constraint is defined at the MessageDefinition level.
C28 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C29 PersonElementRule
One of the elements (Name, BirthDate, CountryAndResidentialStatus,
BeneficiaryCertificationCompletion, OtherIdentification) must be present.
C30 PhysicalDeliveryDetails1Rule
If PhysicalDeliveryIndicator is "false" or "0" (No), then PhysicalDeliveryDetails is not allowed.
C31 PhysicalDeliveryDetails2Rule
If PhysicalDeliveryIndicator is "true" or "1" (Yes), then PhysicalDeliveryDetails must be present.
C32 PriceDifferenceReasonRule
Any occurrence of InformativePriceDetails/PriceDifferenceReason may not be present.
C33 ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present.
If ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
C34 ReceiversIntermediary1DetailsRule
If ReceiversIntermediary2Details is present, then ReceiversIntermediary1Details must be
present. If ReceiversIntermediary2Details is not present, then ReceiversIntermediary1Details is
optional.
C35 RequestedSettlementCurrencyRule
If RequestedSettlementCurrency is present, it must be the same Currency as in all occurrences
of IndividualExecutionDetails/SettlementAmount.
C36 SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
C37 SettlementCurrencyRule
If BulkCashSettlementDetails is present, then Currency in IndividualExecutionDetails/
SettlementAmount must be the same in all occurrences of IndividualExecutionDetails.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2786 May 2026
```

