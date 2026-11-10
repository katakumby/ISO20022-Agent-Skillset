---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.10 AccountDetails <AcctDtls>", "8.4.10.5 Balance <Bal>", "8.4.10.5.12 StreetPositionBalance <StrtPosBal>"]
file_pages: [571]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.10.5.12 StreetPositionBalance <StrtPosBal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 571 to 571.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 571

```text
SettlementPositionBalance <SttlmPosBal> contains one of the following elements (see
"BalanceFormat12Choice" on page 832 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 832
Or   EligibleBalance <ElgblBal> [1..1] ± 832
Or   NotEligibleBalance <NotElgblBal> [1..1] ± 833
Or   FullPeriodUnits <FullPrdUnits> [1..1] ± 833
Or}   PartWayPeriodUnits <PartWayPrdUnits> [1..1] ± 833
8.4.10.5.12  StreetPositionBalance <StrtPosBal>
Presence: [0..1]
Definition: Balance of financial instruments that remain registered in the name of the prior beneficial
owner.
StreetPositionBalance <StrtPosBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
8.4.10.5.13  TradeDatePositionBalance <TradDtPosBal>
Presence: [0..1]
Definition: Balance of securities based on trade date, for example, includes all pending transactions in
addition to the balance of settled transactions.
TradeDatePositionBalance <TradDtPosBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
8.4.10.5.14  InTransshipmentBalance <InTrnsShipmntBal>
Presence: [0..1]
Definition: Balance of physical securities that are in the process of being transferred from one
depository/agent to another.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 571 February 2026
```

