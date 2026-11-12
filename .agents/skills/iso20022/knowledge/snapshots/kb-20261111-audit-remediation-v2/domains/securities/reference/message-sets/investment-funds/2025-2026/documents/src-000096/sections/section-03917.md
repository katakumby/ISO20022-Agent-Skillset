---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.28 AccountStatusUpdateInstruction1", "66.1.45.28.2 UpdateInstructionReason <UpdInstrRsn>", "66.1.45.28.2.2 Reason <Rsn>", "66.1.45.28.2.2.2 AdditionalInformation <AddtlInf>"]
file_pages: [5209]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.28.2.2.2 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5209 to 5209.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5209

```text
66.1.45.28.2.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the reason for the instruction to change the account status.
Datatype: "Max350Text" on page 5403
66.1.45.29  ConditionallyAcceptedStatus3Choice
Definition: Reason for a conditionally accepted status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5209
Or}   ReasonDetails <RsnDtls> [1..5]  5209
     Reason <Rsn> [1..1]  5209
{Or       Code <Cd> [1..1] CodeSet 5210
Or}       Proprietary <Prtry> [1..1] ± 5210
     AdditionalInformation <AddtlInf> [0..1] Text 5210
66.1.45.29.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: No reason available or to report for the conditionally accepted status.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.45.29.2  ReasonDetails <RsnDtls>
Presence: [1..5]
Definition: Reason for the conditionally accepted status, expressed as a code.
ReasonDetails <RsnDtls> contains the following ConditionallyAcceptedStatusReason3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  5209
{Or     Code <Cd> [1..1] CodeSet 5210
Or}     Proprietary <Prtry> [1..1] ± 5210
   AdditionalInformation <AddtlInf> [0..1] Text 5210
66.1.45.29.2.1  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the conditionally accepted status expressed as a code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5209 May 2026
```

