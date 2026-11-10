---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.12 CommonIdentification <CmonId>"]
file_pages: [2530, 2531, 2532, 2533, 2534, 2535]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.12 CommonIdentification <CmonId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2530 to 2535.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2530

```text
Datatype: "Max35Text" on page 3328
72.4.3.4.12  CommonIdentification <CmonId>
Presence: [0..1]
Definition: Unique reference agreed upon by the two trade counterparties to identify the trade.
Datatype: "Max35Text" on page 3328
72.4.3.4.13  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 3328
72.4.3.4.14  ClientCollateralInstructionIdentification <ClntCollInstrId>
Presence: [0..1]
Definition: Unique identification assigned to the instruction by the client.
Datatype: "Max35Text" on page 3328
72.4.3.4.15  ClientTripartyCollateralTransactionIdentification <ClntTrptyCollTxId>
Presence: [0..1]
Definition: Unique reference identifying the triparty collateral management transaction from the client's
point of view.
Datatype: "Max35Text" on page 3328
72.4.3.4.16  TripartyAgentServiceProviderCollateralTransactionIdentification
<TrptyAgtSvcPrvdrCollTxId>
Presence: [0..1]
Definition: Unique identification identifying the triparty collateral management transaction from the
triparty-agent's/service-provider's point of view.
Datatype: "Max35Text" on page 3328
72.4.3.4.17  TripartyAgentServiceProviderCollateralInstructionIdentification
<TrptyAgtSvcPrvdrCollInstrId>
Presence: [0..1]
Definition: Unique identification assigned to the instruction by the triparty-agent/service-provider.
Datatype: "Max35Text" on page 3328
72.4.3.4.18  TransactionDetails <TxDtls>
Presence: [0..1]
Definition: Identifies additional details of the transaction.
Impacted by: C5 "AdditionalDetailsRule", C27 "PostingAmountRule", C37
"TwoLegTransactionOpeningClosing1Rule", C38 "TwoLegTransactionOpeningClosing2Rule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2530 August 2026
```

## File page 2531

```text
TransactionDetails <TxDtls> contains the following TransactionDetails187 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionActivity <TxActvty> [1..1] ± 2536
   SettlementTransactionOrCorporateActionEventType
<SttlmTxOrCorpActnEvtTp>
[0..1] ± 2536
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 2537
   Payment <Pmt> [1..1] CodeSet 2537
   SettlementParameters <SttlmParams> [0..1]  C8, C14,
C32,
C33
2537
     HoldIndicator <HldInd> [0..1] ± 2540
     Priority <Prty> [0..1] ± 2540
     SecuritiesTransactionType <SctiesTxTp> [0..1] ± 2540
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 2540
     PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 2541
     BeneficialOwnership <BnfclOwnrsh> [0..1] ± 2541
     BlockTrade <BlckTrad> [0..1] ± 2541
     CCPEligibility <CCPElgblty> [0..1] ± 2542
     DeliveryReturnReason <DlvryRtrRsn> [0..1] ± 2542
     CashClearingSystem <CshClrSys> [0..1] ± 2542
     ExposureType <XpsrTp> [0..1] ± 2542
     FXStandingInstruction <FxStgInstr> [0..1] ± 2543
     MarketClientSide <MktClntSd> [0..1] ± 2543
     NettingEligibility <NetgElgblty> [0..1] ± 2543
     Registration <Regn> [0..1] ± 2543
     RepurchaseType <RpTp> [0..1] ± 2544
     LegalRestrictions <LglRstrctns> [0..1] ± 2544
     SecuritiesRTGS <SctiesRTGS> [0..1] ± 2544
     SettlingCapacity <SttlgCpcty> [0..1] ± 2544
     SettlementSystemMethod <SttlmSysMtd> [0..1] ± 2545
     TaxCapacity <TaxCpcty> [0..1] ± 2545
     StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 2545
     Tracking <Trckg> [0..1] ± 2545
     AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 2546
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2531 August 2026
```

