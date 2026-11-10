---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["6 camt.065.001.01 LimitUtilisationJournalReportV01", "6.4 Message Building Blocks", "6.4.3 ReportOrError <RptOrErr>", "6.4.3.1 BusinessReport <BizRpt>"]
file_pages: [79, 80]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 6.4.3.1 BusinessReport <BizRpt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 79 to 80.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 79

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       BusinessError <BizErr> [1..*]  90
         Error <Err> [1..1]  90
{Or           Code <Cd> [1..1] CodeSet 90
Or}           Proprietary <Prtry> [1..1] Text 90
         Description <Desc> [0..1] Text 91
Or}   OperationalError <OprlErr> [1..*]  91
     Error <Err> [1..1]  91
{Or       Code <Cd> [1..1] CodeSet 91
Or}       Proprietary <Prtry> [1..1] Text 91
     Description <Desc> [0..1] Text 91
6.4.3.1  BusinessReport <BizRpt>
Presence: [1..*]
Definition: Specifies the business report either as a limit utilisation journal or a business error.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities 79 August 2026
```

## File page 80

```text
BusinessReport <BizRpt> contains the following LimitJournalReport4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LimitIdentification <LmtId> [1..1]  81
     AccountIdentification <AcctId> [1..1] ± 81
     Type <Tp> [1..1] CodeSet 81
     LimitCurrency <LmtCcy> [0..1] CodeSet C1 82
     AccountOwner <AcctOwnr> [1..1] ± 82
     BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 82
   LimitReport <LmtRpt> [1..1]  83
{Or     LimitJournal <LmtJrnl> [1..1]  84
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
Or}     BusinessError <BizErr> [1..*]  90
       Error <Err> [1..1]  90
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities 80 August 2026
```

