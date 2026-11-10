---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.41 NegotiatedTrade <NgtdTrad>"]
file_pages: [2466]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.41 NegotiatedTrade <NgtdTrad>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2466 to 2466.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2466

```text
CodeName Name Definition
RECE Received Advice has been received from an
independent financial advisor.
NREC NotReceived Advice has not been received from an
independent financial advisor.
UKWN Unknown It is not known whether or not advice has
been received from an independent
financial advisor.
46.4.5.10.41  NegotiatedTrade <NgtdTrad>
Presence: [0..1]
Definition: Specifies whether the trade is negotiated.
Datatype: "NegotiatedTrade1Code" on page 5331
CodeName Name Definition
NEGO Negotiated Trade is negotiated.
NNGO NotNegotiated Trade is not negotiated.
UNKW Unknown Whether the trade is negotiated or not is
unknown.
46.4.5.10.42  LateReport <LateRpt>
Presence: [0..1]
Definition: Specifies whether the order execution confirmation is late.
Datatype: "LateReport1Code" on page 5328
CodeName Name Definition
LAT1 Late The confirmation is late.
LAT2 LateBecausePartial The confirmation is late because the
trade was executed as a number of
partials.
46.4.5.10.43  RelatedPartyDetails <RltdPtyDtls>
Presence: [0..10]
Definition: Party related to the transaction.
Impacted by: C24 "OrderOriginatorEligibility1Rule"
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2466 May 2026
```

