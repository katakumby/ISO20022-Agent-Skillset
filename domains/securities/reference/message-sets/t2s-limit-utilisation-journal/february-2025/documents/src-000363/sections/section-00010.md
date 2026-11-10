---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["3 camt.065.001.01 LimitUtilisationJournalReportV01", "3.2 Structure"]
file_pages: [10]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 3.2 Structure

Source: [src-000363](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 10 to 10.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 10

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <LmtUtlstnJrnlRpt> [1..1]  
   MessageHeader <MsgHdr> [0..1]  12
     MessageIdentification <MsgId> [1..1] Text 12
     CreationDateTime <CreDtTm> [0..1] DateTime 12
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 12
   Pagination <Pgntn> [0..1] ± 13
   ReportOrError <RptOrErr> [1..1]  13
{Or     BusinessReport <BizRpt> [1..*]  15
       LimitIdentification <LmtId> [1..1]  17
         AccountIdentification <AcctId> [1..1] ± 17
         Type <Tp> [1..1] CodeSet 17
         LimitCurrency <LmtCcy> [0..1] CodeSet C1 18
         AccountOwner <AcctOwnr> [1..1] ± 18
         BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId> [0..1] ± 18
       LimitReport <LmtRpt> [1..1]  19
{Or         LimitJournal <LmtJrnl> [1..1]  20
           Limit <Lmt> [1..1]  21
             Amount <Amt> [1..1]  22
               Amount <Amt> [1..1] ± 22
               CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 22
             UtilisationAmount <UtlstnAmt> [1..1]  23
               Amount <Amt> [1..1] ± 23
               CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 23
             AvailableAmount <AvlblAmt> [1..1]  23
               Amount <Amt> [1..1] ± 23
               CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 24
           JournalActivityDate <JrnlActvtyDt> [1..1] Date 24
           JournalEntry <JrnlNtry> [0..*]  24
             JournalDate <JrnlDt> [1..1] ± 24
             CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 25
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 10 February 2025
```

