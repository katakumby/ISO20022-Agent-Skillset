---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.9 Financial Instrument", "9.1.9.2 FinancialInstrumentAttributes92", "9.1.9.2.17 PutableDate <PutblDt>"]
file_pages: [215]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.9.2.17 PutableDate <PutblDt>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 215 to 215.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 215

```text
9.1.9.2.17  PutableDate <PutblDt>
Presence: [0..1]
Definition: Date at which the holder has the right to ask for redemption of the security prior to final
maturity.
Datatype: "ISODate" on page 340
9.1.9.2.18  DatedDate <DtdDt>
Presence: [0..1]
Definition: First date at which a security begins to accrue interest.
Datatype: "ISODate" on page 340
9.1.9.2.19  FirstPaymentDate <FrstPmtDt>
Presence: [0..1]
Definition: Date at which the first interest payment is due to holders of the security.
Datatype: "ISODate" on page 340
9.1.9.2.20  PreviousFactor <PrvsFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 that was applicable before the current factor
and defines the outstanding principal of the financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 343
9.1.9.2.21  CurrentFactor <CurFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 defining the outstanding principal of the
financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 343
9.1.9.2.22  NextFactor <NxtFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 that will be applicable as of the next factor
date and defines the outstanding principal of the financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 343
9.1.9.2.23  InterestRate <IntrstRate>
Presence: [0..1]
Definition: Per annum ratio of interest paid to the principal amount of the financial instrument for a
specific period of time.
Datatype: "PercentageRate" on page 343
9.1.9.2.24  YieldToMaturityRate <YldToMtrtyRate>
Presence: [0..1]
Definition: Rate of return anticipated on a bond when held until maturity date.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 215 September 2025
```

