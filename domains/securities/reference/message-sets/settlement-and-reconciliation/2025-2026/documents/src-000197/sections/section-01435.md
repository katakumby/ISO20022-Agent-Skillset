---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.23 PendingReason30Choice", "35.1.29.23.2 Proprietary <Prtry>"]
file_pages: [1919]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.23.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1919 to 1919.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1919

```text
CodeName Name Definition
CDAC ConditionalDeliveryAwaitingCancellation Awaiting cancellation of one of the party.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
35.1.29.23.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the cancellation request is pending.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.24  RejectionOrRepairStatus42Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1919
Or}   Reason <Rsn> [1..*]  1919
     Code <Cd> [1..1] ± 1920
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1920
35.1.29.24.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.24.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason for the status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1919 March 2026
```

