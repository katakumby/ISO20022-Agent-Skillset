---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13", "19.4 Message Building Blocks"]
file_pages: [613]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.025.001.13"]
preceding_topic_continuations: [{"constraint_ids": ["C64"], "until_heading": "19.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 613, "topic": "19.3 Constraints", "reference_path": "domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00400.md"}]
---

# 19.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 613 to 613.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 613, C64 before **19.4 Message Building Blocks** continue [19.3 Constraints](section-00400.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 613

```text
Collateral (giver) Out Return
TransactionIdentificationDetails/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: CollateralOut (COLO)
Collateral (taker) In Initiation
TransactionIdentificationDetails/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI)
Collateral (taker) In Return
TransactionIdentificationDetails/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI).
This constraint is defined at the MessageDefinition level.
C64 VendorPresenceRule
If the settlement standing instruction database is a vendor database, then the vendor must be
identified.
19.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
19.4.1 TransactionIdentificationDetails <TxIdDtls>
Presence: [1..1]
Definition: Provides transaction type and identification information.
Impacted by: C29 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 613 March 2026
```

