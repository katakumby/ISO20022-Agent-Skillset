---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.5 AccountEntry <AcctNtry>", "5.4.2.1.3.2.1.5.2 Entry <Ntry>", "5.4.2.1.3.2.1.5.2.2 Date <Dt>"]
file_pages: [321]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.5.2.2 Date <Dt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 321 to 321.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 321

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
5.4.2.1.3.2.1.5.2.2  Date <Dt>
Presence: [0..1]
Definition: Date at which an entry is posted to an account on the account servicer's books.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 801 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 801
Or}   DateTime <DtTm> [1..1] DateTime 801
5.4.2.1.3.2.1.5.2.3  Status <Sts>
Presence: [0..1]
Definition: Status of an entry on the books of the account servicer.
Datatype: "EntryStatus1Code" on page 851
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
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 321 February 2025
```

