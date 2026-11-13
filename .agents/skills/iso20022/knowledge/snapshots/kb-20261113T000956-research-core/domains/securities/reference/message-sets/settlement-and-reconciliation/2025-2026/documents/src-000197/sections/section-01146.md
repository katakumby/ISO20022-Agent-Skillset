---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.55 HoldIndicator6", "35.1.16.55.1 Indicator <Ind>"]
file_pages: [1593]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.55.1 Indicator <Ind>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1593 to 1593.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1593

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 1593
   Reason <Rsn> [0..*] ± 1593
35.1.16.55.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether the transaction is on hold/blocked/frozen.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.55.2  Reason <Rsn>
Presence: [0..*]
Definition: Specifies the reason of the registration status.
Reason <Rsn> contains the following elements (see "RegistrationReason5" on page 1558 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  1559
{Or     Code <Cd> [1..1] CodeSet 1559
Or}     Proprietary <Prtry> [1..1] ± 1559
   AdditionalInformation <AddtlInf> [0..1] Text 1560
35.1.16.56  DeliveryReturn3Choice
Definition: Choice of format for the delivery return information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1593
Or}   Proprietary <Prtry> [1..1] ± 1594
35.1.16.56.1  Code <Cd>
Presence: [1..1]
Definition: Delivery return expressed as an ISO 20022 code.
Datatype: "DeliveryReturn1Code" on page 2058
CodeName Name Definition
UNRE UnrecognisedDelivery Original delivery is not recognized.
DQUA WrongQuantity Wrong quantity delivered in the original
instruction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1593 March 2026
```

