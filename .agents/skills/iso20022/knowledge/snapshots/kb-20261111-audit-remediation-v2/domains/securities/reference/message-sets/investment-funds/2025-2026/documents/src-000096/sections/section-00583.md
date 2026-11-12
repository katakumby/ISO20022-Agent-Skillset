---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "32.4 Message Building Blocks", "32.4.2.1 Reference <Ref>"]
file_pages: [791]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.009.001.09"]
---

# 32.4.2.1 Reference <Ref>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 791 to 791.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 791

```text
32.4.2.1  Reference <Ref>
Presence: [0..1]
Definition: Reference to the message or communication that was previously sent.
Reference <Ref> contains one of the following References68Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PreviousReference <PrvsRef> [1..1] ± 791
Or}   OtherReference <OthrRef> [1..1] ± 791
32.4.2.1.1  PreviousReference <PrvsRef>
Presence: [1..1]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
32.4.2.1.2  OtherReference <OthrRef>
Presence: [1..1]
Definition: Reference to a linked message sent in a proprietary way or the reference of a system.
OtherReference <OthrRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
32.4.2.2  TypeOfRequest <TpOfReq>
Presence: [0..1]
Definition: Type of request required.
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 791 May 2026
```

