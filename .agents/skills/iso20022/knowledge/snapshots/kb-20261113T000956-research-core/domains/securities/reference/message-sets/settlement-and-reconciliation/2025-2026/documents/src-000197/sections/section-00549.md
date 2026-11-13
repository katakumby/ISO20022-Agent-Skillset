---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.2 NumberCounts <NbCounts>"]
file_pages: [830]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.2 NumberCounts <NbCounts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 830 to 830.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 830

```text
TransactionIdentificationDetails <TxIdDtls> contains the following elements (see
"SettlementTypeAndIdentification29" on page 1516 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1517
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1517
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1517
   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 1517
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1518
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1518
   Payment <Pmt> [1..1] CodeSet 1518
   CommonIdentification <CmonId> [0..1] Text 1518
   PoolIdentification <PoolId> [0..1] Text 1518
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 1519
   NonceIdentification <NonceId> [0..1] Text 1519
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
26.4.2 NumberCounts <NbCounts>
Presence: [0..1]
Definition: Count of the number of transactions linked.
Impacted by: C20 "CurrentInstructionNumberRule"
NumberCounts <NbCounts> contains one of the following elements (see "NumberCount2Choice" on
page 1590 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrentInstructionNumber <CurInstrNb> [1..1] Text 1590
Or}   TotalNumber <TtlNb> [1..1]  C19, C9 1590
     CurrentInstructionNumber <CurInstrNb> [1..1] Text 1591
     TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 1591
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 830 March 2026
```

