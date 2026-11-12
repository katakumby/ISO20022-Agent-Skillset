---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["5 acmt.005.001.06 RequestForAccountManagementStatusReportV06", "5.4 Message Building Blocks"]
file_pages: [79]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.005.001.06"]
---

# 5.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 79 to 79.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 79

```text
C4 OtherReferenceGuideline
OtherReference should be used for an account opening or an account modification instruction
sent in a proprietary way or for system references.
If OtherReference is present, OtherReference/MessageName must contain, for example, 'fax'
or 'phone' or 'email'.
C5 PreviousReferenceGuideline
If PreviousReference/MessageName is present, it must start with acmt.001 or acmt.003 and
PreviousReference/Reference must contain the business reference of a message.
5.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
5.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
5.4.2 RequestDetails <ReqDtls>
Presence: [1..1]
Definition: Identifies the account for which the status of the account management instruction is
requested.
Impacted by: C3 "LinkedReferenceOrAccountApplicationIdentificationRule"
Approved by the Securities SEG on 27 January 2026 acmt.005.001.06
RequestForAccountManagementStatusReportV06
Investment Funds - Maintenance 2025 - 2026 79 May 2026
```

