---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.43 Equalisation <Equlstn>"]
file_pages: [2938]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.43 Equalisation <Equlstn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2938 to 2938.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2938

```text
Definition: Party related to the transaction.
Impacted by: C24 "OrderOriginatorEligibility1Rule"
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
49.4.5.9.43  Equalisation <Equlstn>
Presence: [0..1]
Definition: Part of an investor's subscription amount that is held by the fund in order to pay incentive /
performance fees at the end of the fiscal year.
Equalisation <Equlstn> contains the following elements (see "Equalisation1" on page 4775 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C2, C10 4775
   Rate <Rate> [0..1] Rate 4776
49.4.5.9.44  SourceOfCash <SrcOfCsh>
Presence: [0..*]
Definition: Source of cash used for the settlement of the subscription.
SourceOfCash <SrcOfCsh> contains one of the following elements (see "SourceOfCash1Choice" on
page 5045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5045
Or}   Proprietary <Prtry> [1..1] ± 5046
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2938 May 2026
```

