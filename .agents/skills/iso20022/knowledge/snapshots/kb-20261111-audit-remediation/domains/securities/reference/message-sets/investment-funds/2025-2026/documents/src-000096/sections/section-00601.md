---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "33.4 Message Building Blocks"]
file_pages: [811]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.010.001.07"]
---

# 33.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 811 to 811.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 811

```text
C3 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C4 OtherReferenceRule
Reference/OtherReference should be used to reference a transfer cancellation request
'message' sent in a proprietary way or used for a system reference. If Reference/
OtherReference is present, References/OtherReference/MessageName must contain, for
example, 'fax' or 'phone' or 'email'.
This constraint is defined at the MessageDefinition level.
C5 RelatedReferenceRule
If Reference/RelatedReference/MessageName is present, it must start with sese.002,
sese.006, sese.009 or sese.014.
This constraint is defined at the MessageDefinition level.
33.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
33.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
33.4.2 CounterpartyReference <CtrPtyRef>
Presence: [0..1]
Definition: Unambiguous identification of the transfer allocated by the counterparty.
CounterpartyReference <CtrPtyRef> contains the following elements (see "AdditionalReference10"
on page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
Approved by the Securities SEG on 27 January 2026 sese.010.001.07
TransferCancellationStatusReportV07
Investment Funds - Maintenance 2025 - 2026 811 May 2026
```

