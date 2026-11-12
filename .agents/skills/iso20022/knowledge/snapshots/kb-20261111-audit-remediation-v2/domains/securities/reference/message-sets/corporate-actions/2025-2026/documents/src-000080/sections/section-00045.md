---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.8 AccountDetails <AcctDtls>", "3.4.8.2 AccountsListAndBalanceDetails <AcctsListAndBalDtls>", "3.4.8.2.5 Balance <Bal>", "3.4.8.2.5.17 InstructedBalance <InstdBal>"]
file_pages: [86]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.8.2.5.17 InstructedBalance <InstdBal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 86 to 86.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 86

```text
UninstructedBalance <UinstdBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
3.4.8.2.5.17  InstructedBalance <InstdBal>
Presence: [0..1]
Definition: Balance of instructed position.
InstructedBalance <InstdBal> contains one of the following elements (see "BalanceFormat11Choice"
on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
3.4.8.2.5.18  AffectedBalance <AfctdBal>
Presence: [0..1]
Definition: Balance that has been affected by the process run through the event.
AffectedBalance <AfctdBal> contains one of the following elements (see "BalanceFormat11Choice"
on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
3.4.8.2.5.19  UnaffectedBalance <UafctdBal>
Presence: [0..1]
Definition: Balance that has not been affected by the process run through the event.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 86 February 2026
```

