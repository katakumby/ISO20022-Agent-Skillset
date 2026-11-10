---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.12 PaymentTypeInformation <PmtTpInf>"]
file_pages: [423]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.12 PaymentTypeInformation <PmtTpInf>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 423 to 423.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 423

```text
3.4.2.15.18.2.12  PaymentTypeInformation <PmtTpInf>
Presence: [0..1]
Definition: Set of elements used to further specify the type of transaction.
PaymentTypeInformation <PmtTpInf> contains the following elements (see
"PaymentTypeInformation27" on page 868 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 869
   ClearingChannel <ClrChanl> [0..1] CodeSet 869
   ServiceLevel <SvcLvl> [0..*]  870
{Or     Code <Cd> [1..1] CodeSet 870
Or}     Proprietary <Prtry> [1..1] Text 870
   LocalInstrument <LclInstrm> [0..1]  870
{Or     Code <Cd> [1..1] CodeSet 870
Or}     Proprietary <Prtry> [1..1] Text 870
   SequenceType <SeqTp> [0..1] CodeSet 871
   CategoryPurpose <CtgyPurp> [0..1]  871
{Or     Code <Cd> [1..1] CodeSet 871
Or}     Proprietary <Prtry> [1..1] Text 871
3.4.2.15.18.2.13  Purpose <Purp>
Presence: [0..1]
Definition: Underlying reason for the payment transaction.
Usage: Purpose is used by the end-customers, that is initiating party, (ultimate) debtor, (ultimate)
creditor to provide information concerning the nature of the payment. Purpose is a content element,
which is not used for processing by any of the agents involved in the payment chain.
Purpose <Purp> contains one of the following elements (see "Purpose2Choice" on page 851 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 851
Or}   Proprietary <Prtry> [1..1] Text 851
3.4.2.15.18.2.14  RelatedRemittanceInformation <RltdRmtInf>
Presence: [0..10]
Definition: Provides information related to the handling of the remittance information by any of the
agents in the transaction processing chain.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
423 March 2026
```

