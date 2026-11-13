---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.13 Financial Instrument", "82.1.13.2 FinancialInstrumentAttributes92", "82.1.13.2.11 CouponDate <CpnDt>"]
file_pages: [2939]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.13.2.11 CouponDate <CpnDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2939 to 2939.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2939

```text
Definition: Currency in which a security is issued or redenominated.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 3212
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
82.1.13.2.11  CouponDate <CpnDt>
Presence: [0..1]
Definition: Next payment date of an interest bearing financial instrument.
Datatype: "ISODate" on page 3319
82.1.13.2.12  ExpiryDate <XpryDt>
Presence: [0..1]
Definition: Date on which a privilege expires.
Datatype: "ISODate" on page 3319
82.1.13.2.13  FloatingRateFixingDate <FltgRateFxgDt>
Presence: [0..1]
Definition: Date at which the interest rate of an interest bearing security will be calculated and reset,
according to the terms of the issue.
Datatype: "ISODate" on page 3319
82.1.13.2.14  MaturityDate <MtrtyDt>
Presence: [0..1]
Definition: Planned final repayment date at the time of issuance.
Datatype: "ISODate" on page 3319
82.1.13.2.15  IssueDate <IsseDt>
Presence: [0..1]
Definition: Date at which the security was made available.
Datatype: "ISODate" on page 3319
82.1.13.2.16  NextCallableDate <NxtCllblDt>
Presence: [0..1]
Definition: Next date at which the issuer has the right to pay the security prior to maturity.
Datatype: "ISODate" on page 3319
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2939 August 2026
```

