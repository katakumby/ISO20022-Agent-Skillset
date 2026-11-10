---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.1 MasterReference <MstrRef>"]
file_pages: [3039]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3039 to 3039.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3039

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Type <Tp> [0..1] ± 3239
Or}       BlockChainCashWallet <BlckChainCshWllt> [1..1]  3240
         Identification <Id> [1..1] Text 3240
         Type <Tp> [0..1] ± 3240
         Name <Nm> [0..1] Text 3240
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3241
   TotalSettlementAmount <TtlSttlmAmt> [0..1] Amount C3, C10 3241
Constraints
• BulkCashSettlementDetailsRule
Either one or more occurrences of IndividualOrderDetails/CashSettlementDetails or
BulkCashSettlementDetails may be present, but not both.
• OrderOriginatorEligibility3Rule
Either one or more occurrences of IndividualOrderDetails/RelatedPartyDetails/
OrderOriginatorEligibility or InvestmentAccountDetails/OrderOriginatorEligibility may be present, but
not both.
• SettlementCurrencyRule
If BulkCashSettlementDetails is present, then Currency in IndividualOrderDetails/SettlementAmount,
if present, must be the same in all occurrences of IndividualOrderDetails.
• TotalSettlementCurrencyRule
If TotalSettlementAmount is present, then Currency in IndividualOrderDetails/SettlementAmount, if
present, must be the same in all occurrences of IndividualOrderDetails.
50.4.4.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual orders, as assigned by the
instructing party. This identifier links the individual orders together.
Datatype: "Max35Text" on page 5403
50.4.4.2  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which the advised trade transaction was executed.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3039 May 2026
```

