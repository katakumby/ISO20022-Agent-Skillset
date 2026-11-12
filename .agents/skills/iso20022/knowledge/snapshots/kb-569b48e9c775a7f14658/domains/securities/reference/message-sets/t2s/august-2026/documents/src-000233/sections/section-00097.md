---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["9 camt.068.001.02 IntraBalanceMovementConfirmationV02", "9.4 Message Building Blocks", "9.4.2 AdditionalParameters <AddtlParams>"]
file_pages: [138]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.068.001.02"]
---

# 9.4.2 AdditionalParameters <AddtlParams>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 138 to 138.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 138

```text
MessageRecipient <MsgRcpt> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
9.4.2 AdditionalParameters <AddtlParams>
Presence: [0..1]
Definition: Additional parameters to the transaction.
AdditionalParameters <AddtlParams> contains the following elements (see
"AdditionalParameters16" on page 2982 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartialSettlement <PrtlSttlm> [0..1] CodeSet 2983
   PreviousPartialConfirmationIdentification
<PrvsPrtlConfId>
[0..1] Text 2983
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 2983
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 2983
   PoolIdentification <PoolId> [0..1] Text 2984
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 2984
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2984
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2984
9.4.3 CashAccount <CshAcct>
Presence: [1..1]
Definition: Account to or from which an entry is made.
Impacted by: C9 "IdentificationOrProxyPresenceRule", C8 "IdentificationAndProxyGuideline"
CashAccount <CshAcct> contains the following elements (see "CashAccount40" on page 2832 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 2832
   Type <Tp> [0..1] ± 2832
   Currency <Ccy> [0..1] CodeSet C1 2833
   Name <Nm> [0..1] Text 2833
   Proxy <Prxy> [0..1] ± 2833
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.068.001.02
IntraBalanceMovementConfirmationV02
Target2-Securities 138 August 2026
```

