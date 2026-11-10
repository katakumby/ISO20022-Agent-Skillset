---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["11 Message Items Types", "11.2 Message Datatypes", "11.2.1 CodeSet", "11.2.1.8 RequestType2Code"]
file_pages: [96]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.2.1.8 RequestType2Code

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 96 to 96.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 96

```text
CodeName Name Definition
RT01 ReleasePending Type is a request to release the pending
transactions.
RT02 HoldNormal Type is a request to hold normal
transactions.
RT03 Cancellation Type is a request to cancellation a
transaction.
RT04 ReSequence Type is a request to change the
sequence of the transactions.
RT05 ReleaseSuspicious Type is a request to release the
suspicious transactions.
11.2.1.8  RequestType2Code
Definition: Specifies the request used to further detail the type of information that will be queried.
Type: CodeSet
CodeName Name Definition
RT11 BankPositionEnquiry Type is an enquiry on the bank's
position.
RT12 SpecificTransactionEnquiry Type is an enquiry on a specific
transaction.
RT13 QueuedTransactionEnquiry Type is an enquiry on a queued
transaction.
RT14 SuspiciousTransactionEnquiry Type is an enquiry on a suspicious
transaction.
RT15 PendingInwardCreditsEnquiry Type is an enquiry on pending inward
credits.
11.2.1.9  Status6Code
Definition: Specifies the status of an instruction.
Type: CodeSet
CodeName Name Definition
REJT Rejected Instruction has been rejected.
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
11.2.1.10  SystemSecuritiesAccountType1Code
Definition: Lists the type of the securities account specific for a system.
Type: CodeSet
CodeName Name Definition
CSDP CSDParticipantAccount Account owned by a CSD Participant
.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
Message Items Types
Target2-Securities - Securities Account Reference Data 96 December 2019
```

