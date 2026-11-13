---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["12 camt.013.001.04 GetMemberV04", "12.3 Constraints"]
file_pages: [466]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.013.001.04"]
---

# 12.3 Constraints

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 466 to 466.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 466

```text
12.3 Constraints
C1 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C2 ReturnCriteriaAndOrSearchCriteriaRule
If ReturnCriteria is not present, then at least one occurrence of SearchCriteria must be present.
If ReturnCriteria is present, then any occurrence of SearchCriteria is optional.
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
12.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
12.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader9" on page 810 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 810
   CreationDateTime <CreDtTm> [0..1] DateTime 810
   RequestType <ReqTp> [0..1]  810
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 810
Or     Enquiry <Enqry> [1..1] CodeSet 811
Or}     Proprietary <Prtry> [1..1] ± 811
12.4.2 MemberQueryDefinition <MmbQryDef>
Presence: [0..1]
Definition: Definition of the member query.
Approved by the Payments SEG on 04 February 2025 camt.013.001.04 GetMemberV04
Cash Management - Maintenance 2024 - 2025 466 February 2025
```

