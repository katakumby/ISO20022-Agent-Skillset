---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "52.4.5.10.28.4 SecuritiesSettlementSystemIdentification <SctiesSttlmSysId>"]
file_pages: [3344]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.28.4 SecuritiesSettlementSystemIdentification <SctiesSttlmSysId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3344 to 3344.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3344

```text
SafekeepingPlace <SfkpgPlc> contains one of the following elements (see
"SafekeepingPlaceFormat42Choice" on page 5131 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  5131
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 5131
     Identification <Id> [0..1] Text 5131
Or   Country <Ctry> [1..1] CodeSet C12 5132
Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 5132
Or   TypeAndIdentification <TpAndId> [1..1]  5132
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 5132
     Identification <Id> [1..1] IdentifierSet C4 5133
Or}   Proprietary <Prtry> [1..1] ± 5133
52.4.5.10.28.4  SecuritiesSettlementSystemIdentification <SctiesSttlmSysId>
Presence: [0..1]
Definition: Identification of a specific system or set of rules and/or processes to be applied at the
settlement place.
Datatype: "Max35Text" on page 5403
52.4.5.10.28.5  TradeTransactionCondition <TradTxCond>
Presence: [0..*]
Definition: Condition under which the order/trade is to be/was executed. This may be required for
settlement through T2S.
TradeTransactionCondition <TradTxCond> contains one of the following elements (see
"TradeTransactionCondition8Choice" on page 5254 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5254
Or}   Proprietary <Prtry> [1..1] ± 5255
52.4.5.10.28.6  SettlementTransactionCondition <SttlmTxCond>
Presence: [0..*]
Definition: Condition under which the order/trade is to be settled. This may be required for settlement
through T2S.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3344 May 2026
```

