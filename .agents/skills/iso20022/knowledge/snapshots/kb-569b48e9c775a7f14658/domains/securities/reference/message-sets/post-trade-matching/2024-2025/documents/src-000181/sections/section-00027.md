---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.3 Constraints"]
file_pages: [39, 40, 41, 42, 43, 44]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.3 Constraints

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 39 to 44.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 39

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     StockExchange <StockXchg> [0..1] ± 128
     TradeRegulator <TradRgltr> [0..1] ± 128
     TripartyAgent <TrptyAgt> [0..1] ± 128
     QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± 129
   TwoLegTransactionDetails <TwoLegTxDtls> [0..1]  129
     TradeDate <TradDt> [0..1] ± 130
     OpeningLegIdentification <OpngLegId> [0..1] Text 130
     ClosingLegIdentification <ClsgLegId> [0..1] Text 130
     GrossTradeAmount <GrssTradAmt> [0..1] ± 131
     OtherAmounts <OthrAmts> [0..*] ± 131
     SecondLegNarrative <ScndLegNrrtv> [0..1] Text 133
     EndPrice <EndPric> [0..1] ± 133
     ClosingDate <ClsgDt> [0..1] ± 133
     ClosingSettlementAmount <ClsgSttlmAmt> [0..1] ± 134
     ProcessingDate <PrcgDt> [0..1] ± 134
     TwoLegTransactionType <TwoLegTxTp> [0..1]  134
{Or       FutureOrOptionDetails <FutrOrOptnDtls> [1..1] ± 135
Or}       SecuritiesFinancingDetails <SctiesFincgDtls> [1..1] ± 136
   RegulatoryStipulations <RgltryStiptns> [0..1]  138
     Country <Ctry> [1..1] CodeSet C12 138
     Stipulations <Stiptns> [1..*] Text 138
   SupplementaryData <SplmtryData> [0..*] ± C49 139
3.3 Constraints
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
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 39 February 2025
```

## File page 40

```text
C3 AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information
that can be provided in a structured field.
C4 AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if DeclarationlDetails and/or
PartyContactDetails are present, then they must not contain information that can be provided in
a structured field.
C5 AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be
provided in a structured field unless bilaterally agreed or advised differently in the element
definition as in NarrativeVersion.
C6 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails and
PartyContactDetails must not contain information that can be provided in a structured field.
C7 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C8 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C9 BICNonFI
Valid BICs for non-financial institutions are registered and published by the ISO 9362
Registration Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11)
contiguous characters.
C10 BlockTradeGuideline
In a block trade instruction, the total number of children must be provided using
TotalOfLinkedInstructions.
The CurrentInstructionNumber of the parent must be 000. The children must have an
incremental CurrentInstructionNumber from 001 to 999.
For more details, see the relevant market practice document on www.smpg.info.
C11 CashClearingSystemRule
The CashClearingSystem codes are to be used only by agents directly involved in the
settlement process, such as local settlement agents, CSD's and central banks.
C12 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C13 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 40 February 2025
```

## File page 41

```text
Note: The decimal separator is a dot.
C14 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C15 CurrencyToBuyOrSellRule
CurrencyToBuyOrSell in the TradeDetails message component, provides an instruction to the
account servicer to execute a foreign exchange deal on behalf of the account owner. The
purpose of the forex deal is to fund the purchase of securities. This field is not to be used when
standing instructions have been established.
If CurrencyToSell is used, then it implies the following:
- the instruction is to receive.
- the currency required for funding a purchase of securities, eg, the currency to be purchased,
is the currency of the settlement amount. The currency to be sold to obtain settlement currency
is provided by the currency to sell message element. Normally, this is the base currency of the
portfolio.
- the amount of currency to be bought is equal to the settlement amount of the transaction. This
implies the forex will not be used for other transactions and that a bulk forex deal must be
instructed by other means.
- a forex deal to fund the purchase of securities should be executed in time for the currency to
be available on the settlement date of the securities transaction.
- a bilateral agreement regarding the use of this field has been established.
If CurrencyToBuy is used, then it implies the following:
- the instruction is to delivery
- the currency received as proceeds from the sale of securities, eg, the currency to be sold, is
the currency of the settlement amount. The currency to be bought is provided by the currency
to buy message element. If proceeds are repatriated, this is in the base currency of the
portfolio.
- the amount of currency to be sold is equal to the settlement amount of the transaction. This
implies a bulk forex deal must be instructed by other means.
- a forex deal to repatriate proceeds after the sale of securities should be executed for the
soonest possible value date after settlement of the securities, as permitted by market
convention.
- a bilateral agreement regarding the use of this field has been established.
C16 CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement
instruction, then the CurrentInstructionNumber must be specified.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 41 February 2025
```

## File page 42

```text
C17 CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement
instruction, then the CurrentInstructionNumber must be specified.
C18 DepositoryGuideline
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
C19 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C20 DescriptionUsageRule
Description must be used alone as the last resort.
C21 FXStandingInstructionPresenceRule
If HoldIndicator is present and is value TRUE (Yes), then FXStandingInstruction must not be
present. In ISO 15022, and therefore in ISO 20022, the FXStandingInstruction indicator can
only be used when the transation is instructed in a released mode.
C22 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C23 IdentificationPresenceRule
If Type/Code is not Various (VARI) OR Over The Counter (OTCO) then Identification must be
present. 
C24 IdentificationPresenceRule
If Type/Code is not Various (VARI) OR Over The Counter (OTCO) then Identification must be
present.
C25 IdentificationUsageRule
The presence of Identification and/or CountryOfResidence is mandatory.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 42 February 2025
```

## File page 43

```text
C26 InvestorUsageRule
When investor is used with a country code, the country code specifies the nationality of the
investor, for the settlement of certain securities (i.e. airlines, defence manufacturers) under the
EU legislation.
C27 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C28 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C29 ISO8532AndIssuerSchemeNameRule
If Number is ISO 8532 (Format for transmission of certificate numbers), then Issuer and
SchemeName must not be used.
C30 LinkedIdentificationGuideline
InstructingPartyTransactionIdentification, ExecutingPartyTransactionIdentification,
MarketInfrastructureTransactionIdentification, ClientOrderLinkIdentification, PoolIdentification,
BlockIdentification, AllocationIdentification, IndexIdentification, CommonIdentification and
ComplianceIdentification must not appear more than once in the message.
C31 MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
C32 MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
C33 NumberRule
If Number is negative, then Sign must be present.
C34 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C35 PartialFillsRule
A SecuritiesTradeConfirmation should not be used as a TradeExecution report. PartialFills aims
at providing a for information summary of the different executions that the confirmation
consisted of.
C36 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C37 Party3PresenceRule
If Party3 is present, then Party2 must be present.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 43 February 2025
```

## File page 44

```text
C38 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C39 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C40 PlaceOfListingRule
If PlaceOfListing is used and a ISO 10383 MIC exists for the market to be identified, the ISO
10383 Market Identifier Code (MIC) must be used.
C41 PlaceOfTradeRule
If PlaceOfTrade is used and a ISO 10383 MIC exists for the market to be identified, then the
ISO 10383 Market Identifier Code (MIC) must be used.
C42 PlaceOfTradeRule
If the trade was executed on multiple places of trade and the place of trade field is used, code
VARI must be used.
C43 PlaceOfTradeRule
If the trade was executed on multiple places of trade and the place of trade field is used, code
VARI must be used.
C44 QualifiedForeignIntermediaryRule
If Qualified Foreign Intermediary is used, then the instruction must be a delivery.
C45 SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed
between account owner and account servicer.
C46 SettlementParametersGuideline
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
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 44 February 2025
```

