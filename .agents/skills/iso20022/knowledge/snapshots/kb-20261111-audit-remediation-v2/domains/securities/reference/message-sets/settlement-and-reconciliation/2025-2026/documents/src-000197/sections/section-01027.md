---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.4 FinancialInstrumentAttributes112", "35.1.11.4.11 CouponDate <CpnDt>"]
file_pages: [1466]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.4.11 CouponDate <CpnDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1466 to 1466.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1466

```text
Definition: Currency in which a security is issued or redenominated.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 2044
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
35.1.11.4.11  CouponDate <CpnDt>
Presence: [0..1]
Definition: Next payment date of an interest bearing financial instrument.
Datatype: "ISODate" on page 2185
35.1.11.4.12  ExpiryDate <XpryDt>
Presence: [0..1]
Definition: Date on which a privilege expires.
Datatype: "ISODate" on page 2185
35.1.11.4.13  FloatingRateFixingDate <FltgRateFxgDt>
Presence: [0..1]
Definition: Date at which the interest rate of an interest bearing security will be calculated and reset,
according to the terms of the issue.
Datatype: "ISODate" on page 2185
35.1.11.4.14  MaturityDate <MtrtyDt>
Presence: [0..1]
Definition: Planned final repayment date at the time of issuance.
Datatype: "ISODate" on page 2185
35.1.11.4.15  IssueDate <IsseDt>
Presence: [0..1]
Definition: Date at which the security was made available.
Datatype: "ISODate" on page 2185
35.1.11.4.16  NextCallableDate <NxtCllblDt>
Presence: [0..1]
Definition: Next date at which the issuer has the right to pay the security prior to maturity.
Datatype: "ISODate" on page 2185
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1466 March 2026
```

