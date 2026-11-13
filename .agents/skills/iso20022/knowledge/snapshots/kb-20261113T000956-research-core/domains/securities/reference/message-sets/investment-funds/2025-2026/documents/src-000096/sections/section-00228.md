---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.19 PaymentInstrument <PmtInstrm>"]
file_pages: [330]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.19 PaymentInstrument <PmtInstrm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 330 to 330.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 330

```text
Definition: Characteristics of the investment plan.
Impacted by: C20 "InvestmentPlanRule"
PlanCharacteristics <PlanChrtcs> contains the following elements (see
"InvestmentPlanCharacteristics1" on page 4776 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlanType <PlanTp> [1..1]  4776
{Or     Code <Cd> [1..1] CodeSet 4777
Or}     Proprietary <Prtry> [1..1] ± 4777
   Frequency <Frqcy> [0..1] ± 4777
   TotalNumberOfInstalments <TtlNbOfInstlmts> [0..1] Quantity 4777
   Quantity <Qty> [0..1] ± 4778
   PlanContinuation <PlanConttn> [0..1] Indicator 4778
   AdditionalSubscription <AddtlSbcpt> [0..1] Indicator 4778
   AdditionalSubscriptionFunction <AddtlSbcptFctn> [0..1] Indicator 4778
   AdditionalInformation <AddtlInf> [0..*] ± 4778
Constraints
• InvestmentPlanRule
If PlanType/Code is not INVP the AdditionalSubscription and AdditionalSubscriptionFunction must
not be present.
15.4.5.19  PaymentInstrument <PmtInstrm>
Presence: [0..*]
Definition: Specifies, for a specific type of transaction, how amounts are to be paid in or paid out.
PaymentInstrument <PmtInstrm> contains the following elements (see "PaymentInstrument16" on
page 5055 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderType <OrdrTp> [1..1]  5056
{Or     Code <Cd> [1..1] CodeSet 5056
Or}     Proprietary <Prtry> [1..1] ± 5056
   InstrumentType <InstrmTp> [1..1]  5057
{Or     Code <Cd> [1..1] CodeSet 5057
Or}     Proprietary <Prtry> [1..1] ± 5057
   AdditionalInformation <AddtlInf> [0..*] ± 5058
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 330 May 2026
```

