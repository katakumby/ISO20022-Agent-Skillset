---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.44 Equalisation <Equlstn>"]
file_pages: [2467]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.44 Equalisation <Equlstn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2467 to 2467.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2467

```text
RelatedPartyDetails <RltdPtyDtls> contains the following elements (see "Intermediary49" on
page 5031 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5032
   Account <Acct> [0..1]  5032
     Identification <Id> [1..1] Text 5032
     AccountServicer <AcctSvcr> [0..1] ± 5032
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 5033
   TradingPartyCapacity <TradgPtyCpcty> [0..1] CodeSet 5033
   Role <Role> [0..1] ± 5033
Constraints
• OrderOriginatorEligibility1Rule
OrderOriginatorEligibility may only be present if Role is either UCL1 (UnderlyingClient1) or UCL2
(UnderlyingClient2).
46.4.5.10.44  Equalisation <Equlstn>
Presence: [0..1]
Definition: Part of an investor's subscription amount that was held by the fund in order to pay incentive/
performance fees at the end of the fiscal year, and is returned due to the redemption.
Impacted by: C35 "RedemptionEqualisationMethodologyTypes1Rule", C36
"RedemptionEqualisationMethodologyTypes2Rule"
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2467 May 2026
```

