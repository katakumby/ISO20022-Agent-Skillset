---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.3 Modifications <Mods>", "76.4.3.3 ProcessingStatus <PrcgSts>"]
file_pages: [2665, 2666, 2667]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.3.3 ProcessingStatus <PrcgSts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2665 to 2667.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2665

```text
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
76.4.3.3  ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Status and status reason of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus71Choice" on page 3152 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3152
Or   Pending <Pdg> [1..1] ± 3153
Or   Rejected <Rjctd> [1..1] ± 3153
Or   Repair <Rpr> [1..1] ± 3153
Or   Denied <Dnd> [1..1] ± 3154
Or   Completed <Cmpltd> [1..1] ± C6 3154
Or}   Proprietary <Prtry> [1..1] ± 3155
76.4.3.4  Modification <Mod>
Presence: [1..*]
Definition: Identifies the individual transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2665 August 2026
```

## File page 2666

```text
Modification <Mod> contains the following SecuritiesModificationTransaction2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1] ± 2668
   SafekeepingAccount <SfkpgAcct> [0..1] ± 2668
   ProcessingStatus <PrcgSts> [0..1] ± 2668
   RequestReference <ReqRef> [1..1] Text 2669
   StatusDate <StsDt> [0..1] DateTime 2669
   RequestDetails <ReqDtls> [0..1]  C15,
C17,
C26
2669
     Reference <Ref> [1..1]  C23 2671
       AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 2672
       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 2672
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2672
       CounterpartyMarketInfrastructureTransactionIdenti
fication <CtrPtyMktInfrstrctrTxId>
[0..1] Text 2672
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2672
       PoolIdentification <PoolId> [0..1] Text 2672
       CommonIdentification <CmonId> [0..1] Text 2673
       TradeIdentification <TradId> [0..1] Text 2673
     RestrictionReference <RstrctnRef> [0..*] ± 2673
     AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 2673
     RetainIndicator <RtnInd> [0..1] Indicator 2673
     Linkage <Lkg> [0..1] ± 2673
     Priority <Prty> [0..1] ± 2674
     OtherProcessing <OthrPrcg> [0..*] ± 2674
     PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 2674
     SecuritiesRTGS <SctiesRTGS> [0..1] ± 2675
     HoldIndicator <HldInd> [0..1] ± 2675
     MatchingDenial <MtchgDnl> [0..1] ± 2675
     UnilateralSplit <UnltrlSplt> [0..1] ± 2675
     Linkages <Lnkgs> [0..*]  2676
       ProcessingPosition <PrcgPos> [0..1] ± C29 2676
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2666 August 2026
```

## File page 2667

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       MessageNumber <MsgNb> [0..1] ± C27 2677
       Reference <Ref> [1..1]  2677
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 2678
Or         IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 2678
Or         IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 2678
Or         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2678
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2678
Or         PoolIdentification <PoolId> [1..1] Text 2679
Or}         OtherTransactionIdentification <OthrTxId> [1..1] Text 2679
       ReferenceOwner <RefOwnr> [0..1] ± 2679
   Underlying <Undrlyg> [0..1]  2679
{Or     IntraPositionMovement <IntraPosMvmnt> [1..1]  2680
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C16
2681
       SettlementQuantity <SttlmQty> [1..1] ± 2682
       SettlementDate <SttlmDt> [1..1] ± 2682
       BalanceFrom <BalFr> [0..1] ± 2682
       BalanceTo <BalTo> [0..1] ± 2683
       SecuritiesSubBalanceIdentification
<SctiesSubBalId>
[0..1] ± 2683
       Priority <Prty> [0..1] ± 2683
Or}     SettlementTransaction <SttlmTx> [1..1]  2683
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C16
2684
       SettlementQuantity <SttlmQty> [1..1] ± 2685
       SettlementAmount <SttlmAmt> [0..1] ± 2685
       TradeDate <TradDt> [0..1] ± 2686
       SettlementDate <SttlmDt> [1..1] ± 2686
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2667 August 2026
```

