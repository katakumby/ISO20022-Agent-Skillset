---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.9 Financial Instrument", "9.1.9.2 FinancialInstrumentAttributes92", "9.1.9.2.11 CouponDate <CpnDt>"]
file_pages: [214]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.9.2.11 CouponDate <CpnDt>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 214 to 214.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 214

```text
Definition: Currency in which a security is issued or redenominated.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 315
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
9.1.9.2.11  CouponDate <CpnDt>
Presence: [0..1]
Definition: Next payment date of an interest bearing financial instrument.
Datatype: "ISODate" on page 340
9.1.9.2.12  ExpiryDate <XpryDt>
Presence: [0..1]
Definition: Date on which a privilege expires.
Datatype: "ISODate" on page 340
9.1.9.2.13  FloatingRateFixingDate <FltgRateFxgDt>
Presence: [0..1]
Definition: Date at which the interest rate of an interest bearing security will be calculated and reset,
according to the terms of the issue.
Datatype: "ISODate" on page 340
9.1.9.2.14  MaturityDate <MtrtyDt>
Presence: [0..1]
Definition: Planned final repayment date at the time of issuance.
Datatype: "ISODate" on page 340
9.1.9.2.15  IssueDate <IsseDt>
Presence: [0..1]
Definition: Date at which the security was made available.
Datatype: "ISODate" on page 340
9.1.9.2.16  NextCallableDate <NxtCllblDt>
Presence: [0..1]
Definition: Next date at which the issuer has the right to pay the security prior to maturity.
Datatype: "ISODate" on page 340
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 214 September 2025
```

