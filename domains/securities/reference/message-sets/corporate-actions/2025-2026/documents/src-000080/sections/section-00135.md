---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.17 RateDetails <RateDtls>", "3.4.11.24.17.7 ApplicableRate <AplblRate>"]
file_pages: [194]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.17.7 ApplicableRate <AplblRate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 194 to 194.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 194

```text
FiscalStamp <FsclStmp> contains one of the following elements (see "RateFormat24Choice" on
page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
3.4.11.24.17.7  ApplicableRate <AplblRate>
Presence: [0..1]
Definition: Rate applicable to the event announced, for example, redemption rate for a redemption
event.
ApplicableRate <AplblRate> contains one of the following elements (see "RateFormat24Choice" on
page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
3.4.11.24.17.8  TaxCreditRate <TaxCdtRate>
Presence: [0..1]
Definition: Amount of money per equity allocated as the result of a tax credit.
TaxCreditRate <TaxCdtRate> contains one of the following elements (see "RateFormat26Choice" on
page 1120 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1120
Or   Amount <Amt> [1..1] Amount C1 1120
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1120
3.4.11.24.17.9  FinancialTransactionTaxRate <FinTxTaxRate>
Presence: [0..1]
Definition: Rate of financial transaction tax.
FinancialTransactionTaxRate <FinTxTaxRate> contains one of the following elements (see
"RateFormat24Choice" on page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
3.4.11.24.17.10  WithholdingTaxRate <WhldgTaxRate>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 194 February 2026
```

