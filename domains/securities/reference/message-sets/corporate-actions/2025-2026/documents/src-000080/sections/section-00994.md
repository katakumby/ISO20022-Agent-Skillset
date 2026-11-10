---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.130 RenounceableStatus1Code"]
file_pages: [1240]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.130 RenounceableStatus1Code

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1240 to 1240.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1240

```text
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
INIR InstructionIrrevocable Instruction is irrevocable.
ULNK InvalidReference Linked reference is unknown.
LATE MarketDeadlineMissed Received after market deadline.
OTHR Other Other. See Narrative.
DCAN RejectedSinceAlreadyCancelled Cancellation request was rejected since
the instruction has already been
cancelled.
DPRG RejectedSinceInProgress Cancellation request has been rejected
because the instruction process is in
progress or has been processed.
REJA RejectedByIssuerAgent Instruction rejected by the issuer agent.
CTCT MissingContact Contact information is missing.
DQUA QuantityRejection Unrecognised or invalid instructed
quantity.
PROT MissingProtectDate Protect date is required for cover protect
instructions.
SAFE SafekeepingAccountRejection Unrecognised or invalid message
sender's safekeeping account.
PROI MissingProtectIdentification Protect identification is required for cover
protect instructions.
TRTI MissingTransactionType Transaction type is missing or invalid for
protect or cover protect instructions.
DUPL DuplicateInstruction Instruction is rejected due to duplicate
business message identifier.
ECMD ElectionToCounterpartyMarketDeadlineMissed Received after the election to
counterparty market deadline.
ECRD ElectionToCounterpartyResponseDeadlineMiss
ed
Received after the election to
counterparty response market deadline.
DSEC InvalidSecurity Unrecognised or invalid financial
instrument identification.
16.2.2.130  RenounceableStatus1Code
Definition: Specifies the renounceable status.
Type: CodeSet
CodeName Name Definition
NREN NonRenounceable Intermediate securities cannot be sold.
RENO Renounceable Intermediate securities can be sold.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1240 February 2026
```

