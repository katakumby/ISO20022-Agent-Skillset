---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.10 AccountDetails <AcctDtls>", "8.4.10.5 Balance <Bal>", "8.4.10.5.2 TotalEligibleBalance <TtlElgblBal>"]
file_pages: [568]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.10.5.2 TotalEligibleBalance <TtlElgblBal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 568 to 568.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 568

```text
8.4.10.5.2  TotalEligibleBalance <TtlElgblBal>
Presence: [0..1]
Definition: Total balance of securities eligible for this corporate action event. The entitlement calculation
is based on this balance.
TotalEligibleBalance <TtlElgblBal> contains the following elements (see
"TotalEligibleBalanceFormat10" on page 835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Balance <Bal> [0..1] ± 835
   FullPeriodUnits <FullPrdUnits> [0..1] ± 835
   PartWayPeriodUnits <PartWayPrdUnits> [0..1] ± 836
8.4.10.5.3  BlockedBalance <BlckdBal>
Presence: [0..1]
Definition: Balance of financial instruments that are blocked.
BlockedBalance <BlckdBal> contains one of the following elements (see "BalanceFormat11Choice"
on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
8.4.10.5.4  BorrowedBalance <BrrwdBal>
Presence: [0..1]
Definition: Balance of financial instruments that have been borrowed from another party.
BorrowedBalance <BrrwdBal> contains one of the following elements (see "BalanceFormat11Choice"
on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
8.4.10.5.5  CollateralInBalance <CollInBal>
Presence: [0..1]
Definition: Balance of securities that belong to a third party and that are held for the purpose of
collateralisation.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 568 February 2026
```

