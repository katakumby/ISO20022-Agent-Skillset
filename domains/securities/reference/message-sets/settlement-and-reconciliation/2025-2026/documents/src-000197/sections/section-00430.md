---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12", "20.3 Constraints"]
file_pages: [659, 660, 661, 662, 663, 664]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.026.001.12"]
---

# 20.3 Constraints

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 659 to 664.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 659

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     Broker <Brkr> [0..1] ± C44,
C48
705
   AdditionalPhysicalOrRegistrationDetails
<AddtlPhysOrRegnDtls>
[0..1]  0
     CertificationIdentification <CertfctnId> [0..1] Text 706
     CertificationDateTime <CertfctnDtTm> [0..1] ± 706
     RegistrarAccount <RegarAcct> [0..1] Text 706
     CertificateNumber <CertNb> [0..*] ± C27 706
   SupplementaryData <SplmtryData> [0..*] ± C57 707
20.3 Constraints
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
Unless bilaterally agreed between the sender and receiver, if FXAdditionalDetails and/or
SettlementInstructionProcessingAdditionalDetails are present, then they must not contain
information that can be provided in a structured field.
C4 AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information
that can be provided in a structured field.
C5 AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if DeclarationlDetails and/or
PartyContactDetails are present, then they must not contain information that can be provided in
a structured field.
C6 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 659 March 2026
```

## File page 660

```text
C7 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C8 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C9 BookTransferGuideline
In case of own account internal transfer, own account external transfer, portfolio transfer and in
specie transfer (see SecuritiesTransactionType), the account of (delivering) Party2 at
(delivering) Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
C10 BuyerSSIRule
If standing settlement instruction applies and the instruction is a delivery, then Buyer must be
present.
On Condition
    /TransactionIdentificationDetails/SecuritiesMovementType is equal to 
value 'Delivery'
 And    /StandingSettlementInstructionDetails is present
Following Must be True
    /StandingSettlementInstructionDetails/Counterparty/Buyer Must be present
This constraint is defined at the MessageDefinition level.
C11 CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the
settlement process, such as local settlement agents, CSDs and central banks.
C12 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C13 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C14 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C15 DeliveringDepositoryAndParty1Rule
If the instruction is a receive and no standing settlement instruction applies, then
DeliveringDepository and Party1 must be present.
On Condition
    /TransactionIdentificationDetails/SecuritiesMovementType is equal to 
value 'Receive'
 And    /StandingSettlementInstructionDetails is absent
Following Must be True
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 660 March 2026
```

## File page 661

```text
    /DeliveringSettlementParties/Depository Must be present
 And    /DeliveringSettlementParties/Party1 Must be present
This constraint is defined at the MessageDefinition level.
C16 DenominationRule
Unless bilaterally agreed between the account owner and servicer, if DenominationChoice is
used, it must not contain information that can be provided in a structured field.
C17 DepositoryGuideline
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
C18 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C19 DescriptionUsageRule
Description must be used alone as the last resort.
C20 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C21 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C22 IdentificationNationalityOfInvestorRule
Identification and/or Nationality must be present.
C23 InvestorCapacityRule
If InvestorCapacity is used, then the use of the codes needs to be bi-laterally agreed.
C24 InvestorCountryCodeRule
If Investor is used with a country code, then the country code specifies the nationality of the
investor, for example, for the settlement of certain securities (that is, airlines, defence
manufacturers) under the EU legislation.
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 661 March 2026
```

## File page 662

```text
C25 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C26 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C27 ISO8532AndIssuerSchemeNameRule
If Number is ISO 8532 (Format for transmission of certificate numbers), then Issuer and
SchemeName must not be used.
C28 MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
C29 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be
NONREF.
C30 NumberRule
If Number is negative, then Sign must be present.
C31 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C32 PartialSettlementGuideline
Partial settlement information only applies to markets where partial settlement is allowed.
The SettledQuantity field provides the quantity of securities effectively settled.
The other quantities (PreviouslySettledQuantity and/or RemainingToBeSettledQuantity) may be
provided, but this is not mandatory.
For more details, see the relevant market practice document on www.smpg.info.
C33 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C34 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C35 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C36 Party5PresenceRule
If Party5 is present, then Party4 must be present.
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 662 March 2026
```

## File page 663

```text
C37 PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO
10383 Market Identifier Code (MIC) must be used.
C38 PlaceOfTradeRule
If PlaceOfTrade is used and an ISO 10383 MIC exists for the market to be identified, then the
ISO 10383 Market Identifier Code (MIC) must be used.
C39 QualifiedForeignIntermediaryRule
If Qualified Foreign Intermediary is used, then the instruction must be a delivery.
C40 ReceivingDepositoryAndParty1Rule
If the instruction is a delivery and no standing settlement instruction applies, then
ReceivingDepository and Party1 must be present.
On Condition
    /TransactionIdentificationDetails/SecuritiesMovementType is equal to 
value 'Delivery'
 And    /StandingSettlementInstructionDetails is absent
Following Must be True
    /ReceivingSettlementParties/Depository Must be present
 And    /ReceivingSettlementParties/Party1 Must be present
This constraint is defined at the MessageDefinition level.
C41 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C42 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C43 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C44 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C45 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C46 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C47 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C48 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C49 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C50 SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 663 March 2026
```

## File page 664

```text
C51 SafekeepingPlaceGuideline
When used (see usage rule SafekeepingPlaceRule), unless special arrangements exist
between the account servicer and the account owner, it is recommended to use the place of
safekeeping field following the market practice described below:
• SafekeepingPlaceType/SharesHeldAtNCSD: a NCSD's BIC will be used for domestic and
NCSD to NCSD settlement instructions.
• SafekeepingPlaceType/SharesHeldAtICSD: an ICSD's BIC will be used for ICSD internal,
ICSD/local and ICSD to ICSD settlement instructions.
• SafekeepingPlaceType/SharesHeldAtLoaclCustodian: applicable, for instance, when the
account servicer is a global custodian and provides the account owner with a position reporting
at global custodian's agents' level. When instructing, the fund manager would therefore
mention, as a place of safekeeping, the BIC of the global custodian's agent on the market.
Absence of SafekeepingPlace means that:
• The SafekeepingPlace information is kept by the account servicer (SLA, account structure,
ETC.) and should not be provided by the account owner.
• The SafekeepingPlace is the counterparty's Depository. The transaction is therefore domestic
(to an NCSD) or internal to an ICSD.
For more details, see the relevant market practice document on www.smpg.info.
C52 SafekeepingPlaceRule
The SafekeepingPlace functionality in the settlement instructions is only to be used for global
custodians that allow their clients to specify where the securities are to be held, for example, in
an ICSD account versus an account at the local CSD.
C53 SellerSSIRule
If standing settlement instruction applies and the instruction is a receipt, then Seller must be
present.
On Condition
    /TransactionIdentificationDetails/SecuritiesMovementType is equal to 
value 'Receive'
 And    /StandingSettlementInstructionDetails is present
Following Must be True
    /StandingSettlementInstructionDetails/Counterparty/Seller Must be present
This constraint is defined at the MessageDefinition level.
C54 SettledAmountRule
If the instruction is against payment, then SettledAmount must be present.
On Condition
    /TransactionIdentificationDetails/Payment is equal to value 
'AgainstPaymentSettlement'
Following Must be True
    /SettledAmount Must be present
This constraint is defined at the MessageDefinition level.
C55 SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 664 March 2026
```

