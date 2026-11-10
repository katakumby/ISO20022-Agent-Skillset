---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15", "13.4 Message Building Blocks", "13.4.4 InstructionCancellationRequestStatus <InstrCxlReqSts>", "13.4.4.3 Rejected <Rjctd>", "13.4.4.3.2 Reason <Rsn>", "13.4.4.3.2.1 ReasonCode <RsnCd>", "13.4.4.3.2.1.2 Proprietary <Prtry>"]
file_pages: [745]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.041.001.15"]
---

# 13.4.4.3.2.1.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 745 to 745.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 745

```text
CodeName Name Definition
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
13.4.4.3.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the reason why the instruction/cancellation request has a rejected
status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
13.4.4.3.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the processed instruction.
Datatype: "Max210Text" on page 1249
13.4.4.4  PendingCancellation <PdgCxl>
Presence: [1..1]
Definition: Provides status information related to a pending cancellation request.
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 745 February 2026
```

