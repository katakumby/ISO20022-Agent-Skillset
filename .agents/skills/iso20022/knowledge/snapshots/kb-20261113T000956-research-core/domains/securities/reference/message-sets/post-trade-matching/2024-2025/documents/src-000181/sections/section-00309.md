---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.49 SecuritiesFinancing12", "7.1.19.49.37 MinimumDateForCallBack <MinDtForCallBck>"]
file_pages: [370]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.49.37 MinimumDateForCallBack <MinDtForCallBck>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 370 to 370.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 370

```text
Reversible <Rvsbl> contains one of the following elements (see "Reversible2Choice" on page 309 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 309
Or}   Proprietary <Prtry> [1..1] ± 310
7.1.19.49.37  MinimumDateForCallBack <MinDtForCallBck>
Presence: [0..1]
Definition: This is the minimum date at which the Borrower is allowed to give back the securities.
Datatype: "ISODate" on page 662
7.1.19.49.38  RollOver <RollOver>
Presence: [0..1]
Definition: Indicates that the contract can be rolled over.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.49.39  PeriodicPayment <PrdcPmt>
Presence: [0..1]
Definition: Indicates whether the securities lending fees can be paid periodically or at the end of the
contract.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.49.40  ExCoupon <ExCpn>
Presence: [0..1]
Definition: Indicates whether the trade is executed ex coupon.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.50  InterestComputationMethodFormat4Choice
Definition: Choice between a standard code or proprietary code to specify the type of interest
computation method.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 370 February 2025
```

