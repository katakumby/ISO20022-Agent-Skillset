---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.1 AdditionalBalanceBreakdown1", "82.1.5.1.1 SubBalanceType <SubBalTp>"]
file_pages: [2846]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.1.1 SubBalanceType <SubBalTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2846 to 2846.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2846

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SubBalanceType <SubBalTp> [1..1] ± 2846
   Quantity <Qty> [1..1] ± 2846
   SubBalanceAdditionalDetails <SubBalAddtlDtls> [0..1] Text 2846
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 2847
Constraints
• EligibleForCollateralPurposesRule
If Subbalance type is EligibleForCollateralPurposes, then QuantityAndAvailability cannot be used.
On Condition
    /SubBalanceType/Code is equal to value 'EligibleForCollateralPurposes'
Following Must be True
    /Quantity/Quantity/QuantityAndAvailability Must be absent
• SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
82.1.5.1.1  SubBalanceType <SubBalTp>
Presence: [1..1]
Definition: Reason for the sub-balance.
SubBalanceType <SubBalTp> contains one of the following elements (see
"SubBalanceType12Choice" on page 2853 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2853
Or}   Proprietary <Prtry> [1..1] ± 2854
82.1.5.1.2  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Quantity <Qty> contains the following elements (see "Balance9" on page 2860 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 2860
   Quantity <Qty> [1..1] ± 2861
82.1.5.1.3  SubBalanceAdditionalDetails <SubBalAddtlDtls>
Presence: [0..1]
Definition: Provides additional sub-balance information.
Datatype: "Max140Text" on page 3326
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2846 August 2026
```

