---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02", "4.4 Message Building Blocks", "4.4.3 OtherBusinessParties <OthrBizPties>", "4.4.3.3 TradeRegulator <TradRgltr>"]
file_pages: [145]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.029.001.02"]
---

# 4.4.3.3 TradeRegulator <TradRgltr>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 145 to 145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 145

```text
StockExchange <StockXchg> contains the following elements (see
"PartyIdentificationAndAccount152" on page 475 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 475
   ProcessingIdentification <PrcgId> [0..1] Text 475
   AdditionalInformation <AddtlInf> [0..1] ± C2 475
   AlternateIdentification <AltrnId> [0..1] ± 476
4.4.3.3  TradeRegulator <TradRgltr>
Presence: [0..1]
Definition: Party that identifies the trade regulator.
TradeRegulator <TradRgltr> contains the following elements (see "PartyIdentificationAndAccount152"
on page 475 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 475
   ProcessingIdentification <PrcgId> [0..1] Text 475
   AdditionalInformation <AddtlInf> [0..1] ± C2 475
   AlternateIdentification <AltrnId> [0..1] ± 476
4.4.3.4  TripartyAgent <TrptyAgt>
Presence: [0..1]
Definition: Party that handles tri-party transactions.
TripartyAgent <TrptyAgt> contains the following elements (see "PartyIdentificationAndAccount154"
on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 476
   SafekeepingAccount <SfkpgAcct> [0..1] Text 477
   CashAccount <CshAcct> [0..1] ± 477
   ProcessingIdentification <PrcgId> [0..1] Text 477
   AdditionalInformation <AddtlInf> [0..1] ± C2 477
   AlternateIdentification <AltrnId> [0..1] ± 478
4.4.3.5  QualifiedForeignIntermediary <QlfdFrgnIntrmy>
Presence: [0..1]
Approved by the Securities SEG on 13 February 2025 setr.029.001.02
SecuritiesTradeConfirmationCancellationV02
Post Trade Matching - Maintenance 2024 - 2025 145 February 2025
```

