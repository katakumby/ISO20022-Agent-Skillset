---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks"]
file_pages: [170]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
preceding_topic_continuations: [{"constraint_ids": ["C29", "C30", "C31", "C32", "C33", "C34", "C35", "C36", "C37", "C38"], "until_heading": "6.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 170, "topic": "6.3 Constraints", "reference_path": "domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00129.md"}]
---

# 6.4 Message Building Blocks

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 170 to 170.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 170, C29–C38 before **6.4 Message Building Blocks** continue [6.3 Constraints](section-00129.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 170

```text
C29 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C30 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C31 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C32 PlaceOfTradeRule
If PlaceOfTrade is used and a ISO 10383 MIC exists for the market to be identified, then the
ISO 10383 Market Identifier Code (MIC) must be used.
C33 PlaceOfTradeRule
If the trade was executed on multiple places of trade and the place of trade field is used, code
VARI must be used.
C34 PlaceOfTradeRule
If the trade was executed on multiple places of trade and the place of trade field is used, code
VARI must be used.
C35 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C36 StatusPresenceRule
AffirmationStatus or ProcessingStatus or MatchingStatus or ReplacementProcessingStatus or
CancellationProcessingStatus must be present.
Following Must be True
    /AffirmationStatus Must be present
 Or    /ProcessingStatus Must be present
 Or    /MatchingStatus Must be present
 Or    /ReplacementProcessingStatus Must be present
 Or    /CancellationProcessingStatus Must be present
This constraint is defined at the MessageDefinition level.
C37 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C38 TradeDateTimeUTCRule
If Trade Date/Time is used with a time or a time + UTC indicator, then it must be the local time
of the place of trade, eg, of the stock exchange, or of the selling broker for OTC.
6.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
6.4.1 Identification <Id>
Presence: [1..1]
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 170 February 2025
```

