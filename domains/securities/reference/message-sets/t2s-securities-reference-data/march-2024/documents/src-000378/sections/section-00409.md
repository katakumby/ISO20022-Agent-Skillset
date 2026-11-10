---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.15 Status", "13.1.15.5 ProcessingStatus72Choice", "13.1.15.5.1 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [502]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.15.5.1 AcknowledgedAccepted <AckdAccptd>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 502 to 502.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 502

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1]  502
     Reason <Rsn> [0..*] ± C1 502
Or   PendingProcessing <PdgPrcg> [1..1] ± 502
Or   Rejected <Rjctd> [1..1] ± 503
Or   Completed <Cmpltd> [1..1]  503
     Reason <Rsn> [0..*] ± C1 503
Or}   Proprietary <Prtry> [1..1] ± 504
13.1.15.5.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the executing party.
AcknowledgedAccepted <AckdAccptd> contains the following Reason4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..*] ± C1 502
13.1.15.5.1.1  Reason <Rsn>
Presence: [0..*]
Definition: Specifies the reason of the Status.
Impacted by: C1 "AdditionalReasonInforrmationRule"
Reason <Rsn> contains the following elements (see "ProprietaryReason4" on page 500 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 500
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 500
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
13.1.15.5.2  PendingProcessing <PdgPrcg>
Presence: [1..1]
Definition: Instruction is pendingprocessing by the executing party.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 502 March 2024
```

