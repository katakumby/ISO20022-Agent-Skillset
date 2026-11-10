---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.9 RelatedParties <RltdPties>", "3.4.2.15.18.2.9.1 InitiatingParty <InitgPty>"]
file_pages: [393]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.9.1 InitiatingParty <InitgPty>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 393 to 393.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 393

```text
RelatedParties <RltdPties> contains the following TransactionParties12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InitiatingParty <InitgPty> [0..1]  393
{Or     Party <Pty> [1..1] ± 394
Or}     Agent <Agt> [1..1] ± 395
   Debtor <Dbtr> [0..1]  396
{Or     Party <Pty> [1..1] ± 396
Or}     Agent <Agt> [1..1] ± 397
   DebtorAccount <DbtrAcct> [0..1] ± C20,
C18
398
   UltimateDebtor <UltmtDbtr> [0..1]  399
{Or     Party <Pty> [1..1] ± 399
Or}     Agent <Agt> [1..1] ± 400
   Creditor <Cdtr> [0..1]  401
{Or     Party <Pty> [1..1] ± 401
Or}     Agent <Agt> [1..1] ± 402
   CreditorAccount <CdtrAcct> [0..1] ± C20,
C18
403
   UltimateCreditor <UltmtCdtr> [0..1]  404
{Or     Party <Pty> [1..1] ± 404
Or}     Agent <Agt> [1..1] ± 405
   TradingParty <TradgPty> [0..1]  406
{Or     Party <Pty> [1..1] ± 406
Or}     Agent <Agt> [1..1] ± 407
   Proprietary <Prtry> [0..*]  408
     Type <Tp> [1..1] Text 408
     Party <Pty> [1..1]  408
{Or       Party <Pty> [1..1] ± 409
Or}       Agent <Agt> [1..1] ± 410
3.4.2.15.18.2.9.1  InitiatingParty <InitgPty>
Presence: [0..1]
Definition: Party that initiated the payment that is reported in the entry.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
393 March 2026
```

