---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["5 acmt.005.001.06 RequestForAccountManagementStatusReportV06", "5.4 Message Building Blocks", "5.4.2 RequestDetails <ReqDtls>", "5.4.2.1 LinkedReference <LkdRef>", "5.4.2.1.1 PreviousReference <PrvsRef>"]
file_pages: [81]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.005.001.06"]
---

# 5.4.2.1.1 PreviousReference <PrvsRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 81 to 81.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 81

```text
Constraints
• OtherReferenceGuideline
OtherReference should be used for an account opening or an account modification instruction sent in
a proprietary way or for system references.
If OtherReference is present, OtherReference/MessageName must contain, for example, 'fax' or
'phone' or 'email'.
• PreviousReferenceGuideline
If PreviousReference/MessageName is present, it must start with acmt.001 or acmt.003 and
PreviousReference/Reference must contain the business reference of a message.
5.4.2.1.1  PreviousReference <PrvsRef>
Presence: [1..1]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference13" on
page 4546 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4546
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4547
5.4.2.1.2  OtherReference <OthrRef>
Presence: [1..1]
Definition: Reference to a linked message sent in a proprietary way or reference of a system.
OtherReference <OthrRef> contains the following elements (see "AdditionalReference13" on
page 4546 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4546
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4547
5.4.2.2  StatusRequestType <StsReqTp>
Presence: [1..1]
Definition: Type of account management instruction for which the status is requested or a request to
know the status of the account.
Datatype: "AccountManagementType3Code" on page 5271
CodeName Name Definition
ACCM AccountModification Refers to an account modification
instruction message.
Approved by the Securities SEG on 27 January 2026 acmt.005.001.06
RequestForAccountManagementStatusReportV06
Investment Funds - Maintenance 2025 - 2026 81 May 2026
```

