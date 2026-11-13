---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.4 FinancialInstrumentAttributes112", "35.1.11.4.17 PutableDate <PutblDt>"]
file_pages: [1467]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.4.17 PutableDate <PutblDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1467 to 1467.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1467

```text
35.1.11.4.17  PutableDate <PutblDt>
Presence: [0..1]
Definition: Date at which the holder has the right to ask for redemption of the security prior to final
maturity.
Datatype: "ISODate" on page 2185
35.1.11.4.18  DatedDate <DtdDt>
Presence: [0..1]
Definition: First date at which a security begins to accrue interest.
Datatype: "ISODate" on page 2185
35.1.11.4.19  FirstPaymentDate <FrstPmtDt>
Presence: [0..1]
Definition: Date at which the first interest payment is due to holders of the security.
Datatype: "ISODate" on page 2185
35.1.11.4.20  PreviousFactor <PrvsFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 that was applicable before the current factor
and defines the outstanding principal of the financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 2189
35.1.11.4.21  CurrentFactor <CurFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 defining the outstanding principal of the
financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 2189
35.1.11.4.22  NextFactor <NxtFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 that will be applicable as of the next factor
date and defines the outstanding principal of the financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 2189
35.1.11.4.23  InterestRate <IntrstRate>
Presence: [0..1]
Definition: Per annum ratio of interest paid to the principal amount of the financial instrument for a
specific period of time.
Datatype: "PercentageRate" on page 2190
35.1.11.4.24  YieldToMaturityRate <YldToMtrtyRate>
Presence: [0..1]
Definition: Rate of return anticipated on a bond when held until maturity date.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1467 March 2026
```

