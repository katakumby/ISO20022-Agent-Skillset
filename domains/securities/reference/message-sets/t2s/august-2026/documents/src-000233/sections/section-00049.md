---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["6 camt.065.001.01 LimitUtilisationJournalReportV01", "6.4 Message Building Blocks", "6.4.3 ReportOrError <RptOrErr>", "6.4.3.1 BusinessReport <BizRpt>", "6.4.3.1.2 LimitReport <LmtRpt>", "6.4.3.1.2.1 LimitJournal <LmtJrnl>", "6.4.3.1.2.1.1 Limit <Lmt>"]
file_pages: [85]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 6.4.3.1.2.1.1 Limit <Lmt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 85 to 85.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 85

```text
LimitJournal <LmtJrnl> contains the following LimitJournal3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
6.4.3.1.2.1.1  Limit <Lmt>
Presence: [1..1]
Definition: Maximum value used for risk containment in a system or towards counterparts. The limit may
be a current limit or a default limit.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities 85 August 2026
```

