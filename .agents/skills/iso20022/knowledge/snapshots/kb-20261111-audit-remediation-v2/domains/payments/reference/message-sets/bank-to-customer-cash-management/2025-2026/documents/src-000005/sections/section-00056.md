---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.1 References <Refs>", "2.4.2.15.18.2.1.1 MessageIdentification <MsgId>"]
file_pages: [121]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.1.1 MessageIdentification <MsgId>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 121 to 121.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 121

```text
Definition: Provides the identification of the underlying transaction.
References <Refs> contains the following TransactionReferences10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [0..1] Text 121
   AccountServicerReference <AcctSvcrRef> [0..1] Text 121
   PaymentInformationIdentification <PmtInfId> [0..1] Text 121
   InstructionIdentification <InstrId> [0..1] Text 122
   EndToEndIdentification <EndToEndId> [0..1] Text 122
   UETR <UETR> [0..1] IdentifierSet 122
   TransactionIdentification <TxId> [0..1] Text 122
   MandateIdentification <MndtId> [0..1] Text 122
   ChequeNumber <ChqNb> [0..1] Text 123
   ClearingSystemReference <ClrSysRef> [0..1] Text 123
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 123
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 123
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 123
   ProcessingIdentification <PrcgId> [0..1] Text 123
   ReturnIdentification <RtrId> [0..1] Text 123
   Proprietary <Prtry> [0..*]  124
     Type <Tp> [1..1] Text 124
     Reference <Ref> [1..1] Text 124
2.4.2.15.18.2.1.1  MessageIdentification <MsgId>
Presence: [0..1]
Definition: Point to point reference, as assigned by the instructing party of the underlying message.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.1.2  AccountServicerReference <AcctSvcrRef>
Presence: [0..1]
Definition: Unique reference, as assigned by the account servicing institution, to unambiguously identify
the instruction.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.1.3  PaymentInformationIdentification <PmtInfId>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
121 March 2026
```

