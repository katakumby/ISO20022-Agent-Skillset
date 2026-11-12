---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.6 IntermediaryInformation <IntrmyInf>", "8.4.7.7 Transaction <Tx>", "8.4.7.7.19 TransactionDetails <TxDtls>", "8.4.7.7.19.1 TransactionActivity <TxActvty>"]
file_pages: [232]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.7.7.19.1 TransactionActivity <TxActvty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 232 to 232.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 232

```text
8.4.7.7.19.1  TransactionActivity <TxActvty>
Presence: [1..1]
Definition: Specifies the type of activity to which this instruction relates.
TransactionActivity <TxActvty> contains one of the following elements (see
"TransactionActivity3Choice" on page 2034 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2034
Or}   Proprietary <Prtry> [1..1] ± 2034
8.4.7.7.19.2  SettlementTransactionOrCorporateActionEventType <SttlmTxOrCorpActnEvtTp>
Presence: [0..1]
Definition: Choice of type for the transaction reported.
SettlementTransactionOrCorporateActionEventType <SttlmTxOrCorpActnEvtTp> contains one of
the following elements (see "SettlementOrCorporateActionEvent35Choice" on page 1658 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 1658
Or}   CorporateActionEventType <CorpActnEvtTp> [1..1] ± C13 1659
8.4.7.7.19.3  SecuritiesMovementType <SctiesMvmntTp>
Presence: [1..1]
Definition: Specifies if the movement on a securities account results from a deliver or a receive
instruction.
Datatype: "ReceiveDelivery1Code" on page 2113
CodeName Name Definition
DELI Delivery Financial instruments will be debited
from the safekeeping account.
RECE Receive Financial instruments will be credited to
the safekeeping account.
8.4.7.7.19.4  Payment <Pmt>
Presence: [1..1]
Definition: Specifies how the transaction is to be settled, for example, against payment.
Datatype: "DeliveryReceiptType2Code" on page 2058
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 232 March 2026
```

