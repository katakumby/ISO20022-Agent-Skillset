---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.18 TransactionDetails <TxDtls>", "4.4.3.4.18.7 SafekeepingPlace <SfkpgPlc>"]
file_pages: [152]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.18.7 SafekeepingPlace <SfkpgPlc>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 152 to 152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 152

```text
Definition: Market in which a trade transaction has been executed.
PlaceOfTrade <PlcOfTrad> contains the following elements (see "PlaceOfTradeIdentification1" on
page 357 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketTypeAndIdentification <MktTpAndId> [0..1] ± C17 357
   LEI <LEI> [0..1] IdentifierSet 358
4.4.3.4.18.7  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Impacted by: C31 "SafekeepingPlaceFormatOrLEIRule"
SafekeepingPlace <SfkpgPlc> contains the following elements (see "SafeKeepingPlace3" on
page 453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceFormat <SfkpgPlcFrmt> [0..1] ± 453
   LEI <LEI> [0..1] IdentifierSet 453
Constraints
• SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
Following Must be True
    /SafekeepingPlaceFormat Must be present
 Or    /LEI Must be present
4.4.3.4.18.8  PlaceOfClearing <PlcOfClr>
Presence: [0..1]
Definition: Infrastructure which may be a component of a clearing house and which facilitates clearing
and settlement for its members by standing between the buyer and the seller. It may net transactions
and it substitutes itself as settlement counterparty for each position.
PlaceOfClearing <PlcOfClr> contains the following elements (see "PlaceOfClearingIdentification2" on
page 315 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] IdentifierSet C2 315
   LEI <LEI> [0..1] IdentifierSet 315
4.4.3.4.18.9  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 152 March 2026
```

