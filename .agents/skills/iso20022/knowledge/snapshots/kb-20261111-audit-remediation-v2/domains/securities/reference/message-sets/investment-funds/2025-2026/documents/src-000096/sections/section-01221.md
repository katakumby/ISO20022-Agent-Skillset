---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.3 Constraints"]
file_pages: [1699, 1700, 1701]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
topic_continuations: [{"constraint_ids": ["C31", "C32", "C33", "C34", "C35", "C36", "C37", "C38"], "until_heading": "41.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 1702, "topic": "41.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01222.md"}]
---

# 41.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1699 to 1701.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 41.3 Constraints topic continues in [Constraints continuation C31–C38 (file p1702)](section-01222.md#file-page-1702). Read the text before **41.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 1699

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 1883
             LEI <LEI> [0..1] IdentifierSet 1883
           DrawerIdentification <DrwrId> [0..1] ± 1884
Or         CashAccountDetails <CshAcctDtls> [1..1]  C1 1884
           AccountIdentification <AcctId> [0..1] Text 1884
           Type <Tp> [0..1] ± 1884
Or}         BlockChainCashWallet <BlckChainCshWllt> [1..1]  1885
           Identification <Id> [1..1] Text 1885
           Type <Tp> [0..1] ± 1885
           Name <Nm> [0..1] Text 1885
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1886
   CopyDetails <CpyDtls> [0..1] ± 1886
   Extension <Xtnsn> [0..*] ± C17 0
41.3 Constraints
C1 AccountElementRule
Either AccountIdentification or Type must be present. Both may be present.
C2 AccountIdentificationRule
If this message is linked to an account opening request and the account identification is not yet
known then the value of the AccountIdentification element in BulkOrderDetails/
IndividualOrderDetails/InvestmentAccountDetails must be UNKNOWN.
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
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1699 May 2026
```

## File page 1700

```text
C6 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C7 BulkCashSettlementDetailsRule
Either IndividualOrderDetails/CashSettlementDetails or BulkCashSettlementDetails may be
present, but not both.
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 DeliverersCustodianRule
If DeliverersIntermediary1Details is present, then DeliverersCustodianDetails must be present.
If DeliverersIntermediary1Details is not present then DeliverersCustodianDetails is optional.
C12 DeliverersIntermediary1DetailsRule
If DeliverersIntermediary2Details is present, then DeliverersIntermediary1Details must be
present. If DeliverersIntermediary2Details is not present then DeliverersIntermediary1Details is
optional.
C13 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C14 DescriptionUsageRule
Description must be used alone as the last resort.
C15 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C16 DiscountElementRule
Amount Or Rate Or Basis must be present.
C17 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1700 May 2026
```

## File page 1701

```text
C18 FeeElementRule
One of the elements (Basis, StandardAmount, StandardRate, DiscountDetails,
RequestedAmount, RequestedRate, NonStandardSLAReference, RecipientIdentification) must
be present.
C19 FeeTaxElementRule
One of the elements (CommercialAgreementReference, IndividualFee, IndividualTax,
DigitalNetworkFee) must be present.
C20 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C21 IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C22 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C23 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C24 OrderOriginatorEligibility1Rule
OrderOriginatorEligibility may only be present if Role is either UCL1 (UnderlyingClient1) or
UCL2 (UnderlyingClient2).
C25 OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
C26 OrderOriginatorEligibility3Rule
Either InvestmentAccountDetails/OrderOriginatorEligibility or one or more occurrences of
RelatedPartyDetails/OrderOriginatorEligibility may be present, but not both.
C27 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C28 PersonElementRule
One of the elements (Name, BirthDate, CountryAndResidentialStatus, OtherIdentification) must
be present.
C29 PhysicalDeliveryDetails1Rule
If PhysicalDeliveryIndicator is "false" or "0" (No), then PhysicalDeliveryDetails is not allowed.
C30 PhysicalDeliveryDetails2Rule
If PhysicalDeliveryIndicator is "true" or "1" (Yes), then PhysicalDeliveryDetails must be present.
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1701 May 2026
```

