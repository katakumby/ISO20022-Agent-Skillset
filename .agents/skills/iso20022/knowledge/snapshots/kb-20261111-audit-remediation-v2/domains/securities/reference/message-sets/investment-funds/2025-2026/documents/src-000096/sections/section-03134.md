---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.3 SubBalanceInformation2", "66.1.5.3.3 ExtendedSubBalanceType <XtndedSubBalTp>"]
file_pages: [4362]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.3.3 ExtendedSubBalanceType <XtndedSubBalTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4362 to 4362.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4362

```text
CodeName Name Definition
pertaining to the account, or due to a
missing or incomplete order.
BTRA BeingTransferred Financial instrument is unavailable as a
result of a transfer order, pending
movement in the shareholders' register.
66.1.5.3.3  ExtendedSubBalanceType <XtndedSubBalTp>
Presence: [1..1]
Warning   Either SubBalanceType or ExtendedSubBalanceType must be present, but not both.
Definition: Reason a security is not available or additional information about the financial instrument for
which the balance is given, for example, unregistered, registered in nominee name.
Datatype: "Extended350Code" on page 5402
66.1.5.3.4  AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>
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
66.1.5.4  AggregateBalancePerSafekeepingPlace4
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account at a specified place of safekeeping.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4362 May 2026
```

