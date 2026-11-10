---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.4 RejectionStatus38Choice", "35.1.29.4.2 Reason <Rsn>", "35.1.29.4.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [1877]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.4.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1877 to 1877.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1877

```text
35.1.29.4.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.5  RepoCallRequestStatus8Choice
Definition: Choice of format for the repurchase agreement call acknowledgement.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1877
Or}   Proprietary <Prtry> [1..1] ± 1877
35.1.29.5.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of the repurchase agreement call request.
Datatype: "RepoCallRequestStatus1Code" on page 2133
CodeName Name Definition
CACK AcknowledgedAccepted Repurchase agreement call request is
acknowledged/accepted.
DEND Denied Repuchase agreement call request is
denied.
35.1.29.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of the repurchase agreement call request.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.6  ProprietaryStatusAndReason6
Definition: Provides the proprietary status and reason of an instruction or an instruction cancellation.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1878
   ProprietaryReason <PrtryRsn> [0..*] ± C1 1878
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1877 March 2026
```

