---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.2 Structure"]
file_pages: [2653, 2654]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2653 to 2654.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2653

```text
76.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmCondsModReqRpt> [1..1]  C4, C5
   Pagination <Pgntn> [1..1] ± 2658
   ReportGeneralDetails <RptGnlDtls> [1..1]  C24 2658
     ReportNumber <RptNb> [0..1] ± 2659
     QueryReference <QryRef> [0..1] Text 2659
     ReportIdentification <RptId> [0..1] Text 2660
     ReportDateTime <RptDtTm> [0..1] ± 2660
     ReportPeriod <RptPrd> [0..1] ± 2660
     QueryType <QryTp> [0..1] CodeSet 2660
     Frequency <Frqcy> [0..1] ± 2660
     UpdateType <UpdTp> [1..1] ± 2661
     ActivityIndicator <ActvtyInd> [1..1] Indicator 2661
   Modifications <Mods> [0..*]  C1, C22,
C25
2661
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
           AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 2672
           AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 2672
           MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2672
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2653 August 2026
```

## File page 2654

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           CounterpartyMarketInfrastructureTransactionIdentificati
on <CtrPtyMktInfrstrctrTxId>
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
           MessageNumber <MsgNb> [0..1] ± C27 2677
           Reference <Ref> [1..1]  2677
{Or             SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 2678
Or             IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 2678
Or             IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 2678
Or             AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2678
Or             MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2678
Or             PoolIdentification <PoolId> [1..1] Text 2679
Or}             OtherTransactionIdentification <OthrTxId> [1..1] Text 2679
           ReferenceOwner <RefOwnr> [0..1] ± 2679
       Underlying <Undrlyg> [0..1]  2679
{Or         IntraPositionMovement <IntraPosMvmnt> [1..1]  2680
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2654 August 2026
```

