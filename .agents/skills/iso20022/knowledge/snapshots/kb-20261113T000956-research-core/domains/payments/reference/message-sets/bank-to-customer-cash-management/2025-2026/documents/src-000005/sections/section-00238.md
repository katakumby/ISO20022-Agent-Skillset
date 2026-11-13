---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.1 References <Refs>", "3.4.2.15.18.2.1.1 MessageIdentification <MsgId>"]
file_pages: [381]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.1.1 MessageIdentification <MsgId>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 381 to 381.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 381

```text
Definition: Provides the identification of the underlying transaction.
References <Refs> contains the following TransactionReferences10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [0..1] Text 381
   AccountServicerReference <AcctSvcrRef> [0..1] Text 381
   PaymentInformationIdentification <PmtInfId> [0..1] Text 381
   InstructionIdentification <InstrId> [0..1] Text 382
   EndToEndIdentification <EndToEndId> [0..1] Text 382
   UETR <UETR> [0..1] IdentifierSet 382
   TransactionIdentification <TxId> [0..1] Text 382
   MandateIdentification <MndtId> [0..1] Text 382
   ChequeNumber <ChqNb> [0..1] Text 383
   ClearingSystemReference <ClrSysRef> [0..1] Text 383
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 383
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 383
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 383
   ProcessingIdentification <PrcgId> [0..1] Text 383
   ReturnIdentification <RtrId> [0..1] Text 383
   Proprietary <Prtry> [0..*]  384
     Type <Tp> [1..1] Text 384
     Reference <Ref> [1..1] Text 384
3.4.2.15.18.2.1.1  MessageIdentification <MsgId>
Presence: [0..1]
Definition: Point to point reference, as assigned by the instructing party of the underlying message.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.1.2  AccountServicerReference <AcctSvcrRef>
Presence: [0..1]
Definition: Unique reference, as assigned by the account servicing institution, to unambiguously identify
the instruction.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.1.3  PaymentInformationIdentification <PmtInfId>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
381 March 2026
```

