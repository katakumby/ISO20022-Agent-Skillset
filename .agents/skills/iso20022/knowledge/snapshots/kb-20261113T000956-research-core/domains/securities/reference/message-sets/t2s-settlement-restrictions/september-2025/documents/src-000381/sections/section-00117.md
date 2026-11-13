---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "7.2 Structure"]
file_pages: [146]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 7.2 Structure

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 146 to 146.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 146

```text
7.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesTxCxlReqRpt> [1..1]  C4, C5
   Pagination <Pgntn> [1..1] ± 149
   ReportGeneralDetails <RptGnlDtls> [1..1]  C21 150
     ReportNumber <RptNb> [0..1] ± 150
     QueryReference <QryRef> [0..1] Text 151
     ReportIdentification <RptId> [0..1] Text 151
     ReportDateTime <RptDtTm> [0..1] ± 151
     ReportPeriod <RptPrd> [0..1] ± 151
     QueryType <QryTp> [0..1] CodeSet 151
     Frequency <Frqcy> [0..1] ± 152
     UpdateType <UpdTp> [1..1] ± 152
     ActivityIndicator <ActvtyInd> [1..1] Indicator 152
   Cancellations <Cxls> [0..*]  C1, C20,
C22
152
     AccountOwner <AcctOwnr> [0..1] ± 154
     SafekeepingAccount <SfkpgAcct> [0..1] ± 154
     ProcessingStatus <PrcgSts> [0..1] ± 155
     Cancellation <Cxl> [1..*]  155
       AccountOwner <AcctOwnr> [0..1] ± 157
       SafekeepingAccount <SfkpgAcct> [0..1] ± 157
       ProcessingStatus <PrcgSts> [0..1] ± 157
       RequestReference <ReqRef> [1..1] Text 158
       StatusDate <StsDt> [0..1] DateTime 158
       TransactionIdentification <TxId> [0..1]  158
         AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 158
         AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 159
         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 159
         CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 159
         ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 159
         PoolIdentification <PoolId> [0..1] Text 159
Approved by the Securities SEG on 21 August 2025 semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities - Settlement Restrictions 146 September 2025
```

