---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.3 Constraints"]
file_pages: [166, 167, 168, 169]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.3 Constraints

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 166 to 169.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 166

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     Seller <Sellr> [0..1] ± 201
     Lender <Lndr> [0..1] ± 202
     BrokerOfCredit <BrkrOfCdt> [0..1] ± 203
     IntroducingFirm <IntrdcgFirm> [0..1] ± 204
     StepInFirm <StepInFirm> [0..1] ± 205
     StepOutFirm <StepOutFirm> [0..1] ± 206
     ClearingFirm <ClrFirm> [0..1] ± 207
     ExecutingBroker <ExctgBrkr> [0..1] ± 208
     AffirmingParty <AffrmgPty> [0..1] ± 209
     TradeBeneficiaryParty <TradBnfcryPty> [0..1] ± 210
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C28,
C29,
C30,
C31,
C12
211
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C28,
C29,
C30,
C31,
C12
216
   SupplementaryData <SplmtryData> [0..*] ± C37 221
6.3 Constraints
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
C3 AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be
provided in a structured field unless bilaterally agreed or advised differently in the element
definition as in NarrativeVersion.
C4 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 166 February 2025
```

## File page 167

```text
C5 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C6 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails and
PartyContactDetails must not contain information that can be provided in a structured field.
C7 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 CurrencyToBuyOrSellRule
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
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 167 February 2025
```

## File page 168

```text
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
C12 DepositoryGuideline
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
C13 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C14 DescriptionUsageRule
Description must be used alone as the last resort.
C15 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C16 IdentificationPresenceRule
If Type/Code is not Various (VARI) OR Over The Counter (OTCO) then Identification must be
present. 
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 168 February 2025
```

## File page 169

```text
C17 IdentificationPresenceRule
If Type/Code is not Various (VARI) OR Over The Counter (OTCO) then Identification must be
present.
C18 IdentificationUsageRule
The presence of Identification and/or CountryOfResidence is mandatory.
C19 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C20 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C21 ISO8532AndIssuerSchemeNameRule
If Number is ISO 8532 (Format for transmission of certificate numbers), then Issuer and
SchemeName must not be used.
C22 LinkedIdentificationGuideline
InstructingPartyTransactionIdentification, ExecutingPartyTransactionIdentification,
MarketInfrastructureTransactionIdentification, ClientOrderLinkIdentification, PoolIdentification,
BlockIdentification, AllocationIdentification, IndexIdentification, CommonIdentification,
ComplianceIdentification and CancellationRequestIdentification must not appear more than
once in the message.
C23 MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
C24 MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
C25 NumberRule
If Number is negative, then Sign must be present.
C26 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C27 PartialFillsRule
A SecuritiesTradeConfirmation should not be used as a TradeExecution report. PartialFills aims
at providing a for information summary of the different executions that the confirmation
consisted of.
C28 Party2PresenceRule
If Party2 is present, then Party1 must be present.
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 169 February 2025
```

