---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.10 Price", "4.1.10.1 PriceRateOrAmount3Choice", "4.1.10.1.2 Amount <Amt>"]
file_pages: [72]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.10.1.2 Amount <Amt>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 72 to 72.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 72

```text
Datatype: "PercentageRate" on page 82
4.1.10.1.2  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 73
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
4.1.11 System Identification
4.1.11.1  ClearingSystemIdentification2Choice
Definition: Choice of a clearing system identifier.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 72
Or}   Proprietary <Prtry> [1..1] Text 72
4.1.11.1.1  Code <Cd>
Presence: [1..1]
Definition: Identification of a clearing system, in a coded form as published in an external list.
Datatype: "ExternalClearingSystemIdentification1Code" on page 76
4.1.11.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Identification code for a clearing system, that has not yet been identified in the list of clearing
systems.
Datatype: "Max35Text" on page 83
4.2 Message Datatypes
4.2.1 Amount
4.2.1.1  ActiveCurrencyAndAmount
Definition: A number of monetary units specified in an active currency where the unit of currency is
explicit and compliant with ISO 4217.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
72 March 2024
```

