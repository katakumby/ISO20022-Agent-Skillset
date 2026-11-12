---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.1 SecurityDetails <SctyDtls>", "3.4.11.24.1.17 InterestRate <IntrstRate>"]
file_pages: [180]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.1.17 InterestRate <IntrstRate>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 180 to 180.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 180

```text
NextFactor <NxtFctr> contains one of the following elements (see "RateFormat12Choice" on
page 971 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 971
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 971
3.4.11.24.1.17  InterestRate <IntrstRate>
Presence: [0..1]
Definition: Annualised interest rate of a financial instrument used to calculate the actual interest rate of
the coupon or the accrued interest.
InterestRate <IntrstRate> contains one of the following elements (see "RateFormat24Choice" on
page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
3.4.11.24.1.18  NextInterestRate <NxtIntrstRate>
Presence: [0..1]
Definition: Interest rate applicable to the next interest payment period in relation to variable rate
instruments.
NextInterestRate <NxtIntrstRate> contains one of the following elements (see "RateFormat24Choice"
on page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
3.4.11.24.1.19  MinimumNominalQuantity <MinNmnlQty>
Presence: [0..1]
Definition: Minimum nominal quantity of financial instrument.
Impacted by: C25 "DigitalTokenUnitUsageRule"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 180 February 2026
```

