---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.58 AdditionalParameters33", "35.1.16.58.8 CounterpartyMarketInfrastructureTransactionIdentification <CtrPtyMktInfrstrctrTxId>"]
file_pages: [1597]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.58.8 CounterpartyMarketInfrastructureTransactionIdentification <CtrPtyMktInfrstrctrTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1597 to 1597.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1597

```text
35.1.16.58.8  CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a counterparty transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
35.1.16.58.9  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction assigned by the processor of the instruction other than the
account owner the account servicer and the market infrastructure.
Datatype: "Max35Text" on page 2192
35.1.16.59  ProcessingPosition8Choice
Definition: Choice of format for the processing position.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1597
Or}   Proprietary <Prtry> [1..1] ± 1598
Constraints
• WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and which
must be executed together. Even if one single transactions/instructions/notifications can not be
executed, then all the other transactions/instructions/notifications must also be kept pending.
Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/instructions/
notifications.
35.1.16.59.1  Code <Cd>
Presence: [1..1]
Definition: Processing position expressed as an ISO 20022 code.
Datatype: "ProcessingPosition4Code" on page 2112
CodeName Name Definition
AFTE After Specifies that the transaction/instruction
is to be executed after the linked
transaction/instruction.
BEFO Before Specifies that the transaction/instruction
is to be executed before the linked
transaction/instruction.
WITH With Specifies that the transaction/instruction
is to be executed with the linked
transaction/instruction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1597 March 2026
```

