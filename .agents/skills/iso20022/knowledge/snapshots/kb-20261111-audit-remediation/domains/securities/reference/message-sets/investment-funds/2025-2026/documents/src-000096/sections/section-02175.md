---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.5 FinancialInstrumentDetails <FinInstrmDtls>", "50.4.4.9.5.9 SeriesIdentification <SrsId>", "50.4.4.9.5.9.1 SeriesDate <SrsDt>"]
file_pages: [3064]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.5.9.1 SeriesDate <SrsDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3064 to 3064.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3064

```text
Constraints
• SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
50.4.4.9.5.9.1  SeriesDate <SrsDt>
Presence: [0..1]
Definition: Issue date of the fund series. It is typically applicable to a redemption order, subscription
order confirmation or redemption order confirmation, but may be specified in the subscription order, if
known.
SeriesDate <SrsDt> contains one of the following elements (see "DateFormat42Choice" on page 4467
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   YearMonth <YrMnth> [1..1] YearMonth 4467
Or}   YearMonthDay <YrMnthDay> [1..1] Date 4467
50.4.4.9.5.9.2  SeriesName <SrsNm>
Presence: [0..1]
Definition: Name of the fund series. It is typically applicable to a redemption order, subscription order
confirmation or redemption order confirmation, but may be specified in the subscription, if known.
Datatype: "Max35Text" on page 5403
50.4.4.9.6  SubAccountForHolding <SubAcctForHldg>
Presence: [0..1]
Definition: Subdivision of the account used to segregate specific holdings.
SubAccountForHolding <SubAcctForHldg> contains the following elements (see "SubAccount6" on
page 4642 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4642
   Name <Nm> [0..1] Text 4642
   Characteristic <Chrtc> [0..1] Text 4642
   AccountDesignation <AcctDsgnt> [0..1] Text 4642
50.4.4.9.7  AmountOrUnits <AmtOrUnits>
Presence: [1..1]
Definition: Amount of money or the number of units for the subscription order.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3064 May 2026
```

