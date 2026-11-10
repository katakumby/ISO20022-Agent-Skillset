---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.1 AdditionalBalanceBreakdown1", "82.1.5.1.4 QuantityBreakdown <QtyBrkdwn>"]
file_pages: [2847]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.1.4 QuantityBreakdown <QtyBrkdwn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2847 to 2847.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2847

```text
82.1.5.1.4  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of the aggregate quantity reported into significant lots, for example, tax lots.
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown54" on
page 3111 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 3111
   LotQuantity <LotQty> [0..1] ± 3111
   LotDateTime <LotDtTm> [0..1] ± 3111
   LotPrice <LotPric> [0..1] ± 3112
   TypeOfPrice <TpOfPric> [0..1] ± 3112
82.1.5.2  BalanceQuantity9Choice
Definition: Choice between quantity formats for the balance information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 2847
Or}   Proprietary <Prtry> [1..1] ± 2847
82.1.5.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
Quantity <Qty> contains one of the following elements (see "Quantity6Choice" on page 2954 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 2954
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 2954
82.1.5.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2847 August 2026
```

