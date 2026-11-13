---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks"]
file_pages: [1059]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
preceding_topic_continuations: [{"constraint_ids": ["C23", "C24", "C25", "C26"], "until_heading": "9.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 1059, "topic": "9.3 Constraints", "reference_path": "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00787.md"}]
---

# 9.4 Message Building Blocks

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1059 to 1059.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 1059, C23–C26 before **9.4 Message Building Blocks** continue [9.3 Constraints](section-00787.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 1059

```text
C23 SupplementaryDataRule
The SupplementaryData building block at message level must not be used to provide additional
information about a transaction. The SupplementaryData element at transaction level should be
used for that purpose.
This constraint is defined at the MessageDefinition level.
C24 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C25 ThirdReimbursementAgentAccountRule
If ThirdReimbursementAgentAccount is present, then ThirdReimbursementAgent must be
present.
C26 ThirdReimbursementAgentRule
If ThirdReimbursementAgent is present, then InstructingReimbursementAgent and
InstructedReimbursementAgent must both be present.
9.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
9.4.1 GroupHeader <GrpHdr>
Presence: [1..1]
Definition: Set of characteristics shared by all individual transactions included in the status request
message.
GroupHeader <GrpHdr> contains the following GroupHeader109 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 1059
   CreationDateTime <CreDtTm> [1..1] DateTime 1060
   InstructingAgent <InstgAgt> [0..1] ± 1060
   InstructedAgent <InstdAgt> [0..1] ± 1060
9.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the instructing party, and sent to the next party in the
chain to unambiguously identify the message.
Usage: The instructing party has to make sure that MessageIdentification is unique per instructed party
for a pre-agreed period.
Datatype: "Max35Text" on page 1246
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1059 March 2026
```

