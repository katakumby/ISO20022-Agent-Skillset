---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.2 EstimatedFundCashForecast5", "66.1.25.2.9 EstimatedTotalNAVChangeRate <EstmtdTtlNAVChngRate>"]
file_pages: [4675]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.2.9 EstimatedTotalNAVChangeRate <EstmtdTtlNAVChngRate>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4675 to 4675.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4675

```text
66.1.25.2.9  EstimatedTotalNAVChangeRate <EstmtdTtlNAVChngRate>
Presence: [0..1]
Definition: Rate of change of the net asset value.
Datatype: "PercentageRate" on page 5401
66.1.25.2.10  InvestmentCurrency <InvstmtCcy>
Presence: [0..*]
Definition: Currency of the investment fund class.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
66.1.25.2.11  CurrencyStatus <CcySts>
Presence: [0..1]
Definition: Information about the designation of the share class currency, that is, whether it is for
onshore or offshore purposes and other information that may be required. This is typically only required
for CNY funds.
CurrencyStatus <CcySts> contains the following elements (see "CurrencyDesignation1" on
page 4831 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CurrencyDesignation <CcyDsgnt> [0..1] CodeSet 4831
   Location <Lctn> [0..1] CodeSet C12 4831
   AdditionalInformation <AddtlInf> [0..1] Text 4831
66.1.25.2.12  ExceptionalNetCashFlowIndicator <XcptnlNetCshFlowInd>
Presence: [1..1]
Definition: Indicates whether the estimated net cash flow is exceptional.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.25.2.13  Price <Pric>
Presence: [0..1]
Definition: Price per unit of the previous trade date.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4675 May 2026
```

