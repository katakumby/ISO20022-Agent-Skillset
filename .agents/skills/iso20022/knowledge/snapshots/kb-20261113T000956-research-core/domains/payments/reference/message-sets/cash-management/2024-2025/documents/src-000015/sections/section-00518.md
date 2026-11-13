---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["29 camt.051.001.07 LiquidityDebitTransferV07", "29.4 Message Building Blocks", "29.4.2 LiquidityDebitTransfer <LqdtyDbtTrf>", "29.4.2.1 LiquidityTransferIdentification <LqdtyTrfId>"]
file_pages: [680]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.051.001.07"]
---

# 29.4.2.1 LiquidityTransferIdentification <LqdtyTrfId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 680 to 680.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 680

```text
LiquidityDebitTransfer <LqdtyDbtTrf> contains the following LiquidityDebitTransfer4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LiquidityTransferIdentification <LqdtyTrfId> [0..1]  680
     InstructionIdentification <InstrId> [0..1] Text 680
     EndToEndIdentification <EndToEndId> [1..1] Text 681
     TransactionIdentification <TxId> [0..1] Text 681
     UETR <UETR> [0..1] IdentifierSet 681
   Creditor <Cdtr> [0..1] ± 681
   CreditorAccount <CdtrAcct> [0..1] ± C9, C8 682
   TransferredAmount <TrfdAmt> [1..1] ± 683
   Debtor <Dbtr> [0..1] ± 683
   DebtorAccount <DbtrAcct> [0..1] ± C9, C8 684
   SettlementDate <SttlmDt> [0..1] Date 685
Constraints
• DebtorAccountRule
At least DebitAccount or Debtor must be present, or both.
Following Must be True
    /Debtor Must be present
 Or    /DebtorAccount Must be present
29.4.2.1  LiquidityTransferIdentification <LqdtyTrfId>
Presence: [0..1]
Definition: Used to uniquely identify the liquidity transfer.
LiquidityTransferIdentification <LqdtyTrfId> contains the following PaymentIdentification8
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionIdentification <InstrId> [0..1] Text 680
   EndToEndIdentification <EndToEndId> [1..1] Text 681
   TransactionIdentification <TxId> [0..1] Text 681
   UETR <UETR> [0..1] IdentifierSet 681
29.4.2.1.1  InstructionIdentification <InstrId>
Presence: [0..1]
Definition: Unique identification as assigned by an instructing party for an instructed party to
unambiguously identify the instruction.
Approved by the Payments SEG on 04 February 2025 camt.051.001.07 LiquidityDebitTransferV07
Cash Management - Maintenance 2024 - 2025 680 February 2025
```

