---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 semt.015.001.10 IntraPositionMovementConfirmationV10", "6.4 Message Building Blocks"]
file_pages: [167]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.015.001.10"]
preceding_topic_continuations: [{"constraint_ids": ["C21"], "until_heading": "6.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 167, "topic": "6.3 Constraints", "reference_path": "domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00119.md"}]
---

# 6.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 167 to 167.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 167, C21 before **6.4 Message Building Blocks** continue [6.3 Constraints](section-00119.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 167

```text
This constraint is defined at the MessageDefinition level.
C21 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
6.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
6.4.1 AdditionalParameters <AddtlParams>
Presence: [0..1]
Definition: Additional parameters for the transaction.
AdditionalParameters <AddtlParams> contains the following elements (see
"AdditionalParameters33" on page 1595 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartialSettlement <PrtlSttlm> [0..1] CodeSet 1595
   PreviousPartialConfirmationIdentification
<PrvsPrtlConfId>
[0..1] Text 1596
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 1596
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1596
   PoolIdentification <PoolId> [0..1] Text 1596
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 1596
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1596
   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 1597
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1597
6.4.2 Linkage <Lkg>
Presence: [0..1]
Definition: Link to another transaction that triggered the intra-position movement.
Linkage <Lkg> contains the following Linkages75 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 167
6.4.2.1  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 semt.015.001.10
IntraPositionMovementConfirmationV10
Settlement And Reconciliation - Maintenance 2025 - 2026 167 March 2026
```

