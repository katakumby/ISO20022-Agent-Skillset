---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["6 camt.065.001.01 LimitUtilisationJournalReportV01", "6.4 Message Building Blocks", "6.4.2 Pagination <Pgntn>"]
file_pages: [77, 78]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 6.4.2 Pagination <Pgntn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 77 to 78.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 77

```text
OriginalBusinessInstruction <OrgnlBizInstr> contains the following elements (see
"OriginalBusinessInstruction1" on page 3002 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 3002
   MessageNameIdentification <MsgNmId> [0..1] Text 3002
   CreationDateTime <CreDtTm> [0..1] DateTime 3002
6.4.2 Pagination <Pgntn>
Presence: [0..1]
Definition: Pagination of the message.
Usage: the pagination of the message is only allowed when agreed between the parties.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 2980 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 2980
   LastPageIndicator <LastPgInd> [1..1] Indicator 2980
6.4.3 ReportOrError <RptOrErr>
Presence: [1..1]
Definition: Provides information on report or error resulting from the originating query message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities 77 August 2026
```

## File page 78

```text
ReportOrError <RptOrErr> contains one of the following LimitJournalReportOrError7Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BusinessReport <BizRpt> [1..*]  79
     LimitIdentification <LmtId> [1..1]  81
       AccountIdentification <AcctId> [1..1] ± 81
       Type <Tp> [1..1] CodeSet 81
       LimitCurrency <LmtCcy> [0..1] CodeSet C1 82
       AccountOwner <AcctOwnr> [1..1] ± 82
       BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 82
     LimitReport <LmtRpt> [1..1]  83
{Or       LimitJournal <LmtJrnl> [1..1]  84
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
           Amount <Amt> [1..1] ± 89
           MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 89
           TransactionIdentification <TxId> [0..1] Text 89
           AccountServicerReference <AcctSvcrRef> [0..1] Text 89
           ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 90
           AdditionalEntryInformation <AddtlNtryInf> [0..1] Text 90
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities 78 August 2026
```

