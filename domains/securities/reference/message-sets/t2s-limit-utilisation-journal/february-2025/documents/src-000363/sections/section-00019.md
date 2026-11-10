---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["3 camt.065.001.01 LimitUtilisationJournalReportV01", "3.4 Message Building Blocks", "3.4.3 ReportOrError <RptOrErr>", "3.4.3.1 BusinessReport <BizRpt>", "3.4.3.1.2 LimitReport <LmtRpt>", "3.4.3.1.2.1 LimitJournal <LmtJrnl>", "3.4.3.1.2.1.1 Limit <Lmt>"]
file_pages: [21]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 3.4.3.1.2.1.1 Limit <Lmt>

Source: [src-000363](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 21 to 21.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 21

```text
LimitJournal <LmtJrnl> contains the following LimitJournal3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
3.4.3.1.2.1.1  Limit <Lmt>
Presence: [1..1]
Definition: Maximum value used for risk containment in a system or towards counterparts. The limit may
be a current limit or a default limit.
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 21 February 2025
```

