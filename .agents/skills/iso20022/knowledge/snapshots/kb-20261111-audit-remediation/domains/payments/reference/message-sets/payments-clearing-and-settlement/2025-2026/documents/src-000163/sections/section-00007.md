---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks"]
file_pages: [18]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
preceding_topic_continuations: [{"constraint_ids": ["C27", "C28", "C29", "C30", "C31", "C32", "C33"], "until_heading": "2.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 18, "topic": "2.3 Constraints", "reference_path": "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00006.md"}]
---

# 2.4 Message Building Blocks

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 18 to 18.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 18, C27–C33 before **2.4 Message Building Blocks** continue [2.3 Constraints](section-00006.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 18

```text
C27 SettlementMethodCoverRule
If SettlementMethod is equal to COVE, then SettlementAccount and ClearingSystem are not
allowed.
C28 StatusReasonInformationRule
If GroupStatus is present and is different from RJCT or PDNG then StatusReasonInformation/
AdditionalInformation must be absent.
C29 StatusReasonRule
If Reason/Code is equal to NARR, then AddititionalInformation must be present.
C30 SupplementaryDataRule
The SupplementaryData building block at message level must not be used to provide additional
information about a transaction. The SupplementaryData element at transaction level should be
used for that purpose.
This constraint is defined at the MessageDefinition level.
C31 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C32 ThirdReimbursementAgentAccountRule
If ThirdReimbursementAgentAccount is present, then ThirdReimbursementAgent must be
present.
C33 ThirdReimbursementAgentRule
If ThirdReimbursementAgent is present, then InstructingReimbursementAgent and
InstructedReimbursementAgent must both be present.
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 GroupHeader <GrpHdr>
Presence: [1..1]
Definition: Set of characteristics shared by all individual transactions included in the status report
message.
GroupHeader <GrpHdr> contains the following GroupHeader120 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 19
   CreationDateTime <CreDtTm> [1..1] DateTime 19
   InstructingAgent <InstgAgt> [0..1] ± 19
   InstructedAgent <InstdAgt> [0..1] ± 19
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 20
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
18 March 2026
```

