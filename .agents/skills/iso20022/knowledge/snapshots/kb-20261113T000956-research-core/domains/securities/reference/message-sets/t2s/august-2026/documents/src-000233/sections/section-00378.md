---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02", "20.4 Message Building Blocks", "20.4.2 QueryDefinition <QryDef>", "20.4.2.2 SearchCriteria <SchCrit>", "20.4.2.2.2 ProcessingStatus <PrcgSts>", "20.4.2.2.2.1 Code <Cd>"]
file_pages: [485]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.082.001.02"]
---

# 20.4.2.2.2.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 485 to 485.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 485

```text
Definition: Provides the status of settlement of a transaction.
ProcessingStatus <PrcgSts> contains one of the following CancellationProcessingStatus9Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 485
Or}   Proprietary <Prtry> [1..1] ± 485
20.4.2.2.2.1  Code <Cd>
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
20.4.2.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of a cancellation request.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
20.4.2.2.3  CashAccount <CshAcct>
Presence: [0..*]
Definition: Account in which cash is maintained.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.082.001.02
IntraBalanceMovementCancellationQueryV02
Target2-Securities 485 August 2026
```

