---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["15 sese.021.001.08 SecuritiesTransactionStatusQueryV08", "15.4 Message Building Blocks", "15.4.1 StatusAdviceRequested <StsAdvcReqd>", "15.4.1.2 References <Refs>"]
file_pages: [479]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.021.001.08"]
---

# 15.4.1.2 References <Refs>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 479 to 479.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 479

```text
Number <Nb> contains one of the following elements (see "DocumentNumber5Choice" on page 1444
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 1444
Or   LongNumber <LngNb> [1..1] Text 1445
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 1445
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
15.4.1.2  References <Refs>
Presence: [1..*]
Definition: References of transaction for which the status is requested.
References <Refs> contains the following elements (see "Identification32" on page 1507 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1507
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1508
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1508
   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 1508
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1508
   CommonIdentification <CmonId> [0..1] Text 1508
   TradeIdentification <TradId> [0..*] Text 1508
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 1508
   MasterIdentification <MstrId> [0..1] Text 1509
   BasketIdentification <BsktId> [0..1] Text 1509
   IndexIdentification <IndxId> [0..1] Text 1509
   ListIdentification <ListId> [0..1] Text 1509
   ProgramIdentification <PrgmId> [0..1] Text 1509
   PoolIdentification <PoolId> [0..1] Text 1509
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 1509
Approved by the Securities SEG on 27 January 2026 sese.021.001.08
SecuritiesTransactionStatusQueryV08
Settlement And Reconciliation - Maintenance 2025 - 2026 479 March 2026
```

