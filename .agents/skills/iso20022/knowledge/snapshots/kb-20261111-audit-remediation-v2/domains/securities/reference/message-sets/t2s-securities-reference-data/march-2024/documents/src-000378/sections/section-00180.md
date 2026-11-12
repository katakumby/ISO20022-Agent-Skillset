---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.6 CertificateNumber <CertNb>"]
file_pages: [257]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.6 CertificateNumber <CertNb>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 257 to 257.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 257

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
13.1.6.2.6  CertificateNumber <CertNb>
Presence: [0..1]
Definition: Unique and unambiguous identifier of a certificate assigned by the issuer.
Datatype: "Max35Text" on page 534
13.1.6.2.7  ContractVersionNumber <CtrctVrsnNb>
Presence: [0..1]
Definition: Version number assigned to the contract associated with the security.
Datatype: "Number" on page 532
13.1.6.2.8  CouponAttachedNumber <CpnAttchdNb>
Presence: [0..1]
Definition: Number of the coupon attached to the physical security.
Datatype: "Max3NumericText" on page 534
13.1.6.2.9  TaxLotNumber <TaxLotNb>
Presence: [0..1]
Definition: Identification, for tax purposes, of a lot of identical securities that are bought at a certain date
and at a certain price.
Datatype: "Max15NumericText" on page 533
13.1.6.2.10  PoolNumber <PoolNb>
Presence: [0..1]
Definition: Number identifying a group of underlying assets assigned by the issuer of a factored
security.
Datatype: "Max15NumericText" on page 533
13.1.6.2.11  CoveredIndicator <CvrdInd>
Presence: [0..1]
Definition: Indicates whether the derivative product is covered or not by an underlying financial
instrument position.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 257 March 2024
```

