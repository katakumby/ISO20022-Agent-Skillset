---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["4 reda.008.001.01 SecurityCreationStatusAdviceV01", "4.4 Message Building Blocks", "4.4.1 MessageHeader <MsgHdr>"]
file_pages: [68]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.008.001.01"]
---

# 4.4.1 MessageHeader <MsgHdr>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 68 to 68.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 68

```text
4.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following MessageHeader12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 68
   CreationDateTime <CreDtTm> [0..1] DateTime 68
   OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 68
4.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 534
4.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 529
4.4.1.3  OriginalBusinessInstruction <OrgnlBizInstr>
Presence: [0..1]
Definition: Unique identification of the original instruction.
OriginalBusinessInstruction <OrgnlBizInstr> contains the following elements (see
"OriginalBusinessInstruction1" on page 485 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 485
   MessageNameIdentification <MsgNmId> [0..1] Text 485
   CreationDateTime <CreDtTm> [0..1] DateTime 485
4.4.2 FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: Identification of the financial instrument.
Impacted by: C2 "DescriptionPresenceRule", C3 "DescriptionUsageRule", C4 "ISINGuideline", C5
"ISINPresenceRule", C6 "OtherIdentificationPresenceRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.008.001.01 SecurityCreationStatusAdviceV01
Target2-Securities - Securities Reference Data 68 March 2024
```

