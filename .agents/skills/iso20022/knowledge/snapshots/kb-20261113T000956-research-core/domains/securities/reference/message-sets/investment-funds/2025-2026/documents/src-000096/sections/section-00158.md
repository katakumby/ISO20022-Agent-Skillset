---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks"]
file_pages: [231]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
preceding_topic_continuations: [{"constraint_ids": ["C18", "C19", "C20", "C21"], "until_heading": "14.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 231, "topic": "14.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00157.md"}]
---

# 14.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 231 to 231.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 231, C18–C21 before **14.4 Message Building Blocks** continue [14.3 Constraints](section-00157.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 231

```text
C18 OtherCodeRule
If Structured is OTHR, then AdditionalInformation is mandatory.
C19 OtherCodeRule
If Structured is OTHR, then AdditionalInformation is mandatory.
C20 PriceDetailsRule
If SuspendedIndicator is "true" or "1" (Yes), then PriceDetails is optional.
If SuspendedIndicator is "false" or "0" (No), and if FinancialInstrumentDetails /
DualFundIndicator is "false" or "0" (No), then PriceDetails must be present at least once.
If SuspendedIndicator is "false" or "0" (No), and if FinancialInstrumentDetails /
DualFundIndicator is "true" or "1" (Yes), then PriceDetails must be present two or more times
and PriceDetails/Type must be present with the values "BIDE" and "OFFR".
C21 SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
14.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
14.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies a message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
14.4.2 PoolReference <PoolRef>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
PoolReference <PoolRef> contains the following elements (see "AdditionalReference10" on page 4545
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 231 May 2026
```

