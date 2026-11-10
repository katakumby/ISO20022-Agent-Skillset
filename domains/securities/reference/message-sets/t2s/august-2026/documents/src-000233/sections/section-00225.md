---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "15.4.2.1.8.3 ServiceCategoryTotals <SvcCtgyTtls>", "15.4.2.1.8.3.6 ServiceItemCorrection <SvcItmCrrctn>", "15.4.2.1.8.3.6.7 Tax <Tax>", "15.4.2.1.8.3.6.7.6 ChargesAndFees <ChrgsAndFees>"]
file_pages: [302]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.8.3.6.7.6 ChargesAndFees <ChrgsAndFees>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 302 to 302.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 302

```text
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
15.4.2.1.8.3.6.7.6  ChargesAndFees <ChrgsAndFees>
Presence: [0..*]
Definition: Further details on the charges and fees realted to the tax data.
ChargesAndFees <ChrgsAndFees> contains the following BillingFeeRecord1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 302
   Description <Desc> [0..1] Text 302
   Rate <Rate> [0..1] Rate 302
   Amount <Amt> [0..1] Amount C1, C4 302
15.4.2.1.8.3.6.7.6.1  Type <Tp>
Presence: [0..1]
Definition: Type of the fees or charges.
Datatype: "Max4Text" on page 3329
15.4.2.1.8.3.6.7.6.2  Description <Desc>
Presence: [0..1]
Definition: Further details on the charges or fees
Datatype: "Max35Text" on page 3328
15.4.2.1.8.3.6.7.6.3  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the charges or fees.
Datatype: "PercentageRate" on page 3325
15.4.2.1.8.3.6.7.6.4  Amount <Amt>
Presence: [0..1]
Definition: Amount of money asked or paid for the charges or fees.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 302 August 2026
```

