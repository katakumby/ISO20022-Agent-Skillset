---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 camt.060.001.07 AccountReportingRequestV07", "5.2 Structure"]
file_pages: [782]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.060.001.07"]
---

# 5.2 Structure

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 782 to 782.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 782

```text
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctRptgReq> [1..1]  
   GroupHeader <GrpHdr> [1..1]  783
     MessageIdentification <MsgId> [1..1] Text 784
     CreationDateTime <CreDtTm> [1..1] DateTime 784
     MessageSender <MsgSndr> [0..1]  784
{Or       Party <Pty> [1..1] ± 784
Or}       Agent <Agt> [1..1] ± 785
   ReportingRequest <RptgReq> [1..*]  786
     Identification <Id> [0..1] Text 787
     RequestedMessageNameIdentification <ReqdMsgNmId> [1..1] Text 787
     Account <Acct> [0..1] ± C8, C7 788
     AccountOwner <AcctOwnr> [1..1]  788
{Or       Party <Pty> [1..1] ± 788
Or}       Agent <Agt> [1..1] ± 789
     AccountServicer <AcctSvcr> [0..1] ± 790
     ReportingPeriod <RptgPrd> [0..1]  791
       FromToDate <FrToDt> [1..1]  791
         FromDate <FrDt> [1..1] Date 792
         ToDate <ToDt> [0..1] Date 792
       FromToTime <FrToTm> [0..1] ± 792
       Type <Tp> [1..1] CodeSet 792
     ReportingSequence <RptgSeq> [0..1] ± 793
     RequestedTransactionType <ReqdTxTp> [0..1]  793
       Status <Sts> [1..1] ± 793
       CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 794
       FloorLimit <FlrLmt> [0..*]  794
         Amount <Amt> [1..1] Amount C1, C5 794
         CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 794
     RequestedBalanceType <ReqdBalTp> [0..*] ± 795
   SupplementaryData <SplmtryData> [0..*] ± C9 795
Approved by the Payments SEG on 12 January 2026 camt.060.001.07 AccountReportingRequestV07
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
782 March 2026
```

