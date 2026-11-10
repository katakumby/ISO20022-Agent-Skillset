---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.9 RelatedParties <RltdPties>", "4.4.2.14.18.2.9.1 InitiatingParty <InitgPty>"]
file_pages: [651]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.9.1 InitiatingParty <InitgPty>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 651 to 651.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 651

```text
RelatedParties <RltdPties> contains the following TransactionParties12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InitiatingParty <InitgPty> [0..1]  651
{Or     Party <Pty> [1..1] ± 652
Or}     Agent <Agt> [1..1] ± 653
   Debtor <Dbtr> [0..1]  654
{Or     Party <Pty> [1..1] ± 654
Or}     Agent <Agt> [1..1] ± 655
   DebtorAccount <DbtrAcct> [0..1] ± C19,
C17
656
   UltimateDebtor <UltmtDbtr> [0..1]  657
{Or     Party <Pty> [1..1] ± 657
Or}     Agent <Agt> [1..1] ± 658
   Creditor <Cdtr> [0..1]  659
{Or     Party <Pty> [1..1] ± 659
Or}     Agent <Agt> [1..1] ± 660
   CreditorAccount <CdtrAcct> [0..1] ± C19,
C17
661
   UltimateCreditor <UltmtCdtr> [0..1]  662
{Or     Party <Pty> [1..1] ± 662
Or}     Agent <Agt> [1..1] ± 663
   TradingParty <TradgPty> [0..1]  664
{Or     Party <Pty> [1..1] ± 664
Or}     Agent <Agt> [1..1] ± 665
   Proprietary <Prtry> [0..*]  666
     Type <Tp> [1..1] Text 666
     Party <Pty> [1..1]  666
{Or       Party <Pty> [1..1] ± 667
Or}       Agent <Agt> [1..1] ± 668
4.4.2.14.18.2.9.1  InitiatingParty <InitgPty>
Presence: [0..1]
Definition: Party that initiated the payment that is reported in the entry.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
651 March 2026
```

