---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.11 AccountDetails <AcctDtls>", "7.4.11.2 AccountsListAndBalanceDetails <AcctsListAndBalDtls>", "7.4.11.2.5 Balance <Bal>", "7.4.11.2.5.14 RegisteredBalance <RegdBal>"]
file_pages: [413]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.11.2.5.14 RegisteredBalance <RegdBal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 413 to 413.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 413

```text
InTransshipmentBalance <InTrnsShipmntBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
7.4.11.2.5.14  RegisteredBalance <RegdBal>
Presence: [0..1]
Definition: Balance of financial instruments that are registered (in the name of a nominee name or of the
beneficial owner).
RegisteredBalance <RegdBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
7.4.11.2.5.15  ObligatedBalance <OblgtdBal>
Presence: [0..1]
Definition: Position that account holders should return to the account servicer to participate in the event
or to fulfil their obligation for the event to be complete, for example, return of securities for late
announced drawing.
ObligatedBalance <OblgtdBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
7.4.11.2.5.16  UninstructedBalance <UinstdBal>
Presence: [0..1]
Definition: Balance of uninstructed position.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 413 February 2026
```

