---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.7 SecuritiesFinancingDetails <SctiesFincgDtls>", "29.4.7.1 SecuritiesFinancingTradeIdentification <SctiesFincgTradId>"]
file_pages: [1025]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.7.1 SecuritiesFinancingTradeIdentification <SctiesFincgTradId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1025 to 1025.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1025

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecondLegNarrative <ScndLegNrrtv> [0..1] Text 1032
29.4.7.1  SecuritiesFinancingTradeIdentification <SctiesFincgTradId>
Presence: [0..1]
Definition: Unambiguous identification of the underlying securities financing trade as assigned by the
instructing party. The identification is common to all collateral pieces (one or many).
Datatype: "Max35Text" on page 2192
29.4.7.2  SecuritiesFinancingUniqueTransactionIdentifier <SctiesFincgUnqTxIdr>
Presence: [0..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 2188
29.4.7.3  ClosingLegIdentification <ClsgLegId>
Presence: [0..1]
Definition: Unambiguous identification of the second leg of the transaction as known by the account
owner (or the instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
29.4.7.4  TerminationDate <TermntnDt>
Presence: [0..1]
Definition: Closing date/time or maturity date/time of the transaction.
TerminationDate <TermntnDt> contains one of the following elements (see "TerminationDate6Choice"
on page 1436 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 1437
Or}   Code <Cd> [1..1]  1437
{Or     Code <Cd> [1..1] CodeSet 1437
Or}     Proprietary <Prtry> [1..1] ± 1437
29.4.7.5  RateChangeDate <RateChngDt>
Presence: [0..1]
Definition: Date/Time at which rate change has taken place.
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1025 March 2026
```

