---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.20 Settlement Chain"]
file_pages: [265]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.20 Settlement Chain

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 265 to 265.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 265

```text
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 313
9.1.20 Settlement Chain
9.1.20.1  SettlementParties78
Definition: Chain of parties involved in the settlement of a transaction, including receipts and deliveries,
book transfers, treasury deals, or other activities, resulting in the movement of a security or amount of
money from one account to another.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 266
   Party1 <Pty1> [0..1] ± 266
   Party2 <Pty2> [0..1] ± 266
   Party3 <Pty3> [0..1] ± 267
   Party4 <Pty4> [0..1] ± 267
   Party5 <Pty5> [0..1] ± 267
Constraints
• Party2PresenceRule
If Party2 is present, then Party1 must be present.
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
• Party3PresenceRule
If Party3 is present, then Party2 must be present.
On Condition
    /Party3 is present
Following Must be True
    /Party2 Must be present
• Party4PresenceRule
If Party4 is present, then Party3 must be present.
On Condition
    /Party4 is present
Following Must be True
    /Party3 Must be present
• Party5PresenceRule
If Party5 is present, then Party4 must be present.
On Condition
    /Party5 is present
Following Must be True
    /Party4 Must be present
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 265 September 2025
```

