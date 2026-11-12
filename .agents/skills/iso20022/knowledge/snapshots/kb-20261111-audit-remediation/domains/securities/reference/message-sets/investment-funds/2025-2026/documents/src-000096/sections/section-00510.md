---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["29 sese.006.001.09 TransferInCancellationRequestV09", "29.4 Message Building Blocks", "29.4.4 RelatedReference <RltdRef>"]
file_pages: [692]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.006.001.09"]
---

# 29.4.4 RelatedReference <RltdRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 692 to 692.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 692

```text
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
29.4.4 RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
29.4.5 MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
29.4.6 Function <Fctn>
Presence: [0..1]
Definition: Function of the transfer-in, that is, whether the message is used as a request to cancel a
previously sent instruction or as a cancellation of a previously sent advice and request for information.
The absence of Function indicates the message is a request to cancel a previously sent instruction.
Datatype: "TransferInFunction1Code" on page 5379
CodeName Name Definition
ADRE AdviceAndRequest The transfer-in is an advice and request,
that is, the message is used to inform
the receiver to expect an unsolicited
transfer in confirmation and to request
account information for the transfer.
INST Instruction The transfer-in is an instruction.
Approved by the Securities SEG on 27 January 2026 sese.006.001.09
TransferInCancellationRequestV09
Investment Funds - Maintenance 2025 - 2026 692 May 2026
```

