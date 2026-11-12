---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.18 DateDetails <DtDtls>", "7.4.13.18.7 SubscriptionCostDebitDate <SbcptCostDbtDt>"]
file_pages: [440]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.18.7 SubscriptionCostDebitDate <SbcptCostDbtDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 440 to 440.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 440

```text
7.4.13.18.7  SubscriptionCostDebitDate <SbcptCostDbtDt>
Presence: [0..1]
Definition: Date/time by which cash must be in place in order to take part in the event.
SubscriptionCostDebitDate <SbcptCostDbtDt> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
7.4.13.18.8  DepositoryCoverExpirationDate <DpstryCoverXprtnDt>
Presence: [0..1]
Definition: Last day that a participant of the depository can deliver securities that it had elected on
and/or previously protected.
DepositoryCoverExpirationDate <DpstryCoverXprtnDt> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
7.4.13.18.9  StockLendingDeadline <StockLndgDdln>
Presence: [0..1]
Definition: Date/time set as the deadline to respond, with instructions, to an outstanding event, for which
the underlying security is out on loan.
StockLendingDeadline <StockLndgDdln> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 440 February 2026
```

