---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.4 Message Building Blocks"]
file_pages: [1450]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
preceding_topic_continuations: [{"constraint_ids": ["C22", "C23"], "until_heading": "39.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 1450, "topic": "39.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01050.md"}]
---

# 39.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1450 to 1450.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 1450, C22–C23 before **39.4 Message Building Blocks** continue [39.3 Constraints](section-01050.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 1450

```text
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.
C22 SocialSecurityNumberGuideline
The UK Insurance Number must be indicated without spaces.
C23 SpecificPreviousYearsGuideline
SpecificPreviousYears must not contain the current year.
39.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
39.4.1 MessageReference <MsgRef>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageReference <MsgRef> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
39.4.2 PoolReference <PoolRef>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
PoolReference <PoolRef> contains the following elements (see "AdditionalReference11" on
page 4553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4554
   ReferenceIssuer <RefIssr> [0..1] ± 4554
   MessageName <MsgNm> [0..1] Text 4554
39.4.3 PreviousReference <PrvsRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously sent.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1450 May 2026
```

