---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.4 AmountDetails <AmtDtls>"]
file_pages: [643]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.4 AmountDetails <AmtDtls>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 643 to 643.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 643

```text
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
4.4.2.14.18.2.4  AmountDetails <AmtDtls>
Presence: [0..1]
Definition: Provides detailed information on the original amount.
Usage: This component (on transaction level) should be used in case booking is for a single transaction
and the original amount is different from the entry amount. It can also be used in case individual original
amounts are provided in case of a batch or aggregate booking.
AmountDetails <AmtDtls> contains the following elements (see "AmountAndCurrencyExchange4" on
page 802 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructedAmount <InstdAmt> [0..1] ± 802
   TransactionAmount <TxAmt> [0..1] ± 803
   CounterValueAmount <CntrValAmt> [0..1] ± 803
   AnnouncedPostingAmount <AnncdPstngAmt> [0..1] ± 804
   ProprietaryAmount <PrtryAmt> [0..*] ± 804
4.4.2.14.18.2.5  Availability <Avlbty>
Presence: [0..*]
Definition: Indicates when the booked amount of money will become available, that is can be accessed
and starts generating interest.
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
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
643 March 2026
```

