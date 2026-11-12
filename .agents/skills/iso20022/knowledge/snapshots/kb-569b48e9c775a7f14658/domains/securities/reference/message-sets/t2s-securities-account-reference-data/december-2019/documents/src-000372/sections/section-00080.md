---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["11 Message Items Types", "11.1 MessageComponents", "11.1.4 Miscellaneous", "11.1.4.6 MessageHeader3", "11.1.4.6.3 RequestType <ReqTp>", "11.1.4.6.3.1 PaymentControl <PmtCtrl>"]
file_pages: [86]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.1.4.6.3.1 PaymentControl <PmtCtrl>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 86 to 86.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 86

```text
11.1.4.6.3.1  PaymentControl <PmtCtrl>
Presence: [1..1]
Definition: Request type is a control command on a set of transactions.
Datatype: "RequestType1Code" on page 95
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
11.1.4.6.3.2  Enquiry <Enqry>
Presence: [1..1]
Definition: Request type is an enquiry on a position or a transaction.
Datatype: "RequestType2Code" on page 96
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
11.1.4.6.3.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Request type is in proprietary format.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 80 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 80
   SchemeName <SchmeNm> [0..1] Text 80
   Issuer <Issr> [0..1] Text 80
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
Message Items Types
Target2-Securities - Securities Account Reference Data 86 December 2019
```

