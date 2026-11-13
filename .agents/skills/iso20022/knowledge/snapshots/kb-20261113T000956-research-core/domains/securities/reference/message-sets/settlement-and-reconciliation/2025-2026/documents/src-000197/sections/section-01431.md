---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.22 Status19Choice", "35.1.29.22.11 ReplacementProcessingStatus <RplcmntPrcgSts>", "35.1.29.22.11.1 Code <Cd>"]
file_pages: [1915]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.22.11.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1915 to 1915.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1915

```text
ReplacementProcessingStatus <RplcmntPrcgSts> contains one of the following
ReplacementProcessingStatus8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1915
Or}   Proprietary <Prtry> [1..1] ± 1915
35.1.29.22.11.1  Code <Cd>
Presence: [1..1]
Definition: Provides the processing status of the replacement request.
Datatype: "ReplacementProcessingStatus1Code" on page 2132
CodeName Name Definition
DEND Denied Replacement request cannot be
executed.
EXCH ReceivedAtStockExchange Replacement request previously
received from you has been received at
the stock exchange.
INTE ReceivedAtIntermediary Replacement request previously
received from you has been received at
intermediary (if not stock exchange).
PACK Accepted Replacement request has been
accepted for further processing by the
account servicer (technical receipt).
PART PartialReplacementAccepted Order is partially filled, replacement
processing accepted for the remaining.
PEND Pending Replacement request is pending.
REJT Rejected Replacement request has been rejected
for further processing.
REPL Completed Replacement request has been
completed.
REPR InRepair Replacement request previously
received from you is in repair.
35.1.29.22.11.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the processing status of the replacement request.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1915 March 2026
```

