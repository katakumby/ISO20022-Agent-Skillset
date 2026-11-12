---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["18 semt.002.001.02 CustodyStatementOfHoldingsV02", "18.4 Message Building Blocks"]
file_pages: [379]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.02"]
---

# 18.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 379 to 379.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 379

```text
C15 Party1Rule
If PlaceSafekeeping is not SHHE, then Party is mandatory. If PlaceSafekeeping is SHHE, then
Party is optional.
C16 StreetNameAndOrPostOfficeBoxRule
If StreetName is not present, then PostOfficeBox is mandatory. If StreetName is present, then
PostOfficeBox is optional.
C17 ValueRule
If Type is not MRKT, then Value may not be expressed with UnknownIndicator.
18.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
18.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies a message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
18.4.2 PreviousReference <PrvsRef>
Presence: [0..*]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference2" on
page 4538 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4538
   ReferenceIssuer <RefIssr> [0..1] ± 4538
   MessageName <MsgNm> [0..1] Text 4538
18.4.3 RelatedReference <RltdRef>
Presence: [0..*]
Definition: Reference to a linked message that was previously received.
Approved by the Securities SEG on 27 January 2026 semt.002.001.02 CustodyStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 379 May 2026
```

