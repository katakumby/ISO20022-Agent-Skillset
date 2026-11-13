---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.14 RateAndAmountDetails <RateAndAmtDtls>", "3.4.11.25.14.16 TaxReclaimRate <TaxRclmRate>"]
file_pages: [242]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.14.16 TaxReclaimRate <TaxRclmRate>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 242 to 242.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 242

```text
TaxOnProfits <TaxOnPrfts> contains one of the following elements (see "RateFormat24Choice" on
page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
3.4.11.25.14.16  TaxReclaimRate <TaxRclmRate>
Presence: [0..1]
Definition: Percentage of cash that was paid in excess of actual tax obligation and was reclaimed.
TaxReclaimRate <TaxRclmRate> contains one of the following elements (see "RateFormat24Choice"
on page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
3.4.11.25.14.17  EqualisationRate <EqulstnRate>
Presence: [0..1]
Definition: Portion of the fund distribution which represents the average accrued income included in the
purchase price for units bought during the account period.
EqualisationRate <EqulstnRate> contains one of the following elements (see
"RateAndAmountFormat42Choice" on page 1100 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 1100
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1100
3.4.11.25.14.18  DeemedRate <DmdRate>
Presence: [0..*]
Definition: Rate applied for the calculation of deemed proceeds which are not paid to security holders
but on which withholding tax is applicable.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 242 February 2026
```

