---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.6 FinancialInstrumentAttributes <FinInstrmAttrbts>", "3.4.6.22 NextFactorDate <NxtFctrDt>"]
file_pages: [71]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.6.22 NextFactorDate <NxtFctrDt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 71 to 71.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 71

```text
Datatype: "ISODate" on page 662
3.4.6.22  NextFactorDate <NxtFctrDt>
Presence: [0..1]
Definition: Date on which the current factor will be changed to the next factor.
Datatype: "ISODate" on page 662
3.4.6.23  PreviousFactor <PrvsFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 that was applicable before the current factor
and defines the outstanding principal of the financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 666
3.4.6.24  CurrentFactor <CurFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 defining the outstanding principal of the
financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 666
3.4.6.25  NextFactor <NxtFctr>
Presence: [0..1]
Definition: Rate expressed as a decimal between 0 and 1 that will be applicable as of the next factor
date and defines the outstanding principal of the financial instrument (for factored securities).
Datatype: "BaseOneRate" on page 666
3.4.6.26  EndFactor <EndFctr>
Presence: [0..1]
Definition: End ratio of principal outstanding to the original balance.
Datatype: "BaseOneRate" on page 666
3.4.6.27  InterestRate <IntrstRate>
Presence: [0..1]
Definition: Per annum ratio of interest paid to the principal amount of the financial instrument for a
specific period of time.
Datatype: "PercentageRate" on page 667
3.4.6.28  NextInterestRate <NxtIntrstRate>
Presence: [0..1]
Definition: Interest rate applicable to the next interest payment period in relation to variable rate
instruments.
Datatype: "PercentageRate" on page 667
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 71 February 2025
```

