---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["2 acmt.001.001.08 AccountOpeningInstructionV08", "2.4 Message Building Blocks"]
file_pages: [25]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.001.001.08"]
---

# 2.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 25 to 25.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 25

```text
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
2.4.2 OrderReference <OrdrRef>
Presence: [0..1]
Definition: Identifies a related order or settlement transaction.
OrderReference <OrdrRef> contains the following elements (see "InvestmentFundOrder4" on
page 4754 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderReference <OrdrRef> [0..1] Text 4754
   MasterReference <MstrRef> [0..1] Text 4754
2.4.3 PreviousReference <PrvsRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference13" on
page 4546 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4546
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4547
2.4.4 InstructionDetails <InstrDtls>
Presence: [1..1]
Definition: Information about the opening instruction.
Approved by the Securities SEG on 27 January 2026 acmt.001.001.08 AccountOpeningInstructionV08
Investment Funds - Maintenance 2025 - 2026 25 May 2026
```

