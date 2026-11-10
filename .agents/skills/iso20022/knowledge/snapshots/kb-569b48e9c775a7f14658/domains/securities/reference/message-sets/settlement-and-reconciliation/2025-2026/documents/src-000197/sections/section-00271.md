---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "10.4 Message Building Blocks", "10.4.6 AllegementDetails <AllgmtDtls>", "10.4.6.32 OtherBusinessParties <OthrBizPties>", "10.4.6.32.3 StockExchange <StockXchg>"]
file_pages: [404, 405]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.019.001.12"]
---

# 10.4.6.32.3 StockExchange <StockXchg>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 404 to 405.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 404

```text
10.4.6.32.3  StockExchange <StockXchg>
Presence: [0..1]
Definition: Identification of the stock exchange to which transaction reporting will be done.
StockExchange <StockXchg> contains the following elements (see "PartyIdentification136" on
page 1671 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1672
   LEI <LEI> [0..1] IdentifierSet 1672
10.4.6.32.4  TradeRegulator <TradRgltr>
Presence: [0..1]
Definition: Institution to which a trade must be reported.
TradeRegulator <TradRgltr> contains the following elements (see "PartyIdentification136" on
page 1671 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1672
   LEI <LEI> [0..1] IdentifierSet 1672
10.4.6.32.5  TripartyAgent <TrptyAgt>
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
10.4.6.33  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C46 "SupplementaryDataRule"
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 404 March 2026
```

## File page 405

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
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 405 March 2026
```

