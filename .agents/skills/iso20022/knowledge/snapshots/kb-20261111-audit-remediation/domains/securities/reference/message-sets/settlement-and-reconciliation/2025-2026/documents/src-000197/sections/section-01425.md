---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.22 Status19Choice", "35.1.29.22.3 RepoCallRequestStatus <RepoCallReqSts>"]
file_pages: [1908]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.22.3 RepoCallRequestStatus <RepoCallReqSts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1908 to 1908.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1908

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.22.3  RepoCallRequestStatus <RepoCallReqSts>
Presence: [1..1]
Definition: Provides the status of the repurchase agreement call request.
RepoCallRequestStatus <RepoCallReqSts> contains one of the following elements (see
"RepoCallRequestStatus8Choice" on page 1877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1877
Or}   Proprietary <Prtry> [1..1] ± 1877
35.1.29.22.4  CorporateActionEventProcessingStatus <CorpActnEvtPrcgSts>
Presence: [1..1]
Definition: Provides the status of a corporate action or the status of a payment.
CorporateActionEventProcessingStatus <CorpActnEvtPrcgSts> contains one of the following
CorporateActionEventProcessingStatus3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1908
Or}   Proprietary <Prtry> [1..1] ± 1909
35.1.29.22.4.1  Code <Cd>
Presence: [1..1]
Definition: Status of a corporate action or the status of a payment expressed as an ISO 20022 code.
Datatype: "CorporateActionEventProcessingStatus1Code" on page 2050
CodeName Name Definition
COMP Complete Specifies that a corporate action event
processing has been completed.
PEND Pending Specifies that a corporate action event
processing has not been completed.
RECD Reconciled Corporate action event processing
specifying that the funds paid have been
reconciled with the funds received from
the agent (meaning that there is no more
risk of payment to be reversed).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1908 March 2026
```

