---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.16 PendingDeliveryBalance <PdgDlvryBal>"]
file_pages: [810]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.16 PendingDeliveryBalance <PdgDlvryBal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 810 to 810.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 810

```text
14.4.3.5.3.16  PendingDeliveryBalance <PdgDlvryBal>
Presence: [0..*]
Definition: Balance of financial instruments that are pending delivery.
PendingDeliveryBalance <PdgDlvryBal> contains the following PendingBalance7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Balance <Bal> [1..1] ± 810
   PendingTransactions <PdgTxs> [0..*] ± 810
14.4.3.5.3.16.1  Balance <Bal>
Presence: [1..1]
Definition: Signed quantity of balance.
Balance <Bal> contains the following elements (see "SignedQuantityFormat10" on page 1090 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.16.2  PendingTransactions <PdgTxs>
Presence: [0..*]
Definition: Overall process covering the trade and settlement transactions of financial instruments.
PendingTransactions <PdgTxs> contains the following elements (see
"SettlementTypeAndIdentification25" on page 880 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Payment <Pmt> [1..1] CodeSet 880
   TransactionIdentification <TxId> [1..1] Text 880
   SettlementDate <SttlmDt> [0..1] ± 880
14.4.3.5.3.17  PendingReceiptBalance <PdgRctBal>
Presence: [0..*]
Definition: Balance of financial instruments that are pending receipt.
PendingReceiptBalance <PdgRctBal> contains the following PendingBalance7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Balance <Bal> [1..1] ± 811
   PendingTransactions <PdgTxs> [0..*] ± 811
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 810 February 2026
```

