---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.2 AdditionalParameters <AddtlParams>"]
file_pages: [1009]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.2 AdditionalParameters <AddtlParams>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1009 to 1009.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1009

```text
Securities Lending Initiation
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: SecuritiesLending (SECL)
Securities Lending Return
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: SecuritiesLending (SECL)
Securities Borrowing Initiation
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: SecuritiesBorrowing (SECB)
Securities Borrowing Return
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: SecuritiesBorrowing (SECB).
29.4.2 AdditionalParameters <AddtlParams>
Presence: [0..1]
Definition: Additional parameters for the transaction.
Impacted by: C30 "PartialSettlementGuideline"
AdditionalParameters <AddtlParams> contains the following elements (see
"AdditionalParameters24" on page 1627 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PreConfirmation <PreConf> [0..1] CodeSet 1627
   PartialSettlement <PrtlSttlm> [0..1] CodeSet 1627
   PreviousPartialConfirmationIdentification
<PrvsPrtlConfId>
[0..1] Text 1628
Constraints
• PartialSettlementGuideline
Partial settlement information only applies to markets where partial settlement is allowed.
The PartialSettlement field should be used as follows:
- with code PAIN in the first message(s) (there may be more than one) confirming the partial
settlement of an instruction.
- with code PARC in the very last message sent to confirm the settlement of the remaining part.
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1009 March 2026
```

