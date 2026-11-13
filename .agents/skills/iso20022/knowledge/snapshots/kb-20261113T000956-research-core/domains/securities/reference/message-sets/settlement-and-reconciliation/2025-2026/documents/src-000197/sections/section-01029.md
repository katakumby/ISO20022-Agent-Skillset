---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.4 FinancialInstrumentAttributes112", "35.1.11.4.25 NextInterestRate <NxtIntrstRate>"]
file_pages: [1468]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.4.25 NextInterestRate <NxtIntrstRate>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1468 to 1468.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1468

```text
Datatype: "PercentageRate" on page 2190
35.1.11.4.25  NextInterestRate <NxtIntrstRate>
Presence: [0..1]
Definition: Interest rate applicable to the next interest payment period in relation to variable rate
instruments.
Datatype: "PercentageRate" on page 2190
35.1.11.4.26  IndexRateBasis <IndxRateBsis>
Presence: [0..1]
Definition: Specifies the reference rate for fixed income instruments where the
price of the instrument is indexed to the price of an underlying benchmark.
Datatype: "PercentageRate" on page 2190
35.1.11.4.27  CouponAttachedNumber <CpnAttchdNb>
Presence: [0..1]
Definition: Number of the coupon attached to the physical security.
CouponAttachedNumber <CpnAttchdNb> contains one of the following elements (see
"Number22Choice" on page 1608 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 1608
Or}   Long <Lng> [1..1] ± 1608
35.1.11.4.28  PoolNumber <PoolNb>
Presence: [0..1]
Definition: Number identifying a group of underlying assets assigned by the issuer of a factored
security.
PoolNumber <PoolNb> contains the following elements (see "GenericIdentification37" on page 1498
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1498
   Issuer <Issr> [0..1] Text 1498
35.1.11.4.29  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of a quantity into lots such as tax lots, instrument series.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1468 March 2026
```

