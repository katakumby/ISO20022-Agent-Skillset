---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["20 semt.004.001.02 CustodyStatementOfHoldingsCancellationV02", "20.4 Message Building Blocks"]
file_pages: [400]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.004.001.02"]
---

# 20.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 400 to 400.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 400

```text
C8 BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
C9 BalanceForAccountOrSubAccountDetailsRule
If StatementGeneralDetails/ActivityIndicator is "true" or "1" (Yes), then either
BalanceForAccount or SubAccountDetails is mandatory. If StatementGeneralDetails/
ActivityIndicator is "false" or "0" (No), then BalanceForAccount and SubAccountDetails may be
present.
C10 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C11 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C12 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C13 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C14 FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
C15 Party1Rule
If PlaceSafekeeping is not SHHE, then Party is mandatory. If PlaceSafekeeping is SHHE, then
Party is optional.
C16 StreetNameAndOrPostOfficeBoxRule
If StreetName is not present, then PostOfficeBox is mandatory. If StreetName is present, then
PostOfficeBox is optional.
C17 ValueRule
If Type is not MRKT, then Value may not be expressed with UnknownIndicator.
20.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
20.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies a message from a business application standpoint.
Approved by the Securities SEG on 27 January 2026 semt.004.001.02
CustodyStatementOfHoldingsCancellationV02
Investment Funds - Maintenance 2025 - 2026 400 May 2026
```

