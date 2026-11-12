---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["6 camt.065.001.01 LimitUtilisationJournalReportV01", "6.2 Structure"]
file_pages: [74]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 6.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 74 to 74.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 74

```text
6.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <LmtUtlstnJrnlRpt> [1..1]  
   MessageHeader <MsgHdr> [0..1]  76
     MessageIdentification <MsgId> [1..1] Text 76
     CreationDateTime <CreDtTm> [0..1] DateTime 76
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 76
   Pagination <Pgntn> [0..1] ± 77
   ReportOrError <RptOrErr> [1..1]  77
{Or     BusinessReport <BizRpt> [1..*]  79
       LimitIdentification <LmtId> [1..1]  81
         AccountIdentification <AcctId> [1..1] ± 81
         Type <Tp> [1..1] CodeSet 81
         LimitCurrency <LmtCcy> [0..1] CodeSet C1 82
         AccountOwner <AcctOwnr> [1..1] ± 82
         BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId> [0..1] ± 82
       LimitReport <LmtRpt> [1..1]  83
{Or         LimitJournal <LmtJrnl> [1..1]  84
           Limit <Lmt> [1..1]  85
             Amount <Amt> [1..1]  86
               Amount <Amt> [1..1] ± 86
               CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 86
             UtilisationAmount <UtlstnAmt> [1..1]  87
               Amount <Amt> [1..1] ± 87
               CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 87
             AvailableAmount <AvlblAmt> [1..1]  87
               Amount <Amt> [1..1] ± 87
               CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 88
           JournalActivityDate <JrnlActvtyDt> [1..1] Date 88
           JournalEntry <JrnlNtry> [0..*]  88
             JournalDate <JrnlDt> [1..1] ± 88
             CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 89
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities 74 August 2026
```

