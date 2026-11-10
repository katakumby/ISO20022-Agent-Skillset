---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01", "77.4 Message Building Blocks", "77.4.1 QueryDefinition <QryDef>", "77.4.1.2 SearchCriteria <SchCrit>", "77.4.1.2.2 InstructionQueryType <InstrQryTp>"]
file_pages: [2694]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.032.001.01"]
---

# 77.4.1.2.2 InstructionQueryType <InstrQryTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2694 to 2694.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2694

```text
Datatype: "Max35Text" on page 3328
77.4.1.2.2  InstructionQueryType <InstrQryTp>
Presence: [1..1]
Definition: Type of underlying transaction to be cancelled, such as an settlement instruction or an intra-
position movement.
Datatype: "InstructionQueryType1Code" on page 3256
CodeName Name Definition
SETT SettlementInstruction Query is performed on settlement
transactions.
IPOS IntraPositionMovement Query is performed on intra-position
movements.
BOTH SettlementAndIntraPosition Query is performed on both settlement
transactions and intra-position
movements.
77.4.1.2.3  ProcessingStatus <PrcgSts>
Presence: [0..*]
Definition: Provides the status of settlement of a transaction.
ProcessingStatus <PrcgSts> contains one of the following CancellationProcessingStatus9Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2694
Or}   Proprietary <Prtry> [1..1] ± 2695
77.4.1.2.3.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of a cancellation request.
Datatype: "CancellationProcessingStatus3Code" on page 3219
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.032.001.01
SecuritiesTransactionCancellationRequestQueryV0
1
Target2-Securities 2694 August 2026
```

