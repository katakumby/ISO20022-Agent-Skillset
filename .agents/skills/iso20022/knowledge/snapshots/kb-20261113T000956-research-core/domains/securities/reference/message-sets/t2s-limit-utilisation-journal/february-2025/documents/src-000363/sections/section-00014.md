---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["3 camt.065.001.01 LimitUtilisationJournalReportV01", "3.4 Message Building Blocks", "3.4.3 ReportOrError <RptOrErr>", "3.4.3.1 BusinessReport <BizRpt>"]
file_pages: [15, 16]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 3.4.3.1 BusinessReport <BizRpt>

Source: [src-000363](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 15 to 16.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 15

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       BusinessError <BizErr> [1..*]  26
         Error <Err> [1..1]  26
{Or           Code <Cd> [1..1] CodeSet 26
Or}           Proprietary <Prtry> [1..1] Text 26
         Description <Desc> [0..1] Text 27
Or}   OperationalError <OprlErr> [1..*]  27
     Error <Err> [1..1]  27
{Or       Code <Cd> [1..1] CodeSet 27
Or}       Proprietary <Prtry> [1..1] Text 27
     Description <Desc> [0..1] Text 27
3.4.3.1  BusinessReport <BizRpt>
Presence: [1..*]
Definition: Specifies the business report either as a limit utilisation journal or a business error.
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 15 February 2025
```

## File page 16

```text
BusinessReport <BizRpt> contains the following LimitJournalReport4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LimitIdentification <LmtId> [1..1]  17
     AccountIdentification <AcctId> [1..1] ± 17
     Type <Tp> [1..1] CodeSet 17
     LimitCurrency <LmtCcy> [0..1] CodeSet C1 18
     AccountOwner <AcctOwnr> [1..1] ± 18
     BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 18
   LimitReport <LmtRpt> [1..1]  19
{Or     LimitJournal <LmtJrnl> [1..1]  20
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
Or}     BusinessError <BizErr> [1..*]  26
       Error <Err> [1..1]  26
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 16 February 2025
```

