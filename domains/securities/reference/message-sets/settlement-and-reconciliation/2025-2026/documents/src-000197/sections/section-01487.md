---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.65 DeniedReason14Choice", "35.1.29.65.2 Proprietary <Prtry>"]
file_pages: [1979]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.65.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1979 to 1979.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1979

```text
CodeName Name Definition
DPRG DeniedSinceInProgress Request was denied because the
process of settlement is in progress.
DFOR DeniedSinceNotAllowed Repo call request was denied. Call not
allowed on the concerned repo, for
example, out of delay.
DREP DeniedSinceRepoEnded Request was denied because the repo
was cancelled.
DSET DeniedSinceSettled Request was denied because the
instruction was settled.
IPNC InstructionProcessed Instruction has been processed and
cannot be cancelled.
LATE MarketDeadlineMissed Received after market deadline.
OTHR Other Other. See Narrative.
35.1.29.65.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the request was denied.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.66  AcknowledgementReason13Choice
Definition: Choice of format for the acknowledgement reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1979
Or}   Proprietary <Prtry> [1..1] ± 1980
35.1.29.66.1  Code <Cd>
Presence: [1..1]
Definition: Specifies additional information about the processed instruction.
Datatype: "RepoCallAcknowledgementReason2Code" on page 2133
CodeName Name Definition
CALD InProcess Repurchase agreement call is in
process.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1979 March 2026
```

