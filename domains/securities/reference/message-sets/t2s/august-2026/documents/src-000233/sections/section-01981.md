---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "78.2 Structure"]
file_pages: [2701]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 78.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2701 to 2701.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2701

```text
78.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesTxCxlReqRpt> [1..1]  C4, C5
   Pagination <Pgntn> [1..1] ± 2704
   ReportGeneralDetails <RptGnlDtls> [1..1]  C21 2705
     ReportNumber <RptNb> [0..1] ± 2705
     QueryReference <QryRef> [0..1] Text 2706
     ReportIdentification <RptId> [0..1] Text 2706
     ReportDateTime <RptDtTm> [0..1] ± 2706
     ReportPeriod <RptPrd> [0..1] ± 2706
     QueryType <QryTp> [0..1] CodeSet 2706
     Frequency <Frqcy> [0..1] ± 2707
     UpdateType <UpdTp> [1..1] ± 2707
     ActivityIndicator <ActvtyInd> [1..1] Indicator 2707
   Cancellations <Cxls> [0..*]  C1, C20,
C22
2707
     AccountOwner <AcctOwnr> [0..1] ± 2709
     SafekeepingAccount <SfkpgAcct> [0..1] ± 2709
     ProcessingStatus <PrcgSts> [0..1] ± 2710
     Cancellation <Cxl> [1..*]  2710
       AccountOwner <AcctOwnr> [0..1] ± 2712
       SafekeepingAccount <SfkpgAcct> [0..1] ± 2712
       ProcessingStatus <PrcgSts> [0..1] ± 2712
       RequestReference <ReqRef> [1..1] Text 2713
       StatusDate <StsDt> [0..1] DateTime 2713
       TransactionIdentification <TxId> [0..1]  2713
         AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 2713
         AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 2714
         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2714
         CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 2714
         ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2714
         PoolIdentification <PoolId> [0..1] Text 2714
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities 2701 August 2026
```

