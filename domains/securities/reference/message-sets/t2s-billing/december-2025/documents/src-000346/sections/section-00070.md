---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.10 ServiceCategoryTotals <SvcCtgyTtls>", "3.4.2.1.10.7 ServiceItemTotals <SvcItmTtls>", "3.4.2.1.10.7.5 Tax <Tax>", "3.4.2.1.10.7.5.6 ChargesAndFees <ChrgsAndFees>", "3.4.2.1.10.7.5.6.1 Type <Tp>"]
file_pages: [96]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.10.7.5.6.1 Type <Tp>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 96 to 96.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 96

```text
ChargesAndFees <ChrgsAndFees> contains the following BillingFeeRecord1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 96
   Description <Desc> [0..1] Text 96
   Rate <Rate> [0..1] Rate 96
   Amount <Amt> [0..1] Amount C1, C4 96
3.4.2.1.10.7.5.6.1  Type <Tp>
Presence: [0..1]
Definition: Type of the fees or charges.
Datatype: "Max4Text" on page 153
3.4.2.1.10.7.5.6.2  Description <Desc>
Presence: [0..1]
Definition: Further details on the charges or fees
Datatype: "Max35Text" on page 153
3.4.2.1.10.7.5.6.3  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the charges or fees.
Datatype: "PercentageRate" on page 150
3.4.2.1.10.7.5.6.4  Amount <Amt>
Presence: [0..1]
Definition: Amount of money asked or paid for the charges or fees.
Impacted by: C1 "ActiveCurrency", C4 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 143
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.2.1.10.7.6  TotalInvoiceAmount <TtlInvcAmt>
Presence: [1..1]
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 96 December 2025
```

