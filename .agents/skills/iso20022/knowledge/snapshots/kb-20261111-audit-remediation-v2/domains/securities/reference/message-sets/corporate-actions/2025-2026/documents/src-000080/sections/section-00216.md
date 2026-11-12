---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.6 CorporateActionGeneralInformation <CorpActnGnlInf>", "5.4.6.4 UnderlyingSecurity <UndrlygScty>", "5.4.6.4.13 DatedDate <DtdDt>"]
file_pages: [291]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.6.4.13 DatedDate <DtdDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 291 to 291.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 291

```text
Definition: Date on which a holder of a financial instrument has the right to request redemption of the
principal amount prior to its scheduled maturity date.
Datatype: "ISODate" on page 1243
5.4.6.4.13  DatedDate <DtdDt>
Presence: [0..1]
Definition: Date on which an interest bearing financial instrument begins to accrue interest.
Datatype: "ISODate" on page 1243
5.4.6.4.14  ConversionDate <ConvsDt>
Presence: [0..1]
Definition: Deadline by which a convertible security must be converted, according to the terms of the
issue.
Datatype: "ISODate" on page 1243
5.4.6.4.15  PreviousFactor <PrvsFctr>
Presence: [0..1]
Definition: Factor used to calculate the value of the outstanding principal of the financial instrument (for
factored securities) until the next redemption (factor) date.
Datatype: "BaseOne14Rate" on page 1247
5.4.6.4.16  NextFactor <NxtFctr>
Presence: [0..1]
Definition: Factor used to calculate the value of the outstanding principal of the financial instrument (for
factored securities) that will applicable after the redemption (factor) date.
Datatype: "BaseOne14Rate" on page 1247
5.4.6.4.17  InterestRate <IntrstRate>
Presence: [0..1]
Definition: Annualised interest rate of a financial instrument used to calculate the actual interest rate of
the coupon or the accrued interest.
Datatype: "Percentage14Rate" on page 1247
5.4.6.4.18  NextInterestRate <NxtIntrstRate>
Presence: [0..1]
Definition: Interest rate applicable to the next interest payment period in relation to variable rate
instruments.
Datatype: "Percentage14Rate" on page 1247
5.4.6.4.19  MinimumNominalQuantity <MinNmnlQty>
Presence: [0..1]
Definition: Minimum nominal quantity of financial instrument.
Impacted by: C12 "DigitalTokenUnitUsageRule"
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 291 February 2026
```

