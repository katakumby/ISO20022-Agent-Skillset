---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01", "6.4 Message Building Blocks", "6.4.1 QueryDefinition <QryDef>", "6.4.1.2 SearchCriteria <SchCrit>", "6.4.1.2.2 InstructionQueryType <InstrQryTp>"]
file_pages: [139]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.032.001.01"]
---

# 6.4.1.2.2 InstructionQueryType <InstrQryTp>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 139 to 139.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 139

```text
Datatype: "Max35Text" on page 345
6.4.1.2.2  InstructionQueryType <InstrQryTp>
Presence: [1..1]
Definition: Type of underlying transaction to be cancelled, such as an settlement instruction or an intra-
position movement.
Datatype: "InstructionQueryType1Code" on page 327
CodeName Name Definition
SETT SettlementInstruction Query is performed on settlement
transactions.
IPOS IntraPositionMovement Query is performed on intra-position
movements.
BOTH SettlementAndIntraPosition Query is performed on both settlement
transactions and intra-position
movements.
6.4.1.2.3  ProcessingStatus <PrcgSts>
Presence: [0..*]
Definition: Provides the status of settlement of a transaction.
ProcessingStatus <PrcgSts> contains one of the following CancellationProcessingStatus9Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 139
Or}   Proprietary <Prtry> [1..1] ± 140
6.4.1.2.3.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of a cancellation request.
Datatype: "CancellationProcessingStatus3Code" on page 316
CodeName Name Definition
CANP PendingCancellation Cancellation is pending. It is not known
at this time whether cancellation can be
affected.
REJT Rejected Cancellation has been rejected for
further processing.
REPR InRepair Cancellation request is in repair.
PACK Accepted Cancellation request has been
acknowledged for further processing by
the account servicer.
DEND Denied Cancellation will not be executed.
CAND CancellationCompleted Cancellation has been completed.
Approved by the Securities SEG on 21 August 2025 semt.032.001.01
SecuritiesTransactionCancellationRequestQueryV0
1
Target2-Securities - Settlement Restrictions 139 September 2025
```

