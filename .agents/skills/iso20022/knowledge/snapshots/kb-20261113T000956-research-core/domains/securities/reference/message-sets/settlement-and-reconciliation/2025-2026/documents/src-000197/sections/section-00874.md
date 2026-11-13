---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08", "33.4 Message Building Blocks", "33.4.6 ModificationProcessingStatus <ModPrcgSts>"]
file_pages: [1307]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.039.001.08"]
---

# 33.4.6 ModificationProcessingStatus <ModPrcgSts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1307 to 1307.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1307

```text
TransactionIdentification <TxId> contains the following elements (see "TransactionIdentifications33"
on page 1493 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1493
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1494
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1494
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1494
   OtherIdentification <OthrId> [0..1] Text 1494
Constraints
• AccountOwnerTransactionIdentificationRule
If AccountOwnerTransactionIdentification is NONREF then at least one of the other references must
be present.
On Condition
    /AccountOwnerTransactionIdentification is equal to value 'NONREF'
Following Must be True
    /AccountServicerTransactionIdentification Must be present
 Or    /MarketInfrastructureTransactionIdentification Must be present
 Or    /ProcessorTransactionIdentification Must be present
 Or    /OtherIdentification Must be present
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, then the
AccountOwnerTransactionIdentification must be NONREF.
33.4.6 ModificationProcessingStatus <ModPrcgSts>
Presence: [1..1]
Definition: Provides details on the processing status of the request.
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1307 March 2026
```

