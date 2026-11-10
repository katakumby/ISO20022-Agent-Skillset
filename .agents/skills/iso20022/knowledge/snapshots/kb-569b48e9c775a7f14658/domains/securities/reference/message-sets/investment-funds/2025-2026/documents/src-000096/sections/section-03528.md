---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.23 InvestmentPlanCharacteristics1", "66.1.26.23.4 Quantity <Qty>"]
file_pages: [4778]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.23.4 Quantity <Qty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4778 to 4778.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4778

```text
Datatype: "Number" on page 5400
66.1.26.23.4  Quantity <Qty>
Presence: [0..1]
Definition: Minimum amount of the periodical payments. (If there is no maximum, then '0' must be
specified for the Amount or Units.)
Quantity <Qty> contains one of the following elements (see "UnitsOrAmount1Choice" on page 4528
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1, C13 4529
Or}   Unit <Unit> [1..1] Quantity 4529
66.1.26.23.5  PlanContinuation <PlanConttn>
Presence: [0..1]
Definition: Indicates whether it is possible to continue the savings plan after the end date.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.23.6  AdditionalSubscription <AddtlSbcpt>
Presence: [0..1]
Definition: Indicates whether it is possible to subscribe to additional instalments over and above that
permitted by the savings plan frequency.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.23.7  AdditionalSubscriptionFunction <AddtlSbcptFctn>
Presence: [0..1]
Definition: Indicates whether any additional instalments will reduce the period of the life of the savings
investment plan.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.23.8  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the investment plan.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4778 May 2026
```

