---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.28 AccountStatusUpdateInstruction1", "66.1.45.28.1 UpdateInstruction <UpdInstr>", "66.1.45.28.1.2 Proprietary <Prtry>"]
file_pages: [5207]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.28.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5207 to 5207.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5207

```text
66.1.45.28.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of change to the account status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.45.28.2  UpdateInstructionReason <UpdInstrRsn>
Presence: [0..1]
Definition: Reason for the instruction to change the account status.
UpdateInstructionReason <UpdInstrRsn> contains one of the following
AccountStatusUpdateInstructionReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5207
Or}   Reason <Rsn> [1..*]  C27 5207
     Code <Cd> [0..1]  5208
{Or       Code <Cd> [1..1] CodeSet 5208
Or}       Proprietary <Prtry> [1..1] ± 5208
     AdditionalInformation <AddtlInf> [0..1] Text 5209
66.1.45.28.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: There is no reason available or to report for the instruction to change the account status.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.45.28.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason for the instruction to change the account status.
Impacted by: C27 "ReasonElementRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5207 May 2026
```

