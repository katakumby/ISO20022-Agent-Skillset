---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.26 FinancialAdvice <FinAdvc>"]
file_pages: [3178]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.26 FinancialAdvice <FinAdvc>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3178 to 3178.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3178

```text
StaffClientBreakdown <StffClntBrkdwn> contains the following elements (see
"InvestmentFundsOrderBreakdown2" on page 4733 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderBreakdownType <OrdrBrkdwnTp> [1..1]  4733
{Or     Code <Cd> [1..1] CodeSet 4733
Or}     Proprietary <Prtry> [1..1] ± 4733
   Amount <Amt> [1..1] Amount C1, C13 4734
50.4.4.9.26  FinancialAdvice <FinAdvc>
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
50.4.4.9.27  NegotiatedTrade <NgtdTrad>
Presence: [0..1]
Definition: Specifies whether the trade is negotiated.
Datatype: "NegotiatedTrade1Code" on page 5331
CodeName Name Definition
NEGO Negotiated Trade is negotiated.
NNGO NotNegotiated Trade is not negotiated.
UNKW Unknown Whether the trade is negotiated or not is
unknown.
50.4.4.9.28  RelatedPartyDetails <RltdPtyDtls>
Presence: [0..10]
Definition: Party related to the transaction.
Impacted by: C24 "OrderOriginatorEligibility1Rule"
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3178 May 2026
```

