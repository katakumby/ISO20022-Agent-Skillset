---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "17.3 Constraints"]
file_pages: [497, 498, 499, 500, 501, 502, 503, 504, 505, 506]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.023.001.13"]
---

# 17.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 497 to 506.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 497

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  547
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 548
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C8 548
Or}       LEI <LEI> [1..1] IdentifierSet 548
   OtherBusinessParties <OthrBizPties> [0..1]  C33,
C51
548
     Investor <Invstr> [0..*] ± C31,
C56,
C60
549
     QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C57,
C61
550
     StockExchange <StockXchg> [0..1] ± 551
     TradeRegulator <TradRgltr> [0..1] ± 551
     TripartyAgent <TrptyAgt> [0..1] ± C57,
C61
551
     Broker <Brkr> [0..1] ± C57,
C61
552
   AdditionalPhysicalOrRegistrationDetails
<AddtlPhysOrRegnDtls>
[0..1]  0
     CertificationIdentification <CertfctnId> [0..1] Text 554
     CertificationDateTime <CertfctnDtTm> [0..1] ± 554
     RegistrarAccount <RegarAcct> [0..1] Text 554
     CertificateNumber <CertNb> [0..*] ± C36 554
   SupplementaryData <SplmtryData> [0..*] ± C74 554
17.3 Constraints
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
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 497 March 2026
```

## File page 498

```text
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
C6 AdditionalPhysicalOrRegistrationDetailsRule
If AdditionalPhysicalOrRegistrationDetails is present, then the instruction must be free of
payment.
This constraint is defined at the MessageDefinition level.
C7 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C8 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C9 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C10 BlockTradeGuideline
In a block trade instruction, the total number of children must be provided using
TotalOfLinkedInstructions.
The CurrentInstructionNumber of the parent must be 000000. The children must have an
incremental CurrentInstructionNumber from 1 to 999999.
For more details, see the relevant market practice document on www.smpg.info.
C11 BookTransferGuideline
In case of own account internal transfer, own account external transfer, portfolio transfer and in
specie transfer (see SecuritiesTransactionType), the account of (delivering) Party2 at
(delivering) Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 498 March 2026
```

## File page 499

```text
C12 BuyerSSIRule
If standing settlement instruction applies and the instruction is a delivery, then Buyer must be
present.
On Condition
    /SettlementTypeAndAdditionalParameters/SecuritiesMovementType is equal to 
value 'Delivery'
 And    /StandingSettlementInstructionDetails is present
Following Must be True
    /StandingSettlementInstructionDetails/Counterparty/Buyer Must be present
This constraint is defined at the MessageDefinition level.
C13 BuyToCoverRule
If SettlementParameters/SettlementTransactionCondition BuyToCover (BUTC) is present then
at least one Linkage must be present with the reference of the sell instruction (may be more
than one) to be covered by the concerned buy.
This constraint is defined at the MessageDefinition level.
C14 CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the
settlement process, such as local settlement agents, CSDs and central banks.
C15 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C16 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C17 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C18 CurrencyToBuyOrSellRule
CurrencyToBuy and CurrencyToSell in the TradeDetails message component, provides an
instruction to the account servicer to execute a foreign exchange deal on behalf of the account
owner. The purpose of the forex deal is to fund the purchase of securities. This field is not to be
used when standing instructions have been established.
If CurrencyToSell is used, then it implies the following:
- the instruction is a receive.
- the currency required for funding a purchase of securities, for example, the currency to be
purchased, is the currency of the settlement amount. The currency to be sold to obtain
settlement currency is provided by the currency to sell message element. Normally, this is the
base currency of the portfolio.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 499 March 2026
```

## File page 500

```text
- the amount of currency to be bought is equal to the settlement amount of the transaction. This
implies the forex will not be used for other transactions and that a bulk forex deal must be
instructed by other means.
- a forex deal to fund the purchase of securities should be executed in time for the currency to
be available on the settlement date of the securities transaction.
- a bilateral agreement regarding the use of this field has been established.
If CurrencyToBuy is used, then it implies the following:
- the instruction is a delivery
- the currency received as proceeds from the sale of securities, for example, the currency to be
sold, is the currency of the settlement amount. The currency to be bought is provided by the
currency to buy message element. If proceeds are repatriated, this is in the base currency of
the portfolio.
- the amount of currency to be sold is equal to the settlement amount of the transaction. This
implies a bulk forex deal must be instructed by other means.
- a forex deal to repatriate proceeds after the sale of securities should be executed for the
soonest possible value date after settlement of the securities, as permitted by market
convention.
- a bilateral agreement regarding the use of this field has been established.
C19 CurrencyToBuyRule
If CurrencyToBuy is present then the instruction must be a delivery.
On Condition
    /SettlementTypeAndAdditionalParameters/SecuritiesMovementType is equal to 
