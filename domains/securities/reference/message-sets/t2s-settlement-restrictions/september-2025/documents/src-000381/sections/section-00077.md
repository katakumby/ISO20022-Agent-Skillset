---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.2 Structure"]
file_pages: [98, 99]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 5.2 Structure

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 98 to 99.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 98

```text
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmCondsModReqRpt> [1..1]  C4, C5
   Pagination <Pgntn> [1..1] ± 103
   ReportGeneralDetails <RptGnlDtls> [1..1]  C24 103
     ReportNumber <RptNb> [0..1] ± 104
     QueryReference <QryRef> [0..1] Text 104
     ReportIdentification <RptId> [0..1] Text 105
     ReportDateTime <RptDtTm> [0..1] ± 105
     ReportPeriod <RptPrd> [0..1] ± 105
     QueryType <QryTp> [0..1] CodeSet 105
     Frequency <Frqcy> [0..1] ± 105
     UpdateType <UpdTp> [1..1] ± 106
     ActivityIndicator <ActvtyInd> [1..1] Indicator 106
   Modifications <Mods> [0..*]  C1, C22,
C25
106
     AccountOwner <AcctOwnr> [0..1] ± 109
     SafekeepingAccount <SfkpgAcct> [0..1] ± 109
     ProcessingStatus <PrcgSts> [0..1] ± 110
     Modification <Mod> [1..*]  110
       AccountOwner <AcctOwnr> [0..1] ± 113
       SafekeepingAccount <SfkpgAcct> [0..1] ± 113
       ProcessingStatus <PrcgSts> [0..1] ± 113
       RequestReference <ReqRef> [1..1] Text 114
       StatusDate <StsDt> [0..1] DateTime 114
       RequestDetails <ReqDtls> [0..1]  C15,
C17,
C26
114
         Reference <Ref> [1..1]  C23 116
           AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 117
           AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 117
           MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 117
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 98 September 2025
```

## File page 99

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           CounterpartyMarketInfrastructureTransactionIdentificati
on <CtrPtyMktInfrstrctrTxId>
[0..1] Text 117
           ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 117
           PoolIdentification <PoolId> [0..1] Text 117
           CommonIdentification <CmonId> [0..1] Text 118
           TradeIdentification <TradId> [0..1] Text 118
         RestrictionReference <RstrctnRef> [0..*] ± 118
         AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 118
         RetainIndicator <RtnInd> [0..1] Indicator 118
         Linkage <Lkg> [0..1] ± 118
         Priority <Prty> [0..1] ± 119
         OtherProcessing <OthrPrcg> [0..*] ± 119
         PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 119
         SecuritiesRTGS <SctiesRTGS> [0..1] ± 120
         HoldIndicator <HldInd> [0..1] ± 120
         MatchingDenial <MtchgDnl> [0..1] ± 120
         UnilateralSplit <UnltrlSplt> [0..1] ± 120
         Linkages <Lnkgs> [0..*]  121
           ProcessingPosition <PrcgPos> [0..1] ± C29 121
           MessageNumber <MsgNb> [0..1] ± C27 122
           Reference <Ref> [1..1]  122
{Or             SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 123
Or             IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 123
Or             IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 123
Or             AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 123
Or             MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 123
Or             PoolIdentification <PoolId> [1..1] Text 124
Or}             OtherTransactionIdentification <OthrTxId> [1..1] Text 124
           ReferenceOwner <RefOwnr> [0..1] ± 124
       Underlying <Undrlyg> [0..1]  124
{Or         IntraPositionMovement <IntraPosMvmnt> [1..1]  125
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 99 September 2025
```

