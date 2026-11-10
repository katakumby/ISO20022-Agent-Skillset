---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "12.4 Message Building Blocks"]
file_pages: [156]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.045.001.03"]
---

# 12.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 156 to 156.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 156

```text
C15 FundIdentification2Rule
If Name is not present, then Identification or Legal Entity Identifier must be present.
Identification, Name and Legal Entity Identifier may all be present.
C16 FundIdentification3Rule
If Legal Entity Identifier is not present, then Identification or Name must be present.
Identification, Name and Legal Entity Identifier may all be present.
C17 UserDefinedRule
At least one message element in the list (Party, Country, Currency, UserDefined) must be
present. More than one element in the list (Party, Country, Currency, UserDefined) may be
present.
12.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
12.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Identifies the message.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
12.4.2 PoolReference <PoolRef>
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
12.4.3 PreviousReference <PrvsRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously sent.
Approved by the Securities SEG on 27 January 2026 camt.045.001.03
FundDetailedConfirmedCashForecastReportCancell
ationV03
Investment Funds - Maintenance 2025 - 2026 156 May 2026
```

