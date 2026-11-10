---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.23 CashMovementDetails <CshMvmntDtls>", "7.4.13.23.13 RateAndAmountDetails <RateAndAmtDtls>", "7.4.13.23.13.16 TaxReclaimRate <TaxRclmRate>"]
file_pages: [522]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.23.13.16 TaxReclaimRate <TaxRclmRate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 522 to 522.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 522

```text
TaxOnProfits <TaxOnPrfts> contains one of the following elements (see "RateFormat24Choice" on
page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
7.4.13.23.13.16  TaxReclaimRate <TaxRclmRate>
Presence: [0..1]
Definition: Percentage of cash that was paid in excess of actual tax obligation and was reclaimed.
TaxReclaimRate <TaxRclmRate> contains one of the following elements (see "RateFormat24Choice"
on page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
7.4.13.23.13.17  EqualisationRate <EqulstnRate>
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
7.4.13.23.13.18  DeemedRate <DmdRate>
Presence: [0..*]
Definition: Rate applied for the calculation of deemed proceeds which are not paid to security holders
but on which withholding tax is applicable.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 522 February 2026
```

