---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.3.1.3 Debt <Debt>", "28.4.2.1.3.1.3.59 CouponRange <CpnRg>"]
file_pages: [1434]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.1.3.59 CouponRange <CpnRg>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1434 to 1434.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1434

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
28.4.2.1.3.1.3.59  CouponRange <CpnRg>
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
28.4.2.1.3.1.3.60  Purpose <Purp>
Presence: [0..1]
Definition: Reason for which money is raised through the issuance of a security.
Datatype: "Max256Text" on page 3327
28.4.2.1.3.1.3.61  AlternativeMinimumTaxIndicator <AltrntvMinTaxInd>
Presence: [0..1]
Definition: Identifies whether the issue is subject to alternative minimum taxation (used for municipal
bonds).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1434 August 2026
```

