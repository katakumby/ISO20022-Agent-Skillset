---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.16 OtherBusinessParties <OthrBizPties>", "29.4.16.3 StockExchange <StockXchg>"]
file_pages: [1055]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.16.3 StockExchange <StockXchg>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1055 to 1055.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1055

```text
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
29.4.16.3  StockExchange <StockXchg>
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
29.4.16.4  TradeRegulator <TradRgltr>
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
29.4.16.5  TripartyAgent <TrptyAgt>
Presence: [0..1]
Definition: Party responsible for the administration of a tri-party collateral transaction including collateral
allocation, marking to market and substitution of collateral.
Impacted by: C42 "SafekeepingAccountOrBlockChainAddress1Rule", C46
"SafekeepingAccountOrBlockChainAddress2Rule"
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1055 March 2026
```

