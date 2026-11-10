---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.38 FinancialAdvice <FinAdvc>"]
file_pages: [2937]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.38 FinancialAdvice <FinAdvc>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2937 to 2937.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2937

```text
Datatype: "PercentageRate" on page 5401
49.4.5.9.38  FinancialAdvice <FinAdvc>
Presence: [0..1]
Definition: Specifies if advice has been received from an independent financial advisor.
Datatype: "FinancialAdvice1Code" on page 5302
CodeName Name Definition
RECE Received Advice has been received from an
independent financial advisor.
NREC NotReceived Advice has not been received from an
independent financial advisor.
UKWN Unknown It is not known whether or not advice has
been received from an independent
financial advisor.
49.4.5.9.39  NegotiatedTrade <NgtdTrad>
Presence: [0..1]
Definition: Specifies whether the trade is negotiated.
Datatype: "NegotiatedTrade1Code" on page 5331
CodeName Name Definition
NEGO Negotiated Trade is negotiated.
NNGO NotNegotiated Trade is not negotiated.
UNKW Unknown Whether the trade is negotiated or not is
unknown.
49.4.5.9.40  LateReport <LateRpt>
Presence: [0..1]
Definition: Specifies whether the order execution confirmation is late.
Datatype: "LateReport1Code" on page 5328
CodeName Name Definition
LAT1 Late The confirmation is late.
LAT2 LateBecausePartial The confirmation is late because the
trade was executed as a number of
partials.
49.4.5.9.41  PartialSettlementOfCash <PrtlSttlmOfCsh>
Presence: [0..1]
Definition: Percentage of cash partially settled.
Datatype: "PercentageRate" on page 5401
49.4.5.9.42  RelatedPartyDetails <RltdPtyDtls>
Presence: [0..10]
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2937 May 2026
```

