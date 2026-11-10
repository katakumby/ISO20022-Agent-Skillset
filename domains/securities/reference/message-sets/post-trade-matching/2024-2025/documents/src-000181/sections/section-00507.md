---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.27 Settlement Details", "7.1.27.1 SettlementDetails213", "7.1.27.1.25 Tracking <Trckg>"]
file_pages: [581]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.27.1.25 Tracking <Trckg>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 581 to 581.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 581

```text
7.1.27.1.25  Tracking <Trckg>
Presence: [0..1]
Definition: Specifies whether the loan and/or collateral is tracked.
Tracking <Trckg> contains one of the following elements (see "Tracking4Choice" on page 306 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 306
Or}   Proprietary <Prtry> [1..1] ± 306
7.1.27.1.26  AutomaticBorrowing <AutomtcBrrwg>
Presence: [0..1]
Definition: Condition for automatic borrowing.
AutomaticBorrowing <AutomtcBrrwg> contains one of the following elements (see
"AutomaticBorrowing6Choice" on page 357 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 357
Or}   Proprietary <Prtry> [1..1] ± 358
7.1.27.1.27  LetterOfGuarantee <LttrOfGrnt>
Presence: [0..1]
Definition: Specifies whether physical settlement may be executed using a letter of guarantee or if the
physical certificates should be used.
LetterOfGuarantee <LttrOfGrnt> contains one of the following elements (see
"LetterOfGuarantee4Choice" on page 312 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 312
Or}   Proprietary <Prtry> [1..1] ± 312
7.1.27.1.28  ReturnLeg <RtrLeg>
Presence: [0..1]
Definition: Specifies whether, for a securities lending/borrowing settlement transaction, the lender will
instruct the return leg as agreed with the borrower.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 581 February 2025
```

