---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01", "64.4 Message Building Blocks"]
file_pages: [2361]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.047.001.01"]
---

# 64.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2361 to 2361.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2361

```text
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C4 DescriptionUsageRule
Description must be used alone as the last resort.
C5 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C6 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C7 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C8 StatusReasonRule
If Status equals "Rejected" then StatusReason must be present.
C9 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
64.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
64.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following MessageHeader12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2361
   CreationDateTime <CreDtTm> [0..1] DateTime 2362
   OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 2362
64.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.047.001.01 SecurityCSDLinkStatusAdviceV01
Target2-Securities 2361 August 2026
```

