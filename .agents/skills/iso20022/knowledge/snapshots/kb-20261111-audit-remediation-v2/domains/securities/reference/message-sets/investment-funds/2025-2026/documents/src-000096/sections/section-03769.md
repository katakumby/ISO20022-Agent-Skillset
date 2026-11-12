---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.31 Payment", "66.1.31.4 PaymentInstrument16", "66.1.31.4.1 OrderType <OrdrTp>"]
file_pages: [5056]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.31.4.1 OrderType <OrdrTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5056 to 5056.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5056

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderType <OrdrTp> [1..1]  5056
{Or     Code <Cd> [1..1] CodeSet 5056
Or}     Proprietary <Prtry> [1..1] ± 5056
   InstrumentType <InstrmTp> [1..1]  5057
{Or     Code <Cd> [1..1] CodeSet 5057
Or}     Proprietary <Prtry> [1..1] ± 5057
   AdditionalInformation <AddtlInf> [0..*] ± 5058
66.1.31.4.1  OrderType <OrdrTp>
Presence: [1..1]
Definition: Type of order to which the payment instrument applies.
OrderType <OrdrTp> contains one of the following FundOrderType5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5056
Or}   Proprietary <Prtry> [1..1] ± 5056
66.1.31.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of the investment fund order expressed as a code.
Datatype: "FundOrderType10Code" on page 5305
CodeName Name Definition
SUBS Subscription Investment fund order is a subscription.
RDIV ReinvestmentOfDividend Investment fund order is a dividend
reinvestment (only applicable to a
subscription).
REDM Redemption Investment fund order is a redemption.
RGSV RegularSavingsPlan Investment fund order is a regular
savings plan (only applicable to a
subscription).
WIDP Withdrawal Investment fund order is for a withdrawal
investment plan (only applicable to a
redemption).
66.1.31.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of the investment fund order expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5056 May 2026
```

