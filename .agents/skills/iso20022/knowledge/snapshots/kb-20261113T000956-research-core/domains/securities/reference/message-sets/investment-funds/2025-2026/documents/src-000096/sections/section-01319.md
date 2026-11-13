---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.23 FinancialAdvice <FinAdvc>"]
file_pages: [1838]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.23 FinancialAdvice <FinAdvc>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1838 to 1838.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1838

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
41.4.4.8.23  FinancialAdvice <FinAdvc>
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
41.4.4.8.24  NegotiatedTrade <NgtdTrad>
Presence: [0..1]
Definition: Specifies whether the trade is negotiated.
Datatype: "NegotiatedTrade1Code" on page 5331
CodeName Name Definition
NEGO Negotiated Trade is negotiated.
NNGO NotNegotiated Trade is not negotiated.
UNKW Unknown Whether the trade is negotiated or not is
unknown.
41.4.4.8.25  RelatedPartyDetails <RltdPtyDtls>
Presence: [0..10]
Definition: Party related to the transaction.
Impacted by: C24 "OrderOriginatorEligibility1Rule"
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1838 May 2026
```

