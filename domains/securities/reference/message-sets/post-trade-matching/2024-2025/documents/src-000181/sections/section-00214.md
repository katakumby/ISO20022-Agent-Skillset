---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.11 Date Time", "7.1.11.7 TradeDate7Choice", "7.1.11.7.2 Value <Val>", "7.1.11.7.2.2 Proprietary <Prtry>"]
file_pages: [268]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.11.7.2.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 268 to 268.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 268

```text
Definition: Trading date expressed as a ISO20022 code.
Datatype: "TradingDate1Code" on page 656
CodeName Name Definition
VARI Various Partial trades have occurred over a
period of two or more days.
7.1.11.7.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trading date expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.12 Date Time Period
7.1.12.1  DateTimePeriod1
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 268
   ToDateTime <ToDtTm> [1..1] DateTime 268
7.1.12.1.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the period starts.
Datatype: "ISODateTime" on page 662
7.1.12.1.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the period ends.
Datatype: "ISODateTime" on page 662
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 268 February 2025
```

