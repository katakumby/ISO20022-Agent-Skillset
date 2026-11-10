---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.7 AccountDetails <AcctDtls>", "5.4.7.5 Balance <Bal>", "5.4.7.5.7 PendingDeliveryBalance <PdgDlvryBal>"]
file_pages: [298]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.7.5.7 PendingDeliveryBalance <PdgDlvryBal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 298 to 298.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 298

```text
OnLoanBalance <OnLnBal> contains one of the following elements (see "BalanceFormat11Choice"
on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
5.4.7.5.7  PendingDeliveryBalance <PdgDlvryBal>
Presence: [0..*]
Definition: Balance of financial instruments that are pending delivery.
PendingDeliveryBalance <PdgDlvryBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
5.4.7.5.8  PendingReceiptBalance <PdgRctBal>
Presence: [0..*]
Definition: Balance of financial instruments that are pending receipt.
PendingReceiptBalance <PdgRctBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
5.4.7.5.9  OutForRegistrationBalance <OutForRegnBal>
Presence: [0..1]
Definition: Balance of financial instruments currently being processed by the institution responsible for
registering the new beneficial owner (or nominee).
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 298 February 2026
```

