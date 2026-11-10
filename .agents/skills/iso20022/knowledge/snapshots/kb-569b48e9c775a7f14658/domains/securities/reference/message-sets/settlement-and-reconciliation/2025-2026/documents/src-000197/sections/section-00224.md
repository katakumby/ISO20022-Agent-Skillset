---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.7.15 TransactionDetails <TxDtls>", "9.4.7.15.4 Payment <Pmt>"]
file_pages: [337]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.7.15.4 Payment <Pmt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 337 to 337.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 337

```text
Definition: Specifies if the movement on a securities account results from a deliver or a receive
instruction.
Datatype: "ReceiveDelivery1Code" on page 2113
CodeName Name Definition
DELI Delivery Financial instruments will be debited
from the safekeeping account.
RECE Receive Financial instruments will be credited to
the safekeeping account.
9.4.7.15.4  Payment <Pmt>
Presence: [1..1]
Definition: Specifies how the transaction is to be settled, for example, against payment.
Datatype: "DeliveryReceiptType2Code" on page 2058
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
9.4.7.15.5  SettlementParameters <SttlmParams>
Presence: [0..1]
Definition: Parameters applied to the settlement of a security transfer.
Impacted by: C6 "CashClearingSystemRule", C38 "SettlementDetailsRule"
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 337 March 2026
```

