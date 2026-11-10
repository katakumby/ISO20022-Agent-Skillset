---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "7.4 Message Building Blocks", "7.4.6 FinancialInstrument <FinInstrm>", "7.4.6.3 SubBalance <SubBal>", "7.4.6.3.3 IntraPositionMovement <IntraPosMvmnt>", "7.4.6.3.3.1 Identification <Id>"]
file_pages: [193]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.016.001.10"]
---

# 7.4.6.3.3.1 Identification <Id>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 193 to 193.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 193

```text
IntraPositionMovement <IntraPosMvmnt> contains the following IntraPositionMovementDetails21
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 193
   SettledQuantity <SttldQty> [1..1] ± C12 194
   PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± C12 194
   RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± C12 194
   SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 195
   BalanceTo <BalTo> [1..1] ± 195
   SettlementDate <SttlmDt> [1..1] ± 195
   AvailableDate <AvlblDt> [0..1] ± 196
   AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 196
   CorporateActionEventType <CorpActnEvtTp> [0..1] ± C13 196
   CollateralMonitorAmount <CollMntrAmt> [0..1] ± 197
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 197
   SupplementaryData <SplmtryData> [0..*] ± C22 197
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if InstructionProcessingAdditionalDetails
is present, then it must not contain information that can be provided in a structured field.
7.4.6.3.3.1  Identification <Id>
Presence: [0..1]
Definition: Identifications (account owner and/or account servicer) of the intra-position movement.
Identification <Id> contains one of the following elements (see "References72Choice" on page 1484 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1485
Or   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 1485
Or   PoolIdentification <PoolId> [1..1] Text 1485
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 1485
Or   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 1485
Or}   ProcessorTransactionIdentification <PrcrTxId> [1..1] Text 1485
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 193 March 2026
```

