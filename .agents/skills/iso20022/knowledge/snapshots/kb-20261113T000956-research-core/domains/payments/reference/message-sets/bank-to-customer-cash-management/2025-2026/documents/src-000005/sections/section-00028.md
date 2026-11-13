---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.6 BookingDate <BookgDt>"]
file_pages: [71]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.6 BookingDate <BookgDt>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 71 to 71.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 71

```text
Status <Sts> contains one of the following elements (see "EntryStatus1Choice" on page 882 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 882
Or}   Proprietary <Prtry> [1..1] Text 882
2.4.2.15.6  BookingDate <BookgDt>
Presence: [0..1]
Definition: Date and time when an entry is posted to an account on the account servicer's books.
Usage: Booking date is the expected booking date, unless the status is booked, in which case it is the
actual booking date.
BookingDate <BookgDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 826 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 826
Or}   DateTime <DtTm> [1..1] DateTime 826
2.4.2.15.7  ValueDate <ValDt>
Presence: [0..1]
Definition: Date and time at which assets become available to the account owner in case of a credit
entry, or cease to be available to the account owner in case of a debit entry.
Usage: If entry status is pending and value date is present, then the value date refers to an expected/
requested value date.
For entries subject to availability/float and for which availability information is provided, the value date
must not be used. In this case the availability component identifies the number of availability days.
ValueDate <ValDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 826 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 826
Or}   DateTime <DtTm> [1..1] DateTime 826
2.4.2.15.8  AccountServicerReference <AcctSvcrRef>
Presence: [0..1]
Definition: Unique reference as assigned by the account servicing institution to unambiguously identify
the entry.
Datatype: "Max35Text" on page 916
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
71 March 2026
```

