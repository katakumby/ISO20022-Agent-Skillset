---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.6 CorporateActionGeneralInformation <CorpActnGnlInf>", "5.4.6.4 UnderlyingSecurity <UndrlygScty>", "5.4.6.4.6 NextCouponDate <NxtCpnDt>"]
file_pages: [290]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.6.4.6 NextCouponDate <NxtCpnDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 290 to 290.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 290

```text
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 1157
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
5.4.6.4.6  NextCouponDate <NxtCpnDt>
Presence: [0..1]
Definition: Next payment date of an interest bearing financial instrument.
Datatype: "ISODate" on page 1243
5.4.6.4.7  ExpiryDate <XpryDt>
Presence: [0..1]
Definition: Date on which an order expires or at which a privilege or offer terminates.
Datatype: "ISODate" on page 1243
5.4.6.4.8  FloatingRateFixingDate <FltgRateFxgDt>
Presence: [0..1]
Definition: Date on which the interest rate or redemption price will be/was calculated according to the
terms of the issue.
Datatype: "ISODate" on page 1243
5.4.6.4.9  MaturityDate <MtrtyDt>
Presence: [0..1]
Definition: Date on which a financial instrument becomes due and assets are to be repaid.
Datatype: "ISODate" on page 1243
5.4.6.4.10  IssueDate <IsseDt>
Presence: [0..1]
Definition: Date on which the financial instrument is issued.
Datatype: "ISODate" on page 1243
5.4.6.4.11  NextCallableDate <NxtCllblDt>
Presence: [0..1]
Definition: Date on which a financial instrument is called away/redeemed before its scheduled maturity.
Datatype: "ISODate" on page 1243
5.4.6.4.12  PutableDate <PutblDt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 290 February 2026
```

