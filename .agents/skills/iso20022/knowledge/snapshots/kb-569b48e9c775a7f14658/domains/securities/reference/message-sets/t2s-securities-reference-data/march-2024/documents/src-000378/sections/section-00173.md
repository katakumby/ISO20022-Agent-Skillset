---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.5 Date Time Period"]
file_pages: [237]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.5 Date Time Period

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 237 to 237.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 237

```text
13.1.5 Date Time Period
13.1.5.1  DateTimePeriod1
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 237
   ToDateTime <ToDtTm> [1..1] DateTime 237
13.1.5.1.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the period starts.
Datatype: "ISODateTime" on page 529
13.1.5.1.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the period ends.
Datatype: "ISODateTime" on page 529
13.1.6 Financial Instrument
13.1.6.1  FinancialInstrument97
Definition: Tangible items of value to a business.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Equity <Eqty> [0..1] ± 237
   Warrant <Warrt> [0..1] ± 238
   Debt <Debt> [0..1] ± C11,
C13
239
   Derivative <Deriv> [0..1] ± 243
13.1.6.1.1  Equity <Eqty>
Presence: [0..1]
Definition: Financial instrument which represents a title of ownership in a company, ie, the shareholder
is entitled to a part of the company's profit - usually by payment of a dividend - and to voting rights, if
any. Each company issues generally different classes of shares, eg, ordinary or common shares, which
have no guaranteed amount of dividend but carry voting rights, or preferred shares, which receive
dividends before ordinary shares but have no voting right.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 237 March 2024
```

