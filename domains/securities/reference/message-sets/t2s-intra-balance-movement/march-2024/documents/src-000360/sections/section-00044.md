---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 camt.068.001.02 IntraBalanceMovementConfirmationV02", "4.4 Message Building Blocks", "4.4.2 AdditionalParameters <AddtlParams>"]
file_pages: [55]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.068.001.02"]
---

# 4.4.2 AdditionalParameters <AddtlParams>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 55 to 55.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 55

```text
MessageRecipient <MsgRcpt> contains the following elements (see "PartyIdentification136" on
page 417 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 418
   LEI <LEI> [0..1] IdentifierSet 418
4.4.2 AdditionalParameters <AddtlParams>
Presence: [0..1]
Definition: Additional parameters to the transaction.
AdditionalParameters <AddtlParams> contains the following elements (see
"AdditionalParameters16" on page 410 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartialSettlement <PrtlSttlm> [0..1] CodeSet 411
   PreviousPartialConfirmationIdentification
<PrvsPrtlConfId>
[0..1] Text 411
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 411
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 411
   PoolIdentification <PoolId> [0..1] Text 411
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 411
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 411
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 412
4.4.3 CashAccount <CshAcct>
Presence: [1..1]
Definition: Account to or from which an entry is made.
Impacted by: C9 "IdentificationOrProxyPresenceRule", C8 "IdentificationAndProxyGuideline"
CashAccount <CshAcct> contains the following elements (see "CashAccount40" on page 387 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 388
   Type <Tp> [0..1] ± 388
   Currency <Ccy> [0..1] CodeSet C2 388
   Name <Nm> [0..1] Text 389
   Proxy <Prxy> [0..1] ± 389
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.068.001.02
IntraBalanceMovementConfirmationV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
55 March 2024
```

