---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.5 AccountEntry <AcctNtry>", "5.4.2.1.3.2.1.5.2 Entry <Ntry>", "5.4.2.1.3.2.1.5.2.4 Identification <Id>"]
file_pages: [322]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.5.2.4 Identification <Id>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 322 to 322.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 322

```text
CodeName Name Definition
status Booked in subsequent account
report or statement. Status Pending
cannot be reversed.
FUTR Future Entry is on the books of the account
servicer and value will be applied to the
account owner at a future date and time.
5.4.2.1.3.2.1.5.2.4  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for an entry, as assigned by the account servicer.
Datatype: "Max35Text" on page 889
5.4.2.1.3.2.1.5.2.5  StatementIdentification <StmtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the account servicer, to unambiguously identify the
account statement.
Datatype: "Max35Text" on page 889
5.4.2.1.3.2.1.5.2.6  AccountServicerReference <AcctSvcrRef>
Presence: [0..1]
Definition: Sequential number of the statement, as assigned by the account servicer.
Usage: The sequential number is increased incrementally for each statement sent electronically.
Datatype: "Number" on page 886
5.4.2.1.3.2.1.5.2.7  AdditionalEntryInformation <AddtlNtryInf>
Presence: [0..*]
Definition: Further details of the entry.
Datatype: "Max140Text" on page 888
5.4.2.1.3.2.1.6  SecuritiesTransactionReferences <SctiesTxRefs>
Presence: [0..1]
Definition: Provides the references of the underlying securities transaction.
SecuritiesTransactionReferences <SctiesTxRefs> contains the following
SecuritiesTransactionReferences1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 323
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 323
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 323
   ProcessingIdentification <PrcgId> [0..1] Text 323
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 322 February 2025
```

