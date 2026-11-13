---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "64.4 Message Building Blocks", "64.4.3 IndividualOrderConfirmationDetailsReport <IndvOrdrConfDtlsRpt>", "64.4.3.9 FinancialInstrumentDetails <FinInstrmDtls>", "64.4.3.9.9 SeriesIdentification <SrsId>", "64.4.3.9.9.1 SeriesDate <SrsDt>"]
file_pages: [4302]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.057.001.03"]
---

# 64.4.3.9.9.1 SeriesDate <SrsDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4302 to 4302.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4302

```text
Constraints
• SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
64.4.3.9.9.1  SeriesDate <SrsDt>
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
64.4.3.9.9.2  SeriesName <SrsNm>
Presence: [0..1]
Definition: Name of the fund series. It is typically applicable to a redemption order, subscription order
confirmation or redemption order confirmation, but may be specified in the subscription, if known.
Datatype: "Max35Text" on page 5403
64.4.4 Extension <Xtnsn>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C3 "ExtensionRule"
Extension <Xtnsn> contains the following elements (see "Extension1" on page 4835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [1..1] Text 4836
   Text <Txt> [1..1] Text 4836
Constraints
• ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4302 May 2026
```

