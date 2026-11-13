---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04", "10.4 Message Building Blocks"]
file_pages: [131]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.043.001.04"]
---

# 10.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 131 to 131.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 131

```text
10.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
10.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Identifies the message.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
10.4.2 PoolReference <PoolRef>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
PoolReference <PoolRef> contains the following elements (see "AdditionalReference3" on page 4537
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4537
   ReferenceIssuer <RefIssr> [0..1] ± 4537
   MessageName <MsgNm> [0..1] Text 4537
10.4.3 PreviousReference <PrvsRef>
Presence: [0..*]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference3" on
page 4537 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4537
   ReferenceIssuer <RefIssr> [0..1] ± 4537
   MessageName <MsgNm> [0..1] Text 4537
10.4.4 RelatedReference <RltdRef>
Presence: [0..*]
Definition: Reference to a linked message that was previously received.
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 131 May 2026
```

