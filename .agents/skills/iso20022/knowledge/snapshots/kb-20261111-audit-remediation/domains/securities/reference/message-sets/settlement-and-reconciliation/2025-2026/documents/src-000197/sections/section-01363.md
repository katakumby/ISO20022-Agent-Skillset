---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.7 SettlementDetails225", "35.1.26.7.24 AutomaticBorrowing <AutomtcBrrwg>"]
file_pages: [1830]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.7.24 AutomaticBorrowing <AutomtcBrrwg>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1830 to 1830.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1830

```text
Tracking <Trckg> contains one of the following elements (see "Tracking4Choice" on page 1551 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1551
Or}   Proprietary <Prtry> [1..1] ± 1551
35.1.26.7.24  AutomaticBorrowing <AutomtcBrrwg>
Presence: [0..1]
Definition: Condition for automatic borrowing.
AutomaticBorrowing <AutomtcBrrwg> contains one of the following elements (see
"AutomaticBorrowing6Choice" on page 1600 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1601
Or}   Proprietary <Prtry> [1..1] ± 1601
35.1.26.7.25  LetterOfGuarantee <LttrOfGrnt>
Presence: [0..1]
Definition: Specifies whether physical settlement may be executed using a letter of guarantee or if the
physical certificates should be used.
LetterOfGuarantee <LttrOfGrnt> contains one of the following elements (see
"LetterOfGuarantee4Choice" on page 1557 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1557
Or}   Proprietary <Prtry> [1..1] ± 1557
35.1.26.7.26  ReturnLeg <RtrLeg>
Presence: [0..1]
Definition: Indicates whether, for a securities lending/borrowing settlement transaction, the lender will
instruct the return leg as agreed with the borrower.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.26.7.27  ModificationCancellationAllowed <ModCxlAllwd>
Presence: [0..1]
Definition: Specifies whether a third party is allowed to modify or cancel the transaction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1830 March 2026
```

