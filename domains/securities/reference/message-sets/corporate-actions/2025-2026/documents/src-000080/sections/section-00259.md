---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.4 InstructionProcessingStatus <InstrPrcgSts>", "6.4.4.6 Returned <Rtrd>", "6.4.4.6.2 ReturnedReason <RtrdRsn>", "6.4.4.6.2.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [346]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.4.6.2.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 346 to 346.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 346

```text
ReturnedReason <RtrdRsn> contains one of the following ReturnedStatus2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 346
Or}   Reason <Rsn> [1..*]  C7 346
     ReasonCode <RsnCd> [1..1]  346
{Or       Code <Cd> [1..1] CodeSet 347
Or}       Proprietary <Prtry> [1..1] ± 347
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 347
6.4.4.6.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Reason not specified.
Datatype: "NoReasonCode" on page 1223
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
6.4.4.6.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason why the meeting instruction message or the individual meeting instruction is
returned.
Impacted by: C7 "AdditionalReasonInforrmationRule"
Reason <Rsn> contains the following ReturnedStatusReason2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReasonCode <RsnCd> [1..1]  346
{Or     Code <Cd> [1..1] CodeSet 347
Or}     Proprietary <Prtry> [1..1] ± 347
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 347
Constraints
• AdditionalReasonInforrmationRule
AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
6.4.4.6.2.2.1  ReasonCode <RsnCd>
Presence: [1..1]
Definition: Reason for the returned status.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 346 February 2026
```

