---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.49 SecuritiesFinancing12", "7.1.19.49.11 SpreadRate <SprdRate>"]
file_pages: [363]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.49.11 SpreadRate <SprdRate>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 363 to 363.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 363

```text
PricingRate <PricgRate> contains one of the following elements (see "RateOrName1Choice" on
page 331 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] ± C48 332
Or}   RateName <RateNm> [1..1] ± 332
7.1.19.49.11  SpreadRate <SprdRate>
Presence: [0..1]
Definition: Margin over or under an index that determines the repurchase rate, expressed as a rate or
an amount.
SpreadRate <SprdRate> contains the following elements (see "SpreadRate1" on page 322 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [1..1] Indicator 323
   RateOrAmount <RateOrAmt> [1..1]  323
{Or     Amount <Amt> [1..1] Amount C1, C9 323
Or}     Rate <Rate> [1..1] Rate 323
7.1.19.49.12  CallableTradeIndicator <CllblTradInd>
Presence: [0..1]
Definition: Indicates whether or not the trade is callable.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.49.13  TransactionCallDelay <TxCallDely>
Presence: [0..1]
Definition: Minimum number of days' notice a counterparty needs for terminating the transaction.
Datatype: "Max3NumericText" on page 669
7.1.19.49.14  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Definition: Interest amount that has accrued in between two periods, for example, in between interest
payment periods.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 363 February 2025
```

