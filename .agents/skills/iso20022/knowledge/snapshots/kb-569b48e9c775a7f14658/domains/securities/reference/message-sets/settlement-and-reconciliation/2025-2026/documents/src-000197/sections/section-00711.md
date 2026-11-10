---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10", "30.3 Constraints"]
file_pages: [1063, 1064, 1065]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.036.001.10"]
---

# 30.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1063 to 1065.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1063

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C6, C11,
C21,
C22,
C23,
C24,
C32
1086
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C6, C11,
C21,
C22,
C23,
C24,
C32
1087
   OpeningSettlementAmount <OpngSttlmAmt> [0..1] ± 1089
   OpeningDigitalSettlementAmount <OpngDgtlSttlmAmt> [0..1]  1090
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C12,
C13,
C17,
C18,
C20
1090
     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1091
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1092
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1092
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1092
Or}       LEI <LEI> [1..1] IdentifierSet 1092
   SupplementaryData <SplmtryData> [0..*] ± C35 1092
30.3 Constraints
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
C3 AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1063 March 2026
```

## File page 1064

```text
C4 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C5 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C6 BookTransferGuideline
In case of own account internal transfer, own account external transfer, portfolio transfer and in
specie transfer (see SecuritiesTransactionType), the account of (delivering) Party2 at
(delivering) Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
C7 CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the
settlement process, such as local settlement agents, CSD's and central banks.
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
exists in a particular market, the stock exchange BIC is to be used.
Country code should be used for settlement taking place outside of an institution published in
the PSET's BIC list. This includes physical deliveries and investment funds not settling at a
CSD.
The format and content of the settlement party sequences will comply with the market practices
published for the counterparty depository included in the message.
For more details, see the relevant market practice document on www.smpg.info.
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1064 March 2026
```

## File page 1065

```text
C12 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C13 DescriptionUsageRule
Description must be used alone as the last resort.
C14 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C15 FXStandingInstructionPresenceRule
If HoldIndicator is present and is value TRUE (Yes), then FXStandingInstruction must be
absent.
C16 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C17 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C18 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C19 NumberRule
If Number is negative, then Sign must be present.
C20 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C21 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C22 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C23 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C24 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C25 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C26 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1065 March 2026
```

