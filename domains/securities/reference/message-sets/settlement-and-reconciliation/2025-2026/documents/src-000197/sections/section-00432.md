---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12", "20.4 Message Building Blocks", "20.4.2 ConfirmationReference <ConfRef>"]
file_pages: [666, 667, 668]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.026.001.12"]
---

# 20.4.2 ConfirmationReference <ConfRef>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 666 to 668.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 666

```text
TransactionIdentificationDetails <TxIdDtls> contains the following elements (see
"SettlementTypeAndIdentification29" on page 1516 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1517
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1517
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1517
   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 1517
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1518
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1518
   Payment <Pmt> [1..1] CodeSet 1518
   CommonIdentification <CmonId> [0..1] Text 1518
   PoolIdentification <PoolId> [0..1] Text 1518
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 1519
   NonceIdentification <NonceId> [0..1] Text 1519
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
20.4.2 ConfirmationReference <ConfRef>
Presence: [1..1]
Definition: Reference to the unambiguous identification of the confirmation as per the account servicer.
Datatype: "Max35Text" on page 2192
20.4.3 AdditionalParameters <AddtlParams>
Presence: [0..1]
Definition: Additional parameters for the transaction.
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 666 March 2026
```

## File page 667

```text
AdditionalParameters <AddtlParams> contains the following elements (see
"AdditionalParameters30" on page 1629 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PreConfirmation <PreConf> [0..1] CodeSet 1629
   PartialSettlement <PrtlSttlm> [0..1] CodeSet 1629
   TripartyAgentServiceProviderCollateralTransactionIdentifi
cation <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 1629
   ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 1629
20.4.4 TradeDetails <TradDtls>
Presence: [1..1]
Definition: Details of the trade.
Impacted by: C3 "AdditionalDetailsRule", C23 "InvestorCapacityRule", C38 "PlaceOfTradeRule", C59
"TradeDateTimeUTCRule", C58 "TradeDateGuideline"
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 667 March 2026
```

## File page 668

```text
TradeDetails <TradDtls> contains the following SecuritiesTradeDetails150 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeIdentification <TradId> [0..*] Text 669
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 669
   CollateralTransactionIdentification <CollTxId> [0..*] Text 669
   PlaceOfTrade <PlcOfTrad> [0..1] ± 669
   PlaceOfClearing <PlcOfClr> [0..1] ± 669
   TradeDate <TradDt> [0..1] ± 670
   SettlementDate <SttlmDt> [0..1] ± 670
   EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 670
   DealPrice <DealPric> [0..1] ± 670
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C30 671
   OpeningClosing <OpngClsg> [0..1] ± 671
   Reporting <Rptg> [0..*] ± 671
   TradeTransactionCondition <TradTxCond> [0..*] ± 672
   InvestorCapacity <InvstrCpcty> [0..1] ± 672
   TradeOriginatorRole <TradOrgtrRole> [0..1] ± 672
   TypeOfPrice <TpOfPric> [0..1] ± 672
   FXAdditionalDetails <FxAddtlDtls> [0..1] Text 673
   SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 673
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if FXAdditionalDetails and/or
SettlementInstructionProcessingAdditionalDetails are present, then they must not contain information
that can be provided in a structured field.
• InvestorCapacityRule
If InvestorCapacity is used, then the use of the codes needs to be bi-laterally agreed.
• PlaceOfTradeRule
If PlaceOfTrade is used and an ISO 10383 MIC exists for the market to be identified, then the ISO
10383 Market Identifier Code (MIC) must be used.
• TradeDateGuideline
In addition to the settlement date (ISO 20022 mandatory), trade date is one of the 10 common
elements recommended by SMPG for equities and fixed income settlement instructions.
For more details, see the relevant market practice document on www.smpg.info.
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 668 March 2026
```

