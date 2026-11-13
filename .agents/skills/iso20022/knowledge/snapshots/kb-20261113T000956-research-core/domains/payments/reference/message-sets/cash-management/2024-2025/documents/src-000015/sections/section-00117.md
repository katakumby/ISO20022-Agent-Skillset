---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.4 AccountEntrySearch <AcctNtrySch>", "4.4.2.2.2.2.4.6 EntryDate <NtryDt>"]
file_pages: [188]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.4.6 EntryDate <NtryDt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 188 to 188.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 188

```text
CodeName Name Definition
BOOK Booked Booked means that the transfer of
money has been completed between
account servicer and account owner
Usage:
Status Booked does not necessarily
imply finality of money as this depends
on other factors such as the payment
system used, the completion of the end-
to-end transaction and the terms agreed
between account servicer and owner.
Status Booked is the only status that can
be reversed.
PDNG Pending Booking on the account owner's account
in the account servicer's ledger has not
been completed.
Usage: this can be used for expected
items, or for items for which some
conditions still need to be fulfilled before
they can be booked. If booking takes
place, the entry will be included with
status Booked in subsequent account
report or statement. Status Pending
cannot be reversed.
FUTR Future Entry is on the books of the account
servicer and value will be applied to the
account owner at a future date and time.
4.4.2.2.2.2.4.6  EntryDate <NtryDt>
Presence: [0..*]
Definition: Date and time at which an entry is posted to an account on the account servicer's books.
EntryDate <NtryDt> contains one of the following DateAndDateTimeSearch3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DateTimeSearch <DtTmSch> [1..1]  189
{Or     FromDateTime <FrDtTm> [1..1] DateTime 189
Or     ToDateTime <ToDtTm> [1..1] DateTime 189
Or}     DateTimeRange <DtTmRg> [1..1] ± 189
Or}   DateSearch <DtSch> [1..1]  189
{Or     FromDate <FrDt> [1..1] Date 190
Or     ToDate <ToDt> [1..1] Date 190
Or     FromToDate <FrToDt> [1..1] ± 190
Or     EqualDate <EQDt> [1..1] Date 190
Or}     NotEqualDate <NEQDt> [1..1] Date 190
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 188 February 2025
```

