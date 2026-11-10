---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.13 Financial Instrument", "82.1.13.1 FinancialInstrumentAttributes138", "82.1.13.1.17 PutableDate <PutblDt>"]
file_pages: [2929]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.13.1.17 PutableDate <PutblDt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2929 to 2929.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2929

```text
82.1.13.1.17  PutableDate <PutblDt>
Presence: [0..1]
Definition: Date at which the holder has the right to ask for redemption of the security prior to final
maturity.
Datatype: "ISODate" on page 3319
82.1.13.1.18  DatedDate <DtdDt>
Presence: [0..1]
Definition: First date at which a security begins to accrue interest.
Datatype: "ISODate" on page 3319
82.1.13.1.19  FirstPaymentDate <FrstPmtDt>
Presence: [0..1]
Definition: Date at which the first interest payment is due to holders of the security.
Datatype: "ISODate" on page 3319
82.1.13.1.20  PreviousFactor <PrvsFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 that was applicable before the current factor
and defines the outstanding principal of the financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 3324
82.1.13.1.21  CurrentFactor <CurFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 defining the outstanding principal of the
financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 3324
82.1.13.1.22  NextFactor <NxtFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 that will be applicable as of the next factor
date and defines the outstanding principal of the financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 3324
82.1.13.1.23  InterestRate <IntrstRate>
Presence: [0..1]
Definition: Per annum ratio of interest paid to the principal amount of the financial instrument for a
specific period of time.
Datatype: "PercentageRate" on page 3325
82.1.13.1.24  YieldToMaturityRate <YldToMtrtyRate>
Presence: [0..1]
Definition: Rate of return anticipated on a bond when held until maturity date.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2929 August 2026
```

