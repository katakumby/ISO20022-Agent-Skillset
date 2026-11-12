---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.8 BalanceAmounts3"]
file_pages: [2855]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.8 BalanceAmounts3

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2855 to 2855.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2855

```text
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown32" on
page 3109 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 3110
   LotQuantity <LotQty> [0..1] ± 3110
   SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 3110
82.1.5.8  BalanceAmounts3
Definition: Amounts linked to a securities balance, for example, holding value.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [0..1] ± 2855
   PreviousHoldingValue <PrvsHldgVal> [0..1] ± 2855
   BookValue <BookVal> [0..1] ± 2856
   EligibleCollateralValue <ElgblCollVal> [0..1] ± 2856
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 2856
Constraints
• EligibleCollateralValueRule
EligibleCollateralValue is only to be used in (I)CSD-participant communication or if bilaterally agreed
between the sender and receiver.
82.1.5.8.1  HoldingValue <HldgVal>
Presence: [0..1]
Definition: Value of an individual financial instrument holding within a safekeeping account.
HoldingValue <HldgVal> contains the following elements (see "AmountAndDirection6" on page 2840
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2840
   Sign <Sgn> [1..1] Indicator 2840
82.1.5.8.2  PreviousHoldingValue <PrvsHldgVal>
Presence: [0..1]
Definition: Previous value of an individual financial instrument holding within a safekeeping account.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2855 August 2026
```

