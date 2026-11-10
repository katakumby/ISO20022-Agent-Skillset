---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.96 Registration2Code"]
file_pages: [2114]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.96 Registration2Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2114 to 2114.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2114

```text
CodeName Name Definition
YREG Registered Register on receipt. If there is a standing
instruction in place to hold the securities
in street name, then this standing
instruction is to be ignored.
35.2.2.96  Registration2Code
Definition: Specifies whether registration should occur upon receipt.
Type: CodeSet
CodeName Name Definition
PTYH PartyHold You or your party set the instruction in a
hold/frozen/preadvice mode.
CSDH CSDHold Central securities depository sets the
instruction in a hold/frozen/preadvice
mode.
CDEL ConditionalDelivery Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditional
delivery rules in the market infrastructure
platform for conditional delivery.
CVAL CSDValidation Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditions of
a restriction processing type in the
market infrastructure platform.
35.2.2.97  RegistrationProcessingStatus1Code
Definition: Specifies the status of the registration processing.
Type: CodeSet
CodeName Name Definition
PACK AcknowledgedAccepted Registration has been acknowledged/
accepted by the issuer/registrar.
REJT Rejected Registration has been rejected by the
issuer/registrar.
35.2.2.98  RejectionReason55Code
Definition: Specifies the reason the instruction/cancellation request has a rejected status.
Type: CodeSet
CodeName Name Definition
BENO BeneficialOwnershipDisagreement Disagreement in beneficial ownership.
CAEV CorporateActionRejection Corporate action pending on the
financial instrument instructed.
DQUA QuantityRejection Unrecognised or invalid instructed
quantity.
OTHR Other Other. See Narrative.
PODU PossibleDuplicate Instruction has not been matched. It is a
possible duplicate instruction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2114 March 2026
```

