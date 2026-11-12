---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["6 camt.065.001.01 LimitUtilisationJournalReportV01", "6.4 Message Building Blocks", "6.4.3 ReportOrError <RptOrErr>", "6.4.3.1 BusinessReport <BizRpt>", "6.4.3.1.2 LimitReport <LmtRpt>", "6.4.3.1.2.1 LimitJournal <LmtJrnl>", "6.4.3.1.2.1.3 JournalEntry <JrnlNtry>", "6.4.3.1.2.1.3.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [89]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 6.4.3.1.2.1.3.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 89 to 89.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 89

```text
JournalDate <JrnlDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
6.4.3.1.2.1.3.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether the entry is a credit or a debit entry.
Datatype: "CreditDebitCode" on page 3234
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
6.4.3.1.2.1.3.3  Amount <Amt>
Presence: [1..1]
Definition: Amount of money of individual entry impacting the limit.
Amount <Amt> contains one of the following elements (see "Amount2Choice" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 2840
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 2841
6.4.3.1.2.1.3.4  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 3328
6.4.3.1.2.1.3.5  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique reference as assigned by the account owner institution to unambiguously identify the
entry.
Datatype: "Max35Text" on page 3328
6.4.3.1.2.1.3.6  AccountServicerReference <AcctSvcrRef>
Presence: [0..1]
Definition: Unique reference as assigned by the account servicing institution to unambiguously identify
the entry.
Datatype: "Max35Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities 89 August 2026
```

