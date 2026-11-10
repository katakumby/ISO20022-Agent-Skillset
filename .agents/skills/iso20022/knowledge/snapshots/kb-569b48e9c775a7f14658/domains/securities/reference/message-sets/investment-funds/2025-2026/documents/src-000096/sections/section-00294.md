---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02", "22.2 Structure"]
file_pages: [410]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.006.001.02"]
---

# 22.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 410 to 410.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 410

```text
22.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <StmtOfInvstmtFndTxsV02> [1..1]  C7
   MessageIdentification <MsgId> [1..1] ± 412
   PreviousReference <PrvsRef> [0..*] ± 412
   RelatedReference <RltdRef> [0..*] ± 412
   MessagePagination <MsgPgntn> [1..1] ± 413
   StatementGeneralDetails <StmtGnlDtls> [1..1]  413
     Reference <Ref> [1..1] Text 413
     StatementPeriod <StmtPrd> [1..1] ± 414
     CreationDateTime <CreDtTm> [0..1] ± 414
     Frequency <Frqcy> [0..1] CodeSet 414
     UpdateType <UpdTp> [1..1] CodeSet 415
     ActivityIndicator <ActvtyInd> [1..1] Indicator 415
     ReportNumber <RptNb> [0..1] Text 415
   InvestmentAccountDetails <InvstmtAcctDtls> [1..1] ± 415
   TransactionOnAccount <TxOnAcct> [0..*]  416
     Identification <Id> [1..1] ± 416
     Name <Nm> [0..1] Text 417
     SupplementaryIdentification <SplmtryId> [0..1] Text 417
     SecuritiesForm <SctiesForm> [0..1] CodeSet 417
     ClassType <ClssTp> [0..1] Text 418
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 418
     TransactionDetails <TxDtls> [1..*] ± C9, C10 418
     BalanceByPage <BalByPg> [0..1] ± 420
   SubAccountDetails <SubAcctDtls> [0..*]  C8 420
     Identification <Id> [1..1] ± 421
     ActivityIndicator <ActvtyInd> [1..1] Indicator 421
     TransactionOnSubAccount <TxOnSubAcct> [0..*]  422
       Identification <Id> [1..1] ± 422
       Name <Nm> [0..1] Text 423
       SupplementaryIdentification <SplmtryId> [0..1] Text 423
Approved by the Securities SEG on 27 January 2026 semt.006.001.02
StatementOfInvestmentFundTransactionsV02
Investment Funds - Maintenance 2025 - 2026 410 May 2026
```

