---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.6 AggregateBalanceInformation4", "66.1.5.6.15 AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>"]
file_pages: [4376]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.6.15 AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4376 to 4376.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4376

```text
BalanceBreakdownDetails <BalBrkdwnDtls> contains the following elements (see
"SubBalanceInformation2" on page 4359 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± 4360
{Or   SubBalanceType <SubBalTp> [1..1] CodeSet 4360
Or}   ExtendedSubBalanceType <XtndedSubBalTp> [1..1] Text 4362
   AdditionalBalanceBreakdownDetails
<AddtlBalBrkdwnDtls>
[0..*] ± 4362
66.1.5.6.15  AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>
Presence: [0..*]
Definition: Net position of a segregated holding of a single security within the overall position held in a
securities account, eg, sub-balance per status.
AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls> contains the following elements (see
"AdditionalBalanceInformation2" on page 4367 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± 4368
{Or   SubBalanceType <SubBalTp> [1..1] CodeSet 4368
Or}   ExtendedSubBalanceType <XtndedSubBalTp> [1..1] Text 4369
66.1.5.6.16  BalanceAtSafekeepingPlace <BalAtSfkpgPlc>
Presence: [0..*]
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account at a specified place of safekeeping.
Impacted by: C2 "AccruedInterestAmountSignRule", C6 "AggregateQuantityGuideline"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4376 May 2026
```

