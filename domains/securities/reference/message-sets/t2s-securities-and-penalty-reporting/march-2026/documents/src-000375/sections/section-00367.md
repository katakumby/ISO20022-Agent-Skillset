---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.25 Securities Quantity"]
file_pages: [454]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.25 Securities Quantity

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 454 to 454.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 454

```text
7.1.25 Securities Quantity
7.1.25.1  OriginalAndCurrentQuantities1
Definition: Original and current value of an asset-back instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FaceAmount <FaceAmt> [1..1] Amount 454
   AmortisedValue <AmtsdVal> [1..1] Amount 454
7.1.25.1.1  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is, the principal of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 491
7.1.25.1.2  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 491
7.1.26 Settlement Chain
7.1.26.1  SettlementParties78
Definition: Chain of parties involved in the settlement of a transaction, including receipts and deliveries,
book transfers, treasury deals, or other activities, resulting in the movement of a security or amount of
money from one account to another.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 455
   Party1 <Pty1> [0..1] ± 455
   Party2 <Pty2> [0..1] ± 456
   Party3 <Pty3> [0..1] ± 456
   Party4 <Pty4> [0..1] ± 456
   Party5 <Pty5> [0..1] ± 457
Constraints
• Party2PresenceRule
If Party2 is present, then Party1 must be present.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 454 March 2026
```

