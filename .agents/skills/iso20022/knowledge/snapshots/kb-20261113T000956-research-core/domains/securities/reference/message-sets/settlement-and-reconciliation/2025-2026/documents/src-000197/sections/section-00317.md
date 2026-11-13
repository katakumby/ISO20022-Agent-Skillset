---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["14 sese.020.001.09 SecuritiesTransactionCancellationRequestV09", "14.4 Message Building Blocks", "14.4.2 AccountServicerTransactionIdentification <AcctSvcrTxId>"]
file_pages: [464]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.020.001.09"]
---

# 14.4.2 AccountServicerTransactionIdentification <AcctSvcrTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 464 to 464.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 464

```text
AccountOwnerTransactionIdentification <AcctOwnrTxId> contains one of the following elements
(see "References45Choice" on page 1502 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] ± 1503
Or   SecuritiesFinancingTransactionIdentification
<SctiesFincgTxId>
[1..1] ± 1503
Or   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 1503
Or}   OtherTransactionIdentification <OthrTxId> [1..1]  1504
     MessageNumber <MsgNb> [0..1] ± C20 1504
     Identification <Id> [1..1] Text 1504
14.4.2 AccountServicerTransactionIdentification
<AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 2192
14.4.3 MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
14.4.4 ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Message Reference identifying the Processor of the transaction.
Datatype: "Max35Text" on page 2192
14.4.5 NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 2192
14.4.6 AccountOwner <AcctOwnr>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.020.001.09
SecuritiesTransactionCancellationRequestV09
Settlement And Reconciliation - Maintenance 2025 - 2026 464 March 2026
```

