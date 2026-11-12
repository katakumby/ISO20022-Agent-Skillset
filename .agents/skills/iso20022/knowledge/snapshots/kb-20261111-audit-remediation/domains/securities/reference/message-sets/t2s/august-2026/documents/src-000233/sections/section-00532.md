---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.3 Debt <Debt>", "27.4.2.2.3.59 CouponRange <CpnRg>"]
file_pages: [698]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.3.59 CouponRange <CpnRg>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 698 to 698.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 698

```text
YieldRange <YldRg> contains the following elements (see "AmountOrPercentageRange1" on
page 3003 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Operation <Opr> [0..1] CodeSet 3003
   Term <Term> [0..10]  3003
     Operator <Oprtr> [1..1] CodeSet 3003
     Value <Val> [1..1]  3004
{Or       RateValue <RateVal> [1..1] Rate 3004
Or}       AbsoluteValue <AbsVal> [1..1] Quantity 3004
27.4.2.2.3.59  CouponRange <CpnRg>
Presence: [0..1]
Definition: Identification of a range of coupon numbers attached to its related financial instrument.
CouponRange <CpnRg> contains the following elements (see "AmountOrPercentageRange1" on
page 3003 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Operation <Opr> [0..1] CodeSet 3003
   Term <Term> [0..10]  3003
     Operator <Oprtr> [1..1] CodeSet 3003
     Value <Val> [1..1]  3004
{Or       RateValue <RateVal> [1..1] Rate 3004
Or}       AbsoluteValue <AbsVal> [1..1] Quantity 3004
27.4.2.2.3.60  Purpose <Purp>
Presence: [0..1]
Definition: Reason for which money is raised through the issuance of a security.
Datatype: "Max256Text" on page 3327
27.4.2.2.3.61  AlternativeMinimumTaxIndicator <AltrntvMinTaxInd>
Presence: [0..1]
Definition: Identifies whether the issue is subject to alternative minimum taxation (used for municipal
bonds).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 698 August 2026
```

