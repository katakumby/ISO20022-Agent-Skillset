---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks"]
file_pages: [198]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
preceding_topic_continuations: [{"constraint_ids": ["C16", "C17", "C18"], "until_heading": "5.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 198, "topic": "5.3 Constraints", "reference_path": "domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00149.md"}]
---

# 5.4 Message Building Blocks

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 198 to 198.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 198, C16–C18 before **5.4 Message Building Blocks** continue [5.3 Constraints](section-00149.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 198

```text
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different ReportNumbers. For example, a daily report
sent on day 1 would have ReportNumber 001, on day 2, 002, etc.
C16 SupplementaryDataRule
(Rule)
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C17 TradeIdentificationPresenceRule  '
(Rule)
TradeIdentification Or TradeExecutionIdentification Or UniqueTransactionIdentifier Must be
present.  (CrossElementSimpleRule)
Error handling:
– Error severity: Fatal
– Error Code: X00658
– Error Text: TradeIdentification Or TradeExecutionIdentification Or UniqueTradeIdentifier
Must be present.
C18 ValidationByTable
(Rule)
Must be a valid currency code which is registered with the ISO 4217 Maintenance Agency, and
consist of three contiguous letters. (Algorithm)
5.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
5.4.1 ReportParameters <RptParams>
Presence: [1..1]
Definition: Provides parameters of the margin report such as the creation date and time, the report
currency or the calculation date and time.
Impacted by: C15 ReportNumberRule
ReportParameters <RptParams> contains the following ReportParameters7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NetPositionIdentification <NetPosId> [1..1] Text 199
   ReportDateAndTime <RptDtAndTm> [1..1] ± 199
   UpdateType <UpdTp> [1..1] CodeSet 199
   Frequency <Frqcy> [1..1] CodeSet 199
   ReportNumber <RptNb> [0..1] Text 200
   ActivityIndicator <ActvtyInd> [1..1] Indicator 200
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 198
```

