---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "25.4 Message Building Blocks", "25.4.5 RequestDetails <ReqDtls>", "25.4.5.1 Reference <Ref>"]
file_pages: [808]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.031.001.11"]
---

# 25.4.5.1 Reference <Ref>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 808 to 808.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 808

```text
• SettlementConditionModificationApplicabilityRule
All settlement condition modification request types do not apply to all account servicers.
25.4.5.1  Reference <Ref>
Presence: [1..1]
Definition: References of the transaction for which the securities settlement condition modification is
requested.
Impacted by: C5 "ReferencePresenceRule"
Reference <Ref> contains the following elements (see "References29" on page 1513 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 1513
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1514
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1514
   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 1514
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1514
   PoolIdentification <PoolId> [0..1] Text 1514
   CommonIdentification <CmonId> [0..1] Text 1514
   TradeIdentification <TradId> [0..1] Text 1514
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 1514
Constraints
• ReferencePresenceRule
At least one reference must be present.
On Condition
    /AccountOwnerTransactionIdentification is absent
 And    /AccountServicerTransactionIdentification is absent
 And    /MarketInfrastructureTransactionIdentification is absent
 And    /ProcessorTransactionIdentification is absent
 And    /PoolIdentification is absent
Following Must be True
    /CommonIdentification Must be present
 Or    /TradeIdentification Must be present
25.4.5.2  RestrictionReference <RstrctnRef>
Presence: [0..*]
Definition: Restriction references applied on the transaction for which the securities settlement condition
modification is requested.
Approved by the Securities SEG on 27 January 2026 sese.031.001.11
SecuritiesSettlementConditionModificationStatusAd
viceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 808 March 2026
```

