---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15", "13.4 Message Building Blocks", "13.4.4 InstructionCancellationRequestStatus <InstrCxlReqSts>"]
file_pages: [742]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.041.001.15"]
---

# 13.4.4 InstructionCancellationRequestStatus <InstrCxlReqSts>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 742 to 742.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 742

```text
If Code is present, the code REDM must only be used when the redemption is decided by the issuer
and not by the securities holders.
13.4.4 InstructionCancellationRequestStatus
<InstrCxlReqSts>
Presence: [1..*]
Definition: Provides information about the processing status of the instruction cancellation request.
InstructionCancellationRequestStatus <InstrCxlReqSts> contains one of the following
InstructionCancellationRequestStatus21Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CancellationCompleted <CxlCmpltd> [1..1] ± 742
Or   Accepted <Accptd> [1..1] ± 743
Or   Rejected <Rjctd> [1..1]  743
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 743
Or}     Reason <Rsn> [1..*]  C4 743
       ReasonCode <RsnCd> [1..1]  744
{Or         Code <Cd> [1..1] CodeSet 744
Or}         Proprietary <Prtry> [1..1] ± 745
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 745
Or   PendingCancellation <PdgCxl> [1..1] ± 745
Or}   ProprietaryStatus <PrtrySts> [1..1] ± 746
13.4.4.1  CancellationCompleted <CxlCmpltd>
Presence: [1..1]
Definition: Provides status information related to an instruction cancellation request completed.
CancellationCompleted <CxlCmpltd> contains one of the following elements (see
"CancelledStatus11Choice" on page 1144 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1145
Or}   Reason <Rsn> [1..*]  C3 1145
     ReasonCode <RsnCd> [1..1]  1145
{Or       Code <Cd> [1..1] CodeSet 1146
Or}       Proprietary <Prtry> [1..1] ± 1146
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1146
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 742 February 2026
```

