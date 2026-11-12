---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks", "22.4.4 CounterpartyMarketInfrastructureTransactionIdentification <CtrPtyMktInfrstrctrTxId>", "22.4.5.11 NumberOfDaysAccrued <NbOfDaysAcrd>"]
file_pages: [743]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4.5.11 NumberOfDaysAccrued <NbOfDaysAcrd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 743 to 743.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 743

```text
22.4.5.11  NumberOfDaysAccrued <NbOfDaysAcrd>
Presence: [0..1]
Definition: Number of days on which the interest rate accrues (daily accrual note).
Impacted by: C25 "NumberRule"
Datatype: "Max3Number" on page 2189
Constraints
• NumberRule
If Number is negative, then Sign must be present.
22.4.5.12  TradeTransactionCondition <TradTxCond>
Presence: [0..*]
Definition: Indicates the conditions under which the order/trade is to be/was executed.
TradeTransactionCondition <TradTxCond> contains one of the following elements (see
"TradeTransactionCondition5Choice" on page 2032 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2032
Or}   Proprietary <Prtry> [1..1] ± 2033
22.4.5.13  TypeOfPrice <TpOfPric>
Presence: [0..1]
Definition: Specifies the type of price and information about the price.
TypeOfPrice <TpOfPric> contains one of the following elements (see "TypeOfPrice29Choice" on
page 1711 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1711
Or}   Proprietary <Prtry> [1..1] ± 1711
22.4.6 FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C16 "DescriptionPresenceRule", C17 "DescriptionUsageRule", C21 "ISINGuideline", C22
"ISINPresenceRule", C26 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 743 March 2026
```

