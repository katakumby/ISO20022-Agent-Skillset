---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.129 RejectionReason90Code"]
file_pages: [1239]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.129 RejectionReason90Code

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1239 to 1239.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1239

```text
CodeName Name Definition
NTAX InconsistentTaxRate Tax rate is not consistent with the
documentation in place.
MTAX MissingTaxRate Tax rate is missing.
ISOL InvalidSolicitationDealerFeeUse Invalid use of solicitation dealer fee
indicator.
BSTR BeforeInstructionPeriod Instruction is submitted before instruction
start date.
CTCT MissingContact Contact information is missing.
DUPL DuplicateInstruction Instruction is rejected due to duplicate
business message identifier.
PROI MissingProtectIdentification Protect identification is required for cover
protect instructions.
PRON NoProtectPrivilege No protect privilege for this event.
PROT MissingProtectDate Protect date is required for cover protect
instructions.
TRTI MissingTransactionType Transaction type is missing or invalid for
protect or cover protect instructions.
IPAW InvalidPaperwork Required paperwork is invalid,
incomplete or missing.
REJA RejectedByIssuerAgent Instruction rejected by the issuer agent.
IPED InstructionPriorToEntitlementDate Instruction was received prior to
entitlement date.
BUMM BuyerProtectionMismatch Counterparty disagreement on the
chosen corporate action outturn.
TRTY IncorrectTransactionType Transaction type is incorrect.
DSNA NoBuyerProtectionAllowed Underlying transaction type/status does
not allow for a buyer protection.
DUCK UnderlyingTransactionCancelled Buyer Protection instruction rejected
since underlying settlement transaction
has been cancelled.
DUST UnderlyingTransactionAlreadySettled Buyer Protection instruction was
rejected, because the underlying
settlement transaction has already been
settled.
ECMD ElectionToCounterpartyMarketDeadlineMissed Received after the election to
counterparty market deadline.
ECRD ElectionToCounterpartyResponseDeadlineMiss
ed
Received after the election to
counterparty response market deadline.
INSA InstructionNotSupportedOrAllowed Instruction is not supported or allowed.
DSEC InvalidSecurity Unrecognised or invalid financial
instrument identification.
16.2.2.129  RejectionReason90Code
Definition: Specifies the reason why the instruction/cancellation request has a rejected status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1239 February 2026
```

