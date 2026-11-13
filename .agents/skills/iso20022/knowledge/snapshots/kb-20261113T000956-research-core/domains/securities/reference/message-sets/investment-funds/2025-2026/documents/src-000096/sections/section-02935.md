---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.24 NegotiatedTrade <NgtdTrad>"]
file_pages: [4106]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.24 NegotiatedTrade <NgtdTrad>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4106 to 4106.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4106

```text
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
55.4.5.24  NegotiatedTrade <NgtdTrad>
Presence: [0..1]
Definition: Specifies whether the trade is negotiated.
Datatype: "NegotiatedTrade1Code" on page 5331
CodeName Name Definition
NEGO Negotiated Trade is negotiated.
NNGO NotNegotiated Trade is not negotiated.
UNKW Unknown Whether the trade is negotiated or not is
unknown.
55.4.5.25  LateReport <LateRpt>
Presence: [0..1]
Definition: Specifies whether the order execution confirmation is late.
Datatype: "LateReport1Code" on page 5328
CodeName Name Definition
LAT1 Late The confirmation is late.
LAT2 LateBecausePartial The confirmation is late because the
trade was executed as a number of
partials.
55.4.5.26  CustomerConductClassification <CstmrCndctClssfctn>
Presence: [0..1]
Definition: Assessment of the customer's behaviour at the time of the account opening application.
CustomerConductClassification <CstmrCndctClssfctn> contains one of the following elements (see
"CustomerConductClassification1Choice" on page 4663 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4663
Or}   Proprietary <Prtry> [1..1] ± 4664
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4106 May 2026
```

