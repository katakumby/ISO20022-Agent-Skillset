---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 camt.060.001.07 AccountReportingRequestV07", "5.4 Message Building Blocks", "5.4.2 ReportingRequest <RptgReq>", "5.4.2.1 Identification <Id>"]
file_pages: [787]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.060.001.07"]
---

# 5.4.2.1 Identification <Id>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 787 to 787.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 787

```text
ReportingRequest <RptgReq> contains the following ReportingRequest7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 787
   RequestedMessageNameIdentification
<ReqdMsgNmId>
[1..1] Text 787
   Account <Acct> [0..1] ± C8, C7 788
   AccountOwner <AcctOwnr> [1..1]  788
{Or     Party <Pty> [1..1] ± 788
Or}     Agent <Agt> [1..1] ± 789
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
5.4.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique identification, as assigned by the account owner, to unambiguously identify the
account reporting request.
Datatype: "Max35Text" on page 916
5.4.2.2  RequestedMessageNameIdentification <ReqdMsgNmId>
Presence: [1..1]
Definition: Specifies the type of the requested reporting message.
Datatype: "Max35Text" on page 916
Approved by the Payments SEG on 12 January 2026 camt.060.001.07 AccountReportingRequestV07
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
787 March 2026
```

