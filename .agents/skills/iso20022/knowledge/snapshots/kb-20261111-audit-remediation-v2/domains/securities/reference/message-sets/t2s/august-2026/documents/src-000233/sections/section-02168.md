---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.13 Financial Instrument", "82.1.13.1 FinancialInstrumentAttributes138", "82.1.13.1.25 NextInterestRate <NxtIntrstRate>"]
file_pages: [2930]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.13.1.25 NextInterestRate <NxtIntrstRate>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2930 to 2930.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2930

```text
Datatype: "PercentageRate" on page 3325
82.1.13.1.25  NextInterestRate <NxtIntrstRate>
Presence: [0..1]
Definition: Interest rate applicable to the next interest payment period in relation to variable rate
instruments.
Datatype: "PercentageRate" on page 3325
82.1.13.1.26  IndexRateBasis <IndxRateBsis>
Presence: [0..1]
Definition: Specifies the reference rate for fixed income instruments where the
price of the instrument is indexed to the price of an underlying benchmark.
Datatype: "PercentageRate" on page 3325
82.1.13.1.27  CouponAttachedNumber <CpnAttchdNb>
Presence: [0..1]
Definition: Number of the coupon attached to the physical security.
CouponAttachedNumber <CpnAttchdNb> contains one of the following elements (see
"Number22Choice" on page 3031 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 3031
Or}   Long <Lng> [1..1] ± 3031
82.1.13.1.28  PoolNumber <PoolNb>
Presence: [0..1]
Definition: Number identifying a group of underlying assets assigned by the issuer of a factored
security.
PoolNumber <PoolNb> contains the following elements (see "GenericIdentification37" on page 2965
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
82.1.13.1.29  VariableRateIndicator <VarblRateInd>
Presence: [0..1]
Definition: Indicates whether the interest rate of an interest bearing instrument is reset periodically.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2930 August 2026
```

