---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.2 InvestmentRestrictions3", "66.1.26.2.15 MinimumHoldingUnits <MinHldgUnits>"]
file_pages: [4716]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.2.15 MinimumHoldingUnits <MinHldgUnits>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4716 to 4716.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4716

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.26.2.15  MinimumHoldingUnits <MinHldgUnits>
Presence: [0..1]
Definition: Minimum number of units that must be maintained to avoid automatic redemption.
Datatype: "DecimalNumber" on page 5400
66.1.26.2.16  MinimumHoldingPeriod <MinHldgPrd>
Presence: [0..1]
Definition: Description of the period, that may be a number of days or weeks or another way of
describing the period, during which the units/shares must be held following their issue before
redemption will be permitted.
Datatype: "Max70Text" on page 5404
66.1.26.2.17  HoldingTransferable <HldgTrfbl>
Presence: [0..1]
Definition: Specifies how registered investors are able to transfer some or all of their holdings to third
parties.
Datatype: "HoldingTransferable1Code" on page 5310
CodeName Name Definition
TRAL TransferAllowed Transfer is allowed.
TRNA TransferNotAllowed Transfer is not allowed.
RFOD ReferToFundOrderDesk Indicates that the operation is only
possible in restricted circumstances.
66.1.26.2.18  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the investment restrictions.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4716 May 2026
```

