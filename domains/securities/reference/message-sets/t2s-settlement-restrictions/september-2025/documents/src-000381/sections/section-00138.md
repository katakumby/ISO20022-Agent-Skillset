---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["8 semt.034.001.01 IntraPositionMovementPendingReportV01", "8.2 Structure"]
file_pages: [170]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 8.2 Structure

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 170 to 170.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 170

```text
8.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraPosMvmntPdgRpt> [1..1]  C2, C3
   Pagination <Pgntn> [1..1] ± 174
   ReportGeneralDetails <RptGnlDtls> [1..1]  C17 174
     ReportNumber <RptNb> [0..1] ± 174
     QueryReference <QryRef> [0..1] Text 175
     ReportIdentification <RptId> [0..1] Text 175
     ReportDateTime <RptDtTm> [0..1] ± 175
     ReportPeriod <RptPrd> [0..1] ± 175
     Frequency <Frqcy> [0..1] ± 175
     UpdateType <UpdTp> [1..1] ± 176
     ActivityIndicator <ActvtyInd> [1..1] Indicator 176
   AccountOwner <AcctOwnr> [0..1] ± 176
   SafekeepingAccount <SfkpgAcct> [1..1] ± 176
   Movements <Mvmnts> [0..*]  C19 177
     StatusAndReason <StsAndRsn> [0..1] ± 179
     Movement <Mvmnt> [1..*]  C13 179
       StatusAndReason <StsAndRsn> [0..1] ± 181
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 181
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 181
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 181
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 182
       CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 182
       PoolIdentification <PoolId> [0..1] Text 182
       BalanceFrom <BalFr> [1..1] ± 182
       BalanceTo <BalTo> [1..1] ± 182
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C11,
C12,
C14
182
       FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C16 184
       SettlementQuantity <SttlmQty> [1..1] ± 186
Approved by the Securities SEG on 21 August 2025 semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities - Settlement Restrictions 170 September 2025
```

