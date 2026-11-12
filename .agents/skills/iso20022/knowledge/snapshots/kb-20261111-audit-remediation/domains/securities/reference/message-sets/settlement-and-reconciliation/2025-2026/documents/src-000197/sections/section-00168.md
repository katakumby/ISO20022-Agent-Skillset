---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.6 IntermediaryInformation <IntrmyInf>", "8.4.7.7 Transaction <Tx>", "8.4.7.7.19 TransactionDetails <TxDtls>", "8.4.7.7.19.22 ReversalIndicator <RvslInd>"]
file_pages: [242, 243, 244]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.7.7.19.22 ReversalIndicator <RvslInd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 242 to 244.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 242

```text
8.4.7.7.19.22  ReversalIndicator <RvslInd>
Presence: [0..1]
Definition: Indicates whether it is the reversal of a previously reported movement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
8.4.7.7.19.23  TransactionAdditionalDetails <TxAddtlDtls>
Presence: [0..1]
Definition: Provides additional details on the transaction which cannot be included within the structured
fields of the message.
Datatype: "Max350Text" on page 2192
8.4.7.7.20  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C42 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1565
   Envelope <Envlp> [1..1] (External Schema) 1565
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
8.4.8 SubAccountDetails <SubAcctDtls>
Presence: [0..*]
Definition: Details at sub-account level.
Impacted by: C30 "SafekeepingAccountOrBlockChainAddress1Rule", C33
"SafekeepingAccountOrBlockChainAddress2Rule"
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 242 March 2026
```

## File page 243

```text
SubAccountDetails <SubAcctDtls> contains the following SubAccountIdentification74 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1] ± 245
   SafekeepingAccount <SfkpgAcct> [0..1] ± 245
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 246
   ActivityIndicator <ActvtyInd> [1..1] Indicator 246
   FinancialInstrumentDetails <FinInstrmDtls> [0..*]  246
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C14,
C15,
C20
249
     InvestmentFundsFinancialInstrumentAttributes
<InvstmtFndsFinInstrmAttrbts>
[0..1] ± 250
     PriceDetails <PricDtls> [0..1] ± C47 250
     SafekeepingPlace <SfkpgPlc> [0..1] ± C35 251
     OpeningBalance <OpngBal> [0..1] ± C38 251
     ClosingBalance <ClsgBal> [0..1] ± C39 251
     Transaction <Tx> [1..*]  C18 252
       AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 255
       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 255
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 255
       CounterpartyMarketInfrastructureTransactionIdenti
fication <CtrPtyMktInfrstrctrTxId>
[0..1] Text 255
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 255
       TradeIdentification <TradId> [0..*] Text 255
       UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 255
       PoolIdentification <PoolId> [0..1] Text 256
       CommonIdentification <CmonId> [0..1] Text 256
       CorporateActionEventIdentification
<CorpActnEvtId>
[0..1] Text 256
       TripartyAgentServiceProviderCollateralTransaction
Identification <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 256
       ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 256
       ClientCollateralInstructionIdentification
<ClntCollInstrId>
[0..1] Text 256
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 243 March 2026
```

## File page 244

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       TripartyAgentServiceProviderCollateralInstructionI
dentification <TrptyAgtSvcPrvdrCollInstrId>
[0..1] Text 256
       MasterReference <MstrRef> [0..1] Text 256
       ClientReference <ClntRef> [0..1] ± 257
       AccountOwnerLegIdentification <AcctOwnrLegId> [0..1] Text 257
       AccountServicerLegIdentification <AcctSvcrLegId> [0..1] Text 257
       TransactionDetails <TxDtls> [0..1]  C3, C26,
C44,
C46
257
         TransactionActivity <TxActvty> [1..1] ± 262
         SettlementTransactionOrCorporateActionEventTy
pe <SttlmTxOrCorpActnEvtTp>
[0..1] ± 262
         SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 262
         Payment <Pmt> [1..1] CodeSet 262
         SettlementParameters <SttlmParams> [0..1] ± C5, C37 263
         PlaceOfTrade <PlcOfTrad> [0..1] ± 264
         SafekeepingPlace <SfkpgPlc> [0..1] ± C35 264
         PlaceOfClearing <PlcOfClr> [0..1] ± 264
         PostingQuantity <PstngQty> [1..1] ± 265
         NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C19 265
         PostingAmount <PstngAmt> [0..1] ± 265
         DigitalPaymentPostingSettlement
<DgtlPmtPstngSttlm>
[0..1]  265
           FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C14,
C15,
C20
266
           ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 267
           CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  267
{Or             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 267
Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C4 267
Or}             LEI <LEI> [1..1] IdentifierSet 268
         AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 268
         TradeDate <TradDt> [0..1] ± 268
         EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 268
         SettlementDate <SttlmDt> [0..1] ± 269
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 244 March 2026
```

