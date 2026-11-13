---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.3 CodeSet", "6.2.3.5 Authorisation1Code"]
file_pages: [588]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.3.5 Authorisation1Code

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 588 to 588.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 588

```text
6.2.3.5  Authorisation1Code
Definition: Specifies the level of approval depending on a number of factors, including payment type,
threshold amount or local country or operations practice.
Type: CodeSet
CodeName Name Definition
AUTH PreAuthorisedFile Indicates a file has been pre authorised
or approved within the originating
customer environment and no further
approval is required.
FDET FileLevelAuthorisationDetails Indicates that a file requires additional
file level approval, with the ability to view
both the payment information block and
supporting customer credit transaction
detail.
FSUM FileLevelAuthorisationSummary Indicates that a file requires additional
file level approval, with the ability to view
only the payment information block level
information.
ILEV InstructionLevelAuthorisation Indicates that a file requires all customer
transactions to be authorised or
approved.
6.2.3.6  ChargeBearerType1Code
Definition: Specifies which party(ies) will pay charges due for processing of the instruction.
Type: CodeSet
CodeName Name Definition
DEBT BorneByDebtor All transaction charges are to be borne
by the debtor.
CRED BorneByCreditor All transaction charges are to be borne
by the creditor.
SHAR Shared In a credit transfer context, means that
transaction charges on the sender side
are to be borne by the debtor,
transaction charges on the receiver side
are to be borne by the creditor. In a
direct debit context, means that
transaction charges on the sender side
are to be borne by the creditor,
transaction charges on the receiver side
are to be borne by the debtor.
SLEV FollowingServiceLevel Charges are to be applied following the
rules agreed in the service level and/or
scheme.
6.2.3.7  ChequeDelivery1Code
Definition: Specifies the method to be used in delivering a cheque to a party.
Type: CodeSet
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 588 March 2026
```

