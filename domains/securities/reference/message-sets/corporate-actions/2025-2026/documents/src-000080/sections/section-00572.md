---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15", "13.4 Message Building Blocks", "13.4.4 InstructionCancellationRequestStatus <InstrCxlReqSts>", "13.4.4.2 Accepted <Accptd>"]
file_pages: [743]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.041.001.15"]
---

# 13.4.4.2 Accepted <Accptd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 743 to 743.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 743

```text
13.4.4.2  Accepted <Accptd>
Presence: [1..1]
Definition: Provides status information related to a cancellation request accepted for further processing.
Accepted <Accptd> contains the following elements (see "NoSpecifiedReason1" on page 1144 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1144
13.4.4.3  Rejected <Rjctd>
Presence: [1..1]
Definition: Provides status information related to a cancellation request rejected for further processing
due to system (data) reasons.
Rejected <Rjctd> contains one of the following RejectedStatus65Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 743
Or}   Reason <Rsn> [1..*]  C4 743
     ReasonCode <RsnCd> [1..1]  744
{Or       Code <Cd> [1..1] CodeSet 744
Or}       Proprietary <Prtry> [1..1] ± 745
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 745
13.4.4.3.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Reason not specified.
Datatype: "NoReasonCode" on page 1223
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
13.4.4.3.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason for the rejected status.
Impacted by: C4 "AdditionalReasonInforrmationRule"
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 743 February 2026
```

