---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks", "22.4.17 OtherBusinessParties <OthrBizPties>", "22.4.17.3 StockExchange <StockXchg>"]
file_pages: [765, 766]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4.17.3 StockExchange <StockXchg>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 765 to 766.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 765

```text
22.4.17.3  StockExchange <StockXchg>
Presence: [0..1]
Definition: Identification of the stock exchange to which transaction reporting will be done.
StockExchange <StockXchg> contains the following elements (see "PartyIdentification136" on
page 1671 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1672
   LEI <LEI> [0..1] IdentifierSet 1672
22.4.17.4  TradeRegulator <TradRgltr>
Presence: [0..1]
Definition: Institution to which a trade must be reported.
TradeRegulator <TradRgltr> contains the following elements (see "PartyIdentification136" on
page 1671 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1672
   LEI <LEI> [0..1] IdentifierSet 1672
22.4.17.5  TripartyAgent <TrptyAgt>
Presence: [0..1]
Definition: Party responsible for the administration of a tri-party collateral transaction including collateral
allocation, marking to market and substitution of collateral.
TripartyAgent <TrptyAgt> contains the following elements (see "PartyIdentification136" on page 1671
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1672
   LEI <LEI> [0..1] IdentifierSet 1672
22.4.18 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C46 "SupplementaryDataRule"
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 765 March 2026
```

## File page 766

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1565
   Envelope <Envlp> [1..1] (External Schema) 1565
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 766 March 2026
```

