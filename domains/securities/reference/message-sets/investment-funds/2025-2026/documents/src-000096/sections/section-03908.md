---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.23 CancelledStatusReason16"]
file_pages: [5200]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.23 CancelledStatusReason16

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5200 to 5200.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5200

```text
Definition: Additional information about the in repair reason.
Datatype: "Max350Text" on page 5403
66.1.45.23  CancelledStatusReason16
Definition: Reason for a cancelled status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1]  5200
{Or     Code <Cd> [1..1] CodeSet 5200
Or     Proprietary <Prtry> [1..1] ± 5201
Or}     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5201
   AdditionalInformation <AddtlInf> [0..1] Text 5201
Constraints
• AdditionaInformationRule
The AdditionalInformation element must not contain information that can be provided in a structured
field unless bilaterally agreed.
• CancelledElementRule
Either Reason or AdditionalInformation must be present. Both may be present.
66.1.45.23.1  Reason <Rsn>
Presence: [0..1]
Definition: Reason for the cancelled status.
Reason <Rsn> contains one of the following CancelledReason12Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5200
Or   Proprietary <Prtry> [1..1] ± 5201
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5201
66.1.45.23.1.1  Code <Cd>
Presence: [1..1]
Definition: Cancelled reason expressed as a code.
Datatype: "CancelledStatusReason2Code" on page 5280
CodeName Name Definition
CANH CancelledByHub Transaction is cancelled by the hub.
CANP CancelledByInstructingParty Transaction is cancelled by the
instructing party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5200 May 2026
```

