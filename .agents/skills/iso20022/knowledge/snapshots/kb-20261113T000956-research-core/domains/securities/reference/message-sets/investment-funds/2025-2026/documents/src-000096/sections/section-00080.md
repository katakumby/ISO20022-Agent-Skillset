---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04", "9.4 Message Building Blocks"]
file_pages: [119]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.042.001.04"]
preceding_topic_continuations: [{"constraint_ids": ["C11", "C12", "C13", "C14", "C15", "C16", "C17"], "until_heading": "9.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 119, "topic": "9.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00079.md"}]
---

# 9.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 119 to 119.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 119, C11–C17 before **9.4 Message Building Blocks** continue [9.3 Constraints](section-00079.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 119

```text
Note: The decimal separator is a dot.
C11 ExceptionalCashFlowIndicatorRule
If ExceptionalNetCashFlowIndicator is "true" or "1" (Yes), then at least one or more of the
following must be present:
BreakdownByParty/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByParty/CashOutForecast/ExceptionalCashFlowIndicator, or
BreakdownByCountry/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByCountry/CashOutForecast/ExceptionalCashFlowIndicator, or
BreakdownByCurrency/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByCurrency/CashOutForecast/ExceptionalCashFlowIndicator, or
BreakdownByUserDefinedParameter/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByUserDefinedParameter/CashOutForecast/ExceptionalCashFlowIndicator.
C12 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C13 FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
C14 FundIdentification1Rule
If Identification is not present, then Name or LegalEntityIdentifier must be present. Identification,
Name and Legal Entity Identifier may all be present.
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
9.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
9.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 camt.042.001.04
FundDetailedEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 119 May 2026
```

