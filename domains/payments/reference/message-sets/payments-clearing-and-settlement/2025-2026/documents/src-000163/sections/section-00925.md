---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.17 Regulatory Reporting", "10.1.17.1 RegulatoryReporting10", "10.1.17.1.3 Details <Dtls>", "10.1.17.1.3.5 Amount <Amt>"]
file_pages: [1220]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.17.1.3.5 Amount <Amt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1220 to 1220.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1220

```text
Datatype: "Max10Text" on page 1244
10.1.17.1.3.5  Amount <Amt>
Presence: [0..1]
Definition: Amount of money to be reported for regulatory and statutory requirements.
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
10.1.17.1.3.6  Information <Inf>
Presence: [0..*]
Definition: Additional details that cater for specific domestic regulatory requirements.
Datatype: "Max35Text" on page 1246
10.1.18 System Identification
10.1.18.1  ClearingSystemIdentification2Choice
Definition: Choice of a clearing system identifier.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1220
Or}   Proprietary <Prtry> [1..1] Text 1220
10.1.18.1.1  Code <Cd>
Presence: [1..1]
Definition: Identification of a clearing system, in a coded form as published in an external list.
Datatype: "ExternalClearingSystemIdentification1Code" on page 1228
10.1.18.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Identification code for a clearing system, that has not yet been identified in the list of clearing
systems.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1220 March 2026
```

