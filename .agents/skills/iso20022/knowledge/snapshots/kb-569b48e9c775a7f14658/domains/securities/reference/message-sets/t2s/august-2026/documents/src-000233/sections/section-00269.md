---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["16 camt.078.001.02 IntraBalanceMovementQueryV02", "16.4 Message Building Blocks", "16.4.2 QueryDefinition <QryDef>", "16.4.2.2 SearchCriteria <SchCrit>", "16.4.2.2.1 References <Refs>"]
file_pages: [356]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 16.4.2.2.1 References <Refs>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 356 to 356.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 356

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       ToDateTime <ToDtTm> [1..1] DateTime 380
Or       FromToDateTime <FrToDtTm> [1..1] ± 380
Or       EqualDateTime <EQDtTm> [1..1] DateTime 380
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 380
16.4.2.2.1  References <Refs>
Presence: [0..*]
Definition: Collective reference identifying a set of messages.
References <Refs> contains one of the following References36Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 356
Or   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 356
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 356
Or   ProcessorTransactionIdentification <PrcrTxId> [1..1] Text 356
Or   PoolIdentification <PoolId> [1..1] Text 357
Or}   CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 357
16.4.2.2.1.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 3328
16.4.2.2.1.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 3328
16.4.2.2.1.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 3328
16.4.2.2.1.4  ProcessorTransactionIdentification <PrcrTxId>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 356 August 2026
```