## File page 2532

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     LetterOfGuarantee <LttrOfGrnt> [0..1] ± 2546
     ReturnLeg <RtrLeg> [0..1] Indicator 2546
     ModificationCancellationAllowed <ModCxlAllwd> [0..1] ± 2546
     EligibleForCollateral <ElgblForColl> [0..1] Indicator 2547
     SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 2547
     CashSubBalanceType <CshSubBalTp> [0..1] ± 2547
   PlaceOfTrade <PlcOfTrad> [0..1] ± 2547
   SafekeepingPlace <SfkpgPlc> [0..1] ± C31 2548
   PlaceOfClearing <PlcOfClr> [0..1] ± 2548
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
C16,
C20
2548
   CountryOfIssue <CtryOfIsse> [0..1] CodeSet C9 2549
   ConditionalSecuritiesDelivery <CondlSctiesDlvry> [0..1] Indicator 2550
   SettlementQuantity <SttlmQty> [1..1] ± 2550
   SettledQuantity <SttldQty> [0..1] ± 2550
   PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± 2551
   RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± 2551
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C19 2551
   SettlementAmount <SttlmAmt> [1..1] ± 2551
   SettledAmount <SttldAmt> [0..1] ± 2552
   PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 2552
   RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 2552
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 2552
   TradeDate <TradDt> [0..1] ± 2553
   IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 2553
   EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 2553
   ValueDate <ValDt> [0..1] ± 2554
   StatusDate <StsDt> [0..1] DateTime 2554
   AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 2554
   MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 2554
   Linkages <Lnkgs> [0..*]  2554
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2532 August 2026
```

## File page 2533

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     ProcessingPosition <PrcgPos> [0..1] ± C39 2555
     MessageNumber <MsgNb> [0..1] ± C35 2555
     Reference <Ref> [1..1]  2556
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 2556
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 2556
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 2557
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2557
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2557
Or       PoolIdentification <PoolId> [1..1] Text 2557
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 2557
     ReferenceOwner <RefOwnr> [0..1] ± 2557
   Priority <Prty> [0..1] ± 2558
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
2558
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
2559
   ReversalIndicator <RvslInd> [0..1] Indicator 2560
   MessageOriginator <MsgOrgtr> [0..1] ± 2560
   CreationDateTime <CreDtTm> [1..1] DateTime 2560
   TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 2560
   SupplementaryData <SplmtryData> [0..*] ± C36 2560
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if TransactionAdditionalDetails is present,
then it must not contain information that can be provided in a structured field.
• PostingAmountRule
If the instruction is against payment, PostingAmount must be present.
.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2533 August 2026
```

## File page 2534

```text
• TwoLegTransactionOpeningClosing1Rule
For settlement of two parts transactions (Securities Financing), the opening/initiation and closing/
return of the transaction is confirmed by sending the below combination of SecuritiesMovementType
codes and SettlementParameters/SecuritiesTransactionType codes:
Repo Opening
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: Repo (REPU)
Repo Closing
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: Repo (REPU)
Reverse Repo Opening
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: ReverseRepo (RVPO)
Reverse Repo Closing
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: ReverseRepo (RVPO)
TriParty Repo Opening
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: TriPartyRepo (TRPO)
TriParty Repo Closing
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: TriPartyRepo (TRPO)
TriParty Reverse Repo Opening
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: TriPartyReverseRepo (TRVO)
TriParty Reverse Repo Closing
SecuritiesMovementType: Delivery (DELI)
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2534 August 2026
```

## File page 2535

```text
SettlementParameters/SecuritiesTransactionType: TriPartyReverseRepo (TRVO)
Securities Lending Initiation
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SecuritiesLending (SECL)
Securities Lending Return
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SecuritiesLending (SECL)
Securities Borrowing Initiation
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB)
Securities Borrowing Return
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB).
• TwoLegTransactionOpeningClosing2Rule
For settlement of two parts transactions (buy-sell back, sell buy-back, collateral in and out), the
opening/initiation and closing/return of the transaction is confirmed by sending the below combination
of SecuritiesMovementType codes and SettlementParameters/SecuritiesTransactionType codes:
Sell-Buy Back: Sell
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SellBuyBack (SBBK)
Sell-Buy Back: Buy Back
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SellBuyBack (SBBK)
Buy-Sell Back: Buy
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: BuySellBack (BSBK)
Buy-Sell Back: Sell Back
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2535 August 2026
```