value 'Receive'
Following Must be True
    /TradeDetails/CurrencyToBuyOrSell/CurrencyToBuy Must be absent
This constraint is defined at the MessageDefinition level.
C20 CurrencyToSellRule
If CurrencyToSell is present then the instruction must be a receive.
On Condition
    /SettlementTypeAndAdditionalParameters/SecuritiesMovementType is equal to 
value 'Delivery'
Following Must be True
    /TradeDetails/CurrencyToBuyOrSell/CurrencyToSell Must be absent
This constraint is defined at the MessageDefinition level.
C21 CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement
instruction, then the CurrentInstructionNumber must be specified.
C22 CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement
instruction, then the CurrentInstructionNumber must be specified.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 500 March 2026
```

## File page 501

```text
C23 DeliveringDepositoryAndParty1Rule
If the instruction is a receive and no standing settlement instruction applies, then
DeliveringDepository and Party1 must be present.
On Condition
    /SettlementTypeAndAdditionalParameters/SecuritiesMovementType is equal to 
value 'Receive'
 And    /StandingSettlementInstructionDetails is absent
Following Must be True
    /DeliveringSettlementParties/Depository Must be present
 And    /DeliveringSettlementParties/Party1 Must be present
This constraint is defined at the MessageDefinition level.
C24 DenominationRule
Unless bilaterally agreed between the account owner and servicer, if DenominationChoice is
used, it must not contain information that can be provided in a structured field.
C25 DepositoryGuideline
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
C26 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C27 DescriptionUsageRule
Description must be used alone as the last resort.
C28 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C29 FXStandingInstructionPresenceRule
If HoldIndicator is present and is value TRUE (Yes), then FXStandingInstruction must not be
present. In ISO 15022,
and therefore in ISO 20022, the FXStandingInstruction indicator can only be used when the
transation is instructed
in a released mode.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 501 March 2026
```

## File page 502

```text
C30 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C31 IdentificationNationalityOfInvestorRule
Identification and/or Nationality must be present.
C32 InvestorCapacityRule
If InvestorCapacity is used, then the use of the codes needs to be bi-laterally agreed.
C33 InvestorCountryCodeRule
If Investor is used with a country code, then the country code specifies the nationality of the
investor, for example, for the settlement of certain securities (that is, airlines, defence
manufacturers) under the EU legislation.
C34 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C35 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C36 ISO8532AndIssuerSchemeNameRule
If Number is ISO 8532 (Format for transmission of certificate numbers), then Issuer and
SchemeName must not be used.
C37 LateDeliveryDateRule
If LateDeliveryDate is used, then the transaction must be a pool trade that results from the
original TBA (To Be Announced). The original TBA would be offset by an opposite transaction
and replaced by buys or sells of individual pools. It is a date greater than the settlement date
stated in the trade, for pools designed as settling late.
C38 LinkageGuideline
Global market practice rules on the use of the linkages exists for various business scenarios
such as cancellations, settlement confirmation but also more complex processes like pair-off,
back-to-back, block trades, sell-buy back, buy-sell back, securities lending and borrowing.
For more details, see the relevant market practice documents on www.smpg.info.
This constraint is defined at the MessageDefinition level.
C39 LinkedQuantityRule
If linked quantity for partial pair-off and turned quantity for partial turns is used, then its usage
must be pre-agreed between the message account owner and account servicer.
C40 MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 502 March 2026
```

## File page 503

```text
C41 NetworkFeeCashSettlementQuantityRule
The network fee quantity can appear in only one occurence of Digital Cash Payment.
The cash settlement quantity can appear in only one occurence of Digital Cash Payment.
This constraint is defined at the MessageDefinition level.
C42 NumberRule
If Number is negative, then Sign must be present.
C43 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C44 PairOffTurnRule
If LinkedQuantity is present in minimum one occurrence of Linkages, then the type of
settlement transaction must be a pair-off or a turnaround, that is, SettlementParameters/
SecuritiesTransactionType must be PAIR or TURN.
On Condition
    /Linkages[*]/LinkedQuantity is present
