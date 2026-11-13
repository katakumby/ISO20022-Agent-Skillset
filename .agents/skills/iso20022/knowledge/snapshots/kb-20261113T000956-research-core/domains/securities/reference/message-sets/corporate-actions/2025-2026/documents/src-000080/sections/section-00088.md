---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.7 BidRangeType <BidRgTp>"]
file_pages: [143]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.7 BidRangeType <BidRgTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 143 to 143.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 143

```text
CertificationBreakdownType <CertfctnBrkdwnTp> contains one of the following elements (see
"BeneficiaryCertificationType13Choice" on page 999 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 999
Or}   Proprietary <Prtry> [1..1] ± 1000
3.4.11.7  BidRangeType <BidRgTp>
Presence: [0..1]
Definition: Specifies the type of acceptable bid range values.
BidRangeType <BidRgTp> contains one of the following elements (see "BidRangeType1Choice" on
page 918 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 918
Or}   Proprietary <Prtry> [1..1] ± 919
3.4.11.8  ProrationBelowMinimumQuantity <PrratnBlwMinQty>
Presence: [0..1]
Definition: Specifies how instructions prorated below the minimum quantity to instruct will be processed.
ProrationBelowMinimumQuantity <PrratnBlwMinQty> contains one of the following
ProrationBelowMinimumQuantity3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 143
Or}   Proprietary <Prtry> [1..1] ± 144
3.4.11.8.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of proration below minimum quantity.
Datatype: "ProrationBelowMinimumQuantity2Code" on page 1232
CodeName Name Definition
FULL AcceptedInFull Instructions will be accepted in full (with
their original quantity of securities
instructed).
MIEX MinimumQuantity Instructions will be accepted but prorated
to the minimum quantity to instruct.
REJT Rejected Instructions will be rejected.
MILD RoundDown Instructions will be accepted but rounded
down to the specified minimum multiple
quantity to instruct.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 143 February 2026
```

