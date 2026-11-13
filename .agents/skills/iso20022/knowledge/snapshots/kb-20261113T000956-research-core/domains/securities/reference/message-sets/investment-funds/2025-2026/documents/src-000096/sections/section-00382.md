---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.3 Constraints"]
file_pages: [527, 528, 529]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
topic_continuations: [{"constraint_ids": ["C32", "C33", "C34", "C35"], "until_heading": "26.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 530, "topic": "26.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00383.md"}]
---

# 26.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 527 to 529.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 26.3 Constraints topic continues in [Constraints continuation C32–C35 (file p530)](section-00383.md#file-page-530). Read the text before **26.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 527

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         Party5 <Pty5> [0..1] ± 598
     PhysicalTransfer <PhysTrf> [0..1] CodeSet 599
     PhysicalTransferDetails <PhysTrfDtls> [0..1] ± C23 599
     ClientReference <ClntRef> [0..1] ± 600
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 0
   CopyDetails <CpyDtls> [0..1] ± 0
   Extension <Xtnsn> [0..*] ± C18 0
26.3 Constraints
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
C7 BookTransferGuideline
In the case of an own account internal transfer, the account of (delivering) Party2 at (delivering)
Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 527 May 2026
```

## File page 528

```text
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 DepositoryGuideline
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
C16 DiscountElementRule
Amount Or Rate Or Basis must be present.
C17 EffectiveSettlementDateRule
Either TransferDetails/EffectiveSettlementDate may be present in one or more occurrences of
TransferDetails or SettlementDetails/EffectiveSettlementDate may be present, but not both.
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 528 May 2026
```

## File page 529

```text
This constraint is defined at the MessageDefinition level.
C18 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C19 FeeTaxElementRule
One of the elements (CommercialAgreementReference, IndividualFee, IndividualTax) must be
present.
C20 IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C21 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C22 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C23 NameAndAddress1Rule
If RegisteredAddressIndicator is "true" or "1" (Yes), then NameAndAddress is not allowed.
If RegisteredAddressIndicator is "false" or "0" (No), then NameAndAddress must be present.
C24 NonStandardSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
C25 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C26 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C27 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C28 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C29 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C30 PhysicalTransferDetails1Rule
If PhysicalTransfer is PHYS (Physical), then PhysicalTransferDetails must be present.
C31 PhysicalTransferDetails2Rule
If PhysicalTransfer is DEMT (Dematerialised), then PhysicalTransferDetails is not allowed.
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 529 May 2026
```

