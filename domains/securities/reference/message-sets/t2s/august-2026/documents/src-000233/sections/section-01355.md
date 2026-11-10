---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.4 CertificateNumber <CertNb>"]
file_pages: [1964]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.4 CertificateNumber <CertNb>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1964 to 1964.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1964

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
32.4.3.1.1.3.4  CertificateNumber <CertNb>
Presence: [0..1]
Definition: Unique and unambiguous identifier of a certificate assigned by the issuer.
Datatype: "Max35Text" on page 3328
32.4.3.1.1.3.5  ContractVersionNumber <CtrctVrsnNb>
Presence: [0..1]
Definition: Version number assigned to the contract associated with the security.
Datatype: "Number" on page 3324
32.4.3.1.1.3.6  CouponAttachedNumber <CpnAttchdNb>
Presence: [0..1]
Definition: Number of the coupon attached to the physical security.
Datatype: "Max3NumericText" on page 3328
32.4.3.1.1.3.7  TaxLotNumber <TaxLotNb>
Presence: [0..1]
Definition: Identification, for tax purposes, of a lot of identical securities that are bought at a certain date
and at a certain price.
Datatype: "Max15NumericText" on page 3326
32.4.3.1.1.3.8  PoolNumber <PoolNb>
Presence: [0..1]
Definition: Number identifying a group of underlying assets assigned by the issuer of a factored
security.
Datatype: "Max15NumericText" on page 3326
32.4.3.1.1.3.9  CoveredIndicator <CvrdInd>
Presence: [0..1]
Definition: Indicates whether the derivative product is covered or not by an underlying financial
instrument position.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
32.4.3.1.1.3.10  LegalRestrictions <LglRstrctns>
Presence: [0..1]
Definition: Specifies the regulatory restrictions applicable to a security.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1964 August 2026
```

