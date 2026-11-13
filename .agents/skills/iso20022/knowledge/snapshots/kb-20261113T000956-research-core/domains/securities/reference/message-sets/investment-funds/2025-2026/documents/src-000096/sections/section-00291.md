---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["21 semt.005.001.02 AccountingStatementOfHoldingsCancellationV02", "21.4 Message Building Blocks"]
file_pages: [405]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.005.001.02"]
---

# 21.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 405 to 405.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 405

```text
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C12 FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
C13 Party1Rule
If PlaceSafekeeping is not SHHE, then Party is mandatory. If PlaceSafekeeping is SHHE, then
Party is optional.
C14 StreetNameAndOrPostOfficeBoxRule
If StreetName is not present, then PostOfficeBox is mandatory. If StreetName is present, then
PostOfficeBox is optional.
C15 ValueRule
If Type is not MRKT, then Value may not be expressed with UnknownIndicator.
21.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
21.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies a message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
Approved by the Securities SEG on 27 January 2026 semt.005.001.02
AccountingStatementOfHoldingsCancellationV02
Investment Funds - Maintenance 2025 - 2026 405 May 2026
```

