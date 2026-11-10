---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.5 Balance", "6.1.5.3 CashBalance8", "6.1.5.3.4 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [820]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.5.3.4 CreditDebitIndicator <CdtDbtInd>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 820 to 820.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 820

```text
6.1.5.3.4  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether the balance is a credit or a debit balance.
Usage: A zero balance is considered to be a credit balance.
Datatype: "CreditDebitCode" on page 892
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
6.1.5.3.5  Date <Dt>
Presence: [1..1]
Definition: Indicates the date (and time) of the balance.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 826 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 826
Or}   DateTime <DtTm> [1..1] DateTime 826
6.1.5.3.6  Availability <Avlbty>
Presence: [0..*]
Definition: Set of elements used to indicate when the booked amount of money will become available,
that is can be accessed and starts generating interest.
Usage: This type of information is used in the US and is linked to particular instruments such as
cheques.
Example: When a cheque is deposited, it will be booked on the deposit day, but the amount of money
will only be accessible as of the indicated availability day (according to national banking regulations).
Availability <Avlbty> contains the following elements (see "CashAvailability1" on page 824 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [1..1]  824
{Or     NumberOfDays <NbOfDays> [1..1] Text 825
Or}     ActualDate <ActlDt> [1..1] Date 825
   Amount <Amt> [1..1] Amount C1, C5 825
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 825
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
820 March 2026
```

