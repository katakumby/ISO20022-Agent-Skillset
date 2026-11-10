---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.4 AdditionalBalanceInformation18", "82.1.5.4.2 Quantity <Qty>"]
file_pages: [2851]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.4.2 Quantity <Qty>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2851 to 2851.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2851

```text
SubBalanceType <SubBalTp> contains one of the following elements (see
"SubBalanceType12Choice" on page 2853 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2853
Or}   Proprietary <Prtry> [1..1] ± 2854
82.1.5.4.2  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Quantity <Qty> contains the following elements (see "Balance9" on page 2860 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 2860
   Quantity <Qty> [1..1] ± 2861
82.1.5.4.3  SubBalanceAdditionalDetails <SubBalAddtlDtls>
Presence: [0..1]
Definition: Provides additional sub-balance information.
Datatype: "Max140Text" on page 3326
82.1.5.4.4  QuantityBreakdown <QtyBrkdwn>
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
82.1.5.5  SecuritiesBalanceType7Choice
Definition: Choice of format for the balance type.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2851 August 2026
```

