---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "17.4 Message Building Blocks", "17.4.17 OtherBusinessParties <OthrBizPties>", "17.4.17.3 StockExchange <StockXchg>"]
file_pages: [551]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.023.001.13"]
---

# 17.4.17.3 StockExchange <StockXchg>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 551 to 551.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 551

```text
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
17.4.17.3  StockExchange <StockXchg>
Presence: [0..1]
Definition: Identification of the stock exchange to which transaction reporting will be done.
StockExchange <StockXchg> contains the following elements (see
"PartyIdentificationAndAccount165" on page 1670 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1670
   LEI <LEI> [0..1] IdentifierSet 1670
   AlternateIdentification <AltrnId> [0..1] ± 1671
   ProcessingIdentification <PrcgId> [0..1] Text 1671
   AdditionalInformation <AddtlInf> [0..1] ± C5 1671
17.4.17.4  TradeRegulator <TradRgltr>
Presence: [0..1]
Definition: Institution to which a trade must be reported.
TradeRegulator <TradRgltr> contains the following elements (see "PartyIdentificationAndAccount165"
on page 1670 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1670
   LEI <LEI> [0..1] IdentifierSet 1670
   AlternateIdentification <AltrnId> [0..1] ± 1671
   ProcessingIdentification <PrcgId> [0..1] Text 1671
   AdditionalInformation <AddtlInf> [0..1] ± C5 1671
17.4.17.5  TripartyAgent <TrptyAgt>
Presence: [0..1]
Definition: Party responsible for the administration of a tri-party collateral transaction including collateral
allocation, marking to market and substitution of collateral.
Impacted by: C57 "SafekeepingAccountOrBlockChainAddress1Rule", C61
"SafekeepingAccountOrBlockChainAddress2Rule"
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 551 March 2026
```

