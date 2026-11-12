---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.10 AccountDetails <AcctDtls>", "8.4.10.5 Balance <Bal>", "8.4.10.5.6 CollateralOutBalance <CollOutBal>"]
file_pages: [569]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.10.5.6 CollateralOutBalance <CollOutBal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 569 to 569.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 569

```text
CollateralInBalance <CollInBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
8.4.10.5.6  CollateralOutBalance <CollOutBal>
Presence: [0..1]
Definition: Balance of securities that belong to the safekeeping account indicated within this message,
and are deposited with a third party for the purpose of collateralisation.
CollateralOutBalance <CollOutBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
8.4.10.5.7  OnLoanBalance <OnLnBal>
Presence: [0..1]
Definition: Balance of financial instruments that have been loaned to a third party.
OnLoanBalance <OnLnBal> contains one of the following elements (see "BalanceFormat11Choice"
on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
8.4.10.5.8  PendingDeliveryBalance <PdgDlvryBal>
Presence: [0..*]
Definition: Balance of financial instruments that are pending delivery.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 569 February 2026
```

