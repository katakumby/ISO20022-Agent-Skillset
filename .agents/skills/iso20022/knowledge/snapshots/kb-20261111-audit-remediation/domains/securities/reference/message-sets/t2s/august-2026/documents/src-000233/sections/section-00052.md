---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["6 camt.065.001.01 LimitUtilisationJournalReportV01", "6.4 Message Building Blocks", "6.4.3 ReportOrError <RptOrErr>", "6.4.3.1 BusinessReport <BizRpt>", "6.4.3.1.2 LimitReport <LmtRpt>", "6.4.3.1.2.1 LimitJournal <LmtJrnl>", "6.4.3.1.2.1.1 Limit <Lmt>", "6.4.3.1.2.1.1.3 AvailableAmount <AvlblAmt>", "6.4.3.1.2.1.1.3.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [88]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 6.4.3.1.2.1.1.3.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 88 to 88.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 88

```text
Amount <Amt> contains one of the following elements (see "Amount2Choice" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 2840
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 2841
6.4.3.1.2.1.1.3.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Specifies whether the amount of money is a debit or a credit.
Datatype: "CreditDebitCode" on page 3234
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
6.4.3.1.2.1.2  JournalActivityDate <JrnlActvtyDt>
Presence: [1..1]
Definition: Date upon which journal activity takes place.
Datatype: "ISODate" on page 3319
6.4.3.1.2.1.3  JournalEntry <JrnlNtry>
Presence: [0..*]
Definition: Recording of transaction data pertaining to a transaction in a journal.
JournalEntry <JrnlNtry> contains the following LimitJournalEntry3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
6.4.3.1.2.1.3.1  JournalDate <JrnlDt>
Presence: [1..1]
Definition: Date and time for which the limit journal entry applies.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities 88 August 2026
```

