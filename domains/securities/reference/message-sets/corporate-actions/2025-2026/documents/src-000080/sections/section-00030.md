---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.6 EventsLinkage <EvtsLkg>", "3.4.7.7 UnderlyingSecurity <UndrlygScty>", "3.4.7.7.5 OptionStyle <OptnStyle>"]
file_pages: [70]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.7.7.5 OptionStyle <OptnStyle>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 70 to 70.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 70

```text
3.4.7.7.5  OptionStyle <OptnStyle>
Presence: [0..1]
Definition: Specifies how an option can be exercised.
OptionStyle <OptnStyle> contains one of the following elements (see "OptionStyle8Choice" on
page 923 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 923
Or}   Proprietary <Prtry> [1..1] ± 924
3.4.7.7.6  DenominationCurrency <DnmtnCcy>
Presence: [0..1]
Definition: Currency in which a financial instrument is currently denominated.
Impacted by: C3 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 1157
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
3.4.7.7.7  NextCouponDate <NxtCpnDt>
Presence: [0..1]
Definition: Next payment date of an interest bearing financial instrument.
Datatype: "ISODate" on page 1243
3.4.7.7.8  ExpiryDate <XpryDt>
Presence: [0..1]
Definition: Date on which an order expires or at which a privilege or offer terminates.
Datatype: "ISODate" on page 1243
3.4.7.7.9  FloatingRateFixingDate <FltgRateFxgDt>
Presence: [0..1]
Definition: Date on which the interest rate or redemption price will be/was calculated according to the
terms of the issue.
Datatype: "ISODate" on page 1243
3.4.7.7.10  MaturityDate <MtrtyDt>
Presence: [0..1]
Definition: Date on which a financial instrument becomes due and assets are to be repaid.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 70 February 2026
```

