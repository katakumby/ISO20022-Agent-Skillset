---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["23 sese.029.001.08 SecuritiesSettlementAllegementRemovalAdviceV08", "23.4 Message Building Blocks"]
file_pages: [772]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.029.001.08"]
preceding_topic_continuations: [{"constraint_ids": ["C22"], "until_heading": "23.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 772, "topic": "23.3 Constraints", "reference_path": "domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00504.md"}]
---

# 23.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 772 to 772.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 772, C22 before **23.4 Message Building Blocks** continue [23.3 Constraints](section-00504.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 772

```text
C22 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
23.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
23.4.1 AccountServicerTransactionIdentification
<AcctSvcrTxId>
Presence: [1..1]
Definition: Provides transaction type and identification information.
AccountServicerTransactionIdentification <AcctSvcrTxId> contains the following elements (see
"SettlementTypeAndIdentification18" on page 1501 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 1501
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1501
   Payment <Pmt> [1..1] CodeSet 1501
23.4.2 MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
23.4.3 CounterpartyMarketInfrastructureTransactionIdentific
ation <CtrPtyMktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a counterparty transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
23.4.4 AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
Approved by the Securities SEG on 27 January 2026 sese.029.001.08
SecuritiesSettlementAllegementRemovalAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 772 March 2026
```

