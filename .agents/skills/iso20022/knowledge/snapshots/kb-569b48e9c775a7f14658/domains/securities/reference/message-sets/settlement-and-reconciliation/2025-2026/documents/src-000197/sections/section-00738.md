---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["31 sese.037.001.09 PortfolioTransferNotificationV09", "31.3 Constraints"]
file_pages: [1098, 1099, 1100, 1101]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.037.001.09"]
---

# 31.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1098 to 1101.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1098

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       AccruedCapitalisationAmount <AcrdCptlstnAmt> [0..1] ± 1127
     DigitalPaymentSettlement <DgtlPmtSttlm> [0..2]  1127
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C13,
C14,
C17,
C18,
C21
1128
       Quantity <Qty> [1..1]  1129
{Or         ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1129
Or}         NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 1129
       CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1130
{Or         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1130
Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C6 1130
Or}         LEI <LEI> [1..1] IdentifierSet 1130
     OtherBusinessParties <OthrBizPties> [0..1]  C16 1130
       Investor <Invstr> [0..1] ± 1131
       StockExchange <StockXchg> [0..1] ± 1131
       TradeRegulator <TradRgltr> [0..1] ± 1131
     SupplementaryData <SplmtryData> [0..*] ± C37 1132
31.3 Constraints
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
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information
that can be provided in a structured field.
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1098 March 2026
```

## File page 1099

```text
C4 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C5 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C6 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C7 BookTransferGuideline
In the case of an own account internal transfer, own account external transfer, portfolio transfer
and in specie transfer (see SecuritiesTransactionType), the account of (delivering) Party2 at
(delivering) Party1 must be provided.
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
C11 DeliveringParty1Rule
If the instruction is a receive, then DeliveringParty1 must be present.
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
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1099 March 2026
```

## File page 1100

```text
The format and content of the settlement party sequences will comply with the market practices
published for the counterparty depository included in the message.
For more details, see the relevant market practice document on www.smpg.info.
C13 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C14 DescriptionUsageRule
Description must be used alone as the last resort.
C15 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C16 InvestorCountryCodeRule
If Investor is used with a country code, then the country code specifies the nationality of the
investor, for example for the settlement of certain securities (that is airlines, defence
manufacturers) under the EU legislation.
C17 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C18 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C19 ISO8532AndIssuerSchemeNameRule
If Number is ISO 8532 (Format for transmission of certificate numbers), then Issuer and
SchemeName must not be used.
C20 NumberRule
If Number is negative, then Sign must be present.
C21 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C22 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C23 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C24 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C25 Party5PresenceRule
If Party5 is present, then Party4 must be present.
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1100 March 2026
```

## File page 1101

```text
C26 PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO
10383 Market Identifier Code (MIC) must be used.
C27 ReceivingParty1Rule
If the instruction is a delivery, then ReceivingParty 1 must be present.
C28 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
This constraint is defined at the MessageDefinition level.
C29 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C30 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
This constraint is defined at the MessageDefinition level.
C31 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C32 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
This constraint is defined at the MessageDefinition level.
C33 SecuritiesMarketPracticeGroupGuideline
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the use of this message.
These market practices are available on www.smpg.info.
This constraint is defined at the MessageDefinition level.
C34 SettlementAmountRule
If the instruction is against payment, then SettlementAmount must be present.
C35 SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1101 March 2026
```