Following Must be True
    /SettlementParameters/SecuritiesTransactionType/Code Must be equal to 
value 'PairOff'
 Or    /SettlementParameters/SecuritiesTransactionType/Code Must be equal to 
value 'Turnaround'
This constraint is defined at the MessageDefinition level.
C45 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C46 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C47 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C48 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C49 PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO
10383 Market Identifier Code (MIC) must be used.
C50 PlaceOfTradeRule
If PlaceOfTrade is used and an ISO 10383 MIC exists for the market to be identified, then the
ISO 10383 Market Identifier Code (MIC) must be used.
C51 QualifiedForeignIntermediaryRule
If Qualified Foreign Intermediary is used, then the instruction must be a delivery.
C52 ReceivingDepositoryAndParty1Rule
If the instruction is a delivery and no standing settlement instruction applies, then
ReceivingDepository and Party1 must be present.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 503 March 2026
```

## File page 504

```text
On Condition
    /SettlementTypeAndAdditionalParameters/SecuritiesMovementType is equal to 
value 'Delivery'
 And    /StandingSettlementInstructionDetails is absent
Following Must be True
    /ReceivingSettlementParties/Depository Must be present
 And    /ReceivingSettlementParties/Party1 Must be present
This constraint is defined at the MessageDefinition level.
C53 RegistrationDetailsRule
If SettlementParameters/Registration is present with code YREG (Registration to take place),
then additional registration details must be specified in the AdditonalInformation/
RegistrationDetails field of the Party (Receiving or DeliveringSettlementParties) under whom
the registration must take place, unless this information is already available at the account
servicer via standing instruction/SLA.
This constraint is defined at the MessageDefinition level.
C54 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C55 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C56 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C57 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C58 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C59 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C60 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C61 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C62 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C63 SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
C64 SafekeepingPlaceGuideline
When used (see usage rule SafekeepingPlaceRule), unless special arrangements exist
between the account servicer and the account owner, it is recommended to use the place of
safekeeping field following the market practice described below:
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 504 March 2026
```

## File page 505

```text
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
C65 SafekeepingPlaceRule
The SafekeepingPlace functionality in the settlement instructions is only to be used for global
custodians that allow their clients to specify where the securities are to be held, for example, in
an ICSD account versus an account at the local CSD.
C66 SecuritiesFinancingSettlementRule
In the framework of Securities Financing (repo, reverse repo, sec lending, sec borrowing), the
SettlementInstruction can only be used for the plain vanilla settlement of the opening leg and
closing leg.
This constraint is defined at the MessageDefinition level.
C67 SecuritiesMarketPracticeGroupGuideline
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the use of this message.
These market practices are available on www.smpg.info.
This constraint is defined at the MessageDefinition level.
C68 SellerSSIRule
If standing settlement instruction applies and the instruction is a receipt, then Seller must be
present.
On Condition
    /SettlementTypeAndAdditionalParameters/SecuritiesMovementType is equal to 
value 'Receive'
 And    /StandingSettlementInstructionDetails is present
Following Must be True
    /StandingSettlementInstructionDetails/Counterparty/Seller Must be present
This constraint is defined at the MessageDefinition level.
C69 SettlementAmountRule
If the instruction is against payment, then SettlementAmount must be present.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 505 March 2026
```

## File page 506

```text
On Condition
    /SettlementTypeAndAdditionalParameters/Payment is equal to value 
'AgainstPaymentSettlement'
Following Must be True
    /SettlementAmount Must be present
This constraint is defined at the MessageDefinition level.
C70 SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.
C71 SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed
between account owner and account servicer.
C72 SettlementParametersGuideline
• Physical settlement:
In case of physical receipt at local agent level, the receiving agent must receive a receipt free
instruction
for reconciliation purposes. If the final beneficiary of the securities uses a global custodian, the
receipt free
instruction will be sent to the global custodian that will forward it to his receiving agent on the
market.
For physical settlement, SettlementTransactionCondition/Physical must be used.
• Partial settlement:
This market practice only applies in markets where partial settlement is allowed.
If an account owner wants to specify in its original instruction that partial settlement is allowed
or not, they
must use the PartialSettlementIndicator.
• Book Transfer:
The use of SecuritiesTransactionTypes OWNI, OWNE, INSP and PORT and other booktransfer
related fields is governed by a market practice document.
• Block Trades:
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 506 March 2026
```

