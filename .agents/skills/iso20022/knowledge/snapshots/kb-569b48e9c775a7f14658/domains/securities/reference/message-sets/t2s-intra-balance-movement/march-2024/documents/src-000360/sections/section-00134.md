---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["9 camt.078.001.02 IntraBalanceMovementQueryV02", "9.4 Message Building Blocks", "9.4.2 QueryDefinition <QryDef>", "9.4.2.2 SearchCriteria <SchCrit>", "9.4.2.2.1 References <Refs>"]
file_pages: [165]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 9.4.2.2.1 References <Refs>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 165 to 165.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 165

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       ToDateTime <ToDtTm> [1..1] DateTime 189
Or       FromToDateTime <FrToDtTm> [1..1] ± 189
Or       EqualDateTime <EQDtTm> [1..1] DateTime 189
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 189
9.4.2.2.1  References <Refs>
Presence: [0..*]
Definition: Collective reference identifying a set of messages.
References <Refs> contains one of the following References36Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 165
Or   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 165
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 165
Or   ProcessorTransactionIdentification <PrcrTxId> [1..1] Text 165
Or   PoolIdentification <PoolId> [1..1] Text 166
Or}   CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 166
9.4.2.2.1.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 497
9.4.2.2.1.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 497
9.4.2.2.1.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 497
9.4.2.2.1.4  ProcessorTransactionIdentification <PrcrTxId>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
165 March 2024
```

