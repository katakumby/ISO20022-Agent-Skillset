---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.3 Constraints"]
file_pages: [1447, 1448, 1449]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
topic_continuations: [{"constraint_ids": ["C22", "C23"], "until_heading": "39.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 1450, "topic": "39.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01051.md"}]
---

# 39.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1447 to 1449.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 39.3 Constraints topic continues in [Constraints continuation C22–C23 (file p1450)](section-01051.md#file-page-1450). Read the text before **39.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 1447

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           Party2 <Pty2> [0..1] ± 1485
           Party3 <Pty3> [0..1] ± 1485
           Party4 <Pty4> [0..1] ± 1486
           Party5 <Pty5> [0..1] ± 1486
       AssetsHeldInOwnName <AsstsHeldInOwnNm> [0..1] Indicator 1487
       TransferResultsInChangeOfBeneficialOwner
<TrfRsltsInChngOfBnfclOwnr>
[0..1] Indicator 1487
       AdditionalInformation <AddtlInf> [0..*] ± 1487
     AdditionalInformation <AddtlInf> [0..*] ± 1487
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 1488
   Extension <Xtnsn> [0..*] ± C12 1488
39.3 Constraints
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
C6 BookTransferGuideline
In the case of an own account internal transfer, the account of (delivering) Party2 at (delivering)
Party1 must be provided.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1447 May 2026
```

## File page 1448

```text
For more details, see the relevant market practice document on www.smpg.info.
C7 Corporate1Rule
If PrimaryCorporateInvestor is not present, then SecondaryCorporateInvestor is not allowed.
If PrimaryCorporateInvestor is present, then SecondaryCorporateInvestor may be present.
On Condition
    /PrimaryCorporateInvestor is absent
Following Must be True
    /SecondaryCorporateInvestor Must be absent
This constraint is defined at the MessageDefinition level.
C8 Corporate2Rule
If PrimaryCorporateInvestor is not present, then OtherCorporateInvestor is not allowed.
If PrimaryCorporateInvestor is present, then OtherCorporateInvestor may be present.
On Condition
    /PrimaryCorporateInvestor is absent
Following Must be True
    /OtherCorporateInvestor[*] Must be absent
This constraint is defined at the MessageDefinition level.
C9 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
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
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1448 May 2026
```

## File page 1449

```text
C12 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C13 IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C14 Investor1Rule
If PrimaryIndividualInvestor is not present, then SecondaryIndividualInvestor is not allowed.
If PrimaryIndividualInvestor is present, then SecondaryIndividualInvestor may be present.
On Condition
    /PrimaryIndividualInvestor is absent
Following Must be True
    /SecondaryIndividualInvestor Must be absent
This constraint is defined at the MessageDefinition level.
C15 Investor2Rule
If PrimaryIndividualInvestor is not present, then OtherIndividualInvestor is not allowed.
If PrimaryIndividualInvestor is present, then OtherIndividualInvestor may be present.
On Condition
    /PrimaryIndividualInvestor is absent
Following Must be True
    /OtherIndividualInvestor[*] Must be absent
This constraint is defined at the MessageDefinition level.
C16 NomineeAccountServicerRule
NomineeAccount/Servicer must be present when and only when different from
TransferorAccount/Servicer.
This constraint is defined at the MessageDefinition level.
C17 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C18 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C19 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C20 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C21 SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1449 May 2026
```

