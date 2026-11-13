---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13", "19.4 Message Building Blocks", "19.4.2 Linkages <Lnkgs>"]
file_pages: [614, 615, 616]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.025.001.13"]
---

# 19.4.2 Linkages <Lnkgs>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 614 to 616.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 614

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
19.4.2 Linkages <Lnkgs>
Presence: [0..1]
Definition: Link to another transaction - provided for information only.
Linkages <Lnkgs> contains the following elements (see "Linkages41" on page 1545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± 1545
   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 1545
19.4.3 AdditionalParameters <AddtlParams>
Presence: [0..1]
Definition: Additional parameters for the transaction.
Impacted by: C32 "PartialSettlementGuideline"
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 614 March 2026
```

## File page 615

```text
AdditionalParameters <AddtlParams> contains the following elements (see
"AdditionalParameters29" on page 1601 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PreConfirmation <PreConf> [0..1] CodeSet 1602
   PartialSettlement <PrtlSttlm> [0..1] CodeSet 1602
   PreviousPartialConfirmationIdentification
<PrvsPrtlConfId>
[0..1] Text 1602
   TripartyAgentServiceProviderCollateralTransactionIdentifi
cation <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 1602
   ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 1603
   ClientCollateralInstructionIdentification <ClntCollInstrId> [0..1] Text 1603
   TripartyAgentServiceProviderCollateralInstructionIdentific
ation <TrptyAgtSvcPrvdrCollInstrId>
[0..1] Text 1603
Constraints
• PartialSettlementGuideline
Partial settlement information only applies to markets where partial settlement is allowed.
The PartialSettlement field should be used as follows:
- with code PAIN in the first message(s) (there may be more than one) confirming the partial
settlement of an instruction.
- with code PARC in the very last message sent to confirm the settlement of the remaining part.
For more details, see the relevant market practice document on www.smpg.info.
19.4.4 TradeDetails <TradDtls>
Presence: [1..1]
Definition: Details of the trade.
Impacted by: C3 "AdditionalDetailsRule", C23 "InvestorCapacityRule", C39 "PlaceOfTradeRule", C61
"TradeDateTimeUTCRule", C60 "TradeDateGuideline"
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 615 March 2026
```

## File page 616

```text
TradeDetails <TradDtls> contains the following SecuritiesTradeDetails150 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeIdentification <TradId> [0..*] Text 617
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 617
   CollateralTransactionIdentification <CollTxId> [0..*] Text 617
   PlaceOfTrade <PlcOfTrad> [0..1] ± 617
   PlaceOfClearing <PlcOfClr> [0..1] ± 617
   TradeDate <TradDt> [0..1] ± 618
   SettlementDate <SttlmDt> [0..1] ± 618
   EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 618
   DealPrice <DealPric> [0..1] ± 618
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C30 619
   OpeningClosing <OpngClsg> [0..1] ± 619
   Reporting <Rptg> [0..*] ± 619
   TradeTransactionCondition <TradTxCond> [0..*] ± 620
   InvestorCapacity <InvstrCpcty> [0..1] ± 620
   TradeOriginatorRole <TradOrgtrRole> [0..1] ± 620
   TypeOfPrice <TpOfPric> [0..1] ± 620
   FXAdditionalDetails <FxAddtlDtls> [0..1] Text 621
   SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 621
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
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 616 March 2026
```

