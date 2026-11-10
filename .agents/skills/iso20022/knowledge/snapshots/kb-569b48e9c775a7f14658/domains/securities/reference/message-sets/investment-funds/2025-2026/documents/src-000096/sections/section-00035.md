---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["4 acmt.003.001.08 AccountModificationInstructionV08", "4.4 Message Building Blocks"]
file_pages: [63]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.003.001.08"]
---

# 4.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 63 to 63.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 63

```text
C30 UnitRule
If ModifiedSavingsInvestmentPlan is present, then ModifiedSavingsInvestmentPlan/
InvestmentPlan/Quantity/Unit is not allowed.
On Condition
    /ModifiedSavingsInvestmentPlan[*] is present
Following Must be True
    /ModifiedSavingsInvestmentPlan[*]/InvestmentPlan/Quantity/Unit Must be 
absent
This constraint is defined at the MessageDefinition level.
C31 ValidationByTable
Must be a valid terrestrial language.
C32 ValidationByTable
Must be a valid nationality.
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
4.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
4.4.2 PreviousReference <PrvsRef>
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
4.4.3 InstructionDetails <InstrDtls>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 63 May 2026
```

