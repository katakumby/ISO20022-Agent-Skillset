---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks"]
file_pages: [133]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
preceding_topic_continuations: [{"constraint_ids": ["C19", "C20", "C21"], "until_heading": "4.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 133, "topic": "4.3 Constraints", "reference_path": "domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00101.md"}]
---

# 4.4 Message Building Blocks

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 133 to 133.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 133, C19–C21 before **4.4 Message Building Blocks** continue [4.3 Constraints](section-00101.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 133

```text
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different ReportNumbers. For example, a daily report
sent on day 1 would have ReportNumber 001, on day 2, 002, etc.
C19 SupplementaryDataRule
(Rule)
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C20 TradeIdentificationPresenceRule  '
(Rule)
TradeIdentification Or TradeExecutionIdentification Or UniqueTransactionIdentifier Must be
present.  (CrossElementSimpleRule)
Error handling:
– Error severity: Fatal
– Error Code: X00658
– Error Text: TradeIdentification Or TradeExecutionIdentification Or UniqueTradeIdentifier
Must be present.
C21 ValidationByTable
(Rule)
Must be a valid currency code which is registered with the ISO 4217 Maintenance Agency, and
consist of three contiguous letters. (Algorithm)
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
4.4.1 StatementParameters <StmtParams>
Presence: [1..1]
Definition: Provides various statement parameters such as the statement identification, the statement
date and time or the statement frequency.
Impacted by: C18 ReportNumberRule
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 133
```

