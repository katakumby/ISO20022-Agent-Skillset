---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.6 FinancialInstrumentDetails <FinInstrmDtls>", "46.4.5.10.6.9 SeriesIdentification <SrsId>", "46.4.5.10.6.9.1 SeriesDate <SrsDt>"]
file_pages: [2370]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.6.9.1 SeriesDate <SrsDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2370 to 2370.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2370

```text
Constraints
• SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
46.4.5.10.6.9.1  SeriesDate <SrsDt>
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
46.4.5.10.6.9.2  SeriesName <SrsNm>
Presence: [0..1]
Definition: Name of the fund series. It is typically applicable to a redemption order, subscription order
confirmation or redemption order confirmation, but may be specified in the subscription, if known.
Datatype: "Max35Text" on page 5403
46.4.5.10.7  SubAccountForHolding <SubAcctForHldg>
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
46.4.5.10.8  Units <Units>
Presence: [1..1]
Definition: Quantity of units or digital tokens.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2370 May 2026
```

