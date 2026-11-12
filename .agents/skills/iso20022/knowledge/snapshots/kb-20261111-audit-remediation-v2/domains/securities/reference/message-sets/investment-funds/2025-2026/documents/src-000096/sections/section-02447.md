---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.43 LateReport <LateRpt>"]
file_pages: [3424]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.43 LateReport <LateRpt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3424 to 3424.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3424

```text
52.4.5.10.43  LateReport <LateRpt>
Presence: [0..1]
Definition: Specifies whether the order execution confirmation is late.
Datatype: "LateReport1Code" on page 5328
CodeName Name Definition
LAT1 Late The confirmation is late.
LAT2 LateBecausePartial The confirmation is late because the
trade was executed as a number of
partials.
52.4.5.10.44  RelatedPartyDetails <RltdPtyDtls>
Presence: [0..10]
Definition: Party related to the transaction.
Impacted by: C27 "OrderOriginatorEligibility1Rule"
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
52.4.5.10.45  Equalisation <Equlstn>
Presence: [0..1]
Definition: Part of an investor's subscription amount that is held by the fund in order to pay incentive/
performance fees at the end of the fiscal year.
Impacted by: C9 "ContingentLiquidationMethodologyTypeRule", C15
"DepreciationDepositMethodologyTypeRule", C20 "EqualisationCreditMethodologyTypeRule"
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3424 May 2026
```

