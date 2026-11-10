---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.6 CouponAttachedNumber <CpnAttchdNb>"]
file_pages: [333]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.6 CouponAttachedNumber <CpnAttchdNb>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 333 to 333.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 333

```text
13.1.6.3.6  CouponAttachedNumber <CpnAttchdNb>
Presence: [0..1]
Definition: Number of the coupon attached to the physical security.
Datatype: "Max3NumericText" on page 534
13.1.6.3.7  TaxLotNumber <TaxLotNb>
Presence: [0..1]
Definition: Identification, for tax purposes, of a lot of identical securities that are bought at a certain date
and at a certain price.
Datatype: "Max15NumericText" on page 533
13.1.6.3.8  PoolNumber <PoolNb>
Presence: [0..1]
Definition: Number identifying a group of underlying assets assigned by the issuer of a factored
security.
Datatype: "Max15NumericText" on page 533
13.1.6.3.9  CoveredIndicator <CvrdInd>
Presence: [0..1]
Definition: Indicates whether the derivative product is covered or not by an underlying financial
instrument position.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.6.3.10  LegalRestrictions <LglRstrctns>
Presence: [0..1]
Definition: Specifies the regulatory restrictions applicable to a security.
LegalRestrictions <LglRstrctns> contains one of the following LegalRestrictions4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 333
Or}   Proprietary <Prtry> [1..1] ± 334
13.1.6.3.10.1  Code <Cd>
Presence: [1..1]
Definition: Legal restrictions expressed as an ISO 20022 code.
Datatype: "LegalRestrictions1Code" on page 518
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 333 March 2024
```

