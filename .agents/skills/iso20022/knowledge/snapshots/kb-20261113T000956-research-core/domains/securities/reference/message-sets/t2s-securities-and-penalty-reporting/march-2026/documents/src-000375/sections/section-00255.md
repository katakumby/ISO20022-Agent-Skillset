---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.12 Financial Instrument", "7.1.12.1 FinancialInstrumentAttributes138", "7.1.12.1.25 NextInterestRate <NxtIntrstRate>"]
file_pages: [332]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.12.1.25 NextInterestRate <NxtIntrstRate>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 332 to 332.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 332

```text
Datatype: "PercentageRate" on page 555
7.1.12.1.25  NextInterestRate <NxtIntrstRate>
Presence: [0..1]
Definition: Interest rate applicable to the next interest payment period in relation to variable rate
instruments.
Datatype: "PercentageRate" on page 555
7.1.12.1.26  IndexRateBasis <IndxRateBsis>
Presence: [0..1]
Definition: Specifies the reference rate for fixed income instruments where the
price of the instrument is indexed to the price of an underlying benchmark.
Datatype: "PercentageRate" on page 555
7.1.12.1.27  CouponAttachedNumber <CpnAttchdNb>
Presence: [0..1]
Definition: Number of the coupon attached to the physical security.
CouponAttachedNumber <CpnAttchdNb> contains one of the following elements (see
"Number22Choice" on page 390 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 391
Or}   Long <Lng> [1..1] ± 391
7.1.12.1.28  PoolNumber <PoolNb>
Presence: [0..1]
Definition: Number identifying a group of underlying assets assigned by the issuer of a factored
security.
PoolNumber <PoolNb> contains the following elements (see "GenericIdentification37" on page 351 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 351
   Issuer <Issr> [0..1] Text 351
7.1.12.1.29  VariableRateIndicator <VarblRateInd>
Presence: [0..1]
Definition: Indicates whether the interest rate of an interest bearing instrument is reset periodically.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 332 March 2026
```

