---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02", "13.4 Message Building Blocks", "13.4.2 QueryDefinition <QryDef>", "13.4.2.2 SearchCriteria <SchCrit>", "13.4.2.2.2 ProcessingStatus <PrcgSts>", "13.4.2.2.2.1 Code <Cd>"]
file_pages: [294]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.082.001.02"]
---

# 13.4.2.2.2.1 Code <Cd>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 294 to 294.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 294

```text
Definition: Provides the status of settlement of a transaction.
ProcessingStatus <PrcgSts> contains one of the following CancellationProcessingStatus9Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 294
Or}   Proprietary <Prtry> [1..1] ± 294
13.4.2.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of a cancellation request.
Datatype: "CancellationProcessingStatus3Code" on page 476
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
13.4.2.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of a cancellation request.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 409 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
13.4.2.2.3  CashAccount <CshAcct>
Presence: [0..*]
Definition: Account in which cash is maintained.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.082.001.02
IntraBalanceMovementCancellationQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
294 March 2024
```

