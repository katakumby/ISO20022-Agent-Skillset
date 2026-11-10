---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.30 AcknowledgedAcceptedStatus23Choice", "35.1.29.30.2 Reason <Rsn>", "35.1.29.30.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [1927]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.30.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1927 to 1927.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1927

```text
Code <Cd> contains one of the following elements (see "AcknowledgementReason14Choice" on
page 1939 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1939
Or}   Proprietary <Prtry> [1..1] ± 1939
35.1.29.30.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.31  CancellationReason21Choice
Definition: Choice of format for the cancellation reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1927
Or}   Proprietary <Prtry> [1..1] ± 1927
35.1.29.31.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is cancelled, or the related cancellation
request is executed.
Datatype: "CancelledStatusReason5Code" on page 2049
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
OTHR Other Other. See Narrative.
35.1.29.31.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is cancelled, or the related cancellation
request is executed.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1927 March 2026
```

