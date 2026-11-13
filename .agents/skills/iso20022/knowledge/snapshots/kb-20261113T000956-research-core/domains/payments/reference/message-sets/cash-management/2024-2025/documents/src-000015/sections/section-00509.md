---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["28 camt.050.001.07 LiquidityCreditTransferV07", "28.4 Message Building Blocks", "28.4.2 LiquidityCreditTransfer <LqdtyCdtTrf>", "28.4.2.1 LiquidityTransferIdentification <LqdtyTrfId>"]
file_pages: [671]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.050.001.07"]
---

# 28.4.2.1 LiquidityTransferIdentification <LqdtyTrfId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 671 to 671.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 671

```text
LiquidityCreditTransfer <LqdtyCdtTrf> contains the following LiquidityCreditTransfer4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LiquidityTransferIdentification <LqdtyTrfId> [0..1]  671
     InstructionIdentification <InstrId> [0..1] Text 671
     EndToEndIdentification <EndToEndId> [1..1] Text 672
     TransactionIdentification <TxId> [0..1] Text 672
     UETR <UETR> [0..1] IdentifierSet 672
   Creditor <Cdtr> [0..1] ± 672
   CreditorAccount <CdtrAcct> [0..1] ± C9, C8 673
   TransferredAmount <TrfdAmt> [1..1] ± 674
   Debtor <Dbtr> [0..1] ± 674
   DebtorAccount <DbtrAcct> [0..1] ± C9, C8 675
   SettlementDate <SttlmDt> [0..1] Date 676
Constraints
• CreditAccountRule
At least CreditAccount or Creditor must be present, or both.
Following Must be True
    /CreditorAccount Must be present
 Or    /Creditor Must be present
28.4.2.1  LiquidityTransferIdentification <LqdtyTrfId>
Presence: [0..1]
Definition: Used to uniquely identify the liquidity transfer.
LiquidityTransferIdentification <LqdtyTrfId> contains the following PaymentIdentification8
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionIdentification <InstrId> [0..1] Text 671
   EndToEndIdentification <EndToEndId> [1..1] Text 672
   TransactionIdentification <TxId> [0..1] Text 672
   UETR <UETR> [0..1] IdentifierSet 672
28.4.2.1.1  InstructionIdentification <InstrId>
Presence: [0..1]
Definition: Unique identification as assigned by an instructing party for an instructed party to
unambiguously identify the instruction.
Approved by the Payments SEG on 04 February 2025 camt.050.001.07 LiquidityCreditTransferV07
Cash Management - Maintenance 2024 - 2025 671 February 2025
```

