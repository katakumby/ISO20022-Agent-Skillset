---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.2 ReportGeneralDetails <RptGnlDtls>", "76.4.2.8 UpdateType <UpdTp>"]
file_pages: [2661, 2662, 2663]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.2.8 UpdateType <UpdTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2661 to 2663.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2661

```text
Frequency <Frqcy> contains one of the following elements (see "Frequency22Choice" on page 2958
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2958
Or}   Proprietary <Prtry> [1..1] ± 2959
76.4.2.8  UpdateType <UpdTp>
Presence: [1..1]
Definition: Indicates whether the statement is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see "UpdateType15Choice" on
page 3045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3045
Or}   Proprietary <Prtry> [1..1] ± 3045
76.4.2.9  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
76.4.3 Modifications <Mods>
Presence: [0..*]
Definition: Report on the condition modifications requests.
Impacted by: C1 "AccountOwnerRule", C22 "ProcessingStatusRule", C25 "SafekeepingAccountRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2661 August 2026
```

## File page 2662

```text
Modifications <Mods> contains the following SecuritiesModification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1] ± 2664
   SafekeepingAccount <SfkpgAcct> [0..1] ± 2664
   ProcessingStatus <PrcgSts> [0..1] ± 2665
   Modification <Mod> [1..*]  2665
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
         CounterpartyMarketInfrastructureTransactionIden
tification <CtrPtyMktInfrstrctrTxId>
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2662 August 2026
```

## File page 2663

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       MatchingDenial <MtchgDnl> [0..1] ± 2675
       UnilateralSplit <UnltrlSplt> [0..1] ± 2675
       Linkages <Lnkgs> [0..*]  2676
         ProcessingPosition <PrcgPos> [0..1] ± C29 2676
         MessageNumber <MsgNb> [0..1] ± C27 2677
         Reference <Ref> [1..1]  2677
{Or           SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 2678
Or           IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 2678
Or           IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 2678
Or           AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2678
Or           MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2678
Or           PoolIdentification <PoolId> [1..1] Text 2679
Or}           OtherTransactionIdentification <OthrTxId> [1..1] Text 2679
         ReferenceOwner <RefOwnr> [0..1] ± 2679
     Underlying <Undrlyg> [0..1]  2679
{Or       IntraPositionMovement <IntraPosMvmnt> [1..1]  2680
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
Or}       SettlementTransaction <SttlmTx> [1..1]  2683
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C16
2684
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2663 August 2026
```

