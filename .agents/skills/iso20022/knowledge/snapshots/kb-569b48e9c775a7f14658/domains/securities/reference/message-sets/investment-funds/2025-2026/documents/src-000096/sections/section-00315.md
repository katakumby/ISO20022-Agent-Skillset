---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.3 Constraints"]
file_pages: [441, 442, 443]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 441 to 443.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 441

```text
24.3 Constraints
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
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 441 May 2026
```

## File page 442

```text
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
C17 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C18 FeeTaxElementRule
One of the elements (CommercialAgreementReference, IndividualFee, IndividualTax) must be
present.
C19 IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C20 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 442 May 2026
```

## File page 443

```text
C21 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C22 NameAndAddress1Rule
If RegisteredAddressIndicator is "true" or "1" (Yes), then NameAndAddress is not allowed.
If RegisteredAddressIndicator is "false" or "0" (No), then NameAndAddress must be present.
C23 NonStandardSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
C24 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C25 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C26 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C27 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C28 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C29 PhysicalTransferDetails1Rule
If PhysicalTransfer is PHYS (Physical), then PhysicalTransferDetails must be present.
C30 PhysicalTransferDetails2Rule
If PhysicalTransfer is DEMT (Dematerialised), then PhysicalTransferDetails is not allowed.
C31 RequestedSettlementDateRule
Either TransferDetails/RequestedSettlementDate may be present in one or more occurrences
of TransferDetails or SettlementDetails/RequestedSettlementDate may be present, but not
both.
This constraint is defined at the MessageDefinition level.
C32 SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 443 May 2026
```

