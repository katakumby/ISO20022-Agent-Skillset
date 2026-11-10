---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.8 AccountDetails <AcctDtls>", "3.4.8.2 AccountsListAndBalanceDetails <AcctsListAndBalDtls>", "3.4.8.2.5 Balance <Bal>", "3.4.8.2.5.2 BlockedBalance <BlckdBal>"]
file_pages: [81]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.8.2.5.2 BlockedBalance <BlckdBal>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 81 to 81.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 81

```text
TotalEligibleBalance <TtlElgblBal> contains the following elements (see
"TotalEligibleBalanceFormat10" on page 835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Balance <Bal> [0..1] ± 835
   FullPeriodUnits <FullPrdUnits> [0..1] ± 835
   PartWayPeriodUnits <PartWayPrdUnits> [0..1] ± 836
3.4.8.2.5.2  BlockedBalance <BlckdBal>
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
3.4.8.2.5.3  BorrowedBalance <BrrwdBal>
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
3.4.8.2.5.4  CollateralInBalance <CollInBal>
Presence: [0..1]
Definition: Balance of securities that belong to a third party and that are held for the purpose of
collateralisation.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 81 February 2026
```

