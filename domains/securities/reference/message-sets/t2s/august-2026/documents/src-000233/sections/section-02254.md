---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.42 YieldedOrValueType1Choice"]
file_pages: [3025]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.42 YieldedOrValueType1Choice

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3025 to 3025.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3025

```text
Datatype: "Max35Text" on page 3328
82.1.19.42  YieldedOrValueType1Choice
Definition: Choice of value type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 3025
Or}   ValueType <ValTp> [1..1] CodeSet 3025
82.1.19.42.1  Yielded <Yldd>
Presence: [1..1]
Definition: Indicates whether the price is expressed as a yield.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.19.42.2  ValueType <ValTp>
Presence: [1..1]
Definition: Type of value in which the price is expressed.
Datatype: "PriceValueType1Code" on page 3281
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
example, a discount price of 2.0%
equals a price of 98 when par is 100.
PREM Premium Price expressed as a number of
percentage points above par, for
example, a premium price of 2.0%
equals a price of 102 when par is 100.
PARV Par Price is the face amount.
82.1.19.43  HoldIndicator6
Definition: Specifies whether the transaction is on hold/blocked/frozen.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 3025
   Reason <Rsn> [0..*] ± 3026
82.1.19.43.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether the transaction is on hold/blocked/frozen.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3025 August 2026
```

