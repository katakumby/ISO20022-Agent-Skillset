---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["3 camt.065.001.01 LimitUtilisationJournalReportV01", "3.4 Message Building Blocks", "3.4.2 Pagination <Pgntn>"]
file_pages: [13, 14]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 3.4.2 Pagination <Pgntn>

Source: [src-000363](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 13 to 14.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 13

```text
OriginalBusinessInstruction <OrgnlBizInstr> contains the following elements (see
"OriginalBusinessInstruction1" on page 34 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 34
   MessageNameIdentification <MsgNmId> [0..1] Text 34
   CreationDateTime <CreDtTm> [0..1] DateTime 35
3.4.2 Pagination <Pgntn>
Presence: [0..1]
Definition: Pagination of the message.
Usage: the pagination of the message is only allowed when agreed between the parties.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 33 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 33
   LastPageIndicator <LastPgInd> [1..1] Indicator 33
3.4.3 ReportOrError <RptOrErr>
Presence: [1..1]
Definition: Provides information on report or error resulting from the originating query message.
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 13 February 2025
```

## File page 14

```text
ReportOrError <RptOrErr> contains one of the following LimitJournalReportOrError7Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BusinessReport <BizRpt> [1..*]  15
     LimitIdentification <LmtId> [1..1]  17
       AccountIdentification <AcctId> [1..1] ± 17
       Type <Tp> [1..1] CodeSet 17
       LimitCurrency <LmtCcy> [0..1] CodeSet C1 18
       AccountOwner <AcctOwnr> [1..1] ± 18
       BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 18
     LimitReport <LmtRpt> [1..1]  19
{Or       LimitJournal <LmtJrnl> [1..1]  20
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
           Amount <Amt> [1..1] ± 25
           MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 25
           TransactionIdentification <TxId> [0..1] Text 25
           AccountServicerReference <AcctSvcrRef> [0..1] Text 25
           ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 26
           AdditionalEntryInformation <AddtlNtryInf> [0..1] Text 26
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 14 February 2025
```

