---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["23 semt.007.001.02 StatementOfInvestmentFundTransactionsCancellationV02", "23.4 Message Building Blocks"]
file_pages: [429]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.007.001.02"]
---

# 23.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 429 to 429.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 429

```text
C8 TransactionOnSubAccountRule
If ActivityIndicator is "true" or "1" (Yes), then TransactionOnSubAccount must be present. If
ActivityIndicator is "false" or "0" (No), then TransactionOnSubAccount is not allowed.
C9 TransactionTypeLegExecutionIdentificationRule
If TransactionType is SWII or SWIO, then LegExecutionIdentification is optional. If
TransactionType is neither SWII nor SWIO, then LegExecutionIdentification is not allowed.
C10 TransactionTypeLegIdentificationRule
If TransactionType is SWII or SWIO, then LegIdentification is optional. If TransactionType is
neither SWII nor SWIO, then LegIdentification is not allowed.
23.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
23.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies a message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
23.4.2 PreviousReference <PrvsRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference2" on
page 4538 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4538
   ReferenceIssuer <RefIssr> [0..1] ± 4538
   MessageName <MsgNm> [0..1] Text 4538
23.4.3 RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
Approved by the Securities SEG on 27 January 2026 semt.007.001.02
StatementOfInvestmentFundTransactionsCancellati
onV02
Investment Funds - Maintenance 2025 - 2026 429 May 2026
```

