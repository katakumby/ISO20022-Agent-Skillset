---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["79 semt.034.001.01 IntraPositionMovementPendingReportV01", "79.2 Structure"]
file_pages: [2725]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 79.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2725 to 2725.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2725

```text
79.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraPosMvmntPdgRpt> [1..1]  C2, C3
   Pagination <Pgntn> [1..1] ± 2729
   ReportGeneralDetails <RptGnlDtls> [1..1]  C17 2729
     ReportNumber <RptNb> [0..1] ± 2729
     QueryReference <QryRef> [0..1] Text 2730
     ReportIdentification <RptId> [0..1] Text 2730
     ReportDateTime <RptDtTm> [0..1] ± 2730
     ReportPeriod <RptPrd> [0..1] ± 2730
     Frequency <Frqcy> [0..1] ± 2730
     UpdateType <UpdTp> [1..1] ± 2731
     ActivityIndicator <ActvtyInd> [1..1] Indicator 2731
   AccountOwner <AcctOwnr> [0..1] ± 2731
   SafekeepingAccount <SfkpgAcct> [1..1] ± 2731
   Movements <Mvmnts> [0..*]  C19 2732
     StatusAndReason <StsAndRsn> [0..1] ± 2734
     Movement <Mvmnt> [1..*]  C13 2734
       StatusAndReason <StsAndRsn> [0..1] ± 2736
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 2736
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 2736
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2736
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2737
       CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 2737
       PoolIdentification <PoolId> [0..1] Text 2737
       BalanceFrom <BalFr> [1..1] ± 2737
       BalanceTo <BalTo> [1..1] ± 2737
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C11,
C12,
C14
2737
       FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C16 2739
       SettlementQuantity <SttlmQty> [1..1] ± 2741
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities 2725 August 2026
```

