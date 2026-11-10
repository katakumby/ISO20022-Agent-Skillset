---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.12 Financial Instrument", "7.1.12.1 FinancialInstrumentAttributes138", "7.1.12.1.17 PutableDate <PutblDt>"]
file_pages: [331]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.12.1.17 PutableDate <PutblDt>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 331 to 331.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 331

```text
7.1.12.1.17  PutableDate <PutblDt>
Presence: [0..1]
Definition: Date at which the holder has the right to ask for redemption of the security prior to final
maturity.
Datatype: "ISODate" on page 550
7.1.12.1.18  DatedDate <DtdDt>
Presence: [0..1]
Definition: First date at which a security begins to accrue interest.
Datatype: "ISODate" on page 550
7.1.12.1.19  FirstPaymentDate <FrstPmtDt>
Presence: [0..1]
Definition: Date at which the first interest payment is due to holders of the security.
Datatype: "ISODate" on page 550
7.1.12.1.20  PreviousFactor <PrvsFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 that was applicable before the current factor
and defines the outstanding principal of the financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 554
7.1.12.1.21  CurrentFactor <CurFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 defining the outstanding principal of the
financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 554
7.1.12.1.22  NextFactor <NxtFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 that will be applicable as of the next factor
date and defines the outstanding principal of the financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 554
7.1.12.1.23  InterestRate <IntrstRate>
Presence: [0..1]
Definition: Per annum ratio of interest paid to the principal amount of the financial instrument for a
specific period of time.
Datatype: "PercentageRate" on page 555
7.1.12.1.24  YieldToMaturityRate <YldToMtrtyRate>
Presence: [0..1]
Definition: Rate of return anticipated on a bond when held until maturity date.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 331 March 2026
```

