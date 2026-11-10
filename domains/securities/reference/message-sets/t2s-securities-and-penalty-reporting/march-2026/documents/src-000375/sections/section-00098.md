---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.12 CommonIdentification <CmonId>"]
file_pages: [134, 135, 136, 137, 138, 139]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.12 CommonIdentification <CmonId>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 134 to 139.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 134

```text
Datatype: "Max35Text" on page 557
4.4.3.4.12  CommonIdentification <CmonId>
Presence: [0..1]
Definition: Unique reference agreed upon by the two trade counterparties to identify the trade.
Datatype: "Max35Text" on page 557
4.4.3.4.13  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 557
4.4.3.4.14  ClientCollateralInstructionIdentification <ClntCollInstrId>
Presence: [0..1]
Definition: Unique identification assigned to the instruction by the client.
Datatype: "Max35Text" on page 557
4.4.3.4.15  ClientTripartyCollateralTransactionIdentification <ClntTrptyCollTxId>
Presence: [0..1]
Definition: Unique reference identifying the triparty collateral management transaction from the client's
point of view.
Datatype: "Max35Text" on page 557
4.4.3.4.16  TripartyAgentServiceProviderCollateralTransactionIdentification
<TrptyAgtSvcPrvdrCollTxId>
Presence: [0..1]
Definition: Unique identification identifying the triparty collateral management transaction from the
triparty-agent's/service-provider's point of view.
Datatype: "Max35Text" on page 557
4.4.3.4.17  TripartyAgentServiceProviderCollateralInstructionIdentification
<TrptyAgtSvcPrvdrCollInstrId>
Presence: [0..1]
Definition: Unique identification assigned to the instruction by the triparty-agent/service-provider.
Datatype: "Max35Text" on page 557
4.4.3.4.18  TransactionDetails <TxDtls>
Presence: [0..1]
Definition: Identifies additional details of the transaction.
Impacted by: C5 "AdditionalDetailsRule", C27 "PostingAmountRule", C37
"TwoLegTransactionOpeningClosing1Rule", C38 "TwoLegTransactionOpeningClosing2Rule"
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 134 March 2026
```

## File page 135

```text
TransactionDetails <TxDtls> contains the following TransactionDetails187 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionActivity <TxActvty> [1..1] ± 140
   SettlementTransactionOrCorporateActionEventType
<SttlmTxOrCorpActnEvtTp>
[0..1] ± 140
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 141
   Payment <Pmt> [1..1] CodeSet 141
   SettlementParameters <SttlmParams> [0..1]  C8, C14,
C32,
C33
141
     HoldIndicator <HldInd> [0..1] ± 144
     Priority <Prty> [0..1] ± 144
     SecuritiesTransactionType <SctiesTxTp> [0..1] ± 144
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 144
     PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 145
     BeneficialOwnership <BnfclOwnrsh> [0..1] ± 145
     BlockTrade <BlckTrad> [0..1] ± 145
     CCPEligibility <CCPElgblty> [0..1] ± 146
     DeliveryReturnReason <DlvryRtrRsn> [0..1] ± 146
     CashClearingSystem <CshClrSys> [0..1] ± 146
     ExposureType <XpsrTp> [0..1] ± 146
     FXStandingInstruction <FxStgInstr> [0..1] ± 147
     MarketClientSide <MktClntSd> [0..1] ± 147
     NettingEligibility <NetgElgblty> [0..1] ± 147
     Registration <Regn> [0..1] ± 147
     RepurchaseType <RpTp> [0..1] ± 148
     LegalRestrictions <LglRstrctns> [0..1] ± 148
     SecuritiesRTGS <SctiesRTGS> [0..1] ± 148
     SettlingCapacity <SttlgCpcty> [0..1] ± 148
     SettlementSystemMethod <SttlmSysMtd> [0..1] ± 149
     TaxCapacity <TaxCpcty> [0..1] ± 149
     StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 149
     Tracking <Trckg> [0..1] ± 149
     AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 150
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 135 March 2026
```

## File page 136

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     LetterOfGuarantee <LttrOfGrnt> [0..1] ± 150
     ReturnLeg <RtrLeg> [0..1] Indicator 150
     ModificationCancellationAllowed <ModCxlAllwd> [0..1] ± 150
     EligibleForCollateral <ElgblForColl> [0..1] Indicator 151
     SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 151
     CashSubBalanceType <CshSubBalTp> [0..1] ± 151
   PlaceOfTrade <PlcOfTrad> [0..1] ± 151
   SafekeepingPlace <SfkpgPlc> [0..1] ± C31 152
   PlaceOfClearing <PlcOfClr> [0..1] ± 152
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
C16,
C20
152
   CountryOfIssue <CtryOfIsse> [0..1] CodeSet C9 153
   ConditionalSecuritiesDelivery <CondlSctiesDlvry> [0..1] Indicator 154
   SettlementQuantity <SttlmQty> [1..1] ± 154
   SettledQuantity <SttldQty> [0..1] ± 154
   PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± 155
   RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± 155
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C19 155
   SettlementAmount <SttlmAmt> [1..1] ± 155
   SettledAmount <SttldAmt> [0..1] ± 156
   PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 156
   RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 156
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 156
   TradeDate <TradDt> [0..1] ± 157
   IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 157
   EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 157
   ValueDate <ValDt> [0..1] ± 158
   StatusDate <StsDt> [0..1] DateTime 158
   AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 158
   MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 158
   Linkages <Lnkgs> [0..*]  158
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 136 March 2026
```

## File page 137

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     ProcessingPosition <PrcgPos> [0..1] ± C39 159
     MessageNumber <MsgNb> [0..1] ± C35 159
     Reference <Ref> [1..1]  160
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 160
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 160
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 161
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 161
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 161
Or       PoolIdentification <PoolId> [1..1] Text 161
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 161
     ReferenceOwner <RefOwnr> [0..1] ± 161
   Priority <Prty> [0..1] ± 162
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
162
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
163
   ReversalIndicator <RvslInd> [0..1] Indicator 164
   MessageOriginator <MsgOrgtr> [0..1] ± 164
   CreationDateTime <CreDtTm> [1..1] DateTime 164
   TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 164
   SupplementaryData <SplmtryData> [0..*] ± C36 164
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if TransactionAdditionalDetails is present,
then it must not contain information that can be provided in a structured field.
• PostingAmountRule
If the instruction is against payment, PostingAmount must be present.
.
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 137 March 2026
```

## File page 138

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
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 138 March 2026
```

## File page 139

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
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 139 March 2026
```

