---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["3 camt.065.001.01 LimitUtilisationJournalReportV01", "3.4 Message Building Blocks", "3.4.3 ReportOrError <RptOrErr>", "3.4.3.1 BusinessReport <BizRpt>", "3.4.3.1.2 LimitReport <LmtRpt>", "3.4.3.1.2.1 LimitJournal <LmtJrnl>", "3.4.3.1.2.1.3 JournalEntry <JrnlNtry>", "3.4.3.1.2.1.3.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [25]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 3.4.3.1.2.1.3.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000363](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 25 to 25.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 25

```text
JournalDate <JrnlDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 31 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 32
Or}   DateTime <DtTm> [1..1] DateTime 32
3.4.3.1.2.1.3.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether the entry is a credit or a debit entry.
Datatype: "CreditDebitCode" on page 42
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
3.4.3.1.2.1.3.3  Amount <Amt>
Presence: [1..1]
Definition: Amount of money of individual entry impacting the limit.
Amount <Amt> contains one of the following elements (see "Amount2Choice" on page 31 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 31
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 31
3.4.3.1.2.1.3.4  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 46
3.4.3.1.2.1.3.5  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique reference as assigned by the account owner institution to unambiguously identify the
entry.
Datatype: "Max35Text" on page 46
3.4.3.1.2.1.3.6  AccountServicerReference <AcctSvcrRef>
Presence: [0..1]
Definition: Unique reference as assigned by the account servicing institution to unambiguously identify
the entry.
Datatype: "Max35Text" on page 46
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 25 February 2025
```

