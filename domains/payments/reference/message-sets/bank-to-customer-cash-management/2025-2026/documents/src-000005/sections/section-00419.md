---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.1 References <Refs>", "4.4.2.14.18.2.1.1 MessageIdentification <MsgId>"]
file_pages: [639]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.1.1 MessageIdentification <MsgId>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 639 to 639.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 639

```text
Definition: Provides the identification of the underlying transaction.
References <Refs> contains the following TransactionReferences10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [0..1] Text 639
   AccountServicerReference <AcctSvcrRef> [0..1] Text 639
   PaymentInformationIdentification <PmtInfId> [0..1] Text 639
   InstructionIdentification <InstrId> [0..1] Text 640
   EndToEndIdentification <EndToEndId> [0..1] Text 640
   UETR <UETR> [0..1] IdentifierSet 640
   TransactionIdentification <TxId> [0..1] Text 640
   MandateIdentification <MndtId> [0..1] Text 640
   ChequeNumber <ChqNb> [0..1] Text 641
   ClearingSystemReference <ClrSysRef> [0..1] Text 641
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 641
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 641
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 641
   ProcessingIdentification <PrcgId> [0..1] Text 641
   ReturnIdentification <RtrId> [0..1] Text 641
   Proprietary <Prtry> [0..*]  642
     Type <Tp> [1..1] Text 642
     Reference <Ref> [1..1] Text 642
4.4.2.14.18.2.1.1  MessageIdentification <MsgId>
Presence: [0..1]
Definition: Point to point reference, as assigned by the instructing party of the underlying message.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.1.2  AccountServicerReference <AcctSvcrRef>
Presence: [0..1]
Definition: Unique reference, as assigned by the account servicing institution, to unambiguously identify
the instruction.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.1.3  PaymentInformationIdentification <PmtInfId>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
639 March 2026
```

