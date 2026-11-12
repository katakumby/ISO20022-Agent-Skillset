---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.1 OrderReference <OrdrRef>"]
file_pages: [3304]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.1 OrderReference <OrdrRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3304 to 3304.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3304

```text
• PhysicalDeliveryDetails2Rule
If PhysicalDeliveryIndicator is "true" or "1" (Yes), then PhysicalDeliveryDetails must be present.
On Condition
    /PhysicalDeliveryIndicator is equal to value 'true'
 Or    /PhysicalDeliveryIndicator is equal to value '1'
Following Must be True
    /PhysicalDeliveryDetails Must be present
• PriceDifferenceReasonRule
Any occurrence of InformativePriceDetails/PriceDifferenceReason may not be present.
• RequestedSettlementCurrencyRule
If RequestedSettlementCurrency is present, it must be the same Currency as in SettlementAmount, if
present.
On Condition
    /RequestedSettlementCurrency is present
 And    /SettlementAmount is present
Following Must be True
    /RequestedSettlementCurrency Must be equal to /SettlementAmount/
attribute::Currency
52.4.5.10.1  OrderReference <OrdrRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the order, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
52.4.5.10.2  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the order. This reference can typically be
used in a hub scenario to give the reference of the order as assigned by the underlying client.
Datatype: "Max35Text" on page 5403
52.4.5.10.3  DealReference <DealRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the order execution, as assigned by the confirming
party.
Datatype: "Max35Text" on page 5403
52.4.5.10.4  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 5403
52.4.5.10.5  OrderType <OrdrTp>
Presence: [0..10]
Definition: Category of the investment fund order.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3304 May 2026
```

